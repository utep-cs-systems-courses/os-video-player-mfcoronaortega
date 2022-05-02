import threading
import manageVideo

threadCount = 0

class myThreads(threading.Thread):
    def __init__(self, stage):
        global threadCount
        threading.Thread.__init__(self, name="\nThread-%d" % threadCount)
        threadCount += 1
        self.stage = stage
    def run(self):
        print("\nCreating Thread-%d" % threadCount)
        if(self.stage == 0):
            manageVideo.extractFrames()
        elif(self.stage == 1):
            manageVideo.covertToGrayscale()
        elif(self.stage == 2):
            manageVideo.displayFrames()

if __name__ == "__main__":
    myThreads(0).start()
    myThreads(1).start()
    myThreads(2).start()
