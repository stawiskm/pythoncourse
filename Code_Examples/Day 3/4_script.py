import tkinter as tk

def calculate_bmi(height=0, weight=0):
    if height == 0:
    # If height and weight are not provided, retrieve them from the GUI entry fields
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    # Calculate BMI
    bmi = weight / (height ** 2)
    result_label.config(text=f"Patient's BMI is: {bmi:.2f}")

window = tk.Tk()
window.title("BMI Calculator")

height_label = tk.Label(window, text="Enter height in meters:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Enter weight in kilograms:")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

result_label = tk.Label(window)
result_label.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

window.mainloop()
