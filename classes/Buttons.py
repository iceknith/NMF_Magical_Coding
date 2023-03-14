from PIL import Image, ImageTk
from tkinter import Canvas, NW
if __name__ == "__main__":
    from CodingBlock import Block
if __name__ == "classes.Buttons":
    from classes.CodingBlock import Block


buttonID = 0


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, message: str, buttonType: tuple, canvas: Canvas) -> None:
        # variables defnition
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvasObjectsID = []

        self.isFocused = False
        self.isClicked = False

        self.font = ("Arial", 20, "normal")
        self.message = message

        self.canvas = canvas

        self.typeAssignement(buttonType)

        global buttonID
        self.id = "Button" + str(buttonID)
        buttonID += 1

    def typeAssignement(self, buttonType: str):
        """A function that defines the button type, and the skin it
        should have according to its type

        Args:
            buttonType (str): the type of the button
        """

        # defining images and behaviour according to button type
        if buttonType[0] == "level transition":
            self.type = "level_transition"
            self.level = buttonType[1]

            self.clickedImage = Image.open("assets/buttons/baseClicked.png")
            self.focusedImage = Image.open("assets/buttons/baseFocused.png")
            self.unfocusedImage = Image.open(
                "assets/buttons/baseUnfocused.png")

        elif buttonType[0] == "block creation":
            self.type = "block_creation"
            self.blockType = buttonType[1]

            self.clickedImage = Image.open("assets/blocks/normalBlockRed.png")
            self.focusedImage = Image.open("assets/blocks/normalBlockRed.png")
            self.unfocusedImage = Image.open(
                "assets/blocks/normalBlockRed.png")

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

    def visual_Update(self):
        # destroy previous displayed buttons
        self.delete_Visually()

        # reset variables
        self.canvasObjectsID.clear()

        # display button
        self.canvasObjectsID.append(self.canvas.create_image(
            self.x, self.y, anchor=NW, image=self.image))
        self.canvasObjectsID.append(self.canvas.create_text(self.x + self.width/2, self.y + self.height/2,
                                                            text=self.message, font=("Arial", 20, "bold")))

    def delete_Visually(self):
        """deletes the button image from the canvas
        """
        for objID in self.canvasObjectsID:
            self.canvas.delete(objID)

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
        self.visual_Update()

    def focus_Handler(self, isMouseClick: bool, scene):
        """Changes image according to the state of the mouse
        and triggers the button according to its type
        call only if mouse is in button

        Args:
            isMouseClick (bool): if the mouse is clicked
        """
        if isMouseClick and not scene.focusedBlock:
            self.isClicked = True
            self.image = self.clickedImage
            self.visual_Update()

            # click according to the button type
            if self.type == "block_creation":
                self.isClicked = False
                self.click_Handler(scene)

        # click if button press was released
        elif self.isClicked and not scene.focusedBlock:
            self.click_Handler(scene)

        elif not self.isFocused:
            self.isFocused = True
            self.image = self.focusedImage
            self.visual_Update()

    def click_Handler(self, scene):
        """Handles the button release, and the event that will follow
        """
        # changes the button state
        self.isClicked = False
        self.image = self.focusedImage

        if self.type == "level_transition":
            scene.loadLevel(self.level, self.canvas)

        elif self.type == "block_creation":
            # create block
            bt = self.blockType
            new_block = Block(-10000, 0, bt[0], bt[1], bt[2], self.canvas)
            scene.add_Object(new_block)

            # focus block
            new_block.isFocused = True
            if scene.focusedBlock:
                scene.focusedBlock.isFocused = False
            scene.focusedBlock = new_block
