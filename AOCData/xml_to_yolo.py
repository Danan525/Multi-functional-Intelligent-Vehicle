# -*- coding: utf-8 -*-
import os
from os import getcwd

sets = ['train', 'val', 'test']
classes = ["dog", "kid"]   # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)

# 由于不再需要转换bbox，convert函数不需要
# 同样，不需要解析xml，因此convert_label也大幅简化

def convert_label(image_id):
    # 直接打开txt文件
    in_file_path = 'D:/yolov5/AOCData/label/%s.txt' % image_id
    out_file_path = 'D:/yolov5/AOCData/labels/%s.txt' % image_id
    # 检查文件是否存在，避免FileNotFoundError
    if not os.path.exists(in_file_path):
        print(f"文件不存在：{in_file_path}")
        return
    with open(in_file_path, 'r', encoding='UTF-8') as in_file, open(out_file_path, 'w') as out_file:
        for line in in_file:
            # 假设txt文件已经是YOLO格式，直接复制
            out_file.write(line)

wd = getcwd()
for image_set in sets:
    if not os.path.exists('D:/yolov5/AOCData/labels/'):
        os.makedirs('D:/yolov5/AOCData/labels/')
    image_ids = open('D:/yolov5/AOCData/ImageSets/Main/%s.txt' % image_set).read().strip().split()
    
    if not os.path.exists('D:/yolov5/AOCData/dataSet_path/'):
        os.makedirs('D:/yolov5/AOCData/dataSet_path/')
     
    list_file = open('dataSet_path/%s.txt' % image_set, 'w')
    for image_id in image_ids:
        list_file.write('D:/yolov5/AOCData/images/%s.jpg\n' % image_id)
        convert_label(image_id)
    list_file.close()
