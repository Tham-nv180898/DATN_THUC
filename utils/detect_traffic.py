import argparse
import time
from pathlib import Path

import cv2
import torch


from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages, processing_image
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device

# from pypylon import pylon
import os
import numpy as np


def detect(source=None, weights=None, imgsz=640, device="cpu", conf_thres=0.5, iou_thres=0.45):
    # shape(height, width, channel)
    img = cv2.imread(source)
    img_org = cv2.imread(source)
    img_org1 = img_org.copy()
    # img = cv2.resize(img_org, (38, 640))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)4
    device = select_device(device)
    half = device.type != 'cpu'

    # Load model
    model = attempt_load(weights, map_location=device)
    stride = int(model.stride.max())
    imgsz = check_img_size(imgsz, s=stride)
    names = model.module.names if hasattr(model, 'module') else model.names
    # print(names)
    if half:
        model.half()
    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))
    img = processing_image(img)
    # img = img.transpose(1, 2, 0)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    img = torch.from_numpy(img).to(device)
    img = img.float()
    img /= 255.0
    img = img.unsqueeze(0)
    pred = model(img, augment=False)[0]
    pred = non_max_suppression(pred, conf_thres, iou_thres, classes=None, agnostic=False)
    print(pred)
    for i, det in enumerate(pred):
        # gn = torch.tensor(img_org.shape)[[1, 0, 1, 0]]
        if len(det):
            # rescale boxes from img > img_org
            # print("detect:", det)
            # print("shape:", det.shape)
            # print(det[:, :4][0])
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img_org.shape).round()
            # print(det)

            for *xyxy, conf, cls in reversed(det):
                print("xyxy", xyxy)
                c = int(cls)
                x1 = int(xyxy[0].item())
                y1 = int(xyxy[1].item())
                x2 = int(xyxy[2].item())
                y2 = int(xyxy[3].item())
                image_crop = img_org1[y1:y2, x1:x2]
                conf = conf.item()
                label = names[c] + " " + str(round(conf, 2))
                plot_one_box(xyxy, img_org, label=label, color=colors(c, True), line_thickness=3)
    cv2.imshow("image1", image_crop)
    cv2.imshow("image", img_org)
    cv2.waitKey(0)


if __name__ == '__main__':
    source = "./traffic.jpg"
    weights = "weight_traffic.pt"
    detect(source, weights)
