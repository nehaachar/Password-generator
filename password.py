import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    password_length = length_var.get()
    password = generate_password(password_length)
    result_label.config(text=f"Generated Password: {password}")
    display_password_strength(password)

def display_password_strength(password):
    strength = "Weak" if len(password) < 12 else "Strong"
    strength_label.config(text=f"Password Strength: {strength}")

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets
welcome_label = tk.Label(window, text="Welcome to the Password Generator!", font=('Helvetica', 12, 'bold'))
welcome_label.pack(pady=10)

length_label = tk.Label(window, text="Enter the desired length of the password:")
length_label.pack()

length_var = tk.IntVar()
length_entry = ttk.Entry(window, textvariable=length_var)
length_entry.pack(pady=10)

generate_button = ttk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

result_label = tk.Label(window, text="Generated Password: ")
result_label.pack()

strength_label = tk.Label(window, text="Password Strength: ")
strength_label.pack()

# Run the main loop
window.mainloop()