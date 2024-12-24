
# Graduation Countdown

**Graduation Countdown** is a personal desktop application designed to track the remaining time until your graduation day. The app displays a real-time countdown and allows for easy management with a user-friendly GUI and system tray integration.

---

## Features

- **Real-Time Countdown**: Displays the time remaining until the graduation date in days, hours, minutes, and seconds.
- **Personalized Information**: Shows customized details, such as your name, major, and university.
- **System Tray Support**: Minimize the app to the system tray and access options to show, hide, or quit the app.
- **Custom Background**: Uses a custom background image for enhanced visuals.

---

## Prerequisites

- **Python**: Python 3.7 or later is required.
- **Required Libraries**:
  - `pystray`
  - `pillow`
  - `tkinter` (included with Python)

To install the required libraries:
```bash
pip install pystray pillow
```

---

## Installation and Usage

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/graduation-countdown.git
   cd graduation-countdown
   ```

2. Place a background image named `background.png` in the same directory as the script.

3. Run the script:
   ```bash
   python graduation_countdown.py
   ```

---

## Customization

- **Set Your Graduation Date**:
  Modify the `graduation_date` variable in the script:
  ```python
  graduation_date = datetime(2025, 5, 17)
  ```

- **Update Personal Information**:
  Change the `albert_info` variable to include your details:
  ```python
  albert_info = "Your Name\nYour Major, Minor: Your Minor\nYour University"
  ```

- **Change the Background**:
  Replace the `background.png` file with your preferred image.

---

## Building a Standalone Executable

To distribute the app as an executable, you can use **PyInstaller**.

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole --hidden-import pystray --add-data "background.png;." graduation_countdown.py
   ```

3. The executable will be located in the `dist` folder.

---

## File Structure

```
.
├── graduation_countdown.py  # Main application script
├── background.png           # Background image for the GUI
├── README.md                # Project documentation
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Developed by **Albert Essiaw** as a personal project.
- Special thanks to the developers of Python, Tkinter, Pystray, and Pillow for the tools and libraries used in this app.

---

Feel free to adapt this README further based on additional features or resources you may want to include. Let me know if you need assistance with anything else!