from ctypes import *
from cv2 import cv

# ctypes IplImage
class cIplImage(Structure):
    _fields_ = [("nSize", c_int),
                ("ID", c_int),
                ("nChannels", c_int),
                ("alphaChannel", c_int),
                ("depth", c_int),
                ("colorModel", c_char * 4),
                ("channelSeq", c_char * 4),
                ("dataOrder", c_int),
                ("origin", c_int),
                ("align", c_int),
                ("width", c_int),
                ("height", c_int),
                ("roi", c_void_p),
                ("maskROI", c_void_p),
                ("imageID", c_void_p),
                ("tileInfo", c_void_p),
                ("imageSize", c_int),
                ("imageData", POINTER(c_char)),
                ("widthStep", c_int),
                ("BorderMode", c_int * 4),
                ("BorderConst", c_int * 4),
                ("imageDataOrigin", c_char_p)]

# load DLL containing needed OpenCV functions
libr = cdll.LoadLibrary("OpenCV_test_DLL.dll")
cvSetData = libr.aux_cvSetData
cvCreateImageHeader = libr.aux_cvCreateImageHeader
cvCvtColor = libr.aux_cvCvtColor
cvCopy = libr.aux_cvCopy
cvReleaseImage = libr.aux_cvReleaseImage
cvReleaseImageHeader = libr.aux_cvReleaseImageHeader
# set return types for library functions
cvSetData.restype = None
cvCreateImageHeader.restype = POINTER(cIplImage)
cvCvtColor.restype = POINTER(cIplImage)
cvCopy.restype = None
cvReleaseImage.restype = None
cvReleaseImageHeader.restype = None
#print "auxlib loaded"

# convert Python PIL to ctypes Ipl
def PIL2Ipl(pil_img):
    """Converts a PIL image to the OpenCV/IplImage data format.

    Supported input image formats are:
        RGB
        L
        F
    """

    # mode dictionary:
    # (pil_mode : (ipl_depth, ipl_channels)
    mode_list = {
        "RGB" : (cv.IPL_DEPTH_8U, 3),
        "L"   : (cv.IPL_DEPTH_8U, 1),
        "F"   : (cv.IPL_DEPTH_32F, 1)
        }

    if not mode_list.has_key(pil_img.mode):
        raise ValueError, 'unknown or unsupported input mode'

    depth = c_int(mode_list[pil_img.mode][0])
    channels = c_int(mode_list[pil_img.mode][1])
    height = c_int(pil_img.size[1])
    width = c_int(pil_img.size[0])
    data = pil_img.tostring()

    ipl_img = cvCreateImageHeader(width, height, depth, channels);
    cvSetData(ipl_img, create_string_buffer(data,len(data)), c_int(width.value * channels.value))
    brg_img = cvCvtColor(ipl_img,cv.CV_RGB2BGR)
    cvReleaseImageHeader(byref(ipl_img))
    return brg_img