from tkinter import Toplevel


def lock(waiting_window: Toplevel):
    waiting_window.grab_set()
    print("Grab set!")


def unlock(waiting_window: Toplevel):
    waiting_window.grab_release()
    print("Grab released!")


def on_close(waiting_window: Toplevel):
    if waiting_window is not None:
        unlock(waiting_window)
        waiting_window.destroy()  # Code Review: Pycharm is telling me off, is the way I'm doing this an issue?
        # If so, What's a better way to do this?




