from time import sleep
from ctypes import *
from modules.acquisition import InitCamera, GetImage
from modules.utils import struct
import cv2.cv as cv
from modules.ipl import *

# load DLL containing image functions
print "Loading shared library with C functions...",
image_lib = cdll.LoadLibrary("OpenCV_test_DLL.dll")
print "Done."
# get function handles
print "Loading functions of library...",
image_load = image_lib.Load
image_show = image_lib.Show
cvReleaseImage = image_lib.aux_cvReleaseImage
# set return type for functions (because ctypes default is int)
image_load.restype = c_void_p
image_show.restype = None
cvReleaseImage.restype = None
print "Done."

# initialize source
print "Initializing camera",
source = struct()
InitCamera(source)
print "Done."

# show video
while (1):
    # get image as PIL image
    img = GetImage(source)
    # transform image to OpenCV IplImage
    cv_img = PIL2Ipl(img)
    # show image using OpenCV highgui lib
    image_show(cv_img)
    # release memory
    cvReleaseImage(byref(cv_img))