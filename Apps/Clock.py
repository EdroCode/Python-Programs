import tkinter as tk
import math
from datetime import datetime

# Create the main window
root = tk.Tk()

# Set the title and size of the window
root.title("Clock")
root.geometry("200x200")

# Create a canvas to draw the clock on
canvas = tk.Canvas(root, width=150, height=150)
canvas.pack()

# Define the center and radius of the clock
center_x = 75
center_y = 75
radius = 70

# Draw the face of the clock
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill="white", outline="black")

# Draw the ticks on the clock
for i in range(12):
  angle = i * 30
  x1 = center_x + radius * 0.9 * math.sin(math.radians(angle))
  y1 = center_y - radius * 0.9 * math.cos(math.radians(angle))
  x2 = center_x + radius * 0.95 * math.sin(math.radians(angle))
  y2 = center_y - radius * 0.95 * math.cos(math.radians(angle))
  canvas.create_line(x1, y1, x2, y2, width=2, fill="black")

# Draw the hands of the clock
hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.6, width=4, fill="black")
minute_hand = canvas.create_line(center_x, center_y, center_x, center_y - radius * 0.8, width=2, fill="black")

# Create a label to display the time
time_label = tk.Label(root, font=("Helvetica", 12))
time_label.pack()

# Define a function to update the time
def update_time():
  # Get the current time
  current_time = datetime.now()
  hour = current_time.hour % 12
  minute = current_time.minute
  second = current_time.second

  # Update the time label
  time_label.configure(text=current_time.strftime("%I:%M:%S %p"))

  # Update the position of the hands
  canvas.coords(hour_hand, center_x, center_y, center_x + radius * 0.6 * math.sin(math.radians(hour * 30)), center_y - radius * 0.6 * math.cos(math.radians(hour * 30)))
  canvas.coords(minute_hand, center_x, center_y, center_x + radius * 0.8 * math.sin(math.radians(minute * 6)), center_y - radius * 0.8 * math.cos(math.radians(minute * 6)))

  # Call this function again in one second
  root.after(1000, update_time)

# Call the update_time function for the first time
update_time()

root.mainloop()
