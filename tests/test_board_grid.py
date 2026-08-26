import cv2
import numpy as np

image_path = "samples/img/state_test_board_perspective.jpg"
board = cv2.imread(image_path)

if board is None:
    raise RuntimeError("Perspective 변환 이미지를 불러오지 못했습니다.")    

print("Perspective 변환 이미지 로드 성공")
print(f"board shape: {board.shape}")

gray = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)

print("Grayscale 변환 성공")
print(f"gray shape: {gray.shape}")

# Edge detection
edges = cv2.Canny(gray, 50, 150)
print("Edge detection 성공")
print(f"edges shape: {edges.shape}")

edges_output_path = "samples/img/state_test_board_edges.jpg"

if not cv2.imwrite(edges_output_path, edges):
    raise RuntimeError("Edge detection 이미지를 저장하지 못했습니다.")

print(f"Edge detection 이미지 저장 성공: {edges_output_path}")

# Hough Line Transform
lines = cv2.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi / 180,
    threshold=100,
    minLineLength=300,
    maxLineGap=20
)

if lines is None:
    raise RuntimeError("Hough Line Transform에서 선을 찾지 못했습니다.")

print(f"Found {len(lines)} lines using Hough Line Transform.")

# debugging information
print(f"lines type: {type(lines)}")
print(f"lines shape: {lines.shape}")
print(f"lines dtype: {lines.dtype}")
print(f"first line: {lines[0]}")

line_image = board.copy()

for line in lines:
    # x1, y1, x2, y2 = line[0]
    x1, y1, x2, y2 = line
    cv2.line(
        line_image, 
        (x1, y1), 
        (x2, y2), 
        (0, 0, 255), 
        2
    )

# Save the image with detected lines
line_output_path = "samples/img/state_test_board_lines.jpg"
if not cv2.imwrite(line_output_path, line_image):
    raise RuntimeError("Line detection 이미지를 저장하지 못했습니다.")

print(f"Line detection 이미지 저장 성공: {line_output_path}")