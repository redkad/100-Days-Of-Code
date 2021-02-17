import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=300)
window.config(padx=70, pady=100)

text1 = tkinter.Label(text="is equal to",padx=10)
text1.grid(column=1, row=1)

mile_input = tkinter.Entry()
mile_input.grid(column=2, row=0)
mile_input.insert(0, 0)

text2 = tkinter.Label(text="Miles",padx=10)
text2.grid(column=3, row=0)

text3 = tkinter.Label(text=0,padx=10)
text3.grid(column=2, row=1)

text4 = tkinter.Label(text="Km",padx=10)
text4.grid(column=3, row=1)

btn = tkinter.Button(text="Calculate",padx=10)
btn.grid(column=2, row=2)

def calculate_km():
    mile = int(mile_input.get())
    km = round(mile * 1.609, 2)
    mile_input.config(text=km)
    text3.config(text=km)


btn.config(command=calculate_km)

window.mainloop()
