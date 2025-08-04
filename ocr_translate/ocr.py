from PIL import Image
import numpy as np

def run_ocr(pil_image):
    image = np.array(pil_image.convert("RGB"))  # Convert to OpenCV format
    text = ocr_image(image)  # Uses Crivella's main function
    return text
