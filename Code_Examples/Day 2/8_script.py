import tkinter as tk
import logging
import csv

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("BMI_Calculator")

def calculate_bmi(height=0, weight=0):
    if height == 0:
    # If height and weight are not provided, retrieve them from the GUI entry fields
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    # Calculate BMI
    bmi = weight / (height ** 2)
    result_label.config(text=f"Patient's BMI is: {bmi:.2f}")

    cardiac_event = cardiac_event_var.get()
    logger.info(f"Height: {height} m, Weight: {weight} kg")
    logger.info(f"BMI: {bmi:.2f}, Cardiac Event: {cardiac_event}")

    # Save patient data
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([height, weight, bmi, cardiac_event])

def display_data():
    # Read data from the CSV file
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Create a new window to display the data
    display_window = tk.Toplevel(window)
    display_window.title("Data Display")

    # Create a label for each row of data, a delete button, and pack them in the window
    for i, row in enumerate(data):
        row_label = tk.Label(display_window, text=row)
        row_label.pack()

        delete_button = tk.Button(display_window, text="Delete", command=lambda i=i: delete_row(i, display_window))
        delete_button.pack()

def delete_row(index, display_window):
    # Read data from the CSV file
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Delete the selected row
    del data[index]

    # Write the updated data back to the CSV file
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    display_window.destroy()
    display_data()

window = tk.Tk()
window.title("Electronic Data Capture")

height_label = tk.Label(window, text="Enter height in meters:")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

weight_label = tk.Label(window, text="Enter weight in kilograms:")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

cardiac_event_var = tk.StringVar()
cardiac_event_var.set("No")  # Set the default value to "No"
cardiac_event_checkbox = tk.Checkbutton(window, text="Cardiac Event (Yes/No)", variable=cardiac_event_var, onvalue="Yes", offvalue="No")
cardiac_event_checkbox.pack()

result_label = tk.Label(window)
result_label.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

display_button = tk.Button(window, text="Records", command=display_data)
display_button.pack()

window.mainloop()
