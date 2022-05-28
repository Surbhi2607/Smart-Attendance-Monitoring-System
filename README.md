<h1 align="center">Smart Attendance Monitoring System 
</h1>    
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#salient-features">Salient Features</a></li>
        <li><a href="#compatible-platforms">Compatible Platforms</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#agile-methodology">Agile Methodology</a>
      <ul>
        <li><a href="#what-is-agile">What is Agile</a></li>
        <li><a href="#how-i-incorporated-agile-methodology-during-the-development-cycle">How I Incorporated Agile Methodology During The Development Cycle</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#navigating-through-the-app">Navigating through the App</a></li><ul>
        <li><a href="#register">Register</a></li>
        <li><a href="#taking-images">Taking Images</a></li>
        <li><a href="#train-the-model">Train the Model</a></li>
        <li><a href="#login">Login</a></li>
        <li><a href="#Predict">Predict</a></li>
        <li><a href="#attendance-in-database">Attendance in Database</a></li>
      </ul>
    <li><a href="#resources-used">Resources Used</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project
* Smart Attendance Monitoring System project built during Microsoft Engage 2022 program. 
* It is an attendance monitoring application based on computer vision AI based services to detect, identify and mark attendance for the students. 
* Multiple Images of a student will be captured during first time registration to the system which will be used to train the convolutional neural network based model.
* It also leverages a NN based framework to detect face coordinates & create boundary boxes around the same for each student. And then using the training data, match & recognize the student face image to call out his/her name around the boundary box.
* Attendance is updated in the MySQL database

### Salient Features
* It does not require any existing dataset and the model is trained using the images captured from the camera of user's device during registration.
* It can detect multiple faces at the same time.
* Student data is automatically added in the database at the time of user registration.
* Attendance is updated in the database as soon as the face is detected

### Compatible Platforms
Laptops and Desktops

### Built With
* ![Programming-Language][programming-language-shield]
* ![Deep-Learning-Framework][deep-learning-framework-shield]
* ![Desktop-Framework][desktop-framework-shield]
* ![Image-Processing][image-processing-shield]
* ![Face-Detection-Algorithm][face-detection-algorithm-shield]
* ![Face-Recognition-Algorithm][face-recognition-algorithm-shield]

<!-- AGILE METHODOLOGY -->
## Agile Methodology

### What is Agile

Agile is a development methodology adopted today in the software industry. Agile promotes teamwork, flexible procedures, and sle-organizing teams.

### How I Incorporated Agile Methodology During The Development Cycle

SCRUM is a subset of Agile, a framework for developing software. SCRUM takes advantage of different techniques to achieve goals in Agile. SCRUM promotes an iterative model where the planning is performed on a very short term. The basic time working unit is the sprint. SCRUM teams always reason in sprints and their planning is limited to sprints.

* Sprint 1: Requirement Gathering, Tech Stack Finalization, Project IDE Setup, dependencies & configuration settings -Researching across various websites and sources like paperswithcode.com, medium.com, towardsdatascience.com, machinelearningmastery.com. Setting up and configuiring IDE: pycharm. Reading about various deep learning frameworks like MXnet, YOLO, Resnet, Facenet etc., face detection algorithms like MTCNN, Haarcascades, RetinaFace and face recognition algorithms like Arcface, FaceNet and OpenFace. 

* Sprint 2: Software development and debugging - By assessing the performance across various models to be used for face recognition algorithm along with the provided datasets, I finalized the model, deep learning framework and image processing framework. Started the development of Tkinter GUI to record student information & collect training data using live camera feed. Image Processing, model training and saving weights. Encountered occasional bugs which I debugged timely.

* Sprint 3: Testing and debugging - Processing test data from live camera feed, image processing, embedding comparisons, loading recognition model from pickled files and predicting the faces. Built the MySQL database to store user information and update the attendance as soon as the face is recognized.

<!-- INSTALLATIONS -->

## Getting Started
To install and run the project on your local system, following are the requirements:
### Installation

### Prerequisites
 In your local IDE,make sure to install the required dependencies(requirements.txt) via terminal
```
  pip install -r requirements.txt
```
To install Deep Learning Framework: MXnet
```
conda install -c anaconda mxnet
```
To install dlib
```
conda install -c conda-forge dlib
```
To run the project, uninstall all versions of numpy
```
uninstall numpy
```
Install numpy version 1.16.1
```
pip install numpy==1.16.1
```
To connect python with MySQL
```
pip install mysql-connector-python
```
To get real time date and time
```
pip install datetime
```
<!-- APP TUTORIAL-->
## Navigating Through The App
### Register
Register in the application by filling your details.
### Taking Images
Click on the Take Images button and a grant the application access to webcam. A new window opens and 50 images of the user are captured automatically.
### Train the model
After the notification bar shows that 50 images have been captured, click on the Train Images button. The model gets trained using the captured images.
### Login
After completing the registration process, click on Login. As soon as you click on the Login button a new window opens, where you get the option to predict or to exit.
### Predict
After clicking  on predict, a new window opens and a bounding box comes around the user's face along with their name.
### Attendance in database
On detecting the face, the attendance is updated automatically in MySQL database along with the date and time.

<!-- ACKNOWLEDGEMENTS -->

## Resources Used

* [paperswithcode.com](https://paperswithcode.com/)
* [towardsdatascience.com](https://towardsdatascience.com/)
* [medium.com](https://medium.com/)
* [machinelearningmastery.com](https://machinelearningmastery.com/)

<!--MARKDOWN LINKS-->
[programming-language-shield]: https://img.shields.io/badge/Programming%20Language-Python%203.6-blue
[deep-learning-framework-shield]: https://img.shields.io/badge/Deep%20Learning%20Framework-MXnet-blue
[desktop-framework-shield]: https://img.shields.io/badge/Desktop%20Framework-Tkinter-blue
[image-processing-shield]: https://img.shields.io/badge/Image%20Processing-OpenCV-blue
[face-detection-algorithm-shield]: https://img.shields.io/badge/Face%20Detection%20Algorithm-MTCNN-blue
[face-recognition-algorithm-shield]: https://img.shields.io/badge/Face%20Recognition%20Algorithm-Arcface-blue



