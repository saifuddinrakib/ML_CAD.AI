import pyautogui
import pygetwindow

titles = pygetwindow.getAllTitles()
print(titles)  # Check the output and find the title of the Chrome window you want to track

import keyboard
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from mpl_toolkits.mplot3d import Axes3D
import datetime

# Get the handle to the window you want to track
# Get the handle to the window you want to track
window = pygetwindow.getWindowsWithTitle('Google - Chrome')[0]

# Activate the window
window.activate()

while True:
    if not window.isActive:
        break
    keys = keyboard.record(until='enter')
    words = []
    for key in keys:
        words.append(key.name)
    words.append('\n')
    with open('words.txt', 'a') as file:
        file.writelines(words)



# Start recording the keys that are typed in the window
keyboard.start_recording()

# Create empty lists to store the typing times, timestamps, and z-values
typing_times = []
timestamps = []
z_values = []

while True:
    # Check if the window is still open
    if not window.is_active:
        break
    
    # Wait for a key to be pressed
    event = keyboard.wait()
    
    # Check if the key was typed in the window
    if event.window == window.handle:
        # Add the current timestamp to the list of timestamps
        timestamps.append(datetime.datetime.now())
        
        # Calculate the typing time as the difference between the current and previous timestamps
        if len(typing_times) == 0:
            typing_times.append(0)
        else:
            typing_times.append((timestamps[-1] - timestamps[-2]).total_seconds())
        
        # Print the key and typing time
        print(event.name, typing_times[-1])
        
        # Prompt the user to enter a z-value
        z_value = input("Enter a z-value: ")
        try:
            z_value = float(z_value)
        except ValueError:
            print("Invalid z-value, using default value of 0.")
            z_value = 0
        
        # Add the z-value to the list of z-values
        z_values.append(z_value)

# Stop recording the keys
keyboard.stop_recording()

# Create a 3D plot of the typing times with the z-values as the z-axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(range(len(typing_times)), z_values, typing_times)
ax.set_xlabel('Keystroke')
ax.set_ylabel('Z-Value')
ax.set_zlabel('Typing Time (seconds)')
ax.set_title('Typing Time vs. Keystroke and Z-Value')
ax.zaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
plt.show()
