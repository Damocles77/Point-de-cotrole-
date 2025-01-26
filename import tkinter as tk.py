import tkinter as tk
!apt-get install xvfb
!Xvfb :99 -screen 0 1024x768x24 &
import os
os.environ['DISPLAY'] = ':99'

def fahrenheit_to_celsius():
    """Convert the temperature from Fahrenheit to Celsius and display the result."""
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    except ValueError:
        lbl_result["text"] = "Entrée invalide"

# Create the main window
window = tk.Tk()
window.title("Convertisseur de Température")
window.resizable(width=False, height=False)

# Create a frame for the input field and label
frm_entry = tk.Frame(master=window)

# Create the input field for Fahrenheit temperature
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Create a label for the Fahrenheit symbol
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Arrange the input field and label in the frame
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create a button to trigger the conversion
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

# Create a label to display the result in Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Arrange the widgets in the main window
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Start the application
window.mainloop()
