# 🕒 Digital Clock in Python using Tkinter

import tkinter as tk       # Import tkinter for GUI
from time import strftime  # Import strftime to get formatted time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")  # Set window title
root.geometry("400x150")     # Set window size
root.resizable(False, False) # Disable window resizing

# Function to update time
def time():
    # Get current time in HH:MM:SS format
    current_time = strftime("%H:%M:%S %p")  # %p adds AM/PM
    label.config(text=current_time)         # Update the label with current time
    label.after(1000, time)                 # Call this function again after 1 second (1000 ms)

# Create a label to display time
label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
label.pack(anchor="center", pady=30)  # Center the label with padding

# Call the time function to start the clock
time()

# Run the Tkinter event loop
root.mainloop()
