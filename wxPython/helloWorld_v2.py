import wx
ID_ABOUT = 101
ID_EXIT = 110

class MainWindow(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,wx.ID_ANY,title,size = (400, 200), style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE )
		self.control = wx.TextCtrl(self,1,style = wx.TE_MULTILINE)
		global myval
		self.control.SetValue(myval)
		self.Show(True)
		
myval = 

app = wx.PySimpleApp()
frame = MainWindow(None,-1,"Small Editor")
#frame = wx.Frame(None, -1, "Hello World")
#frame.Show(1)
app.MainLoop()