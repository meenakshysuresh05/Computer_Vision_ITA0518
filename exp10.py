import cv2
import os

image_path = r"C:\Users\menak\Downloads\image\drib.jpg"
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

image = cv2.imread(image_path)
if image is None:
    raise ValueError("Failed to load image")

(h, w) = image.shape[:2]
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", image)
cv2.imshow("90° Clockwise Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()