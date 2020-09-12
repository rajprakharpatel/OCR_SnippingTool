import os


def main():
    TESSDATA_ENV = 'TESSDATA_PREFIX'
    TESSDATA_PATH1 = 'C:/Program Files/Tesseract-OCR/tessdata'
    TESSDATA_PATH2 = 'C:\\Program Files\\Tesseract-OCR\\tessdata'
    TESSOCR_ENV = 'PATH'
    TESSOCR_PATH1 = 'C:/Program Files/Tesseract-OCR'
    TESSOCR_PATH2 = 'C:\\Program Files\\Tesseract-OCR'

    if os.environ.get(TESSDATA_ENV) not in [TESSDATA_PATH1, TESSDATA_PATH2]:
        os.environ[TESSDATA_ENV] = TESSDATA_PATH2
    if os.environ.get(TESSOCR_ENV).find(TESSOCR_PATH1) == -1 and -1 == os.environ.get(TESSOCR_ENV).find(TESSOCR_PATH2):
        os.environ[TESSOCR_ENV] += os.pathsep + TESSOCR_PATH2


if __name__ == '__main__':
    # sys.path.extend('C:/Program Files/Tesseract-OCR')
    # os.environ['TESSDATA_PREFIX'] = 'C:/Program Files/Tesseract-OCR/tessdata'
    main()
