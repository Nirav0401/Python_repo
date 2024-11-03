import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Text Editor - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"Text Editor - {file_path}")
        messagebox.showinfo("Save", "File saved successfully")

def new_file():
    if messagebox.askyesno("New File", "Are you sure you want to create a new file? Unsaved changes will be lost."):
        text_area.delete(1.0, tk.END)
        root.title("Text Editor - New File")

# Initialize main window
root = tk.Tk()
root.title("Text Editor")
root.geometry("500x350")

# Create Text widget for the text area
text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start the application
root.mainloop()
