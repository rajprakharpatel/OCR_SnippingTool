import subprocess
import sys

import cv2
import numpy as np
import pytesseract


class ImageOcr:
    def __init__(self, image, grayscale=True, threshold=True,
                 invert=True, blur=False, dilate=False, erode=False,
                 opening=False, canny=False, de_skew=False):
        self.image = image

        if grayscale:
            self.image = self.get_grayscale()
        if threshold:
            self.image = self.threshold()
        if invert:
            self.image = self.invert()
        if blur:
            self.image = self.remove_noise()
        if dilate:
            self.image = self.dilate()
        if erode:
            self.image = self.erode()
        if opening:
            self.image = self.opening()
        if canny:
            self.image = self.canny()
        if de_skew:
            self.image = self.de_skew()

        # cv2.imshow('processed img', self.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.txt = self.get_text()

    def invert(self):
        return cv2.bitwise_not(self.image)

    # get grayscale image
    def get_grayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(self):
        return cv2.medianBlur(self.image, 5)

    # threshold
    def threshold(self):
        return cv2.threshold(self.image, 250, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # return cv2.adaptiveThreshold(np.array(self.image), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
        # 11,2)

    # dilation
    def dilate(self):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.dilate(self.image, kernel, iterations=1)

    # erosion
    def erode(self):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.erode(self.image, kernel, iterations=1)

    # opening - erosion followed by dilation
    def opening(self):
        kernel = np.ones((5, 5), np.uint8)
        return cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)

    # canny edge detection
    def canny(self):
        return cv2.Canny(self.image, 100, 200)

    # skew correction
    def de_skew(self):
        coords = np.column_stack(np.where(self.image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(self.image, M, (w, h), flags=cv2.INTER_CUBIC,
                                 borderMode=cv2.BORDER_REPLICATE)
        return rotated

    # template matching
    def match_template(self, template):
        return cv2.matchTemplate(self.image, template, cv2.TM_CCOEFF_NORMED)

    def get_text(self):
        custom_config = r'--oem 3 --psm 6'
        return pytesseract.image_to_string(self.image, config=custom_config)

    def to_clipboard(self):
        if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'win64':
            subprocess.Popen(['clip'], encoding='utf8',
                             stdin=subprocess.PIPE).communicate(self.txt)
        elif sys.platform == 'linux':
            subprocess.Popen(['xclip'], encoding='utf8',
                             stdin=subprocess.PIPE).communicate(self.txt)
        else:
            raise Exception('Platform not supported')


if __name__ == '__main__':
    image = cv2.imread('/capture.png')
    img_ocr = ImageOcr(image)
    print(img_ocr.get_text())
