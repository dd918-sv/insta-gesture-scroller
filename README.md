# Instagram Gesture Control

Control Instagram Reels using facial gestures through your webcam.

This project uses computer vision and facial landmark detection to perform actions on Instagram Reels hands-free.

---

# Features

| Gesture | Action |
|---|---|
| Smile | Next Reel |
| Pout/Kiss Face | Previous Reel |
| Open Mouth | Pause / Play |

---

# Requirements

- Python 3.10 or 3.11
- Webcam
- Instagram account
- Browser (Chrome recommended)

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/dd918-sv/insta-gesture-scroller.git
cd instagram-gesture-control
```
## 2. Create Virtual environment
### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
To avoid any issues please firstly install python's version 3.9.6(search for this version on the webpage) using the link: https://www.python.org/downloads/windows/

Download the 64-bit version.
Below is the installation guide:
1. CHECK: Add Python to PATH option
2. Click: Customize Installation
3. Keep defaults
4. Install
5. Verify the version exists using
   ```bash
     py -0
   ## You should see something like:
   ##  -v:3.13*
   ##  -v:3.9
   ```
Go to the project folder and open the terminal for that folder.
Then follow the below steps:
```bash
py -3.9 -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
## Check python version:
python --version
## It should show Python 3.9.x
```
Install dependencies:

```bash
pip install opencv-python mediapipe=0.10.14 numpy pyautogui
```

## 4. Start the project
### macOS/Linux
```bash
python3 main.py
```

### Windows
```bash
python main.py
```
On starting it might require some camera permissions. Please give the required permission to use the project without facing problems.

After the script starts running open instagram and go to reels for using the app.


