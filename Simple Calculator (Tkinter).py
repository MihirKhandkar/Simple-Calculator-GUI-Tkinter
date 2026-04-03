from tkinter import *
root = Tk()

root.geometry("467x325")
root.title("Simple Calculator")


entryvalue = StringVar()

def click(value):
    global entryvalue
    match value:

        case"Clear":
            entryvalue.set(" ")

        case"Del":
            entryvalue.set(entryvalue.get()[:-1])
       
        case" / ":
            entryvalue.set(entryvalue.get()+"/")

        case" * ":
            entryvalue.set(entryvalue.get()+"*")
        
        case" 7 ":
           entryvalue.set(entryvalue.get()+"7")
        
        case" 8 ":
            entryvalue.set(entryvalue.get()+"8")

        case" 9 ":
            entryvalue.set(entryvalue.get()+"9")

        case" - ":
           entryvalue.set(entryvalue.get()+"-")

        case" 4 ":
            entryvalue.set(entryvalue.get()+"4")

        case" 5 ":
            entryvalue.set(entryvalue.get()+"5")

        case" 6 ":
            entryvalue.set(entryvalue.get()+"6")
         
        case" + ":
           entryvalue.set(entryvalue.get()+"+")

        case" 1 ":
            entryvalue.set(entryvalue.get()+"1")

        case" 2 ":
            entryvalue.set(entryvalue.get()+"2")

        case" 3 ":
            entryvalue.set(entryvalue.get()+"3")
         
        case" = ":
           entryvalue.set(eval(entryvalue.get())) # eval is built-in . Evaluates result

        case" 0 ":
            entryvalue.set(entryvalue.get()+"0")

        case" . ":
            entryvalue.set(entryvalue.get()+".")
        

        
# Creating Buttons

clear = Button(root,text="Clear", command = lambda: click("Clear"), font =  ("Arial 15"))
clear.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

backspace = Button(root, text="Del", command = lambda: click("Del"), font =  ("Arial 15"))
backspace.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

divide = Button(root, text = " / ", command = lambda: click(" / "), font =  ("Arial 15"))
divide.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

multiply = Button(root, text = " * ", command = lambda: click(" * "), font =  ("Arial 15"))
multiply.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

seven = Button(root, text = " 7 ", command = lambda: click(" 7 "), font =  ("Arial 15"))
seven.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

eight = Button(root, text = " 8 ", command = lambda: click(" 8 "), font =  ("Arial 15"))
eight.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

nine = Button(root, text = " 9 ", command = lambda: click(" 9 "), font =  ("Arial 15"))
nine.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)

subtract = Button(root, text = " - ", command = lambda: click(" - "), font =  ("Arial 15"))
subtract.grid(row=2, column=3, sticky="nsew", padx=5, pady=5)

four = Button(root, text = " 4 ", command = lambda: click(" 4 "), font =  ("Arial 15"))
four.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

five = Button(root, text = " 5 ", command = lambda: click(" 5 "), font =  ("Arial 15"))
five.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

six = Button(root, text = " 6 ", command = lambda: click(" 6 "), font =  ("Arial 15"))
six.grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

add = Button(root, text = " + ", command = lambda: click(" + "), font =  ("Arial 15"))
add.grid(row=3, column=3, sticky="nsew", padx=5, pady=5)

one = Button(root, text = " 1 ", command = lambda: click(" 1 "), font =  ("Arial 15"))
one.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)

two = Button(root, text = " 2 ", command = lambda: click(" 2 "), font =  ("Arial 15"))
two.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

three = Button(root, text = " 3 ", command = lambda: click(" 3 "), font =  ("Arial 15"))
three.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

equal = Button(root, text = " = ", command = lambda: click(" = "), font =  ("Arial 15 bold"))
equal.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)

zero = Button(root, text = " 0 ", command = lambda: click(" 0 "), font =  ("Arial 15"))
zero.grid(row=5, sticky="nsew",padx=5, pady=5, columnspan=3)

decimal = Button(root, text = " . ", command = lambda: click(" . "), font =  ("Arial 15 bold"))
decimal.grid(row=5, column=3, sticky="nsew", padx=5, pady=5)

# Display Entry

display = Entry(root, textvariable=entryvalue, font=("Arial 30"))
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


root.mainloop()