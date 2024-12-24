import tkinter as tk
from tkinter import PhotoImage
from datetime import datetime
from pystray import Icon, MenuItem 
from PIL import Image, ImageDraw, ImageTk
import threading
import time
import sys
import os

# Graduation details
graduation_date = datetime(2025, 5, 17)
albert_info = "Albert Essiaw\nComputer Engineering, Minor: Computer Science\nVirginia Tech"

def get_remaining_time():
    now = datetime.now()
    remaining = graduation_date - now
    if remaining.total_seconds() > 0:
        days, seconds = divmod(remaining.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"
    else:
        return "Congratulations, Graduate!"

# System tray icon logic
class TrayApp:
    def __init__(self, root):
        self.root = root
        self.icon = None
        self.running = True

    def show_window(self, icon, item):
        self.root.deiconify()

    def hide_window(self, icon, item):
        self.root.withdraw()

    def quit_app(self, icon, item):
        self.running = False
        self.icon.stop()
        self.root.destroy()
        sys.exit()

    def create_image(self):
        # Create a small image for the tray icon
        image = Image.new('RGB', (64, 64), color="black")
        draw = ImageDraw.Draw(image)
        draw.text((10, 20), "🎓", fill="white")
        return image

    def update_tooltip(self):
        while self.running:
            countdown = get_remaining_time()
            if self.icon:
                self.icon.title = f"Countdown: {countdown}"
            time.sleep(1)

    def run_tray_icon(self):
        menu = (
            MenuItem("Show", self.show_window),
            MenuItem("Hide", self.hide_window),
            MenuItem("Quit", self.quit_app),
        )
        self.icon = Icon(
            "Graduation Countdown",
            self.create_image(),
            menu=menu
        )
        threading.Thread(target=self.update_tooltip, daemon=True).start()
        self.icon.run()

# Countdown update
def update_countdown():
    remaining_time = get_remaining_time()
    countdown_label.config(text=f"Countdown: {remaining_time}")
    root.after(1000, update_countdown)

# GUI setup
root = tk.Tk()
root.title("Graduation Countdown")
root.geometry("500x400")
root.resizable(False, False)

# Function to locate resources
def resource_path(relative_path):
    """Get the absolute path to the resource, works for PyInstaller bundled files."""
    if hasattr(sys, '_MEIPASS'):
        # Path to the temporary folder used by PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Load background image
background_image = ImageTk.PhotoImage(file=resource_path("background.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Styling variables
label_font_color = "#FFFFFF"  # Light color to contrast the background
shadow_color = "#222222"  # Subtle shadow color

# Info label
info_label = tk.Label(
    root,
    text=albert_info,
    font=("Helvetica", 12, "bold"),
    fg=label_font_color,
    bg="black",
    justify="center",
    padx=5,
    pady=5,
)
info_label.place(relx=0.5, rely=0.15, anchor="center")

# Countdown label
countdown_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 20, "bold"),
    fg=label_font_color,
    bg="black",
    padx=5,
    pady=5,
)
countdown_label.place(relx=0.5, rely=0.4, anchor="center")

# Graduation date label
graduation_date_label = tk.Label(
    root,
    text=f"Graduation Date: {graduation_date.strftime('%B %d, %Y')}",
    font=("Helvetica", 14, "italic"),
    fg=label_font_color,
    bg="black",
    padx=5,
    pady=5,
)
graduation_date_label.place(relx=0.5, rely=0.6, anchor="center")

# Minimize to tray button
def minimize_to_tray():
    root.withdraw()

minimize_button = tk.Button(
    root,
    text="Minimize to Tray",
    command=minimize_to_tray,
    bg="#333333",
    fg="white",
    relief="flat",
)
minimize_button.place(relx=0.5, rely=0.85, anchor="center")

# Start countdown update
update_countdown()

# Run the system tray in a separate thread
tray_app = TrayApp(root)
threading.Thread(target=tray_app.run_tray_icon, daemon=True).start()

# Override close button to minimize to tray
root.protocol("WM_DELETE_WINDOW", minimize_to_tray)

# Start the Tkinter main loop
root.mainloop()
