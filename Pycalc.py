from tkinter import *

win = Tk() # This is to create a basic window
win.geometry("340x390")  # this is for the size of the window 
win.resizable(0, 0)  # this is to prevent from resizing the window
win.title("PyCalc")

# the btn_click function is used to set the input field using the but value passed to the method
def btn_click(but):
    global expression
    expression = expression + str(but)
    input_text.set(expression)

# the btn_clear function is used to clear the input field
def btn_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
 

lastExpression = StringVar()

# the btn_equal method calculates the expression present in the input field
def btn_equal():
    global expression
    if expression == "":
        print("Empty")
        return;
    result = str(eval(expression)) # The eval function is used to evaluate the string expression
    lastExpression.set(input_text.get() + "=" + result) #sets the current calculation as the lastExpression to be used it the btn_prevExpression method
    input_text.set(result)
    expression = input_text.get()

# the btn_prevExpress method sets the input field to the previous expression
def btn_prevExpress():
    if lastExpression.get() == "":
        print("No Previous Expression")
        return;
    input_text.set(lastExpression.get())
    expression = lastExpression.get()
 
expression = ""
 
# 'StringVar()' is used to get the instance of input field
 
input_text = StringVar()
 
# Creating the frame for the input field
 
calc_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
calc_frame.pack(side=TOP)
 
# Create an input field inside the Frame
 
input_field = Entry(calc_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT, state='disabled')

input_field.grid(row=0, column=0)
 
input_field.pack(ipady=12) # 'ipady' is y axis (height) padding to increase the height of the input field
 
# Creating another 'Frame' for the buttons below the 'calc_frame'

buttons_frame = Frame(win, width=340, height=330, bg="grey")
 
buttons_frame.pack()
 
# first row with clear and division buttons
 
clear = Button(buttons_frame, text = "CE", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row with 7, 8, 9, and multiply buttons
 
seven = Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(buttons_frame, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row with 4, 5, 6, and subtract buttons
 
four = Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row with 1, 2, 3, and add button
 
one = Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row with 0, decimal, and equals button
 
zero = Button(buttons_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(buttons_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
# sixth row with previous calculation button

prev = Button(buttons_frame, text = "Previous Calculation", fg = "black", width = 43, height = 3, bd = 0, bg = "#99c0ff", cursor = "hand2", command = lambda: btn_prevExpress()).grid(row = 5, column = 0, columnspan = 4, padx = 0, pady = 0)

win.mainloop()