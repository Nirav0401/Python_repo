import tkinter as tk
from tkinter import messagebox
from time import strftime

def show_time():
    # Get current time and date
    current_time = strftime("%H:%M:%S %p \n %D")
    label.config(text=current_time)
    label.after(1000, show_time)

    # Show message box with the time and date (will update the time as changes)
    # messagebox.showinfo("Time-Date", f"Time: {current_time}")
    
# optional
# def show_popup():
#     # Show message box with the initial time and date
#     current_time = strftime("%H:%M:%S %p \n %D")
#     messagebox.showinfo("Time-Date", f"Time: {current_time}")

# Create the main window
root = tk.Tk()
root.title("Time Display")
# root.geometry("300x100")

# label to show the time
label = tk.Label(root, font=("calibri", 50, "bold"), background="yellow", foreground="black")
# show_time_button.pack(pady=20)
label.pack(anchor="center")

# show_popup()
show_time()
root.mainloop()
