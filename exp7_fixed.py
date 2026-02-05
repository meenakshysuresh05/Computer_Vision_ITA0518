import cv2
import os

video_path = r"C:\Users\menak\Downloads\image\WhatsApp Video 2026-02-05 at 1.28.17 PM.mp4"

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video not found: {video_path}")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise FileNotFoundError("Cannot open video file. Check the path and that codecs are installed.")

print("Controls:")
print("- Normal speed: Press 'n'")
print("- Slow motion: Press 's'")
print("- Fast motion: Press 'f'")
print("- Quit: Press 'q'")

mode = 'n'
while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    cv2.imshow("Video Player", frame)
    
    if mode == 'n':
        delay = 30
    elif mode == 's':
        delay = 80
    elif mode == 'f':
        delay = 10

    key = cv2.waitKey(delay) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n'):
        mode = 'n'
        print("Normal speed")
    elif key == ord('s'):
        mode = 's'
        print("Slow motion")
    elif key == ord('f'):
        mode = 'f'
        print("Fast motion")

cap.release()
cv2.destroyAllWindows()
