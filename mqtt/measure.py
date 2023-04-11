import time
import threading

# 타이머가 호출할 함수
def my_function():
    print("타이머 실행")

# 5초 타이머
duration = 5
t = threading.Timer(duration, my_function)
t.start()  # 타이머 시작
t.join()  # 타이머가 종료될 때까지 대기
print("타이머 종료")
def measure_sensor_data(sensor, repeat=1, cycle=24, from=0)
    duration = cycle
    num_repeat = repeat
    if not repeat:                      # repeat forever
        t = threading.Timer(from, sensor.get_data())    # wait from time and execute a measuurement of the sensor data
        num_repeat -= 1
        while(num_repeat):
            t = threading.Timer(from, sensor.get_data())    # wait a cycle and execute a measuurement of the sensor data
        time.sleep(from)
        sensor.get_data()
        time.sleep(
   sensor.get_data(
