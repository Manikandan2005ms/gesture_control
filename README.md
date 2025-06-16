# Gesture Control System

This project is a gesture recognition system that processes and recognizes gestures to perform specific actions. It consists of several components that work together to achieve this functionality.

## Project Structure

```
gesture_control/
├── main.py                 # Main file to run the system
├── utils.py                # Utility functions for gestures
├── gesture_map.py          # Gesture logic mapping
├── screenshots/            # Folder where screenshots are saved
└── logs/
    └── gesture_log.csv     # Action logs
```

## Files Description

- **main.py**: This is the main entry point of the application. It initializes the system and orchestrates the gesture recognition process.

- **utils.py**: Contains utility functions that assist with gesture processing, such as data preprocessing and normalization.

- **gesture_map.py**: Defines the logic for mapping recognized gestures to specific actions. It includes classes or functions that handle the gesture recognition logic.

- **screenshots/**: A directory intended to store screenshots captured during the gesture recognition process for reference or debugging purposes.

- **logs/**: This directory contains log files. The `gesture_log.csv` file logs actions taken by the system, including timestamps and recognized gestures.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd gesture_control
   ```

3. Install the required dependencies (if any):
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To run the gesture recognition system, execute the following command:
```
python main.py
```

Ensure that your camera is accessible and properly configured to capture gestures.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.