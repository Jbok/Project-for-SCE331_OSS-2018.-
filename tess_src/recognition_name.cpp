/*
 * Developed by Taeklim Kim
 */

#include <tesseract/baseapi.h>
#include <leptonica/allheaders.h>

#define FILE_ 139

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
/*
    // Open input image with leptonica library
    string input;
    input = "/home/tlimkim/workspace/kbo/image/vfc_sample_2/0.jpg";
    
    const char* c = input.c_str();

    //input = "jpg";
    //Pix *image = pixRead("/home/tlimkim/workspace/kbo/image/vfc_sample_2/image_00000000%d.jpg", 0);
    Pix *image = pixRead(c);
  
    api->SetImage(image);
    // Get OCR result
    outText = api->GetUTF8Text();

    printf("Batter Name: %s \n", outText);

    // Destroy used object and release memory
    api->End();
    delete [] outText;
    pixDestroy(&image);
    */
    for (int i = 0; i < FILE_; i++) {
      api->Init("/usr/share/tesseract-ocr/tessdata", "kor");

      string input_img = "/home/tlimkim/workspace/kbo/image/vfc_sample_2/";
      string num = std::to_string(i);
      
      input_img = input_img + num + ".jpg";

      const char * str = input_img.c_str();

      //printf("%s \n", str);
      Pix *image = pixRead(str);
      api->SetImage(image);

      outText = api->GetUTF8Text();

      printf("Batter Name: %s \n", outText);

      api->End();
      delete [] outText;
      pixDestroy(&image);
    }

    return 0;
}
