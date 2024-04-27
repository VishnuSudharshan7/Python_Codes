import tkinter as tk
import time
#update loop
def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

#main window
root = tk.Tk()
root.title("Vishnu's Digital Clock")

#label to display the time
clock_label = tk.Label(root, font=('Arial', 60, 'bold'), background='black', 
foreground='orange') # styling the lable
clock_label.pack(padx=20, pady=20)

#update the time initially and start the update loop
update_time()

#runs the application
root.mainloop()
