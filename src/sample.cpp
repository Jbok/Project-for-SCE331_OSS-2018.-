#include <baseapi.h>
// #include <allheaders.h>
#include <sys/time.h>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;

int main(int argc, char* argv[]) {

    // initilize tesseract OCR engine
    tesseract::TessBaseAPI *myOCR = new tesseract::TessBaseAPI();

    printf("Tesseract-ocr version: %s\n", myOCR->Version());

    if (myOCR->Init(NULL, "eng")) {
	fprintf(stderr, "Could not initialize tesseract.\n");
	exit(1);
    }

    tesseract::PageSegMode pagesegmode = static_cast<tesseract::PageSegMode>(7); // treat the image as a single text line
    myOCR->SetPageSegMode(pagesegmode);

    // read iamge
    namedWindow("sample", 0);
    Mat image = imread("./sample.png", 0);

    // set region of interest (ROI), i.e. regions that contain text
    Rect text1ROI(80, 50, 800, 110);
    Rect text2ROI(190, 200, 550, 50);

    // recognize text
    myOCR->TesseractRect(image.data, 1, image.step1(), text1ROI.x, text1ROI.y, text1ROI.width, text1ROI.height);
    const char *text1 = myOCR->GetUTF8Text();

    myOCR->TesseractRect(image.data, 1, image.step1(), text2ROI.x, text2ROI.y, text2ROI.width, text2ROI.height);
    const char *text2 = myOCR->GetUTF8Text();

    // remove "newline"

    // print found text
    printf("found text1: \n");
    printf("%s \n", text1);
    printf("\n");

    printf("found text2: \n");
    printf("%s \n", text2);
    printf("\n");


    return 0;
}
