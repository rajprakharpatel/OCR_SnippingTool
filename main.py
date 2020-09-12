import sys

# import tess_env_setup
from PyQt5 import QtWidgets
from Snip_Ocr import Image_OCR
from Snip_Ocr import Snipper


def main(*args, **kwargs):
    # tess_env_setup.main()

    # Capturing Screenshot
    app = QtWidgets.QApplication(sys.argv)
    size = app.primaryScreen().size()
    snip = Snipper.SnipWidget(size.width(), size.height())
    snip.show()
    app.aboutToQuit.connect(app.deleteLater)
    app.exec_()
    image = snip.get_image()

    # Detecting Text
    img_ocr = Image_OCR.ImageOcr(image)
    img_ocr.to_clipboard()
    print(img_ocr.txt)
    sys.exit()


if __name__ == '__main__':
    main()
