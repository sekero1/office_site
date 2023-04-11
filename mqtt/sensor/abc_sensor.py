from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read_data(self):
        pass

    def __init__(self, sensor_id, sensor_name):
        self.sensor_id = sensor_id
        self.sensor_name = sensor_name

    # 센서의 초기화 설정 등을 수행하는 메서드
    def setup(self):
        pass

    # 센서의 종료 작업을 수행하는 메서드
    def teardown(self):
        pass
