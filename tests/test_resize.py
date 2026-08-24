import cv2

TEST_SIZE = 1000

image_path = "samples/img/state_test0.jpg"

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

# Board ROI
x1 = 200
y1 = 27
x2 = 705
y2 = 430

board = resized_frame[y1:y2, x1:x2]
print(f"Board shape: {board.shape}")    
output_path = "samples/img/state_test_board_roi.jpg"
cv2.imwrite(output_path, board)
print(f"Board ROI saved to {output_path}")