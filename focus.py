import time

while True:
    print(time.strftime("%H:%M:%S", time.localtime()), end='\r')
    time.sleep(1)
