import wx


class MyDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(MyDialog, self).__init__(parent, title = title, size = (250,150)) 
        panel = wx.Panel(self) 
        self.btn = wx.Button(panel, wx.ID_OK, label = "OK", size = (50,20), pos = (75,50))

class MyPanel1(wx.Panel):
    def __init__(self, parent): 
        super(MyPanel1, self).__init__(parent)
        self.btn = wx.Button(self, label="Open Dialog", pos=(20, 20))
        self.Bind(wx.EVT_BUTTON, self.OnModal)

    def OnModal(self, e):
        a = MyDialog(self, "Dialog").ShowModal()
        print (a)

class MyPanel2(wx.Panel): 
   def __init__(self, parent): 
      super(MyPanel2, self).__init__(parent) 
      lblList = ['Value X', 'Value Y', 'Value Z']         
      rbox = wx.RadioBox(self, label = 'RadioBox', pos = (25,10), choices = lblList, majorDimension = 1, style = wx.RA_SPECIFY_ROWS) 


class WxWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WxWindow, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        nb = wx.Notebook(self)
        nb.AddPage(MyPanel1(nb), "Panel 1")
        nb.AddPage(MyPanel2(nb), "Panel 2")

        toolbar = self.CreateToolBar()

        tb = toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('images/exit-icon.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnClose, tb)

        self.SetSize((350, 250))
        self.SetMinSize((200, 200))
        self.SetTitle("My App")
        self.Centre()

    def OnClose(self, e):
        self.Close(True)


def main():
    app = wx.App()
    ex = WxWindow(None)
    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
