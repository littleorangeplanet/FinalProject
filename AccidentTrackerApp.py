'''Tkinter Python GUI'''

import matplotlib
matplotlib.use("TkAgg")
''' the backend of matplotlib '''

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ('Verdana', 12)

class AccidentTrackerApp(tk.Tk):

	''' the baseline to build the framework '''

	def __init__(self, *args, **kwargs):
		# *args: you can pass as many as parameters as you want
		# **kwargs: pass dictionary, usually.
		tk.Tk.__init__(self, *args, **kwargs)
		'''initialize the tkinter'''
		
		# tk.TK.iconbitmap(self,default='')
		''' Change the icon of the GUI '''
		tk.Tk.wm_title(self, "Accident Tracker")
		''' Change the title of the GUI '''

		container = tk.Frame(self)
		'''make a frame for the GUI'''

		container.pack(side='top', fill = 'both', expand = True)

		container.grid_rowconfigure(0, weight = 1)
		# 0 is minimun size
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}
		''' the container for all the pages '''

		for F in (StartPage, PageOne, PageTwo):
			
			frame = F(container, self)

			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')
			'''  "nsew" = "north south east west" --- alignment definition 
			Streth everything to the edge of the window.'''

		self.show_frame(StartPage)


	def show_frame(self, cont):
		# cont, controller, is a key
		'''   function to show a page afront  '''

		frame = self.frames[cont]
			# corresponding to the self.frames in the constructor
		frame.tkraise()
		''' inherited from tk.TK. Used to raise the page to the front '''


class StartPage(tk.Frame):
	''' to add a page, inherit from tk.Frame '''
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Start Page", font = LARGE_FONT)
		label.pack(padx=10, pady=10)

		''' navigating button '''
		button1 = tk.Button(self,text='Go to Page 1', 
			command = lambda: controller.show_frame(PageOne))
		# command is just used to run a function.
		# In here, we want it to open the PageOne, the class of page one.
		button1.pack()
		button2 = tk.Button(self,text='Go to Page 2', 
			command = lambda: controller.show_frame(PageTwo))
		button2.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Page One", font = LARGE_FONT)
		label.pack(padx=10, pady=10)
		button1 = tk.Button(self,text='Go to Page 2', 
			command = lambda: controller.show_frame(PageTwo))
		button1.pack()
		button2 = tk.Button(self,text='Back to Home', 
			command = lambda: controller.show_frame(StartPage))
		button2.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Page Two", font = LARGE_FONT)
		label.pack(padx=10, pady=10)
		
		f = Figure(figsize =(5, 5), dpi = 100)
		a = f.add_subplot(111)
		a.plot([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 2, 4])
		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand = True)
		''' show the plot '''


		button1 = tk.Button(self,text='Go to Page 1', 
			command = lambda: controller.show_frame(PageOne))
		button1.pack()
		button2 = tk.Button(self,text='Back to Home', 
			command = lambda: controller.show_frame(StartPage))
		button2.pack()



		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		''' add the navigation bar '''


app = AccidentTrackerApp()
app.mainloop()






