import re
import random
import string
import tkinter as tk
from tkinter import messagebox

def check_password_complexity(password):
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_numbers = re.search(r'[0-9]', password)
    has_special_characters = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    criteria = {
        "Length at least 8 characters": len(password) >= min_length,
        "Contains uppercase letter": bool(has_uppercase),
        "Contains lowercase letter": bool(has_lowercase),
        "Contains number": bool(has_numbers),
        "Contains special character": bool(has_special_characters)
    }

    return criteria

def suggest_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_check_password():
    username = username_entry.get()
    password = password_entry.get()

    if not username:
        messagebox.showerror("Input Error", "Username cannot be empty!")
        return

    criteria = check_password_complexity(password)

    result_text = f"Username: {username}\n\n"
    for criterion, met in criteria.items():
        status = "Met" if met else "Not Met"
        result_text += f"{criterion}: {status}\n"

    if all(criteria.values()):
        complexity = "Strong"
    elif any(criteria.values()):
        complexity = "Moderate"
    else:
        complexity = "Weak"

    result_text += f"\nOverall password complexity: {complexity}"
    
    result_label.config(text=result_text)

    if complexity != "Strong":
        feedback_text = "\nYour password is not strong enough. Here are some suggestions:"
        if len(password) < 8:
            feedback_text += "\n- Make your password at least 8 characters long."
        if not re.search(r'[A-Z]', password):
            feedback_text += "\n- Include at least one uppercase letter."
        if not re.search(r'[a-z]', password):
            feedback_text += "\n- Include at least one lowercase letter."
        if not re.search(r'[0-9]', password):
            feedback_text += "\n- Include at least one number."
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            feedback_text += "\n- Include at least one special character."

        feedback_text += f"\n\nSuggested strong password:\n{suggest_strong_password()}"
        messagebox.showinfo("Password Feedback", feedback_text)

# Create the main window
root = tk.Tk()
root.title("Login and Password Complexity Checker")

# Create and place widgets for username
tk.Label(root, text="Enter your username:").pack(pady=10)

username_entry = tk.Entry(root, width=40)
username_entry.pack(pady=10)

# Create and place widgets for password
tk.Label(root, text="Enter your password:").pack(pady=10)

password_entry = tk.Entry(root, show='*', width=40)
password_entry.pack(pady=10)

# Create and place the Check Password button
check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.pack(pady=10)

# Label to display the results
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
