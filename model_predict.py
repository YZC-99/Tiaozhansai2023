# -----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
# -----------------------------------------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image
from yolo import YOLO

def refer_from_yolo(image_path):
    yolo = YOLO()
    image = Image.open(image_path)
    '''
    "ymin":bottom,
    "xmin":left,
    "ymax":top,
    "xmax":right,
    'conf':score,
    'class_pred':predicted_class
    '''
    outs = yolo.get_out_coords(image)
    return [outs['ymin'],outs['xmin'],outs['ymax'],outs['xmax'],outs['conf'],outs['class_pred']]
class predict(object):
    def __init__(self, **kwargs):
        print("init success!")
    def detect_image(self, image_path):
        results = refer_from_yolo(image_path)
        return results
