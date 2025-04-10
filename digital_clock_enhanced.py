import tkinter as tk
from time import strftime
import random
from tkinter import font

def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%A, %d %B %Y')
    
    label_time.config(text=current_time)
    label_date.config(text=current_date)

    colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33F5', '#33FFF5']
    color = random.choice(colors)
    
    label_time.config(fg=color)
    label_date.config(fg=color)

    label_time.after(1000, update_time)

# Main window
root = tk.Tk()
root.title('Enhanced Digital Clock')
root.geometry('600x300')
root.configure(bg='black')
root.resizable(True, True)

# Custom fonts
try:
    time_font = font.Font(family='DS-Digital', size=70)
    date_font = font.Font(family='Arial', size=20, weight='bold')
except:
    time_font = font.Font(size=70)
    date_font = font.Font(size=20, weight='bold')

# Time Label
label_time = tk.Label(root, font=time_font, bg='black')
label_time.pack(expand=True, pady=10)

# Date Label
label_date = tk.Label(root, font=date_font, bg='black')
label_date.pack(expand=True)

# Exit Button
exit_btn = tk.Button(root, text='Exit', command=root.destroy, 
                    bg='red', fg='white', font=('Arial', 12))
exit_btn.pack(side='bottom', pady=10)

update_time()

root.mainloop()
