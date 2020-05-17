import Tkinter as tk
import time

class GUIHenry(tk.Frame):

    def servoMotion(self, channel, angle):
        print("Channel number %s with angle %s" % (channel, angle))
    
    def servoLine(self):

        row = 0
        column = 0
        servoLabel = []
        self.servo_line = []

        self.servoLabel = tk.Label(self, text="Servo output 0")
        self.servoLabel.grid(row = row, column = column, padx=5, pady=5)
        
        for self.scale in ("0", "1", "2", "3"):
            servoLabel.append(row)
            self.servo_line.append(row)
            
            servoLabel[row] = tk.Label(self, text="Servo output " + str(row))
            servoLabel[row].grid(row = row, column = column, padx=5, pady=5)
            
            self.servo_line[row] = tk.Scale(self, from_=0, to=180,  length=400, orient="horizontal", command=lambda value, channel=self.scale: self.servoMotion(channel, value))
            self.servo_line[row].set(90)
            self.servo_line[row].grid(row = row, column = column + 1, padx=5, pady=5)
        
            row += 1
    
    def lidsMotion(self, args):
    
        angle = (self.motionLine.get())
        invertAngle = round((100 - angle * 100 /180) * 1.8, 2)
        #set servoMotion

        self.servo_line[0].set(angle)
        self.servo_line[1].set(invertAngle)
        self.servo_line[2].set(invertAngle)
        self.servo_line[3].set(angle)


    def MotionBlink(self):
        angle_reset=90
        angle = (self.motionLine.get())
        invertAngle = round((100 - angle * 100 /180) * 1.8, 2)
        #set servoMotion

        self.servo_line[0].set(70)
        self.servo_line[1].set(110)
        self.servo_line[2].set(110)
        self.servo_line[3].set(80)

        x=0
        while x<4:
            newangle=(self.servo_line[x].get())
            x+=1
            print("Blinking close original angle : %s" % (newangle))

        self.motionLine.set(newangle)

        time.sleep(.5)

        self.servo_line[0].set(angle_reset)
        self.servo_line[1].set(invertAngle)
        self.servo_line[2].set(invertAngle)
        self.servo_line[3].set(angle_reset)

        
        print("Blinking open")

    def motionLine(self):
        
        motionLabel = tk.Label(self, text="Lids")
        motionLabel.grid(row = 0, column = 2, padx=5, pady=5)

        self.motionLine = tk.Scale(self, from_=0, to=180,  length=400, orient="horizontal", command=self.lidsMotion)
        self.motionLine.set(90)  
        self.motionLine.grid(row = 0, column = 3, padx=5, pady=5)

        self.buttonBlink = tk.Button(self, text="Blink", command= self.MotionBlink)
        self.buttonBlink.grid(row = 2, column = 3, padx=5, pady=5)

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.servoLine()
        self.motionLine()

if __name__ == "__main__":
    root=tk.Tk()
    root.title("GUI Servos")
    GUIHenry(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
