import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

# Secure random generator
secure_random = random.SystemRandom()

def generate_password():
    length = password_length.get()
    include_special = special_chars.get()

    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4!")
        return

    chars = string.ascii_letters + string.digits
    if include_special:
        chars += string.punctuation

    password = ''.join(secure_random.choice(chars) for _ in range(length))

    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def copy_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Warning", "No password to copy!")
        return
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def save_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Warning", "No password to save!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Password As"
    )
    if file_path:
        with open(file_path, "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Saved", f"Password saved to:\n{file_path}")

def on_enter(e):
    e.widget['background'] = 'blue'

def on_leave(e):
    e.widget['background'] = e.widget.original_bg

# Main window
root = tk.Tk()
root.title("Fancy Password Generator")
root.geometry("550x420")
root.configure(bg="#121212")  # Dark background

# Heading
heading = tk.Label(root, text="Password Generator", font=("Arial Black", 22), bg="#121212", fg="cyan")
heading.pack(pady=10)

# Password Entry
entry_password = tk.Entry(root, font=("Arial", 18), width=30, bd=2, relief="solid", justify="center")
entry_password.pack(pady=15)

# Special Characters Checkbox
special_chars = tk.BooleanVar(value=True)
checkbox = tk.Checkbutton(
    root,
    text="Include Special Characters ( !@#$ )",
    variable=special_chars,
    font=("Arial", 12),
    bg="#121212",
    fg="white",
    activebackground="#121212",
    activeforeground="lime",
    selectcolor="#121212"
)
checkbox.pack(pady=5)

# Password Length Slider
tk.Label(root, text="Select Password Length:", font=("Arial", 12), bg="#121212", fg="white").pack()
password_length = tk.IntVar(value=12)
slider = tk.Scale(
    root,
    from_=4,
    to=40,
    orient="horizontal",
    variable=password_length,
    bg="#121212",
    fg="lime",
    troughcolor="gray",
    highlightbackground="#121212"
)
slider.pack(pady=5)

# Create buttons with hover effects
def make_hover_button(text, command, color):
    btn = tk.Button(root, text=text, font=("Arial", 14), bg=color, fg="white", command=command)
    btn.original_bg = color
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=5)
    return btn

btn_generate = make_hover_button("Generate Password", generate_password, "magenta")
btn_copy = make_hover_button("Copy Password", copy_password, "green")
btn_save = make_hover_button("Save Password", save_password, "orange")

# Start the GUI loop
root.mainloop()
 