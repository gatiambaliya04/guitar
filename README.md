# Virtual Guitar using OpenCV & MediaPipe

A virtual guitar built using Python, OpenCV, and MediaPipe! Control the guitar with your thumb gestures — open your hand to play, close your fist to mute. Simple and fun to play using just your webcam.

---

## Project Structure

```
├── main.py           # Main code to run the virtual guitar
├── check_cam.py      # Utility to check if the webcam is accessible
├── sounds/           # Contains the 6 string sound files (.wav)
```

---

## Requirements

- Python 3.12
- opencv-python
- mediapipe
- pygame
- numpy

### Install with pip:

```bash
pip install opencv-python mediapipe pygame numpy
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/gatiambaliya04/guitar.git
   cd guitar
   ```

2. (Optional) Check webcam access:
   ```bash
   python check_cam.py
   ```

3. Run the virtual guitar:
   ```bash
   python main.py
   ```

---

## Sound Customization

You can replace the sound files in the `sounds/` folder with your own `.wav` files if you want different tones or instruments.  
The files must be named:
```
string_0.wav, string_1.wav, ..., string_5.wav
```

---

## Controls

- Open Hand → Tracks thumb tip to play string  
- Closed Fist → Disables tracking (mute)

---

## Dependencies

This project uses MediaPipe for hand tracking and OpenCV for camera and visualization. The sounds are handled using pygame's mixer module.

---

## License

MIT License © 2025

