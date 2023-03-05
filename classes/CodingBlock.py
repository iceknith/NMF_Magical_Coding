from tkinter import Canvas


class Block:
    """Coding Block: is used to graphically display actions of code
        they can interract with each other, and form programms"""

    def __init__(self, posX: int, posY: int, w: int, h: int) -> None:
        self.width = w
        self.height = h
        self.x = posX - self.width/2
        self.y = posY - self.height/2

    def display(self, canvas: Canvas):
        """draws code block on the canvas

        Args:
            canvas (Canvas): The canvas the code block is drawn on
        """
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height, fill="#05f")

    def setX(self, posX: int):
        """set the center X position of the block

        Args:
            posX (int): the x center
        """
        self.x = posX - self.width/2

    def setY(self, posY: int):
        """set the center Y position of the block

        Args:
            posX (int): the y center
        """
        self.y = posY - self.height/2
