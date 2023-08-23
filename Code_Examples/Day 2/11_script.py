import tkinter as tk
import logging
import csv
import matplotlib.pyplot as plt
import requests
import random

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("BMI_Calculator")

def calculate_bmi(height=0, weight=0):
    if height == 0:
    # If height and weight are not provided, retrieve them from the GUI entry fields
        height = float(height_entry.get())
        weight = float(weight_entry.get())
    # Calculate BMI
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive values.")
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
    if index < 0 or index >= len(data):
        raise IndexError("Invalid row index.")
    del data[index]

    # Write the updated data back to the CSV file
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    display_window.destroy()
    display_data()
    
def visualize_data():
    # Read data from the CSV file
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Extract the necessary data for visualization
    heights = []
    weights = []
    cardiac_events = []
    bmis = []

    for row in data:
        if len(row) != 4:
            raise ValueError("Invalid data format in CSV file.")
        height = float(row[0])
        weight = float(row[1])
        bmi = float(row[2])
        cardiac_event = row[3]

        heights.append(height)
        weights.append(weight)
        cardiac_events.append(cardiac_event)
        bmis.append(bmi)

    # Group the BMI values by CardiacEvent
    grouped_data = {}
    for event, bmi_value, height_value, weight_value in zip(cardiac_events, bmis, heights, weights):
        if event not in grouped_data:
            grouped_data[event] = {'BMI': [], 'Height': [], 'Weight': []}
        grouped_data[event]['BMI'].append(bmi_value)
        grouped_data[event]['Height'].append(height_value)
        grouped_data[event]['Weight'].append(weight_value)

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Boxplot for BMI
    ax1.boxplot([grouped_data['No']['BMI'], grouped_data['Yes']['BMI']], labels=['No', 'Yes'])
    ax1.set_xlabel('Cardiac Event')
    ax1.set_ylabel('BMI [kg/m²]')
    ax1.set_title('Body mass index (BMI) Distribution by Cardiac Event')

    # Scatterplot for height and weight
    ax2.scatter(grouped_data['No']['Height'], grouped_data['No']['Weight'], c='blue', label='No')
    ax2.scatter(grouped_data['Yes']['Height'], grouped_data['Yes']['Weight'], c='red', label='Yes')
    ax2.set_xlabel('Height [m]')
    ax2.set_ylabel('Weight [kg]')
    ax2.set_title('Relationship between Height and Weight')
    ax2.legend()

    # Adjust spacing between subplots
    plt.tight_layout()

    # Show the plot
    plt.show()


def create_random_patient():
    # Generate random height and weight values
    height = float(get_random_height())
    weight = float(get_random_weight())
    height_entry.delete(0, tk.END)
    height_entry.insert(0, height)
    weight_entry.delete(0, tk.END)
    weight_entry.insert(0, weight)

    logger.info(f"Generated random patient: Height: {height} m, Weight: {weight} kg")

    # Calculate BMI for the generated patient
    bmi = weight / (height ** 2)
    result_label.config(text=f"Patient's BMI is: {bmi:.2f}")

    # Determine the cardiac event for the generated BMI
    event = get_cardiac_event_distribution(bmi)
    # Set the cardiac event value in the checkbox
    cardiac_event_var.set(event)

    logger.info(f"Height: {height} m, Weight: {weight} kg")
    logger.info(f"BMI: {bmi:.2f}, Cardiac Event: {event}")

    # Save the generated patient data
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([height, weight, bmi, event])


def get_random_height():
    # Retrieve a random height value from an API
    response = requests.get("https://www.random.org/integers/?num=1&min=130&max=210&col=1&base=10&format=plain&rnd=new")
    if response.status_code != 200:
        raise requests.RequestException("Failed to retrieve random height.")
    data = response.json()
    if not data:
        raise ValueError("Empty response received for random height.")
    height = float(data)
    if height < 130:
        raise ValueError("Invalid random height value received.")
    logger.info(f"Random height generated: {height} cm")
    return height / 100

def get_random_weight():
    # Retrieve a random weight value from an API
    response = requests.get("https://www.random.org/integers/?num=1&min=40&max=140&col=1&base=10&format=plain&rnd=new")
    if response.status_code != 200:
        raise requests.RequestException("Failed to retrieve random weight.")
    data = response.json()
    if not data:
        raise ValueError("Empty response received for random weight.")
    weight = data
    if weight < 40:
        raise ValueError("Invalid random weight value received.")
    logger.info(f"Random weight generated: {weight} kg")
    return weight

def get_cardiac_event_distribution(bmi):
    if bmi < 9 or bmi > 83:
        raise ValueError("BMI value should be between 9 and 83.")
    if bmi <= 22:
        return "No"
    if bmi <= 38:
        risk = (bmi - 22) / (38 - 22)
        return 'Yes' if random.random() < risk else 'No'
    return "Yes"

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

visualize_button = tk.Button(window, text="Visualize Data", command=visualize_data)
visualize_button.pack()

randompatient_button = tk.Button(window, text="Generate one Random Patient", command=create_random_patient)
randompatient_button.pack()

window.mainloop()