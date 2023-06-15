from collections import namedtuple
import numpy as np
import cv2
Detection = namedtuple("Detection", ["image_path", "gt", "pred"])
def bb_intersection_over_union(boxA, boxB):
	bx = max(boxA[0], boxB[0])
	by = max(boxA[1], boxB[1])
	bh = min(boxA[2], boxB[2])
	bw = min(boxA[3], boxB[3])
	interArea = max(0, bh - bx + 1) * max(0, bw - by + 1)
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	iou = interArea / float(boxAArea + boxBArea - interArea)
	return iou
Signature = [Detection("1.jpg", [384, 142, 480, 211], [370, 136, 460, 200])]
Date = [Detection("1.jpg", [371, 18, 494, 46], [361, 14, 484, 36])]
Amount = [Detection("1.jpg", [367, 94, 499, 123], [370, 100, 491, 118])]
Account_No = [Detection("1.jpg", [28, 128, 169, 148], [38, 138, 170, 151])]
for detection in Signature:
	image = cv2.imread(detection.image_path)
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	cv2.imshow("Image", image)
	cv2.waitKey(0)
for detection in Date:
	image = cv2.imread(detection.image_path)
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	cv2.imshow("Image", image)
	cv2.waitKey(0)
for detection in Amount:
	image = cv2.imread(detection.image_path)
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	cv2.imshow("Image", image)
	cv2.waitKey(0)
for detection in Account_No:
	image = cv2.imread(detection.image_path)
	cv2.rectangle(image, tuple(detection.gt[:2]), 
		tuple(detection.gt[2:]), (0, 255, 0), 2)
	cv2.rectangle(image, tuple(detection.pred[:2]), 
		tuple(detection.pred[2:]), (0, 0, 255), 2)
	iou = bb_intersection_over_union(detection.gt, detection.pred)
	cv2.putText(image, "IoU: {:.4f}".format(iou), (10, 170),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
	print("{}: {:.4f}".format(detection.image_path, iou))
	cv2.imshow("Image", image)
	cv2.waitKey(0)
