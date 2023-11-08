import os
import numpy
import pandas as pd
import csv
mapping = {
'E2': 0,
'B52': 1,
'B2': 2,
'Mirage2000': 3,
'F4': 4,
'F14': 5,
'Tornado': 6,
'J20': 7,
'JAS39': 8,
}
root = 'E:/Deep_Learning_DATABASE/object_detection/plane/dataset/train'
save_dir = './'
file_list= [os.path.join(root,i) for i in os.listdir(root) if i.endswith('.csv')]
all_labels = []
with open(os.path.join(save_dir, 'ftrainval.txt'), 'w') as save_txt:
    for file in file_list:
        with open(file,'r') as f:
            # img_name = f.read().splitlines()[-1].split(',')[0]
            all_data = data = f.read().splitlines()
            # print(all_data)
            # break
            current_lenght = len(all_data) - 1
            for line in range(current_lenght):
                # if line == len(all_data):
                #     break
                current_line = line + 1
                data = all_data[current_line].split(',')
                name = data[0]
                data.pop(0)
                label = data[2]
                label = mapping[label]
                data.pop(2)
                data = [ float(i) for i in data]
                # image
                w,h = data[0],data[1]
                # anchor coordinate
                xmin,xmax = data[2] ,data[4]
                ymin,ymax = data[3] ,data[5]
                # anchor center
                x_center,y_center = (xmin + xmax) / 2,(ymin + ymax) / 2
                # anchor h and w
                new_w,new_h = xmax - xmin,ymax - ymin

                x_center, y_center, new_w,new_h = int(x_center), int(y_center), int(new_w),int(new_h)
                if current_lenght == 1:
                    save_txt.write("{} {},{},{},{},{}\n".format(file.replace('.csv','.jpg'), x_center, y_center, new_w,
                                                           new_h,label))
                else:
                    if current_line == 1:
                        save_txt.write("{} {},{},{},{},{}".format(file.replace('.csv', '.jpg'),
                                                                    x_center, y_center,
                                                                    new_w,
                                                                    new_h, label))
                    elif current_line == current_lenght:
                        save_txt.write(" {},{},{},{},{}\n".format(x_center, y_center,
                                                                    new_w,
                                                                    new_h, label))
                    else:
                        save_txt.write(" {},{},{},{},{}".format(x_center, y_center,
                                                                    new_w,
                                                                    new_h, label))