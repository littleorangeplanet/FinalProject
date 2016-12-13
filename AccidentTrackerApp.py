'''Tkinter Python GUI'''
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
''' the backend of matplotlib '''

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import *

from AccidentAnalysis import *

EXSTRA_LARGE_FONT = ('Helvatica', 24)
LARGE_FONT = ('Verdana', 16)
NORMAL_FONT = ('Verdana', 12)
style.use('ggplot')

def popupmsg(msg):
	popup = tk.Tk()
	popup.wm_title("Analysis")
	label = tk.Label(popup, text = msg, font = NORMAL_FONT)
	lable.pack(side="top", fill='x', pady=10)
	button1 = tk.Button(popup, text = "Close", command = popup.destroy())
	button1.pack()
	popup.mainloop()


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

		menubar = tk.Menu()
		filemenu = tk.Menu(menubar, tearoff = 0)
		filemenu.add_command(label="Overview", command = lambda: popupmsg('Coming Soon'))
		filemenu.add_command(label="Location Analysis", command = lambda: popupmsg('Coming Soon'))
		filemenu.add_command(label="Fun3", command = lambda: popupmsg('Coming Soon'))
		filemenu.add_command(label="Fun4", command = lambda: popupmsg('Coming Soon'))
		filemenu.add_command(label="Exit", command = quit)
		'''backend of the menubar '''
		menubar.add_cascade(label = 'Menu', menu= filemenu)
		tk.Tk.config(self, menu=menubar)
		''' the placement of menu bar, more like the front end kind of thing '''


		self.frames = {}
		''' the container for all the pages '''

		for page in (LoadingPage, StartPage, Overview, LocPage):
			
			frame = page(container, self)

			self.frames[page] = frame
			frame.grid(row=0, column=0, sticky='nsew')
			'''  "nsew" = "north south east west" --- alignment definition 
			Streth everything to the edge of the window.'''

		self.show_frame(LoadingPage)


	def show_frame(self, cont):
		# cont, controller, is a key
		'''   function to show a page afront  '''

		frame = self.frames[cont]
			# corresponding to the self.frames in the constructor
		frame.tkraise()
		''' inherited from tk.TK. Used to raise the page to the front '''


class LoadingPage(tk.Frame):
	''' to add a page, inherit from tk.Frame '''
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label1 = tk.Label(self, text = "Welcome", font = EXSTRA_LARGE_FONT)
		label1.pack(padx=10, pady=10)

		'''loading data'''
		button = tk.Button(self, text = 'Load the data', command = lambda: obj() & controller.show_frame(StartPage))
		button.pack()

		''' navigating button '''

		label2 = tk.Label(self, text = "Click Button to Continue", font = LARGE_FONT)
		label2.pack(padx=10, pady=10)
		# button1 = tk.Button(self,text='Go to Page 1', 
		# 	command = lambda: controller.show_frame(PageOne))
		# command is just used to run a function.
		# In here, we want it to open the PageOne, the class of page one.
		# button1.pack()
		# button2 = tk.Button(self,text='Go to Page 2', 
		# 	command = lambda: controller.show_frame(PageTwo))
		# button2.pack()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Menu", font = EXSTRA_LARGE_FONT)
		label.pack(padx=10, pady=10)
		button1 = tk.Button(self,text='Overview Information', 
			command = lambda: controller.show_frame(Overview))
		button1.pack()
		button2 = tk.Button(self,text='Location Analysis', 
			command = lambda: controller.show_frame(LocPage))
		button2.pack()


class Overview(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Overview", font = LARGE_FONT)
		label.pack(padx=10, pady=10)
		


		# Label(PageTwo, text="Borough").grid(row=0)
		# Label(PageTwo, text="Type").grid(row=1)

		# e1 = Entry(PageTwo)
		# e2 = Entry(PageTwo)

		# e1.grid(row=0, column=1)
		# e2.grid(row=1, column=1)

		label = tk.Label(self, text = "Choose a Borough", font = LARGE_FONT)
		label.pack()

		var1 = StringVar(self)
		var1.set("ALL") # default value

		''' dropdown menu to choose the value '''
		boro_opt = OptionMenu(self, var1, "ALL", "MANHATTAN", "BROOKLYN", "QUEENS", "BRONX", "STATEN ISLAND")
		boro_opt.pack()

		# boro_opt.grid(row=1, column=1)
		# Label(self, text="Borough").grid(row = 2, column=1)
	
	
		'''get the value user chose as the input and plot '''
		def ok(boro):
			''' show the plot '''
			# f = Figure(figsize =(5, 5), dpi = 100)
			# # f.clear()
			# # plt.clf()
			
			# # f = Figure(figsize =(5, 5), dpi = 100)
			# a = f.add_subplot(111)
			# # plt.clf()
			# a = obj().borough_year_count(borough = boro)
			# a.plot([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 2, 4])
			# a.borough_year_count(borough = boro)

			# f, a = plt.subplots()
			# a.clear()
			a = obj().borough_year_count(borough = boro)
			canvas = FigureCanvasTkAgg(a, self)
			canvas.show()
			canvas.get_tk_widget().pack()#side = tk.TOP, fill=tk.BOTH, expand = True)
			# canvas.draw()
			# quit()

		button = Button(self, text="OK", command=lambda: ok(var1.get()))
		button.pack()


		# f = a.borough_year_count(borough = boro)

		# menubar = Menu(container)
		# boroMenu = Menu(menubar, tearoff = 1)
		# boroMenu.add_command(label = "All", command = lambda: a.borough_year_count())
		# boroMenu.add_command(label = "Manhattan", command = lambda: a.borough_year_count(borough = "MANHATTAN"))
		# boroMenu.add_command(label = "Queens", command = lambda:  a.borough_year_count(borough = "QUEENS"))
		# boroMenu.add_command(label = "Bronx", command = lambda:  a.borough_year_count(borough = "BRONX"))
		# boroMenu.add_command(label = "Brooklyn", command = lambda: a.borough_year_count(borough = "BROOKLYN"))
		# boroMenu.add_command(label = "Staten Island", command = lambda: a.borough_year_count(borough = "STATEN ISLAND"))




		# f = Figure(figsize =(5, 5), dpi = 100)
		# a = f.add_subplot(111)
		# a.plot([1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 2, 4])
		# canvas = FigureCanvasTkAgg(f, self)
		# canvas.show()
		# canvas.get_tk_widget().pack(side = tk.TOP, fill=tk.BOTH, expand = True)
		


		# button1 = tk.Button(self,text='Go to Page 1', 
		# 	command = lambda: controller.show_frame(PageOne))
		# button1.pack()
		button2 = tk.Button(self,text='Back to Home', 
			command = lambda: controller.show_frame(StartPage))
		button2.pack(side="bottom", fill='x', pady=10)

class LocPage(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text = "Collision Location Analysis", font = LARGE_FONT)
		label.pack(padx=10, pady=10)



		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		''' add the navigation bar '''



app = AccidentTrackerApp()
app.geometry("1280x720")
app.mainloop()






