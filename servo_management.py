from tkinter import *

from board import SCL, SDA
import busio

# Import the PCA9685 module.
from adafruit_pca9685 import PCA9685

# This example also relies on the Adafruit motor library available here:
# https://github.com/adafruit/Adafruit_CircuitPython_Motor
from adafruit_motor import servo

class ScaleTest:
    
    max_servo = 16
    
    def CloseMe(self):
        self.root.destroy()
    
    def ShowTheValue(self, args):
        i2c = busio.I2C(SCL, SDA)

        # Create a simple PCA9685 class instance.
        
        pca = PCA9685(i2c)
        pca.frequency = 50
        
        self.servo_number = []
        self.servo_move = 0
        
        while self.servo_move < self.max_servo:
            self.servo_number.append(self.servo_move)
            self.servo_number[self.servo_move] = servo.Servo(pca.channels[self.servo_move])
            self.servo_number[self.servo_move].angle = self.scale[self.servo_move].get()
        
            self.servo_move += 1
        
    def ServoSlide(self):
        self.label = []
        self.scale = []
        self.servo = 0
        
        while self.servo < self.max_servo:
            self.label.append(self.servo)
            self.label[self.servo] = Label(self.root, text="Servo " + str(self.servo + 1))
            self.label[self.servo].grid(row = self.servo, column = 0, padx=5, pady=5)
            
            self.scale.append(self.servo)
            self.scale[self.servo] = Scale(self.root, from_=0, to=180, orient=HORIZONTAL, length=400, resolution=0.1, command=self.ShowTheValue)
            self.scale[self.servo].grid(row= self.servo, column = 1, padx=5, pady=5)
            
            self.servo += 1
    
    def __init__(self):
        
        self.root = Tk()
        self.root.title("GUI Servos")
        
        self.menubar = Menu(self.root)
        mainmenu = Menu(self.menubar, tearoff=0)
        mainmenu.add_command(label="Quit", command=self.CloseMe)
        
        self.menubar.add_cascade(label="Config", menu=mainmenu)
        
        self.root.config(menu=self.menubar)
        
        self.ServoSlide()
        
        self.root.mainloop()

st = ScaleTest()