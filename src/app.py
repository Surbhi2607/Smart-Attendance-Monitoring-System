# -*- coding: utf-8 -*-
import mysql.connector
import argparse
import logging
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

import tkinter.font as font
import webbrowser
import random

from readme_renderer import txt

from src.clientApp import collectUserImageForRegistration, getFaceEmbedding, trainModel
from src.collect_trainingdata.get_faces_from_camera import TrainingDataCollector
from src.face_embedding.faces_embedding import GenerateFaceEmbedding
from src.predictor.facePredictor import FacePredictor
from src.training.train_softmax import TrainFaceRecogModel


class DBConnect:
    def __init__(self):
        self.connection = None

    def connect_to_db(self):
        try:
            # self.connection = mysql.connector.connect(user='root', password='abc@123',
            #                                           host='127.0.0.1', database='AttendanceMaster')
            self.connection = mysql.connector.connect(option_files='DB_conn.txt', option_groups=['connection_details'])
        except mysql.connector.Error as err:
            print(err)

    def close_db_connection(self):
        if self.connection.is_connected():
            self.connection.close()


class RegistrationModule:

    def __init__(self, logFileName):
        self.logFileName = logFileName
        self.window = tk.Tk()
        self.window.title("Face Recognition and Tracking")

        # this removes the maximize button
        self.window.resizable(0, 0)
        window_height = 880
        window_width = 880

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        self.window.configure(background='#000000')

        self.window.attributes('-fullscreen', True)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        header = tk.Label(self.window, text="Student Attendance Registration", width=110, height=2, fg="white",
                          bg="#00008B",
                          font=('times', 18, 'bold', 'underline'))
        header.place(x=0, y=0)

        header1 = tk.Label(self.window, text="Register Here", width=25, height=2, fg="white",
                           bg="#000000",
                           font=('times', 22, 'bold', 'underline'))
        header1.place(x=1000, y=220)

        header4 = tk.Label(self.window, text="Registered users login here:", width=25, height=2, fg="white",
                           bg="#000000",
                           font=('times', 22, 'bold', 'underline'))
        header4.place(x=1025, y=75)

        photo1 = Image.open('C:\\Users\\surbh\\PycharmProjects\\Visionbasedatt\\Image.jpg')
        bgphoto = ImageTk.PhotoImage(photo1)
        placephoto = Label(self.window, image=bgphoto)
        placephoto.place(x=0, y=60)

        studentID = tk.Label(self.window, text="Student ID", width=10, height=2, fg="white", bg="#00008B",
                             font=('times', 15))
        studentID.place(x=1000, y=300)

        displayVariable = StringVar()
        self.studentIDTxt = tk.Entry(self.window, width=20, text=displayVariable, bg="white", fg="black",
                                     font=('times', 15, 'bold'))
        self.studentIDTxt.place(x=1125, y=310)

        studentName = tk.Label(self.window, text="Student Name", width=10, fg="white", bg="#00008B", height=2,
                               font=('times', 15))
        studentName.place(x=1000, y=360)

        self.studentNameTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.studentNameTxt.place(x=1125, y=370)

        emailId = tk.Label(self.window, text="Email ID :", width=10, fg="white", bg="#00008B", height=2,
                           font=('times', 15))
        emailId.place(x=1000, y=420)

        self.emailIDTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.emailIDTxt.place(x=1125, y=430)

        mobileNo = tk.Label(self.window, text="Mobile No :", width=10, fg="white", bg="#00008B", height=2,
                            font=('times', 15))
        mobileNo.place(x=1000, y=480)

        self.mobileNoTxt = tk.Entry(self.window, width=20, bg="white", fg="black", font=('times', 15, ' bold '))
        self.mobileNoTxt.place(x=1125, y=490)

        lbl3 = tk.Label(self.window, text="Notification : ", width=15, fg="white", bg="#00008B", height=2,
                        font=('times', 15))
        lbl3.place(x=1150, y=540)

        self.message = tk.Label(self.window, text="", bg="#FFFFFF", fg="black", width=48, height=2,
                                activebackground="#bbc7d4",
                                font=('times', 15))
        self.message.place(x=990, y=600)

        takeImg = tk.Button(self.window, text="Take Images", command=self.collectUserImageForRegistration, fg="white",
                            bg="#00008B", width=15,
                            height=2,
                            activebackground="#118ce1", font=('times', 15, ' bold '))
        takeImg.place(x=1050, y=680)

        trainImg = tk.Button(self.window, text="Train Images", command=self.trainModel, fg="white", bg="#00008B",
                             width=15,
                             height=2,
                             activebackground="#118ce1", font=('times', 15, ' bold '))
        trainImg.place(x=1250, y=680)

        def new():
            new1 = tk.Tk()
            new1.title("Get Attendance")
            new1.configure(background="black")
            # new1.geometry('400x400')
            new1.attributes('-fullscreen', True)
            header2 = tk.Label(new1, text="WELCOME TO SMART ATTENDANCE SYSTEM!", width=50, height=2, fg="white",
                               bg="#000000",
                               font=('times', 26, 'bold', 'underline'))
            header2.place(x=250, y=100)
            header3 = tk.Label(new1, text="To identify students click:", width=50, height=2, fg="white",
                               bg="#000000",
                               font=('times', 22, 'bold'))
            header3.place(x=350, y=200)
            predictImg = tk.Button(new1, text="Predict", command=self.makePrediction, fg="white", bg="#00008B",
                                   width=15, height=2, activebackground="#118ce1", font=('times', 15, ' bold '))
            predictImg.place(x=680, y=300)
            quitWindow1 = tk.Button(new1, text="Exit", command=new1.quit, fg="white", bg="#00008B",
                                    width=10,
                                    height=2,
                                    activebackground="#118ce1", font=('times', 15, 'bold'))
            quitWindow1.place(x=1000, y=600)

        loginnext = tk.Button(self.window, text="Login", command=new, fg="white", bg="#00008B",
                              width=10, height=2, activebackground="#118ce1", font=('times', 15, ' bold '))
        loginnext.place(x=1150, y=150)

        quitWindow = tk.Button(self.window, text="Quit", command=self.close_window, fg="white", bg="#00008B", width=10,
                               height=2,
                               activebackground="#118ce1", font=('times', 15, 'bold'))
        quitWindow.place(x=1380, y=775)

        label = tk.Label(self.window)

        self.window.mainloop()

        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename=self.logFileName,
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S')

    def getRandomNumber(self):
        ability = str(random.randint(1, 10))
        self.updateDisplay(ability)

    def updateDisplay(self, myString):
        self.displayVariable.set(myString)

    def manipulateFont(self, fontSize=None, *args):
        newFont = (font.get(), fontSize.get())
        return newFont

    def clear(self):
        txt.delete(0, 'end')
        res = ""
        self.message.configure(text=res)

    def clear2(self, txt2=None):
        txt2.delete(0, 'end')
        res = ""
        self.message.configure(text=res)

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def insert_in_table(self, db_connection, statement, params):
        if not statement:
            return None
        cursor = db_connection.connection.cursor(prepared=True)

        cursor.execute(statement, params)
        db_connection.connection.commit()
        cursor.close()

    def insert_new_row(self, db_connection, studentIDVal, name, email, mobile):

        insert_statement = """INSERT INTO AttendanceMaster.Attendance (student_id, student_name, student_mobile, student_emailid, Attendance_Status) 
        values (%s, %s, %s, %s, %s )"""
        values = (studentIDVal, name, mobile, email, 0)

        self.insert_in_table(db_connection, insert_statement, values)

    def collectUserImageForRegistration(self):

        studentIDVal = self.studentIDTxt.get()

        name = (self.studentNameTxt.get())
        email = (self.emailIDTxt.get())
        mobile = (self.mobileNoTxt.get())

        ## Inserting the registration details into MYSQL DB table: Attendance
        db_connection = DBConnect()
        db_connection.connect_to_db()
        self.insert_new_row(db_connection, studentIDVal, name, email, mobile)
        db_connection.close_db_connection()
        ap = argparse.ArgumentParser()

        ap.add_argument("--faces", default=50,
                        help="Number of faces that camera will get")
        ap.add_argument("--output", default="../datasets/train/" + name,
                        help="Path to faces output")

        args = vars(ap.parse_args())

        trnngDataCollctrObj = TrainingDataCollector(args)
        trnngDataCollctrObj.collectImagesFromCamera()

        notifctn = "We have collected " + str(args["faces"]) + " images for training."
        self.message.configure(text=notifctn)

    def getFaceEmbedding(self):

        ap = argparse.ArgumentParser()

        ap.add_argument("--dataset", default="../datasets/train",
                        help="Path to training dataset")
        ap.add_argument("--embeddings", default="faceEmbeddingModels/embeddings.pickle")
        # Argument of insightface
        ap.add_argument('--image-size', default='112,112', help='')
        ap.add_argument('--model', default='../insightface/models/model-y1-test2/model,0', help='path to load model.')
        ap.add_argument('--ga-model', default='', help='path to load model.')
        ap.add_argument('--gpu', default=0, type=int, help='gpu id')
        ap.add_argument('--det', default=0, type=int,
                        help='mtcnn option, 1 means using R+O, 0 means detect from begining')
        ap.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
        ap.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
        args = ap.parse_args()

        genFaceEmbdng = GenerateFaceEmbedding(args)
        genFaceEmbdng.genFaceEmbedding()

    def trainModel(self):
        # ============================================= Training Params ====================================================== #

        ap = argparse.ArgumentParser()

        # ap = argparse.ArgumentParser()
        ap.add_argument("--embeddings", default="faceEmbeddingModels/embeddings.pickle",
                        help="path to serialized db of facial embeddings")
        ap.add_argument("--model", default="faceEmbeddingModels/my_model.h5",
                        help="path to output trained model")
        ap.add_argument("--le", default="faceEmbeddingModels/le.pickle",
                        help="path to output label encoder")

        args = vars(ap.parse_args())

        self.getFaceEmbedding()
        faceRecogModel = TrainFaceRecogModel(args)
        faceRecogModel.trainKerasModelForFaceRecognition()

        notifctn = "Model training is successful.No you can go for prediction."
        self.message.configure(text=notifctn)

    def makePrediction(self):
        faceDetector = FacePredictor()
        faceDetector.detectFace()

    def close_window(self):
        self.window.destroy()

    def callback(self, url):
        webbrowser.open_new(url)


logFileName = "ProceduralLog.txt"
regStrtnModule = RegistrationModule(logFileName)
