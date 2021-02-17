import tkinter


window = tkinter.Tk()
window.minsize(width=500, height=500)

label = tkinter.Label(text = "Hello Tkinter")
label.grid(row = 0, column = 0)

def button_clicked():
    label.config(text = input.get())


button = tkinter.Button(text = "Click me", command = button_clicked)
button.grid(row = 0, column = 2)

input = tkinter.Entry(width = 20)
input.grid(row = 1, column = 1)

txt = tkinter.Entry(width = 20)
txt.grid(row = 3, column = 4)


window.mainloop()