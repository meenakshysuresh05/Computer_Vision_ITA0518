import cv2
import os

image_path = r"C:\Users\menak\Downloads\image\download (1).jpg"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at path: {image_path}")

image = cv2.imread(image_path)

if image is None:
    raise ValueError(f"Failed to load image. File may be corrupted or in an unsupported format: {image_path}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

output_path = r"C:\Users\menak\Downloads\grayscale_output.jpg"
cv2.imwrite(output_path, gray_image)
print(f"✓ Grayscale image saved to: {output_path}")

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Original shape: {image.shape} | Grayscale shape: {gray_image.shape}")
print("Grayscale conversion complete! ✅")
