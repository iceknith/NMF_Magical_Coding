from PIL import Image, ImageTk
from tkinter import Canvas, NW
"""if __name__ == "__main__":
    from Scene import Scene
elif __name__[:8] == "classes.":
    from classes.Scene import Scene"""


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, message: str, buttonType: str) -> None:
        # variables defnition
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.isFocused = False
        self.isClicked = False

        self.font = ("Arial", 20, "normal")
        self.message = message

        self.typeAssignement(buttonType)

    def typeAssignement(self, buttonType: str):
        """A function that defines the button type, and the skin it
        should have according to its type

        Args:
            buttonType (str): the type of the button
        """

        # pickng images
        if buttonType == "level transition":
            self.type = "level_transition"
            self.clickedImage = Image.open("assets/buttons/baseClicked.png")
            self.focusedImage = Image.open("assets/buttons/baseFocused.png")
            self.unfocusedImage = Image.open(
                "assets/buttons/baseUnfocused.png")

        # resizing images
        self.clickedImage = self.clickedImage.resize(
            (self.width, self.height), Image.BICUBIC)
        self.focusedImage = self.focusedImage.resize(
            (self.width, self.height), Image.BICUBIC)
        self.unfocusedImage = self.unfocusedImage.resize(
            (self.width, self.height), Image.BICUBIC)

        # adapting them into tkinter mode
        self.clickedImage = ImageTk.PhotoImage(self.clickedImage)
        self.focusedImage = ImageTk.PhotoImage(self.focusedImage)
        self.unfocusedImage = ImageTk.PhotoImage(self.unfocusedImage)

        # setting active image
        self.image = self.unfocusedImage

    def display(self, canvas: Canvas):
        canvas.create_image(self.x, self.y, anchor=NW, image=self.image)
        canvas.create_text(self.x + self.width/2, self.y + self.height/2,
                           text=self.message, font=("Arial", 20, "bold"))

    def contains(self, x: int, y: int):
        return x > self.x and x < self.x + self.width \
            and y > self.y and y < self.y + self.height

    def unfocus_Handler(self):
        """Changes image and state to unfocus
        call only if mouse is not in button
        """

        self.isClicked = False
        self.isFocused = False
        self.image = self.unfocusedImage

    def focus_Handler(self, isMouseClick):
        """Changes image according to the state of the mouse
        call only if mouse is in button

        Args:
            isMouseClick (bool): if the mouse is clicked
        """
        if isMouseClick:
            self.isClicked = True
            self.image = self.clickedImage

        elif not self.isFocused:
            self.isFocused = True
            self.image = self.focusedImage

    def click_Handler(self, scene):
        """Handles the button release, and the event that will follow
        """

        # changes the button state
        self.isClicked = False
        self.image = self.focusedImage

        if self.type == "level_transition":
            scene.loadLevel("editor")
