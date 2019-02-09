from Stitcher import stitcher
# import the necessary packages
import argparse
import imutils
import cv2
cap = cv2.VideoCapture(0)
stitcher = stitcher()
frame1 = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic1.jpg')
while True:
	flag, frame = cap.read()

	# load the two images and resize them to have a width of 400 pixels
	# (for faster processing)
	#imageA = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic1.jpg')
	#imageB = cv2.imread(r'C:\Users\PIYUSH\Desktop\pic2.jpg')
	#frame = imutils.resize(frame, width=400)
		#imageB = imutils.resize(imageB, width=400)

	# stitch the images together to create a panorama
	#stitcher = stitcher()
	(result, vis) = stitcher.stitch([frame, frame1], showMatches=True)
	frame1=frame
	break
	# show the images
	#cv2.imshow("Image A", imageA)
	#cv2.imshow("Image B", imageB)
	cv2.imshow("Keypoint Matches",frame)
	#cv2.imshow("Result", result)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()
