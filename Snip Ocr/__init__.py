import sys

import cv2
from Image_OCR import ImageOcr
from PyQt5 import QtWidgets
from Snipper import SnipWidget


def main(*args, **kwargs):
    # Capturing Screenshot
    app = QtWidgets.QApplication(sys.argv)
    size = app.primaryScreen().size()
    snip = SnipWidget(size.width(), size.height())
    snip.show()
    app.aboutToQuit.connect(app.deleteLater)
    cv2.destroyAllWindows()
    app.exec_()
    image = snip.get_image()

    # Detecting Text
    img_ocr = ImageOcr(image)
    print(img_ocr.txt)
    sys.exit()


if __name__ == '__main__':
    main()
