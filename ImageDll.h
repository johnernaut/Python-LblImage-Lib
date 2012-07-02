#include "opencv2/opencv.hpp"

extern "C"  //Tells the compile to use C-linkage for the next scope.
{
    // Returns image loaded from location
    __declspec(dllexport) IplImage* Load(char* dir);

    // Show image
    __declspec(dllexport) void Show(IplImage* img);

    // Auxiliary functions
    __declspec(dllexport) void aux_cvSetData(CvArr* arr, void* data, int step);
    __declspec(dllexport) IplImage* aux_cvCreateImageHeader(int width, int height, int depth, int channels);
    __declspec(dllexport) IplImage* aux_cvCvtColor(const IplImage* src, int code);
    __declspec(dllexport) void aux_cvCopy(const CvArr* src, CvArr* dst);
    __declspec(dllexport) void aux_cvReleaseImage(IplImage** image);
    __declspec(dllexport) void aux_cvReleaseImageHeader(IplImage** image);
}