import cv2
import torch
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages, processing_image
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import colors, plot_one_box
from utils.torch_utils import select_device


class Detect_Traffic:
    def __init__(self):
        self._source = None
        self._weight = None
        self._image_size = None
        self._device = None
        self._conf_threshold = None
        self._iou_threshold = None

    def set_spec(self, path_image, weight, mage_size=320, device='cpu', conf_threshold=0.5, iou_threshold=0.45):
        self._source = path_image
        self._weight = weight
        self._image_size = mage_size
        self._device = device
        self._conf_threshold = conf_threshold
        self._iou_threshold = iou_threshold

    def detect_image(self):
        img = cv2.imread(self._source)
        org_img = img.copy()
        device = select_device(self._device)
        half = device.type != 'cpu'

        # Load model
        model = attempt_load(self._weight, map_location=device)
        stride = int(model.stride.max())
        image_size = check_img_size(self._image_size, s=stride)
        names = model.module.names if hasattr(model, 'module') else model.names
        if half:
            model.half()
        if device.type != 'cpu':
            model(torch.zeros(1, 3, image_size, image_size).to(device).type_as(next(model.parameters())))
        img = processing_image(img)
        img = torch.from_numpy(img).to(device)
        img = img.float()
        img /= 255.0
        img = img.unsqueeze(0)
        prediction = model(img, augment=False)[0]
        prediction = non_max_suppression(prediction, self._conf_threshold, self._iou_threshold, classes=None)
        print(prediction)
        number_object = 0
        object_cls = {}
        for i, det in enumerate(prediction):
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], org_img.shape).round()
                for *xy_xy, conf, cls in reversed(det):
                    c = int(cls)
                    conf = conf.item()
                    label = names[c] + " " + str(round(conf, 2))
                    plot_one_box(xy_xy, org_img, label=label, color=colors(c, True), line_thickness=1)
                    object_cls[number_object] = c
                    number_object += 1
        returned_data = (org_img, number_object, object_cls)
        return returned_data
