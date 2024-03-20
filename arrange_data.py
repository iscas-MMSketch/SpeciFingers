import os
import shutil

for index in range(0, 20):
    print(index)
    for root, dirs, files in os.walk(
            'jpg_video'
            , topdown=False):
        if root.endswith('/' + str(index)):
            for dir in dirs:
                shutil.copytree(os.path.join(root, dir),
                                os.path.join(
                                    os.path.join(os.path.join('jpg_video_arrange', str(index)), 'First_test'), dir))

    for index_u in range(0, 20):
        if index_u != index:
            for root, dirs, files in os.walk(
                    'jpg_video'
                    , topdown=False):
                if root.endswith('/' + str(index_u)):
                    print(':::', root)
                    for dir in dirs:
                        shutil.copytree(os.path.join(root, dir),
                                        os.path.join(
                                            os.path.join(os.path.join('jpg_video_arrange', str(index)), 'First_train'),
                                            dir))
