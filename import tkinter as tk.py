import tkinter as tk

def convert_temp():
    try:
        temp = float(entry.get())
        if var.get() == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result_label.config(text=f"Fahrenheit: {fahrenheit:.2f}°F\nKelvin: {kelvin:.2f}K")
        elif var.get() == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(text=f"Celsius: {celsius:.2f}°C\nKelvin: {kelvin:.2f}K")
        else:
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"Celsius: {celsius:.2f}°C\nFahrenheit: {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

app = tk.Tk()
app.title("Temperature Converter")
app.geometry("300x250")

tk.Label(app, text="Enter Temperature:").pack()
entry = tk.Entry(app)
entry.pack()

var = tk.StringVar(value="Celsius")
options = ["Celsius", "Fahrenheit", "Kelvin"]
tk.OptionMenu(app, var, *options).pack()

tk.Button(app, text="Convert", command=convert_temp).pack()
result_label = tk.Label(app, text="Result will appear here")
result_label.pack()

app.mainloop()
