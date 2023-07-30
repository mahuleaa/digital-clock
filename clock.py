import tkinter as tk
from time import strftime
from datetime import date

def time():
    time_12h = strftime('%I:%M:%S %p')  # 12-hour format
    time_24h = strftime('%H:%M:%S')     # 24-hour format
    label_12h.config(text=time_12h)
    label_24h.config(text=time_24h)
    label_date.config(text=date.today().strftime("%B %d, %Y"))
    label_12h.after(1000, time)
    label_24h.after(1000, time)

# Create the main window
root = tk.Tk()
root.title("Attractive Digital Clock")
root.geometry("500x300")
root.config(bg='#E6E6FA')

# Create a custom font for the labels
font_style = ('Arial', 60, 'bold')
small_font_style = ('Arial', 24, 'bold')

# Create labels to display the 12-hour and 24-hour time formats
label_12h = tk.Label(root, font=font_style, fg='#1E90FF', bg='#E6E6FA')
label_24h = tk.Label(root, font=font_style, fg='#1E90FF', bg='#E6E6FA')

# Pack the labels to display them in the window
label_12h.pack(pady=20)
label_24h.pack(pady=5)

# Create a label to display the date
label_date = tk.Label(root, font=small_font_style, fg='#1E90FF', bg='#E6E6FA')
label_date.pack(pady=10)

# Set margins on the left and right sides of the window
left_margin = tk.Frame(root, bg='black', width=100)
left_margin.pack(side=tk.LEFT, fill=tk.Y)
right_margin = tk.Frame(root, bg='black', width=100)
right_margin.pack(side=tk.RIGHT, fill=tk.Y)

# Call the time function to update the time display
time()

# Start the GUI main loop
root.mainloop()
