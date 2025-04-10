import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os

def generate_qr():
    data = entry.get()
    if data == "":
        messagebox.showerror("Error", "Please enter some data to generate QR Code.")
        return

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("temp_qr.png")

    # Show image in GUI
    show_qr("temp_qr.png")

    messagebox.showinfo("Success", "QR Code Generated Successfully!")

def save_qr():
    try:
        if qr_label.image is None:
            messagebox.showerror("Error", "No QR Code to save. Generate one first.")
            return
    except:
        messagebox.showerror("Error", "No QR Code to save. Generate one first.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("temp_qr.png")
        img.save(file_path)
        messagebox.showinfo("Saved", f"QR Code saved to:\n{file_path}")

def show_qr(image_path):
    img = Image.open(image_path)
    img = img.resize((200, 200))
    qr_tk = ImageTk.PhotoImage(img)

    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk

# Main GUI
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="lightgray")

tk.Label(root, text="Enter data for QR Code:", font=("Arial", 12), bg="lightgray").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr, font=("Arial", 12), bg="green", fg="white")
save_button.pack(pady=5)

qr_label = tk.Label(root, bg="lightgray")
qr_label.pack(pady=20)

# Show placeholder image if exists
if os.path.exists("temp_qr.png"):
    show_qr("temp_qr.png")

root.mainloop()
