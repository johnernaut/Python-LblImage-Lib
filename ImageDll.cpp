#include "ImageDll.h"

using namespace std;

extern "C"  //Tells the compile to use C-linkage for the next scope.
{
    IplImage* Load(char* dir)
    {
        return cvLoadImage(dir, CV_LOAD_IMAGE_COLOR);
    }

    void Show(IplImage* img)
    {
        cvShowImage("image", img);
        cvWaitKey(5);
    }

    void aux_cvSetData(CvArr* arr, void* data, int step)
    {
        cvSetData(arr,data,step);
    }

    IplImage* aux_cvCreateImageHeader(int width, int height, int depth, int channels)
    {
        return cvCreateImageHeader(cvSize(width,height), depth, channels);
    }

    IplImage* aux_cvCvtColor(const IplImage* src, int code)
    {
        IplImage* dst = cvCreateImage(cvSize(src->width,src->height),src->depth,src->nChannels);
        cvCvtColor(src, dst, code);
        return dst;
    }

    void aux_cvCopy(const CvArr* src, CvArr* dst)
    {
        cvCopy(src, dst, NULL);
    }

    void aux_cvReleaseImage(IplImage** image)
    {
        cvReleaseImage(image);
    }

    void aux_cvReleaseImageHeader(IplImage** image)
    {
        cvReleaseImageHeader(image);
    }
}