# from PIL import Image
# import glob
# import os

# folder = './test_folder/**/'
# new_folder = './processed_folder/'
# imList = glob.glob(folder + '*.jpg', recursive=True)

# print('Processing')

# os.makedirs(new_folder)
# print(imList)
# for img in imList:
#     im = Image.open(img)
#     fileName, fileExt = os.path.splitext(img)
#     if len(fileName.split('/')) > 3:
#         if not os.path.exists(new_folder + fileName.split('/')[2] + '/'):
#             os.makedirs(new_folder + fileName.split('/')[2] + '/')
#         im.save(new_folder + fileName.split('/')[2] + '/' + fileName.split('/')[3] + '.png')
#     else:
#         im.save(new_folder + fileName.split('/')[2] + '.png')

# print('Done!')

from skimage.color import rgb2gray, label2rgb
from skimage.filters import sobel, threshold_otsu
from skimage.io import imread, imsave
from skimage import img_as_uint
import scipy.misc
from PIL import Image
import glob
import os

folder = './flower_data/**/'
new_folder = './processed_folder/'
imList = glob.glob(folder + '*.jpg', recursive=True)

print('Processing')
os.makedirs(new_folder)

for img in imList:
    image = rgb2gray(imread(img))
    thresh = threshold_otsu(image)
    binary = image > thresh
    fileName, fileExt = os.path.splitext(img)
    if len(fileName.split('/')) > 3:
        save_path = new_folder + fileName.split('/')[2]
        print(fileName.split('/'))
        for x in range(3, len(fileName.split('/')) - 1):
            new_save_path = save_path + '/' + fileName.split('/')[x]
            if not os.path.exists(new_save_path):
                os.makedirs(new_save_path)
                imsave(new_save_path + '/' + fileName.split('/')[-1] + '.jpg', img_as_uint(binary))
            else:
                imsave(new_save_path + '/' + fileName.split('/')[-1] + '.jpg', img_as_uint(binary))
    else:
        imsave(new_folder + fileName.split('/')[2] + '.jpg', img_as_uint(binary))

print('Done!')