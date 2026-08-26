import cv2

TEST_SIZE = 1000

image_path = "samples/img/state_test_empty1.jpg"

frame = cv2.imread(image_path)

if frame is None:
    raise RuntimeError("이미지를 불러오지 못했습니다.")

print("이미지 로드 성공")
print(f"원본 shape: {frame.shape}")

target_width = TEST_SIZE

height = int(
    frame.shape[0] * target_width / frame.shape[1]
)

resized_frame = cv2.resize(
    frame,
    (target_width, height)
)

print(f"resize shape: {resized_frame.shape}")

output_path = "samples/img/state_test_empty1_resized.jpg"

if not cv2.imwrite(output_path, resized_frame):
    raise RuntimeError("resize 이미지 저장 실패")

print(f"resize image saved to {output_path}")