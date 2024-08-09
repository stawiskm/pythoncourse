# Assignments (Py02)

## Problem 1: Patient Monitoring and Alert System

### Hard

**Scenario:**  
A hospital has a patient monitoring system that tracks the vital signs of patients in the intensive care unit (ICU). Each patient’s heart rate is recorded every minute and stored in an array. The array for each patient contains the heart rate data for the last 24 hours (1440 minutes). The hospital wants to implement an alert system that detects potential issues based on abnormal heart rate patterns.

**Problem Statement:**  
Write a program that takes in the heart rate data for a patient as an array of 1440 integers and checks for the following:
    1. **Tachycardia Alert:** If the heart rate exceeds 100 bpm for 15 consecutive minutes or more, raise a Tachycardia alert.
    2. **Bradycardia Alert:** If the heart rate drops below 60 bpm for 10 consecutive minutes or more, raise a Bradycardia alert.

The program should output a list of times (in minutes from the start of the 24-hour period) where alerts were triggered.

**Array Usage:**  

- The heart rate data is stored in an array of integers.
- The program uses the array to check for consecutive abnormal values and raises alerts accordingly.

```python
# Example usage (dummy data)
# Random seed random.seed(seed=None)
np.random.seed(42)
# Generate dummy heart rate data
high_phase_data = np.random.randint(95, 130, size=500)
normal_phase_data = np.random.randint(50, 120, size=440)
low_phase_data = np.random.randint(35, 70, size=500)
heart_rate_data = np.concatenate([high_phase_data, normal_phase_data, low_phase_data])
# Check for alerts
alerts = check_heart_rate(heart_rate_data)
print(alerts)  # Print the detected alerts

# {'Tachycardia': [(47, 65, 19), (234, 248, 15), (315, 329, 15), (404, 439, 36)], 'Bradycardia': [(990, 1001, 12), (1090, 1100, 11), (1166, 1179, 14), (1374, 1388, 15)]}

```

*If you stop here, and code this function, by yourself, you will learn a lot. (HARD)*

---
---
---

### Medium

To solve the problem more efficiently using array functions and reduce the number of iterations, follow these steps:

#### 1. **Identify Consecutive Segments**

- Use a **sliding window** or **filtering technique** to find segments of the array where the heart rate is consistently above 100 bpm or below 60 bpm.
- For each value in the array, you can create a binary mask (an array of 0s and 1s), where:
  - 1 indicates the heart rate exceeds 100 bpm (for Tachycardia) or drops below 60 bpm (for Bradycardia).
  - 0 indicates normal heart rate.

#### 2. **Find Runs of 1s**

- Use **array operations** to identify consecutive runs of 1s in the binary mask.
- This can be achieved by using functions that help detect the start and end of each run, such as **`diff`**, **`cumsum`**, or by combining conditions.

#### 3. **Filter Based on Length**

- Once you have the segments where the heart rate is consistently abnormal, filter these segments by their length:
  - For Tachycardia, only keep segments where the length is 15 minutes or more.
  - For Bradycardia, only keep segments where the length is 10 minutes or more.
- The length of a segment is determined by counting the consecutive 1s.

#### 4. **Extract Start and End Times**

- For each valid segment that meets the length criteria, calculate the start and end times.
- Use the indices of the start and end of the segments to determine the exact times (in minutes from the start of the 24-hour period).

#### 5. **Output the Alerts**

- Compile the start and end times of all valid Tachycardia and Bradycardia alerts into a list.
- Return or print this list.

#### Efficiency Considerations

- By converting the heart rate data into binary masks and then using array operations to detect and filter segments, you minimize the need for explicit loops.
- This approach leverages vectorized operations that are typically more efficient than manual iteration, especially for large datasets like a 1440-element array.

#### Summary of Steps Using Array Functions

1. **Create binary masks** for abnormal heart rates.
2. **Identify consecutive runs** of abnormal values using array operations.
3. **Filter** these runs by duration to determine valid alerts.
4. **Calculate and store** the times of these alerts.
5. **Return the results** in a structured format.

*If you stop here, and code this function, with the help of the instructions above, you still learn a lot. (MEDIUM)*

---
---
---

### Easy

Fill the TODOs in the code below to complete the function.

Here's the dummy Python code that outlines the process using array functions to minimize iterations:

```python
import numpy as np

def check_heart_rate(heart_rate_data):
    # Step 1: Create binary masks
    tachy_mask = #TODO # Mask for Tachycardia
    brady_mask = #TODO # Mask for Bradycardia
    
    # Step 2: Identify consecutive runs of abnormal values
    # Calculate differences to find the start and end of runs
    tachy_diff = #TODO  # Calculate diff for Tachycardia
    brady_diff = #TODO  # Calculate diff for Bradycardia

    # Find the indices where runs start and end
    tachy_start_indices = np.where(tachy_diff == 1)[0]
    tachy_end_indices = np.where(tachy_diff == -1)[0] - 1

    brady_start_indices = #TODO
    brady_end_indices = #TODO

    # Step 3: Filter by length of runs
    tachy_alerts = []
    brady_alerts = []

    for start, end in zip(tachy_start_indices, tachy_end_indices):
        lenght = end - start + 1
        if lenght >= 15:  # Check if the run is 15 minutes or more
            tachy_alerts.append((start, end, lenght))

    #TODO same for brady_alerts loop

    # Step 4: Combine the alerts
    alerts = {
        "Tachycardia": tachy_alerts,
        "Bradycardia": brady_alerts
    }

    return alerts

```

#### Breakdown of the Python Code

1. **Binary Masks:**
   - `tachy_mask` and `brady_mask` are arrays where each element is `True` if the corresponding heart rate meets the criteria for Tachycardia or Bradycardia, respectively.

2. **Identifying Consecutive Runs:**
   - `np.diff` is used to find where the binary mask switches from `False` to `True` (indicating the start of a run) and from `True` to `False` (indicating the end of a run).
   - Concatenating with `[0]` ensures that changes at the boundaries (beginning or end) are detected.

3. **Filtering Runs:**
   - The code checks each run to see if it meets the minimum duration required for an alert.
   - Only runs that are long enough are stored in the `tachy_alerts` or `brady_alerts` lists.

4. **Combining Alerts:**
   - The alerts are stored in a dictionary and returned.

*You finished this problem, if you complete the code above, and test it with the example usage. (EASY)*

---
---
---

## Problem 2: Medical Imaging Pixel Intensity Analysis

**Scenario:**  
A radiologist is analyzing a grayscale MRI image represented as a 2D array, where each element in the array represents the intensity of a pixel (ranging from 0 to 255). The radiologist wants to identify regions of interest (ROI) where the pixel intensity exceeds a certain threshold, indicating possible abnormalities.

**Problem Statement:**  
Write a program that takes a 2D array representing an MRI scan and a threshold value as input. The program should:

1. Identify all contiguous regions (clusters) in the array where the pixel intensity exceeds the threshold.
2. For each cluster, calculate the size of the region (number of pixels) and the average intensity.
3. Return a list of clusters with their respective sizes and average intensities.

**Array Usage:**  

- The MRI scan data is stored in a 2D array of integers.
- The program uses the array to identify contiguous regions (clusters) of high intensity, calculate their sizes, and determine the average intensity within each cluster.

These problems can be solved efficiently using arrays and basic array operations in coding.
