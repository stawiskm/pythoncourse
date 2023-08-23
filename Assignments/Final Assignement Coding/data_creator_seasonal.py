import pandas as pd
import random
from datetime import datetime, timedelta

# Generate sample patient names
def generate_patient_name():
    first_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(first_names) + " " + random.choice(last_names)

# Generate random visit reasons with associated seasonal tendencies
def generate_visit_reason():
    visit_reasons = [
        ("Fever", [100,10, 10, 60, 20, 10, 10, 10, 10, 80, 20, 40]),
        ("Cough", [100,80, 10, 10, 40, 10, 40, 10, 10, 80, 20, 40]),
        ("Headache", [90, 60, 10, 55, 10, 30, 40, 100, 10, 10, 10, 80]),
        ("Allergy", [70, 10, 100, 100,10,10, 10, 80, 10, 10, 80, 10]),
        ("Injury", [50, 10, 50, 10, 60, 10, 100, 10, 50, 100, 50, 40]),
        ("Routine Checkup", [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1])
    ]
    return random.choice(visit_reasons)

# Generate random visit dates with associated seasonal tendencies
def generate_visit_date(seasonal_tendencies):
    month = random.choices(range(1, 13), seasonal_tendencies)[0]
    random_day = random.randint(1, 28)  # To ensure realistic day values
    visit_date = datetime(2022, month, random_day)
    return visit_date

# Generate random visit durations with associated visit reason tendencies
def generate_visit_duration(visit_reason):
    visit_duration_ranges = {
        "Fever": (15, 45),
        "Cough": (10, 30),
        "Headache": (5, 25),
        "Stomachache": (20, 40),
        "Allergy": (10, 30),
        "Injury": (30, 60),
        "Fatigue": (15, 35),
        "Routine Checkup": (15, 30)
    }
    min_duration, max_duration = visit_duration_ranges[visit_reason]
    visit_duration = random.randint(min_duration, max_duration)
    return visit_duration

# Generate sample data with visit durations
def generate_sample_data(num_entries, num_duplicates):
    data = []
    for _ in range(num_entries):
        patient_name = generate_patient_name()
        visit_reason, seasonal_tendencies = generate_visit_reason()
        visit_date_generator = generate_visit_date(seasonal_tendencies)
        visit_date = generate_visit_date(seasonal_tendencies).strftime("%Y-%m-%d")
        visit_duration = generate_visit_duration(visit_reason)
        data.append([patient_name, visit_reason, visit_date, visit_duration])
    
    # Add duplicates
    for _ in range(num_duplicates):
        existing_entry = random.choice(data)
        data.append(existing_entry)
    
    return data

# Save the data to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data, columns=["Patient", "Visit_Reason", "Date", "Visit_Duration"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    num_entries = 10000
    num_duplicates = 100
    filename = "visit_data.csv"
    
    sample_data = generate_sample_data(num_entries, num_duplicates)
    save_to_csv(sample_data, filename)