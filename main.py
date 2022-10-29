import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=600, height=400)
window.config(padx=132, pady=120)

# no = 0


def mile_to_km():
    miles = float(miles_input.get())
    km = round(miles*1.609)
    kilometer_result_label.config(text=km)


miles_input = tkinter.Entry(width=15)
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 19))
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 19))
is_equal_label.grid(row=1, column=0)

kilometer_result_label = tkinter.Label(text=0, font=("Arial", 19))
kilometer_result_label.grid(row=1, column=1)

kilometer_label = tkinter.Label(text="KM", font=("Arial", 19))
kilometer_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=mile_to_km)
button.grid(row=2, column=1)


window.mainloop()
