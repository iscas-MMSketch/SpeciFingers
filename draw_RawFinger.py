import json
import os

import cv2 as cv
import numpy as np

path = 'video_users'

for root, dirs, files in os.walk(
        'raw_log_data',
        topdown=False):
    print(files)
    for name in files:
        file_name = os.path.join(root, name)
        file = open(file_name, encoding='utf_8')

        js = file.read()
        start_pos = 0
        dic_all = []
        for index, i in enumerate(js):
            if i == '{':
                start_pos = index
                break
        dic_list = js[index:]
        dic_list = dic_list.replace("'", '"')
        split_lsit = dic_list.split('\n')
        for j in split_lsit:
            if 'Type' in j:
                try:
                    user_dict = json.loads(j)
                    dic_all.append(user_dict)
                except:
                    print('finish')

        user_num = (((root.split('/'))[-1]).split('_'))[0]
        if not os.path.exists(os.path.join(path, user_num)):
            os.makedirs(os.path.join(path, user_num))
        img = np.zeros((1080, 1920, 3), np.uint8)
        img_out = np.zeros((160, 160, 3), np.uint8)
        img[:] = [0, 0, 0]
        img_out[:] = [0, 0, 0]
        fourcc = cv.VideoWriter_fourcc(*'XVID')
        video = cv.VideoWriter(os.path.join(os.path.join(path, user_num),
                                            'v_' + name.replace('.log', '') + ".mp4"), fourcc,
                               2,
                               (img_out.shape[1], img_out.shape[0]))
        for dic in dic_all:
            for point in dic['rawPoints']:
                sensitivity = point['Sensitivity']
                cv.rectangle(img, (
                    int(point['RawX'] * (1920 / 122) - (1920 / 244)), int(point['RawY'] * (1080 / 70) - (1080 / 140))),
                             (int(point['RawX'] * (1920 / 122) + (1920 / 244)),
                              int(point['RawY'] * (1080 / 70) + (1080 / 140))),
                             (sensitivity / 4, sensitivity / 4, sensitivity / 4), -1)
            gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            th, binary = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU)
            contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
            bounding_boxes = [cv.boundingRect(cnt) for cnt in contours]
            if len(bounding_boxes) == 1:
                bbox = bounding_boxes[0]
                [x, y, w, h] = bbox
                img_out = img[y - 50: y + 110, x - 50:x + 110]
            cv.waitKey(1000)
            video.write(img_out)
            img[:] = [0]
            img_out[:] = [0]
        video.release()
        cv.destroyAllWindows()
