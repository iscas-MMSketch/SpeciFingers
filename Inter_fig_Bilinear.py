import os
import cv2
import numpy as np
import scipy.ndimage

Figures = []
Num_fig = 50

for root, dirs, files in os.walk(
        'jpg_video',
        topdown=False):
    for dir in dirs:
        if 'v_' in dir:
            lens = len([lists for lists in os.listdir(os.path.join(root, dir)) if
                        os.path.isfile(os.path.join(os.path.join(root, dir), lists))])
            if lens<50:
                print('filenum:', lens, dir)
                if lens < Num_fig:
                    Fig_all = np.empty((160, 160, 0))
                    Fig_inter = np.empty((160, 160, 0))
                    Figs = os.listdir(os.path.join(root, dir))
                    for Fig in Figs:
                        if 'jpg' in Fig:
                            im = cv2.imread(os.path.join(os.path.join(root, dir), Fig), -1)
                            Fig_all = np.dstack((Fig_all, im[:, :, 0]))
                    Multiple = int(Num_fig / (max(1,Fig_all.shape[2]-1))) + 1
                    for index in range(Fig_all.shape[2] - 1):
                        im1 = Fig_all[:, :, index:index + 2]
                        im_out = scipy.ndimage.interpolation.zoom(im1, [1, 1, Multiple], order=1)
                        Fig_inter = np.dstack((Fig_inter, im_out[:, :, 0]))
                        Fig_list = []
                        for M in range(2, Multiple + 1):
                            Fig_list.append(2*M - 3)
                        for Num in Fig_list:
                            Fig_inter = np.dstack((Fig_inter, im_out[:, :, Num]))
                    Fig_inter = np.dstack((Fig_inter, im_out[:, :, -1]))

                    for index_i in range(Fig_inter.shape[2]):
                        target = os.path.join(os.path.join(root, dir),
                                            'image_{:05d}.jpg'.format(index_i))
                        print("target",target)
                        frame = Fig_inter[:, :, index_i]
                        frame = frame.astype(np.uint16)
                        cv2.imwrite(target, frame)
                        cv2.imwrite(target, np.dstack((frame,
                                                    frame,
                                                    frame)))
