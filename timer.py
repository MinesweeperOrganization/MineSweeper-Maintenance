import time
class TimeManager:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0
        self.elapsed = 0.0

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        print(self.elapsed)