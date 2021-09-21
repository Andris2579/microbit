def on_gesture_shake():
    basic.show_number(randint(1, 6))
    basic.clear_screen()
    basic.pause(500)
    basic.show_string("10.i")
    control.reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
