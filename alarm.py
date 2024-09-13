import time, sched
#store (alarm_name, time, repeat_bool, repeat_frequency)
class alarm():
    def __init__(self, alarm_name: str, startTime: int, repeat: bool, frequency: int) -> None:
        self.alarm_name = alarm_name
        self.startTime = startTime
        self.repeat = repeat
        self.frequency = frequency

    def update(self, alarm_name: str, startTime: int, repeat: bool, frequency: int):
        self.alarm_name = alarm_name
        self.startTime = startTime
        self.repeat = repeat
        self.frequency = frequency