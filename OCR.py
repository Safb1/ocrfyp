try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

#---Configuration Of Tesseract---
pytesseract.pytesseract.tesseract = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text  # Then we will print the text in the image
    print(ocr_core('/Users/safabutt/PycharmProjects/OCRfyp/images/demo.png'))