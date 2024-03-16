import tkinter

window = tkinter.Tk()


window.title("Unit Converter")
window.config(padx=100, pady=100)

def convert_miles_to_km():
    miles = float(entry_miles.get())
    km = miles * 1.609
    output_label.config(text=f"{km}")


miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

entry_miles = tkinter.Entry()
entry_miles.grid(row=0, column=1)
entry_miles.config(width=5)
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=3,column=1)

output_label = tkinter.Label(text="")
output_label.grid(row=1,column=1)

tkinter.mainloop()