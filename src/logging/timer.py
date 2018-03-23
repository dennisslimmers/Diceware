import datetime

class Timer:    
    def __init__(self):
        pass
    
    def start(self): # pylint: disable=E0202
        self.start = datetime.datetime.now()
        return self.start
    
    def stop(self, message="Finished generating at: "): # pylint: disable=E0202
        self.stop = datetime.datetime.now()
        return message + str(self.stop)

    def elapsed(self, message="Elapsed generation time: "):
        elapsed = datetime.datetime.now() - self.start
        return message + str(elapsed.total_seconds()) + "s"
