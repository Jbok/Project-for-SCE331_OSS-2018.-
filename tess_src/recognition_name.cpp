#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

int main()
{
    char *outText;

    tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
    // Initialize tesseract-ocr with English, without specifying tessdata path
    if (api->Init("/usr/share/tesseract-ocr/tessdata", "kor")) {
	fprintf(stderr, "Could not initialize tesseract.\n");
	exit(1);
    }

    // Open input image with leptonica library
    Pix *image = pixRead("./sample_pixel_image.jpg");
    
    api->SetImage(image);
    // Get OCR result
    api->SetRectangle(455, 685, 125, 55);
    outText = api->GetUTF8Text();

    printf("Batter Name: %s \n", outText);

    // Destroy used object and release memory
    api->End();
    delete [] outText;
    pixDestroy(&image);

    return 0;
}
