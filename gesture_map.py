class GestureMapper:
    def __init__(self):
        self.gesture_actions = {
            "swipe_left": self.action_swipe_left,
            "swipe_right": self.action_swipe_right,
            "tap": self.action_tap,
            "pinch": self.action_pinch,
            "zoom": self.action_zoom
        }

    def map_gesture(self, gesture):
        action = self.gesture_actions.get(gesture)
        if action:
            action()
        else:
            print(f"Gesture '{gesture}' not recognized.")

    def action_swipe_left(self):
        print("Action: Swipe Left")

    def action_swipe_right(self):
        print("Action: Swipe Right")

    def action_tap(self):
        print("Action: Tap")

    def action_pinch(self):
        print("Action: Pinch")

    def action_zoom(self):
        print("Action: Zoom")