import waiting_window_settings as wws

waiting_window = None


def waiting_popup():
    global waiting_window

    if waiting_window is None:
        waiting_window = wws.initialized_waiting_window


