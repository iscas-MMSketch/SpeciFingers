import os


for root, dirs, files in os.walk(
            'jpg_video_arrange'
        , topdown=False):
    for dir in dirs:
        dir_list = dir.split('_')
        if len(dir_list) == 4:
            if 'Left' in dir_list[2]:
                finger = dir_list[2].replace('Left', '')
            if 'Right' in dir_list[2]:
                finger = dir_list[2].replace('Right', '')
            dir_new = 'v_' + finger + '_g' + dir_list[1] + '_c01'
            dir_name = os.path.join(root, dir_new)
            print(dir_name)
            os.rename(os.path.join(root, dir), os.path.join(root, dir_new))

        if dir_list[1] == 'ForeFinger' or dir_list[1] == 'MiddleFinger' or dir_list[1] == 'RingFinger':
            dir_new = dir.replace(dir_list[1], '3Middle')
            dir_name = os.path.join(root, dir_new)
            print(dir_name)
            os.rename(os.path.join(root, dir), os.path.join(root, dir_new))
            
for root, dirs, files in os.walk(
            'jpg_video_arrange'
        , topdown=False):
    for dir in dirs:
        dir_list = dir.split('_')

        if dir_list[1] == 'ForeFinger' or dir_list[1] == 'MiddleFinger' or dir_list[1] == 'RingFinger':
            dir_new = dir.replace(dir_list[1], '3Middle')
            dir_name = os.path.join(root, dir_new)
            print(dir_name)
            os.rename(os.path.join(root, dir), os.path.join(root, dir_new))