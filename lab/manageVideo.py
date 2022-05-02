import cv2
import framesQueue
from matplotlib import pyplot as plt

frames = framesQueue.FramesQueue() #OG frames
converted = framesQueue.FramesQueue() #converted to greyscale
outputDir = 'frames'
clipFileName = 'clip.mp4'

def extractFrames(): #DONE
    global frames, outputDir, clipFileName
    count = 0 # initialize frame count
    vidcap = cv2.VideoCapture(clipFileName) # open the video clip
    success, image = vidcap.read()  # read first one
    while success and count < 72: #72 video frames
        print(f'\nReading frame {count} {success}\n')
        frames.insert(image) #insert frame into queue
        count += 1
        success, image = vidcap.read()
    frames.insert(None)  #inserts None into queue indicating done
    print('\nDone Extracting\n')


def covertToGrayscale():
    global frames, converted
    count = 0 # initialize frame count
    frame = frames.remove() #top of queue, pulls last

    while frame is not None:
        print(f'\nConverting frame {count}\n')
        new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# convert the image to grayscale
        converted.insert(new_frame) #inserts frame into queue
        count += 1
        frame = frames.remove() #remove from the front of the "queue", will block while empty
    converted.insert(None) #inserts None into queue indicating done
    print('\nDone Converting\n')

def displayFrames():
    global converted, outputDir
    delay = 42  # the answer to everything delays 42ms
    count = 0 # initialize frame count
    frame = converted.remove() # read first one

    while frame is not None:
        print(f'\nDisplaying frame {count}\n')
        #Also optional code, needed to get frame file name so matplotlib can show
        outFileName = f'{outputDir}/frames{count:04d}.bmp'
        cv2.imwrite(outFileName, frame) # write output file
        #OPtional code, cv2.imshow keeps crashing the kernel,  this plots the image as a matplotlib
        image = cv2.imread(outFileName)
        plt.imshow(image)
        plt.show()
        #OPTIONAL CODE

        #this code is typically all we need but it doesnt work
        # cv2.imshow('Video', frame) # Display the frame in a window called "Video"
        if cv2.waitKey(delay) and 0xFF == ord("q"):# Wait for 42 ms and check if the user wants to quit
            break
        count += 1
        frame = converted.remove()# get the next frame filename
    print("\nDONE displaying\n")
    cv2.destroyAllWindows() # make sure we cleanup the windows, otherwise we might end up with a mess