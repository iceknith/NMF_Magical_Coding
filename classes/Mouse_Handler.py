from tkinter import Tk


class Mouse:

    def __init__(self, root: Tk) -> None:
        # variables definition
        self.isLeftClick = False
        self.isRightClick = False
        self.isMiddleClick = False
        self.x = 0
        self.y = 0

        # binding fontions to root
        root.bind("<ButtonPress>", self.button_Pressed_Handler)
        root.bind("<ButtonRelease>", self.button_Release_Handler)
        root.bind("<Motion>", self.movement_Handler)

    def button_Pressed_Handler(self, event):
        """Handles a click by setting to true selected variables

        Args:
            event (ButtonPress Event): the click
        """
        if event.num == 1:
            self.isLeftClick = True
        elif event.num == 2:
            self.isRightClick = True
        elif event.num == 3:
            self.isMiddleClick = True

    def button_Release_Handler(self, event):
        """Handles the end of a click by setting to false selected variables

        Args:
            event (ButtonRelease Event): the end of the click
        """
        if event.num == 1:
            self.isLeftClick = False
        elif event.num == 2:
            self.isRightClick = False
        elif event.num == 3:
            self.isMiddleClick = False

    def movement_Handler(self, event):
        """Handles the movement

        Args:
            event (Motion Event): the mouse movement
        """
        self.x, self.y = event.x, event.y
