import threading
import time

def int_sleep():
    for _ in range(1, 600):
        time.sleep(1)
        print("sleep")

def main():
    thread = threading.Thread(target=int_sleep)
    thread.daemon = True
    thread.start()
    time.sleep(2)
    print("main thread end...")

thread = threading.Thread(target=main)
thread.daemon = True
thread.start()

