import numpy as np
import cv2 as cv
import os

tv_channels = ['geo_news', 'ary_news', 'sama_news', 'express_news', 'bol_news', 'dunya_news', '92_news', 'dawn_news', 'ptv_news', 'aaj_news']
img_dir = os.getcwd() + '/tv_channel_images/'
dir_loc = os.getcwd() + '/tv_channel_videos/'

if not os.path.exists(img_dir):
    os.makedirs(img_dir)
for channel in tv_channels:
    channel_dir = img_dir + channel
    if not os.path.exists(channel_dir):
        os.makedirs(channel_dir)
        print('Folder {} created'.format(channel_dir))

geo_img_dir = img_dir + tv_channels[0]
ary_img_dir = img_dir + tv_channels[1]
sama_img_dir = img_dir + tv_channels[2]
express_img_dir = img_dir + tv_channels[3]
bol_img_dir = img_dir + tv_channels[4]
dunya_img_dir = img_dir + tv_channels[5]
_92_img_dir = img_dir + tv_channels[6]
dawn_img_dir = img_dir + tv_channels[7]
ptv_img_dir = img_dir + tv_channels[8]
aaj_img_dir = img_dir + tv_channels[9]

## Frame extraction

row_th, col_th = .35, .35

for i, video in enumerate(os.listdir(dir_loc)):
    vid_loc = dir_loc + video
    # set video file path of input video with name and extension
    vid = cv.VideoCapture(vid_loc)

    #for frame identity
    index = 0
    while(True):
        # Extract images
        ret, a = vid.read()
        # end of frames
        if not ret:
            break
        # Segment frames
        if video.split('_')[0] in ['sama', 'aaj']:
            frame = a[:int(np.shape(a)[0]*row_th), -int(np.shape(a)[1]*col_th):]
        elif video.split('_')[0] in ['bol']:
            if 'wK1w8r4molE' in i.split('_')[2]:
                frame = a[-int(np.shape(a)[0]*row_th):, -int(np.shape(a)[1]*col_th):]
            else:
                frame = a[:int(np.shape(a)[0]*row_th), :int(np.shape(a)[1]*col_th)]
        else:
            frame = a[-int(np.shape(a)[0]*row_th):, -int(np.shape(a)[1]*col_th):]
        
        if video.split('_')[0] in ['geo']:
            folder = geo_img_dir
        elif video.split('_')[0] in ['ary']:
            folder = ary_img_dir
        elif video.split('_')[0] in ['sama']:
            folder = sama_img_dir
        elif video.split('_')[0] in ['express']:
            folder = express_img_dir
        elif video.split('_')[0] in ['bol']:
            folder = bol_img_dir
        elif video.split('_')[0] in ['dunya']:
            folder = dunya_img_dir
        elif video.split('_')[0] in ['92']:
            folder = _92_img_dir
        elif video.split('_')[0] in ['dawn']:
            folder = dawn_img_dir
        elif video.split('_')[0] in ['ptv']:
            folder = ptv_img_dir
        elif video.split('_')[0] in ['aaj']:
            folder = aaj_img_dir
        else:
            folder = img_dir
        
        name = folder + '/' + video.replace('.mp4','') + 'frame' + str(index) + '.jpg'      
        #print ('Creating...' + name)
        cv.imwrite(name, frame)

        # next frame
        index += 1
    print('{}: Created frames for {} done'.format(i, video))

geo_img_list = os.listdir(geo_img_dir)
ary_img_list = os.listdir(ary_img_dir)
sama_img_list = os.listdir(sama_img_dir)
express_img_list = os.listdir(express_img_dir)
bol_img_list = os.listdir(bol_img_dir)
dunya_img_list = os.listdir(dunya_img_dir)
_92_img_list = os.listdir(_92_img_dir)
dawn_img_list = os.listdir(dawn_img_dir)
ptv_img_list = os.listdir(ptv_img_dir)
aaj_img_list = os.listdir(aaj_img_dir)
print('Geo: {}\nAry: {}\nSama: {}\nExpress: {}\nBol: {}\nDunya: {}\n92: {}\nDawn: {}\nPTV: {}\nAaj: {}\n'.format(len(geo_img_list), 
                                                                                                                         len(ary_img_list),
                                                                                                                        len(sama_img_list),
                                                                                                                        len(express_img_list),
                                                                                                                        len(bol_img_list),
                                                                                                                        len(dunya_img_list),
                                                                                                                        len(_92_img_list),
                                                                                                                        len(dawn_img_list),
                                                                                                                        len(ptv_img_list),
                                                                                                                        len(aaj_img_list)))
