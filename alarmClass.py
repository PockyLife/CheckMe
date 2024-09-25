import datetime

class Alarm():
    def __init__(self, alarmName: str, startTime: datetime.time, endTime: datetime.time, frequency: int, days: list) -> None:
        self.alarmName = alarmName
        self.startTime = startTime
        self.endTime = endTime
        self.frequency = frequency
        self.days = days
    
    def __str__(self) -> str:
        return self.alarmName

    def update(self, alarmName: str, startTime: datetime.time, endTime: datetime.time, frequency: int, days: list) -> None:
        self.alarmName = alarmName
        self.startTime = startTime
        self.endTime = endTime
        self.frequency = frequency
        self.days = days

    def get_name(self):
        return self.alarmName

    def get_start(self):
        return self.startTime

    def get_end(self):
        return self.endTime

    def get_frequency(self):
        return self.frequency

    def get_days(self):
        return self.days