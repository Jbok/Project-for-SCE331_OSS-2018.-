/*
 * Developed by Taeklim Kim
 */

#include <tesseract/baseapi.h>
#include <tesseract/publictypes.h>
#include <leptonica/allheaders.h>

#define FILE_ 25

using namespace std;

int main()
{
    char *outText;

    tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();
   
    // Initialize tesseract-ocr with Kor
    if (api->Init("/usr/share/tesseract-ocr/tessdata", "kor")) {
      fprintf(stderr, "Could not initialize tesseract.\n");
	    exit(1);
    }
    
    // To Iterate each Image Frames
    for (int i = 0; i < FILE_; i++) {
      api->Init("/usr/share/tesseract-ocr/tessdata", "kor");

      string input_img = "/home/tlimkim/workspace/kbo/opencv_src/sample_frame_image/sample_2018/";
      
      //string input_img = "/home/tlimkim/workspace/kbo/image/vfc_sample_2/";
      string num = std::to_string(i);
      
      input_img = input_img + num + ".jpg";

      const char * str = input_img.c_str();

      //printf("%s \n", str);
      Pix *image = pixRead(str);

      //api->setPageSegMode(TessBaseAPI.PageSegMode.PSM_SINGLE_LINE);
      api->SetImage(image);
      api->SetPageSegMode(tesseract::PSM_SINGLE_WORD);
      outText = api->GetUTF8Text();

      printf("Batter Name: %s \n", outText);

      api->End();
      delete [] outText;
      pixDestroy(&image);
    }

    return 0;
}
