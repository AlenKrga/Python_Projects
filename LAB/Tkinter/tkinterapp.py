import tkinter as tk

class UsernameApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a label for the entry box
        label = tk.Label(self, text="Enter your username:")
        label.pack()

        # Create an entry box for the user to input their name
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a button to submit the name
        button = tk.Button(self, text="Submit", command=self.submit_name)
        button.pack()

    def submit_name(self):
        # Get the name entered by the user
        name = self.entry.get()

        # Create a label to display the welcome message
        welcome_label = tk.Label(self, text=f"Welcome, {name}!")
        welcome_label.pack()

if __name__ == '__main__':
    app = UsernameApp()
    app.mainloop()
