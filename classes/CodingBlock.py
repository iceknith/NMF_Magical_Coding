from tkinter import Canvas

blockID = 0


class Block:
    """Coding Block: is used to graphically display actions of code
        they can interract with each other, and form programms"""

    def __init__(self, posX: int, posY: int, w: int, h: int, bType: str) -> None:
        self.width = w
        self.height = h
        self.x = posX - self.width/2
        self.y = posY - self.height/2

        self.defineType(bType)

        self.isFocused = False
        self.attached = None

        global blockID
        self.id = blockID
        blockID += 1

    def defineType(self, bType: str):
        if bType == "fire_ball":
            self.color = "#a60303"
            self.cost = 100
            self.message = "Fire Ball"

        elif bType == "checker":
            self.color = "#e600ac"
            self.cost = 1
            self.message = "Checker"

        elif bType == "ice_ahnilator":
            self.color = "#87ffff"
            self.cost = 1000
            self.message = "Ice Ahnilator"

        else:
            self.color = "#696969"
            self.cost = 0
            self.message = "None"

    def display(self, canvas: Canvas):
        """draws code block on the canvas

        Args:
            canvas (Canvas): The canvas the code block is drawn on
        """
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
        canvas.create_text(self.x + self.width/2, self.y + self.height/2,
                           text=self.message, font=("Arial", 20, "bold"))

    def update(self):
        pass

    def setX(self, posX: int):
        """set the center X position of the block

        Args:
            posX (int): the x center
        """
        self.setExactX(posX - self.width/2)

    def setY(self, posY: int):
        """set the center Y position of the block

        Args:
            posX (int): the y center
        """
        self.setExactY(posY - self.height/2)

    def setExactX(self, posX: int):
        self.x = posX
        if self.attached:
            self.attached.setExactX(self.x)

    def setExactY(self, posY: int):
        self.y = posY
        if self.attached:
            self.attached.setExactY(self.y + self.height)

    def moove(self, posX: int, posY: int, blockList: list):
        self.setX(posX)
        self.setY(posY)
        for b in blockList:

            if b.attached and b.attached.id == self.id:
                b.attached = None

            if b.id != self.id and self.isNear(b):
                b.attach(self)

    def contains(self, x: int, y: int):
        return x > self.x and x < self.x + self.width \
            and y > self.y and y < self.y + self.height

    def isNear(self, block):
        """Check if we are near a block we can attach to

        Args:
            block (Block): the block the check is effectued on

        Returns:
            Boolean
        """
        return abs(self.y - block.y - block.height) < self.height/2\
            and abs(block.x + block.width/2 - self.x - self.width/2) < self.width/2

    def attach(self, b):
        b.setExactX(self.x)
        b.setExactY(self.y + self.height)
        if self.attached:
            b.attach(self.attached)
        self.attached = b


if __name__ == "__main__":
    # test zone
    pass
