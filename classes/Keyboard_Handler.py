from tkinter import Tk


class Keyboard:

    def __init__(self, root: Tk) -> None:
        # varaible definition
        self.__keyPressed = None

        # binding fontions to root
        root.bind("<Key>", self.key_Pressed_Handler)

    def key_Pressed_Handler(self, event):
        """Handles a key press, by changing the pressed key

        Args:
            event (KeyPress Event): the click
        """
        self.__keyPressed = event

    def getLastKeyPressed(self):
        """Returns the last key pressed and deletes it
        and returns None if no key was pressed since the last call

        Returns:
            KeyPress event: the last pressed key
        """
        if self.__keyPressed:
            key = self.__keyPressed
            self.__keyPressed = None
            return key
        else:
            return None
