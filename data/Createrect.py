import cv2
def create_rectangle(image, x, y, height, width):
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
    return image
