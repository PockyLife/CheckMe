import time, sched
#store (alarm_name, time, repeat_bool, repeat_frequency)
class Alarm():
    def __init__(self, alarmName: str, startTime: int, endTime: int, frequency: int, days: str) -> None:
        self.alarmName = alarmName
        self.startTime = startTime
        self.endTime = endTime
        self.frequency = frequency
        self.days = days

    def update(self, alarmName: str, startTime: int, endTime: int, frequency: int, days: str) -> None:
        self.alarmName = alarmName
        self.startTime = startTime
        self.endTime = endTime
        self.frequency = frequency
        self.days = days