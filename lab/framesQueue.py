import threading

class FramesQueue:
    def __init__(self): #constructor
        self.buff = list()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(10) #ten frame queue

    def insert(self, frame): #inserts into queue
        self.empty.acquire()  # decrement empty semaphore since we are filling buff
        self.buff.append(frame)  # append frame to the end of the buffer
        self.full.release()  # increment full since we just took a spot

    def remove(self):  # remove from the front of the "queue", will block while empty
        self.full.acquire()  # decrement full semaphore since we are removing from buff
        frame = self.buff.pop(0)  # remove frame from the front of buff
        self.empty.release()  # increment empty since we just opened a spot
        return frame