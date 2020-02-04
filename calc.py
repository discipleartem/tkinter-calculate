from tkinter import *


def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator = ""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator = ""

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
							  bg="powder blue", justify='right').grid(columnspan=4)

btn7 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "7", bg="powder blue", command = lambda:btnClick(7)).grid(row = 1, column = 0)

btn8 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "8", bg="powder blue", command = lambda:btnClick(8)).grid(row = 1, column = 1)

btn9 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "9", bg="powder blue", command = lambda:btnClick(9)).grid(row = 1, column = 2)

Addition = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "+", bg="powder blue", command = lambda:btnClick('+')).grid(row = 1, column = 3)

#==================================================================================================

btn4 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "4", bg="powder blue", command = lambda:btnClick(4)).grid(row = 2, column = 0)

btn5 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "5", bg="powder blue", command = lambda:btnClick(5)).grid(row = 2, column = 1)

btn6 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "6", bg="powder blue", command = lambda:btnClick(6)).grid(row = 2, column = 2)

Subtraction = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "-", bg="powder blue", command = lambda:btnClick('-')).grid(row = 2, column = 3)

#==================================================================================================

btn1 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "1", bg="powder blue", command = lambda:btnClick(1)).grid(row = 3, column = 0)

btn2 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "2", bg="powder blue", command = lambda:btnClick(2)).grid(row = 3, column = 1)

btn3 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "3", bg="powder blue", command = lambda:btnClick(3)).grid(row = 3, column = 2)

Multiply = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "*", bg="powder blue", command = lambda:btnClick('*')).grid(row = 3, column = 3)

#==================================================================================================

btn0 = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "0", bg="powder blue", command = lambda:btnClick(0)).grid(row = 4, column = 0)

btnClear = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "C", bg="powder blue", command = btnClearDisplay).grid(row = 4, column = 1)

btnEquals = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "=", bg="powder blue", command = btnEqualsInput).grid(row = 4, column = 2)

Bivision = Button(cal, padx = 16, pady = 16, bd = 8, fg = "black", font = ('arial', 20, 'bold'),
			  text = "/", bg="powder blue", command = lambda:btnClick('/')).grid(row = 4, column = 3)
#==================================================================================================
cal.mainloop()

# для преобразования в .exe файл нам нужно установить pyinstaller
# python3 -m pip install pyinstaller
# в нужной директории с программой мы выполняем
# "-w" - блокируем вывод консоли, "-F" - создает 1 файл, -i'абсолютный путь к иконке'
# pyinstaller -w -F -i'/home/discipleartem/work/QML/tkinter calc/icon.ico' calc.py
#
# если не видит библиотеки python, то нужно выйти из виртуального окружения и установить "-dev" версию
# sudo apt-get install -y python3.7-dev