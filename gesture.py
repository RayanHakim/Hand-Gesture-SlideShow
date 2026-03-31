import cv2
import mediapipe as mp
import pyautogui
import time

# --- 1. SETUP MEDIAPIPE ---
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5
)

# --- 2. SETUP KAMERA ---
cap = cv2.VideoCapture(0)
width, height = 320, 240 # Ukuran diperkecil agar tidak menutupi materi PPT
cap.set(3, width)
cap.set(4, height)

zona_kiri = width // 3
zona_kanan = (width // 3) * 2
last_action = time.time()
cooldown = 1.5 

window_name = "Hand Gesture PPT Controller"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

# JURUS SAKTI: Membuat window selalu di depan (Always on Top)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

print("🚀 AI PPT Controller AKTIF!")
print("Tips: Klik slide PPT sekali agar fokus, lalu gunakan tangan.")

while True:
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            wrist = handLms.landmark[0]
            cx = int(wrist.x * width)
            
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
            cv2.circle(img, (cx, int(wrist.y * height)), 10, (0, 255, 0), -1)

            now = time.time()
            if now - last_action > cooldown:
                if cx > zona_kanan:
                    print("➡️ NEXT")
                    pyautogui.press('right') # Kirim ke sistem
                    last_action = now
                elif cx < zona_kiri:
                    print("⬅️ BACK")
                    pyautogui.press('left')
                    last_action = now

    # UI Ringkas
    cv2.line(img, (zona_kiri, 0), (zona_kiri, height), (200, 200, 200), 1)
    cv2.line(img, (zona_kanan, 0), (zona_kanan, height), (200, 200, 200), 1)
    
    cv2.imshow(window_name, img)
    
    # LOGIKA CLOSE: Bisa pakai 'q' ATAU klik tombol silang (X) di window
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()