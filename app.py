
#import libraries
import cv2
from flask import Flask, render_template, request, Response
import jsonify
import requests

app= Flask(__name__)

@app.route('/')
def Home():
	return render_template('index.html')
	#return Response(code())


def code():
	# define a video capture object 
	vid = cv2.VideoCapture(0) 
	
	while(True):
		# Capture the video frame by frame
		ret, frame = vid.read() #ret=True when video is being captured

		# Convert the frame to sketch
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		inverted_frame = 255 - gray_frame
		blurred_frame = cv2.GaussianBlur(inverted_frame, (21, 21), 0)
		inverted_blurred_frame = 255 - blurred_frame
		pencil_sketch = cv2.divide(gray_frame, inverted_blurred_frame, scale=256.0)
		
		# Display the resulting frame
		cv2.imshow('Original', frame)
		cv2.imshow('Sketch', pencil_sketch)
		
		# the 'q' button is set as the quitting button you may use any desired button of your choice
		# set 0xFF == 27 to use Esc key 
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# After the loop release the cap object
	vid.release()
	# Destroy all the windows 
	cv2.destroyAllWindows() 