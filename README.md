# Virtual-Hand-Write


**ABOUT**
This project is an ai gesture painter or type writer that recognises and prints the written text by our index finger. This project is made on python using computer vision (OpenCV).


**HOW TO USE THE PROGRAM?**
Given below are the various modes:
1)	Writing mode (condition: only index finger up): the tip of index finger is considered for drawing.
2)	Pause mode (condition: only index and middle finger up): the program stops to draw. This mode is used to provide spaces between characters and to hover around the canvas without drawing.
3)	Detection mode (condition: index, middle and ring finger up): it is used to detect the written text after the user is done writing.
4)	Clear mode (condition: all four fingers up): it is used for clearing the canvas by removing the text written previously.



**MODULES USED**

1.	Mediapipe :-There are many machine learning solutions inside mediapipe that includes face detection, face mesh, iris detection, hand detection.
We used Hands inside mediapipe. MediaPipe Hands utilizes an ML pipeline consisting of multiple models working together: A palm detection model that operates on the full image and returns an oriented hand bounding box. A hand landmark model that operates on the cropped image region defined by the palm detector and returns high-fidelity 3D hand keypoints.

2.	Pytesseract :- Pytesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images or videos.

3.	Numpy :- NumPy is a Python library used for working with arrays.
