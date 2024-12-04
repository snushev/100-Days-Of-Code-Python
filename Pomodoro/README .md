
# Pomodoro Timer ⏲️

A simple **Pomodoro Timer** built using Python and the Tkinter library. This application helps users stay productive by using the Pomodoro Technique: alternating between focused work sessions and short breaks.

## Features
- **Work Timer:** 25-minute focused work sessions (default).
- **Short Breaks:** 5-minute breaks after each work session.
- **Long Breaks:** 20-minute breaks after every 4th work session.
- **Visual Feedback:** Tomato image with a countdown timer.
- **Audio Alert:** Beeping sound when a session ends.
- **Progress Tracking:** Checkmarks to track completed work sessions.

## Demo
![Pomodoro Timer Screenshot](https://imgur.com/a/HQh935h)

## Requirements
- Python 3.x
- `winsound` (included in the Python standard library)
- Tkinter (comes pre-installed with Python)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. Make sure the `tomato.png` file is in the same folder as the Python script.

3. Run the script:
   ```bash
   python pomodoro_timer.py
   ```

4. Enjoy your Pomodoro sessions!

## Customization
You can customize the timer durations by changing the following constants in the script:
```python
WORK_MIN = 25  # Minutes for a work session
SHORT_BREAK_MIN = 5  # Minutes for a short break
LONG_BREAK_MIN = 20  # Minutes for a long break
```

## The Pomodoro Technique
The Pomodoro Technique is a time management method that increases productivity:
1. Choose a task.
2. Work on it for 25 minutes (a "Pomodoro").
3. Take a 5-minute break.
4. After 4 Pomodoros, take a 20-minute break.

## Contributing
If you have ideas for improving the app, feel free to open an issue or submit a pull request!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
