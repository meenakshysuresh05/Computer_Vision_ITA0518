import cv2
import os

image_path = r"C:\Users\menak\Downloads\image\drib.jpg"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at path: {image_path}")

image = cv2.imread(image_path)

if image is None:
    raise ValueError(f"Failed to load image. File may be corrupted or in an unsupported format: {image_path}")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

output_path = r"C:\Users\menak\Downloads\blurred_output.jpg"
cv2.imwrite(output_path, blurred_image)
print(f"Blurred image saved to: {output_path}")

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Gaussian blur applied successfully!")