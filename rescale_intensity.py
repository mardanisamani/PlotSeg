import numpy as np
import glob
import cv2
import matplotlib.pyplot as plt
import skimage.io as io

def apply_fn_to_img_without_overflow(f, im):
    """
    :param f: must take only an im as an argument.
    :param im: must be an np integer type image
    :return: transformed image, in original type.
    """

    max_val = np.iinfo(im.dtype).max
    return np.rint(np.clip(f(im.astype(np.float64)), 0, max_val)).astype(im.dtype)


im = io.imread ('/home/masi/Desktop/orthomosaic.tif')
r = im[:,:,0]
g = im[:,:,1]
b = im[:,:,2]
rgb = np.dstack((r,g,b,))
# print (im)
im20 = apply_fn_to_img_without_overflow(lambda img: img * 5, rgb)
cv2.imwrite('/home/masi/Desktop/rgb.tif', im20)
# rgb = sorted(glob.glob('/home/masi/Desktop/rescale/*.png'))
# nir = sorted(glob.glob('/home/masi/Desktop/rescale/*.png'))
# t= 0
# for i in nir:
#     im = cv2.imread (i)
#     #print (im)
#     im20 = apply_fn_to_img_without_overflow(lambda img: img * 4, im)
#     cv2.imwrite ('/home/masi/Desktop/rescale/wheat_rgb/' + 'wheat_{0}_rgb.png'.format(t), im20)
#     t += 1

# red = cv2.imread('/home/masi/Desktop/1138_real_B.png')
# red = red[120:904, 120:904]
# cv2.imwrite('/home/masi/Desktop/nir.png', red)
