import cv2
import numpy as np

image_path = "samples/img/state_test_board_roi.jpg"

board = cv2.imread(image_path)

if board is None:
    raise RuntimeError("ROI 이미지를 불러오지 못했습니다.")

print("ROI 이미지 로드 성공")
print(f"board shape: {board.shape}")

# ROI 이미지 기준 바둑판 네 꼭짓점
# src_points = np.float32([
#     [40, 21],       # top-left
#     [897, 37],      # top-right
#     [900, 860],    # bottom-right
#     [75, 848]       # bottom-left
# ])
# ROI 이미지 기준 바둑판 네 꼭짓점 - Master img 기준 좌표
src_points = np.array([
    [20, 0],       # top-left
    [372, 7],      # top-right
    [370, 340],    # bottom-right
    [20, 342]      # bottom-left
], dtype=np.float32)

BOARD_SIZE = 800

dst_points = np.float32([
    [0, 0],
    [BOARD_SIZE - 1, 0],
    [BOARD_SIZE - 1, BOARD_SIZE - 1],
    [0, BOARD_SIZE - 1]
])

matrix = cv2.getPerspectiveTransform(
    src_points,
    dst_points
)

warped = cv2.warpPerspective(
    board,
    matrix,
    (BOARD_SIZE, BOARD_SIZE)
)

print("Perspective 변환 완료")
print(f"warped shape: {warped.shape}")

output_path = "samples/img/state_test_board_perspective.jpg"

if not cv2.imwrite(output_path, warped):
    raise RuntimeError("Perspective 이미지 저장 실패")

print(f"Perspective image saved to {output_path}")