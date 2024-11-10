from spellchecker import SpellChecker as PySpellChecker  # type: ignore
import tkinter as tk

class SpellCheckerApp:
    def __init__(self, root):
        self.spell = PySpellChecker()
        self.root = root

        # Set up the window
        root.title("Spelling Check")
        root.geometry("400x300")

        # Create label for user instruction
        self.label = tk.Label(root, text="Enter the Text Here", font=("Arial", 10, "bold"))
        self.label.pack(pady=10)

        # Create a multi-line Text widget for user input
        self.textbox = tk.Text(root, wrap="word", width=40, height=5)
        self.textbox.pack(pady=5)

        # Button to check spelling
        self.button = tk.Button(root, text="Submit", command=self.correct_check)
        self.button.pack(pady=10)

        # Label for displaying corrected text
        self.result_label = tk.Label(root, text="Corrected Text:", font=("Arial", 10, "bold"))
        self.result_label.pack(pady=5)

        # Multi-line Text widget to display corrected text
        self.corrected_textbox = tk.Text(root, wrap="word", width=40, height=5, state="disabled", fg="green")
        self.corrected_textbox.pack(pady=5)

    def correct_check(self):
        # Get the user input from textbox
        user_text = self.textbox.get("1.0", tk.END).strip()  # Retrieve all text from the Text widget
        corrected_words = []

        # Split text into words and correct them
        words = user_text.split()
        for word in words:
            corrected_word = self.spell.correction(word)
            corrected_words.append(corrected_word)

        # Display corrected text
        corrected_text = ' '.join(corrected_words)
        
        # Enable corrected_textbox to insert text, then disable it again to make it read-only
        self.corrected_textbox.config(state="normal")
        self.corrected_textbox.delete("1.0", tk.END)  # Clear previous content
        self.corrected_textbox.insert(tk.END, corrected_text)  # Insert new corrected text
        self.corrected_textbox.config(state="disabled") # Make it read-only

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()
