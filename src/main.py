import cv2

# 스마트폰 IP Webcam 주소 (주의: 주소 맨 끝에 '/video'를 꼭 붙여야 영상 데이터만 가져옵니다)
# 예시: url = 'http://192.168.0.123:8080/video'
url = 'http://192.168.173.2.:8080/video' 

# 1. 영상 스트림(카메라) 연결
print(f"{url} 에 연결을 시도합니다...")
cap = cv2.VideoCapture(url)

# 2. 딱 한 장(단일 프레임)만 읽어오기
ret, frame = cap.read()

if ret:
    print("성공적으로 프레임을 가져왔습니다!")
    # 3. 화면에 출력
    cv2.imshow('AI-Go Single Frame Test', frame)
    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)  # 사용자가 아무 키나 누를 때까지 화면 유지
else:
    print("프레임을 가져오지 못했습니다. URL 주소나 네트워크 연결을 다시 확인해 주세요.")

# 4. 자원 해제 및 창 안전하게 닫기
cap.release()
cv2.destroyAllWindows()