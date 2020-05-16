#!/usr/bin/python3

import wx
import time
import cv2

class GUIHenry(wx.Frame):
    
    def servoMotion(self, angle, channel):
 
        if str(type(angle)) == "<type 'classobj'>":
            print (type(angle))

        print("servoMotion actuate channel number is %s and angle is %s" % (channel, angle))

    def servoLine(self):

        row = 0
        servoLabel = []
        self.servo_line = []
        
        for self.scale in ("0", "1", "2", "3", "4", "5", "6"):
            servoLabel.append(row)
            self.servo_line.append(row)
            
            self.servo_line[row] = wx.Slider(self.panel, 100, 90, 0, 180, pos=(10, 55 * row + 10), size=(250, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
            self.servo_line[row].Bind(wx.EVT_SCROLL , lambda evt, channel=row: self.servoMotion(evt, channel))
        
            row += 1

    def motion(self, evt, channel):

        obj = evt.GetEventObject()
        currentAngle = obj.GetValue()

        for line in channel:
            if (channel[line] == "invert"):
                angle = round((100 - currentAngle * 100 /180) * 1.8, 2)
            else:
                angle = currentAngle

            self.servo_line[line].SetValue(angle)
            self.servoMotion(angle, line)
            
    def motionAction(self, evt, channel):

        currentAngle = self.motion_lids.GetValue()

        self.servo_line[0].SetValue(70)
        self.servoMotion(70, 0)
        
        self.servo_line[1].SetValue(110)
        self.servoMotion(110, 1)
        
        self.servo_line[2].SetValue(110)
        self.servoMotion(110, 2)
        
        self.servo_line[3].SetValue(70)
        self.servoMotion(70, 3)
        
        time.sleep(.100)

        for line in channel:
            if (channel[line] == "invert"):
                 angle = round((100 - currentAngle * 100 /180) * 1.8)
            else:
                 angle = currentAngle

            self.servo_line[line].SetValue(angle)
            self.servoMotion(angle, line)
    
    def motionLine(self):

        servoLids = {
            0:"normal",
            1:"invert",
            2:"invert",
            3:"normal"
            }

        self.motion_lids = wx.Slider(self.panel, 100, 90, 70, 110, pos=(270, 10), size=(250, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
        self.motion_lids.Bind(wx.EVT_SCROLL, lambda evt, channel=servoLids: self.motion(evt, channel))

        self.tbtn = wx.Button(self.panel , -1, "click to on", pos=(270, 55))
        self.tbtn.Bind(wx.EVT_BUTTON, lambda evt, channel=servoLids: self.motionAction(evt, channel))
    
    def __init__(self):
        wx.Frame.__init__(self, None,  wx.ID_ANY, 'GUI Henry', size=(640,480))
        self.panel = wx.Panel(self,  wx.ID_ANY)
        
        self.servoLine()
        self.motionLine()

    # def Motion(self, args):
    #     print ("do something")

    #     origin = self.slider.GetValue()
    #     print (self.slider.GetValue())
    #     self.slider.SetValue(75)

    #     time.sleep(1)

    #     self.slider.SetValue(40)

    #     time.sleep(1)

    #     self.slider.SetValue(origin)

app = wx.App()
frame = GUIHenry()
frame.Show()
app.MainLoop()