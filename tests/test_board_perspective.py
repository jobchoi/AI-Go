import cv2
import numpy as np

# image_path = "samples/img/state_test_board_roi.jpg"
image_path = "samples/img/state_test_empty0.jpg"


board = cv2.imread(image_path)

if board is None:
    raise RuntimeError("ROI 이미지를 불러오지 못했습니다.")

print("ROI 이미지 로드 성공")
print(f"board shape: {board.shape}")

# ROI 이미지 기준 바둑판 네 꼭짓점
src_points = np.float32([
    [21,0],  # top-left
    [502, 21],  # bottom-left
    [0, 390],  # bottom-left   
    [505,403]  # bottom-right 
])

print(f"src_points: {src_points}")
print(f"src_points dtype: {src_points.dtype}")
print(f"src_points shape: {src_points.shape}")

BOARD_SIZE = 800

dst_points = np.float32([
    [0,0],
    [BOARD_SIZE-1,0],
    [0, BOARD_SIZE-1],
    [BOARD_SIZE-1, BOARD_SIZE-1]
])

print(f"dst_points dtype: {dst_points.dtype}")
print(f"dst_points shape: {dst_points.shape}")

matrix = cv2.getPerspectiveTransform(src_points, dst_points)
warped = cv2.warpPerspective(board, matrix, (BOARD_SIZE, BOARD_SIZE))

# Perspective transformed 결과저장
output_path = "samples/img/state_test_board_perspective.jpg"

success = cv2.imwrite(output_path, warped)
if not success:
    raise RuntimeError("Perspective 변환 이미지를 저장하지 못했습니다.")

print(f"Perspective 변환 이미지 저장 성공: {output_path}")
print(f"warped shape: {warped.shape}")