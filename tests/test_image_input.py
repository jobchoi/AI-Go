import cv2

image_path = "samples/img/state_test0.jpg"

frame = cv2.imread(image_path)

if frame is None:
    raise RuntimeError("이미지를 불러오지 못했습니다.")

print("이미지 로드 성공")
print(frame.shape)
print(f"shape:{frame.shape}")

# 처리할 이미지의 가로 크기
target_width = 1000

height = int(
    frame.shape[0] * (target_width / frame.shape[1])
)
resized_frame = cv2.resize(
    frame, 
    (target_width, height)
)

print(f"resized shape:{resized_frame.shape}")

# cv2.imshow("AI-Go Sample", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()