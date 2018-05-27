/*
 * Developed by Taeklim Kim
 * Use Opensource Tesseract API
 * All Licenses are explained at LICENSE.md
 */

#include <tesseract/baseapi.h>
#include <tesseract/publictypes.h>
#include <leptonica/allheaders.h>

#define FILE_ 139 // Number of Frame Image files

using namespace std;

int main()
{
  char *outText;
  string str_outArray[FILE_][1]; // String Array for Find the Recognition Word
  int flag[FILE_];

  tesseract::TessBaseAPI *api = new tesseract::TessBaseAPI();

  // Initialize tesseract-ocr with Kor Lang
  if (api->Init("/usr/share/tesseract-ocr/tessdata", "kor")) {
    fprintf(stderr, "Could not initialize tesseract.\n");
    exit(1);
  }

  // Iterate for each Image Frames
  for (int i = 0; i < FILE_; i++) {
    api->Init("/usr/share/tesseract-ocr/tessdata", "kor");

    //string input_img = "/home/tlimkim/workspace/kbo/opencv_src/sample_frame_image/sample_2018/";
    string input_img = "/home/tlimkim/workspace/kbo/image/vfc_sample_2/"; // path for KIA Video

    string num = std::to_string(i); // for number of image file
    input_img = input_img + num + ".jpg";
    const char * str = input_img.c_str(); // String to char

    // Reading Image by 'str' path
    Pix *image = pixRead(str);

    api->SetImage(image);
    api->SetPageSegMode(tesseract::PSM_SINGLE_WORD);
    api->SetVariable("tessedit_char_blacklist", "[]_\n-1234567890~/");
    outText = api->GetUTF8Text();

    //printf("Result for each frame: %s", outText); // regonized word from the image

    string str_outText(outText);

    str_outArray[i][0] = str_outText; // assign the string of outText to Array
    flag[i] = 0;

    for (int j = 0; j <= FILE_; j++) {
      if (str_outArray[j][0] == str_outText) {
        flag[i]++;
      }
    }

    api->End();
    delete [] outText;
    pixDestroy(&image); // end of recognize of each frame
  }

  // This section is to find the mostly recognized word
  int max = flag[0];
  int idx = 0;

  for (int i = 1; i < FILE_; i++) {
    if (max < flag[i] && str_outArray[i][0] != "") {
      max = flag[i];
      idx = i;
    }
  }
  
  const char *str = str_outArray[idx][0].c_str();
  printf("Batter Name (Final Result): %s", str);

  return 0;
}
