################################################################################
# 						Created by JADID Taha							 	   #
#																		 	   #
# 				FOR USAGE Put the following Command 				     	   #
# python MaskDetect.py --shape-predictor shape_predictor_68_face_landmarks.dat #
################################################################################


# importing part
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import argparse
import imutils
import time
import dlib
import cv2


# construct the argument parse & parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam", type=int, default=0,
	help="index of webcam on system")
args = vars(ap.parse_args())


# initialize a var just to know the state of the face 
StateFace = 0

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[START] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# the mouth respectively
(m_start, m_end) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# start the video stream thread
print("[START] starting video stream thread...")
# in case you didn't use the default WebCamera
vs = VideoStream(src=args["webcam"]).start() 
time.sleep(1.0)

# Face time
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')



# loop over frames from the video stream
while True:
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	frame = vs.read()
	frame = imutils.resize(frame, width=750)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=4)

	# detect faces in the grayscale frame
	rects = detector(gray, 0)
	StateFace = 0
	for rect in rects:
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			# extract the mouth coordinates
			mouthCordinates = shape[m_start:m_end]
			# for getting an idea in your terminal
			print(mouthCordinates)
			
			# visualize the mouth
			mouth_hull = cv2.convexHull(mouthCordinates)

			#cv2.drawContours(frame, [mouth_hull], -1, (0, 0, 255), 1)
			
			# draw a message on the frame to remmember the person
			cv2.putText(frame, "Put Your Mask Please !!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

			# the case when we detect the mouth so the person need to put on the face
			# we change the var StateFace to 1(True) value
			StateFace = 1

	# loop over the face detections
	for (x,y,w,h) in faces:

		if StateFace == 1 :
			# when a person doesn't wear a mask
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
		else :
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			cv2.putText(frame, "Good State ^^", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()