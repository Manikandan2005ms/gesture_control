def preprocess_data(data):
    # Function to preprocess gesture data
    # Normalize the data or perform any necessary transformations
    normalized_data = (data - data.mean()) / data.std()
    return normalized_data

def save_screenshot(image, filename):
    # Function to save a screenshot
    # image: the image to save
    # filename: the name of the file to save the image as
    image.save(f'screenshots/{filename}')

def log_action(action, gesture):
    # Function to log actions taken by the system
    # action: the action performed
    # gesture: the recognized gesture
    with open('logs/gesture_log.csv', 'a') as log_file:
        log_file.write(f'{action},{gesture}\n')