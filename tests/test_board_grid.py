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

# Hough parameters
HOUGH_THRESHOLD = 100
HOUGH_MIN_LINE_LENGTH = 300
HOUGH_MAX_LINE_GAP = 50

# Hough Line Transform
lines = cv2.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi / 180,
    threshold=HOUGH_THRESHOLD,
    minLineLength=HOUGH_MIN_LINE_LENGTH,
    maxLineGap=HOUGH_MAX_LINE_GAP
)

print("[GRID][HOUGH]")
print(f"  threshold     : {HOUGH_THRESHOLD}")
print(f"  minLineLength : {HOUGH_MIN_LINE_LENGTH}")
print(f"  maxLineGap    : {HOUGH_MAX_LINE_GAP}")
print(f"  lines         : {len(lines)}")

if lines is None:
    raise RuntimeError("Hough Line Transform에서 선을 찾지 못했습니다.")

print(f"Found {len(lines)} lines using Hough Line Transform.")

# debugging information
print(f"lines type: {type(lines)}")
print(f"lines shape: {lines.shape}")
print(f"lines dtype: {lines.dtype}")
print(f"first line: {lines[0]}")

horizontal_lines = []
vertical_lines = []

for line in lines:
    x1, y1, x2, y2 = line

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        horizontal_lines.append(line)
    else:
        vertical_lines.append(line)

print(f"[GRID] Hough lines      : {len(lines)}")
print(f"[GRID] Horizontal lines : {len(horizontal_lines)}")
print(f"[GRID] Vertical lines   : {len(vertical_lines)}")



line_image = board.copy()

# Horizontal lines
for i, line in enumerate(horizontal_lines, start=1):
    x1, y1, x2, y2 = line

    cv2.line(
        line_image,
        (x1, y1),
        (x2, y2),
        (0, 0, 255),
        2
    )

    cv2.putText(
        line_image,
        f"H{i:02d}",
        (x1, y1 - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 0, 255),
        1
    )


# Vertical lines
for i, line in enumerate(vertical_lines, start=1):
    x1, y1, x2, y2 = line

    cv2.line(
        line_image,
        (x1, y1),
        (x2, y2),
        (255, 0, 0),
        2
    )

    cv2.putText(
        line_image,
        f"V{i:02d}",
        (x1 + 5, y1),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        1
    )    

print("[GRID][HORIZONTAL]")

for i, line in enumerate(horizontal_lines, start=1):
    x1, y1, x2, y2 = line
    print(f"  H{i:02d}: ({x1}, {y1}) -> ({x2}, {y2})")


print("[GRID][VERTICAL]")

for i, line in enumerate(vertical_lines, start=1):
    x1, y1, x2, y2 = line
    print(f"  V{i:02d}: ({x1}, {y1}) -> ({x2}, {y2})")

print("[GRID][SEGMENT LENGTH]")

for i, line in enumerate(horizontal_lines, start=1):
    x1, y1, x2, y2 = line

    length = np.hypot(x2 - x1, y2 - y1)

    print(f"  H{i:02d}: {length:.1f}px")

for i, line in enumerate(vertical_lines, start=1):
    x1, y1, x2, y2 = line

    length = np.hypot(x2 - x1, y2 - y1)

    print(f"  V{i:02d}: {length:.1f}px")



# Save the image with detected lines
line_output_path = "samples/img/state_test_board_grid_lines.jpg"

if not cv2.imwrite(line_output_path, line_image):
    raise RuntimeError("Line detection 이미지를 저장하지 못했습니다.")

print(f"[GRID] Visualization saved : {line_output_path}")

