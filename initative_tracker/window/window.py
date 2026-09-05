from tkinter import TclError, Tk
from tkinter.ttk import Button, Frame, Label

window: Tk = Tk()
window.title("Initative Tracking Application")


def window_main():
    """Main function for the windowing systems for the initative tracker."""
    try:
        frame: Frame = Frame(window, padding=10)
        frame.grid()
        Label(frame, text="Test application").grid(column=0, row=0)

        Button(frame, text="quit", command=window.destroy).grid(column=1, row=0)
        window.mainloop()
    except TclError as e:
        print(f"Error: {e}")
