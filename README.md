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
```bash
python -m venv venv
venv\Scripts\activate
```
## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Start the project
```bash
python3 main.py
```
On starting it will require some camera permissions. Please give the required permission to use the project without facing problems.




