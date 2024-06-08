import keyboard
import mouse
import time


def change():
    global work, start_time, elapsed_time
    work = not work
    if work:
        start_time = time.time()
        elapsed_time = 0


work = False
start_time = 0
elapsed_time = 0

#заупск и остановка на клвишу '/'
keyboard.add_hotkey('/', change)

while True:
    if work:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= 300:  # 5 минут работы
            print("Приостановка на 15 минут")
            work = False
            time.sleep(900)  # 15 минут отдыха
            print("Возобновление работы")
            work = True
            start_time = time.time()
            elapsed_time = 0

        mouse.click(button='left')
        time.sleep(0.1)
