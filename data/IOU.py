# import the necessary packages
from collections import namedtuple
import numpy as np
import cv2
# define the `Detection` object
Detection = namedtuple("Detection", ["image_path", "gt", "pred"])
def bb_intersection_over_union(boxA, boxB):
	# determine the (x, y)-coordinates of the intersection rectangle
	bx = max(boxA[0], boxB[0])
	by = max(boxA[1], boxB[1])
	bh = min(boxA[2], boxB[2])
	bw = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, bh - bx + 1) * max(0, bw - by + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# return the intersection over union value
	return iou

# define the list of example detections
Signature = [
	Detection("1.jpg", [384, 142, 480, 211], [370, 136, 460, 200]),
	# Detection("2.jpg", [380, 145, 479, 211], [376, 137, 460, 208]),
	# Detection("3.jpg", [383, 142, 478, 210], [379, 139, 468, 207]),
	# Detection("4.jpg", [389, 147, 479, 211], [381, 135, 469, 207]),
	# Detection("5.jpg", [386, 144, 482, 208], [376, 134, 462, 206])
	]
Date = [
	Detection("1.jpg", [371, 18, 494, 46], [361, 14, 484, 36]),
	# Detection("2.jpg", [380, 145, 479, 211], [376, 137, 460, 208]),
	# Detection("3.jpg", [383, 142, 478, 210], [379, 139, 468, 207]),
	# Detection("4.jpg", [389, 147, 479, 211], [381, 135, 469, 207]),
	# Detection("5.jpg", [386, 144, 482, 208], [376, 134, 462, 206])
	]
Amount = [
	Detection("1.jpg", [367, 94, 499, 123], [370, 100, 491, 118]),
	# Detection("2.jpg", [380, 145, 479, 211], [376, 137, 460, 208]),
	# Detection("3.jpg", [383, 142, 478, 210], [379, 139, 468, 207]),
	# Detection("4.jpg", [389, 147, 479, 211], [381, 135, 469, 207]),
	# Detection("5.jpg", [386, 144, 482, 208], [376, 134, 462, 206])
	]
Account_No = [
	Detection("1.jpg", [28, 128, 169, 148], [38, 138, 170, 151]),
	# Detection("2.jpg", [380, 145, 479, 211], [376, 137, 460, 208]),
	# Detection("3.jpg", [383, 142, 478, 210], [379, 139, 468, 207]),
	# Detection("4.jpg", [389, 147, 479, 211], [381, 135, 469, 207]),
	# Detection("5.jpg", [386, 144, 482, 208], [376, 134, 462, 206])
	]
# loop over the example detections
for detection in Signature:
	# load the image
	image = cv2.imread(detection.image_path)
	# draw the ground-truth bounding box along with the predicted
	# bounding box
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	# compute the intersection over union and display it
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

for detection in Date:
	# load the image
	image = cv2.imread(detection.image_path)
	# draw the ground-truth bounding box along with the predicted
	# bounding box
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	# compute the intersection over union and display it
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

for detection in Amount:
	# load the image
	image = cv2.imread(detection.image_path)
	# draw the ground-truth bounding box along with the predicted
	# bounding box
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	# compute the intersection over union and display it
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

for detection in Account_No:
	# load the image
	image = cv2.imread(detection.image_path)
	# draw the ground-truth bounding box along with the predicted
	# bounding box
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	# compute the intersection over union and display it
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	# show the output image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
