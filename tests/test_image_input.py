import cv2

image_path = "samples/img/state_test0.jpg"

frame = cv2.imread(image_path)

if frame is None:
    raise RuntimeError("이미지를 불러오지 못했습니다.")

print("이미지 로드 성공")
print(frame.shape)
print(f"shape:{frame.shape}")

# cv2.imshow("AI-Go Sample", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()