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
        self.attachedTop = None
        self.attachedBottom = None

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
            self.message = "Unknown"

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
        self.setCornerX(posX - self.width/2)

    def setY(self, posY: int):
        """set the center Y position of the block

        Args:
            posX (int): the y center
        """
        self.setCornerY(posY - self.height/2)

    def getX(self):
        """get center X position of the block

        Returns:
            int: the x center
        """
        return self.x + self.width/2

    def getY(self):
        """get center Y position of the block

        Returns:
            int: the y center
        """
        return self.y + self.height/2

    def setCornerX(self, posX: int):
        self.x = posX
        if self.attachedBottom:
            self.attachedBottom.setCornerX(self.x)

    def setCornerY(self, posY: int):
        self.y = posY
        if self.attachedBottom:
            self.attachedBottom.setCornerY(self.y + self.height)

    def moove(self, posX: int, posY: int, blockList: list):
        self.setX(posX)
        self.setY(posY)
        for b in blockList:

            if self.attachedTop and self.attachedTop.id == b.id and not self.isNearUnder(self.attachedTop):
                b.disatach(self)

            elif b.id != self.id and self.isNearUnder(b):
                b.attach(self)

    def contains(self, x: int, y: int):
        return x > self.x and x < self.x + self.width \
            and y > self.y and y < self.y + self.height

    def isNearUnder(self, block):
        """Check if we are near a block we can attach to

        Args:
            block (Block): the block the check is effectued on

        Returns:
            Boolean
        """
        return abs(self.y - block.y - block.height) < self.height/2\
            and abs(block.x + block.width/2 - self.x - self.width/2) < self.width/2

    def attach(self, b):
        b.setCornerX(self.x)
        b.setCornerY(self.y + self.height)

        if self.attachedBottom and self.attachedBottom.id != b.id:
            a = self.attachedBottom
            self.attachedBottom = b

            b.attachedTop = self
            b.attach(a)
        else:
            self.attachedBottom = b
            b.attachedTop = self

    def disatach(self, b):
        b.attachedTop = None
        self.attachedBottom = None

    def __str__(self) -> str:
        if self.attachedTop:
            at = self.attachedTop.message
        else:
            at = "N"
        if self.attachedBottom:
            ab = self.attachedBottom.message
        else:
            ab = "N"
        return f"{self.message} block, x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}, isFocused: {self.isFocused}, attachedTop: {at}, attachedBottom: {ab}"


if __name__ == "__main__":
    # test zone
    b1 = Block(100, 100, 100, 50, "fire_ball")
    b2 = Block(0, 0, 100, 50, "checker")
    blockList = [b1, b2]
    b2.moove(1000, 500, blockList)
    assert b2.getX() == 1000, "movement X not working"
    assert b2.getY() == 500, "movement Y not working"

    b2.moove(130, 170, blockList)
    assert b2.attachedTop == b1, "top attaching not working"
    assert b1.attachedBottom == b2, "bottom attaching not working"
    assert b2.getX() == b1.getX(), "clipping X not working"
    assert b2.getY() == b1.getY() + b1.height, "clipping Y not working"

    b1.moove(500, 500, blockList)
    assert b2.getX() == 500, "stack x movement not working"
    assert b2.getY() == 550, "stack y movement not working"

    b3 = Block(0, 0, 100, 50, "ice_ahnilator")
    blockList.append(b3)
    b4 = Block(0, 0, 100, 50, "unknown")
    blockList.append(b4)

    b3.moove(500, 610, blockList)
    b4.moove(500, 550, blockList)
    assert b2.attachedTop == b4, "top insertion not working"
    assert b1.attachedBottom == b4, "bottom insertion not working"

    assert b3.attachedTop == b2, "top insertion chain 3rd block not working"
    assert b2.attachedBottom == b3, "bottom insertion chain 2cond block not working"

    assert b2.getY() == 600, "insertion 1st y shift not working"
    assert b3.getY() == 650, "insertion 2cond shift not working"
