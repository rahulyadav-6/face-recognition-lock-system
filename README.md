# Face Recognition Lock System

This project implements a face recognition-based lock system using OpenCV and Arduino. It detects and recognizes faces to control an external lock mechanism.

## Project Structure

```
haarcascade_frontalface_default.xml  # Pre-trained Haar Cascade for face detection
main.py                              # Main script to run the face recognition system
requirement.txt                      # Python dependencies
arduino/
    led_control/
        led_control.ino              # Arduino code for controlling the lock
dataset/
    person_1/
        img1.jpg                     # Dataset images for person 1
    person_2/
        img1.jpg, img2.jpg, ...      # Dataset images for person 2
    person_3/
        img1.jpg, img2.jpg, ...      # Dataset images for person 3
    person_4/
        img1.jpg, img2.jpg, ...      # Dataset images for person 4
trainer/
    labels.pickle                    # Pickle file for storing label data
    train.py                         # Script to train the face recognizer
    trainer.yml                      # Trained model file
```

## Features

- Face detection using Haar Cascade.
- Face recognition using OpenCV's LBPHFaceRecognizer.
- Arduino integration to control a lock mechanism.

## Requirements

Install the required Python dependencies:

```bash
pip install -r requirement.txt
```

## Usage

1. **Train the Model**:
   Run the training script to train the face recognizer:
   ```bash
   python trainer/train.py
   ```

2. **Run the System**:
   Execute the main script to start the face recognition lock system:
   ```bash
   python main.py
   ```

3. **Arduino Setup**:
   - Upload the `led_control.ino` file from the `arduino/led_control/` directory to your Arduino board.
   - Connect the Arduino to the system for lock control.

## Dataset

The `dataset/` directory contains images of individuals used for training the face recognizer. Add new images to this directory to include more people.

## Files

- `haarcascade_frontalface_default.xml`: Pre-trained Haar Cascade model for face detection.
- `trainer/labels.pickle`: Stores label data for the trained model.
- `trainer/trainer.yml`: Contains the trained face recognition model.

## Arduino Integration

The Arduino code in `arduino/led_control/led_control.ino` is used to control an external lock mechanism. Ensure the Arduino is properly connected to the system.

## Contributing

Feel free to fork this repository and contribute to the project.

## License

This project is licensed under the MIT License.

---

### Repository

This project is hosted on GitHub: [Face Recognition Lock System](https://github.com/rahulyadav-6/face-recognition-lock-system)
