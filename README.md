# Driver-Drowsiness-Detection-System-using-OpenCV

## Overview
This project implements a real-time driver drowsiness detection system using OpenCV, dlib, and Tkinter. It continuously monitors the driver’s eyes and provides alerts if they detect drowsiness. Additionally, the system offers beverage recommendations based on the detected drowsiness level.

## How It Works

***1. Face and Eye Detection :***

-Utilizes OpenCV's Haar cascades to detect the face and eyes within the face.

***2. Eye Aspect Ratio (EAR) :***

-Determine if the eyes are closed by computing the Eye Aspect Ratio.

-Calculates EAR using the distances between vertical and horizontal eye landmarks.

***3. Drowsiness Alert :***

-Triggers an alert if the EAR is below a threshold for a continuous period, indicating potential drowsiness.

***4.  Beverage Recommendation :***

-Recommends beverages based on the drowsiness level detected.

## Built With

***1. OpenCV -***  Open source computer vision and machine learning software library.

***2. dlib -***  Toolkit for machine learning and data analysis applications.

***3. Tkinter -*** Python’s standard GUI package.

***4. Pygame -*** Modules designed for writing video games.

***5. NumPy -*** Fundamental package for scientific computing with Python.

***6. imutils -*** Convenience functions for basic image processing tasks with OpenCV.

**Download Pre-trained Model:**  https://www.kaggle.com/datasets/sajikim/shape-predictor-68-face-landmarks
