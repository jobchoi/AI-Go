import cv2

image_path = "samples/img/state_test_empty1_resized.jpg"

frame = cv2.imread(image_path)

if frame is None:
    raise RuntimeError("resize 이미지를 불러오지 못했습니다.")

print("Resize 이미지 로드 성공")
print(f"image shape: {frame.shape}")

# Board ROI
# resize 이미지 기준 좌표
# x1 = 0
# y1 = 490
# x2 = 920
# y2 = 1400

# Master img points
x1 = 200
y1 = 60
x2 = 600
y2 = 430

board = frame[y1:y2, x1:x2]

print(f"Board ROI shape: {board.shape}")

output_path = "samples/img/state_test_board_roi.jpg"

if not cv2.imwrite(output_path, board):
    raise RuntimeError("ROI 저장 실패")

print(f"Board ROI saved to {output_path}")