import wx
 
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Programmatic binding of accelerators in wxPython", size=(450,150))
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        bindings = [
                  (wx.ACCEL_CTRL,  wx.WXK_UP, 'up'),
                  (wx.ACCEL_CTRL,  wx.WXK_DOWN, 'down'),
                  (wx.ACCEL_CTRL,  wx.WXK_LEFT, 'left'),
                  (wx.ACCEL_CTRL,  wx.WXK_RIGHT, 'right'),
                  ]


        accelEntries = []

        for binding in bindings:
            eventId = wx.NewId()
            accelEntries.append( (binding[0], binding[1], eventId) )
            
            self.Bind(wx.EVT_MENU, lambda evt, temp=binding[2]: self.on_move(evt, temp), id=eventId)
            
        accelTable  = wx.AcceleratorTable(accelEntries)
        self.SetAcceleratorTable(accelTable )
     #----------------------------------------------------------------------

    def on_move(self, Event, direction):
        print "You pressed CTRL+"+direction
        
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()