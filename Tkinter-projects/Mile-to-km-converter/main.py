import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=450, height=200)
window.config(padx=50, pady=20)


miles_label = tkinter.Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)
is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal_label.grid(column=0, row=1)
convert_label = tkinter.Label(text="0", font=("Arial", 12))
convert_label.grid(column=1, row=1)
km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

def miles_to_km():
    miles = input.get()
    km = round(float(miles) * 1.609)  # Conversion factor from Miles to Kilometers
    return convert_label.config(text=km)

convert_button = tkinter.Button(text="Calculate", command=miles_to_km)
#button.pack(side="left")
convert_button.grid(column=1, row=2)

input = tkinter.Entry(width=12)
input.grid(column=1, row=0)






window.mainloop()