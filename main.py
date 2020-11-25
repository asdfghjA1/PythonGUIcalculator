#This everything is just for test purpose :) 
#  Python program to create a simple GUI 
# calculator using Tkinter 
# import everything from tkinter module 
from tkinter import *

# globally declare the expression variable 
expression = "" 


# Function to update expressiom 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 


# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 

		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialze the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 

		equation.set(" Ooops Its seems you have something wrong going on....Please check") 
		expression = "" 


# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 


# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="white") 


	# set the configuration of GUI window 
	camZ = gui.geometry("1080x720") 
 
	# set the title of GUI window 
	gui.title("Simple Calculator" + camZ) 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = Entry(gui, textvariable=equation) 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=40, ipadx=300) 

	equation.set('enter your expression') 

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = Button(gui, text=' Fucking this is  1 ', fg='black', bg='red', 
					command=lambda: press(1), height=2, width=35) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' Fucking this is 2 ', fg='black', bg='red', 
					command=lambda: press(2), height=2, width=35) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' Fucking this is 3', fg='black', bg='red', 
					command=lambda: press(3), height=2, width=35) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' Fucking this is 4', fg='black', bg='red', 
					command=lambda: press(4), height=2, width=35) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' Fucking this is 5', fg='black', bg='red', 
					command=lambda: press(5), height=2, width=35) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' Fucking this is 6 ', fg='black', bg='red', 
					command=lambda: press(6), height=2, width=35) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' Fucking this is 7', fg='black', bg='red', 
					command=lambda: press(7), height=2, width=35) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' Fucking this is 8', fg='black', bg='red', 
					command=lambda: press(8), height=2, width=35) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' Fucking this is 9 ', fg='black', bg='red', 
					command=lambda: press(9), height=2, width=35) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' God dam this is fucking 0', fg='black', bg='red', 
					command=lambda: press(0), height=2, width=35) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='red', 
				command=lambda: press("+"), height=2, width=35) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='red', 
				command=lambda: press("-"), height=2, width=12) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='red', 
					command=lambda: press("*"), height=2, width=12) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='red', 
					command=lambda: press("/"), height=2, width=12) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='red', 
				command=equalpress, height=2, width=12) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear', fg='black', bg='red', 
				command=clear, height=2, width=12) 
	clear.grid(row=5, column='1') 

	Decimal= Button(gui, text='.', fg='black', bg='red', 
					command=lambda: press('.'), height=2, width=12) 
	Decimal.grid(row=6, column=0) 
	# start the GUI 
	gui.mainloop() 
