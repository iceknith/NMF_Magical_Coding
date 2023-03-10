from tkinter import Canvas, NW
from PIL import Image, ImageTk

blockID = 0


class Block:
    """Coding Block: is used to graphically display actions of code
        they can interract with each other, and form programms"""

    def __init__(self, posX: int, posY: int, w: int, h: int, bType: str, canvas: Canvas) -> None:
        self.width = w
        self.height = h
        self.x = posX - self.width/2
        self.y = posY - self.height/2
        self.canvasObjectsID = []

        self.defineType(bType)

        self.isFocused = False
        self.attachedTop = None
        self.attachedBottom = None

        self.attachPointsMale = [(0.32, -0.145)]  # temporary, will change
        self.attachPointsFemale = [(0.32, 0.855)]
        self.shadowBlock = None

        self.canvas = canvas

        global blockID
        self.id = "Block" + str(blockID)
        blockID += 1

    def defineType(self, bType: str):
        """definies and initiates variable according to type, like the image and the mana cost

        Args:
            bType (str): the type
        """

        # 114.5% height, because the little connecting square (on top) is 0.145 the height of the image
        h = int(self.height*1.148)

        if bType == "fire_ball":
            self.image = ImageTk.PhotoImage(Image.open(
                "assets/blocks/normalBlockRed.png").resize((self.width, h), Image.BICUBIC))
            self.cost = 100
            self.message = "Fire Ball"

        elif bType == "checker":
            self.image = ImageTk.PhotoImage(Image.open(
                "assets/blocks/normalBlockPurple.png").resize((self.width, h), Image.BICUBIC))
            self.cost = 1
            self.message = "Checker"

        elif bType == "ice_ahnilator":
            self.image = ImageTk.PhotoImage(Image.open(
                "assets/blocks/normalBlockBlue.png").resize((self.width, h), Image.BICUBIC))
            self.cost = 1000
            self.message = "Ice Ahnilator"

        else:
            self.image = ImageTk.PhotoImage(Image.open(
                "assets/blocks/normalBlockBlack.png").resize((self.width, h), Image.BICUBIC))
            self.cost = 0
            self.message = ""

    def visual_Update(self):
        """draws the code block on the canvas
        """

        # destroy previous displayed block
        self.delete_Visually()

        # reset variables
        self.canvasObjectsID.clear()

        # displays actual block
        self.canvasObjectsID.append(self.canvas.create_image(self.x, self.y - 0.145 *
                                                             self.height, anchor=NW, image=self.image))
        self.canvasObjectsID.append(self.canvas.create_text(self.x + self.width/2, self.y + self.height*0.855/2,
                                                            text=self.message, font=("Arial", 20, "bold")))

    def delete_Visually(self):
        """deletes the code block image from the canvas
        """

        for objID in self.canvasObjectsID:
            self.canvas.delete(objID)

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
        """set the corner X position of the block,
        update it visually to display the change and repeat for
        the attached blocks

        Args:
            posX (int): the x positon
        """
        # visual update
        for objID in self.canvasObjectsID:
            self.canvas.move(objID, posX - self.x, 0)

            # put on top
            self.canvas.tag_raise(objID)

        # set variables
        self.x = posX

        # continue chain
        if self.attachedBottom:
            self.attachedBottom.setCornerX(self.x)

    def setCornerY(self, posY: int):
        """set the corner Y position of the block,
        update it visually to display the change and repeat for
        the attached blocks

        Args:
            posY (int): the x positon
        """
        # visual update
        for objID in self.canvasObjectsID:
            self.canvas.move(objID, 0, posY - self.y)
            # put on top
            self.canvas.tag_raise(objID)

        # set variables
        self.y = posY

        # continue chain
        if self.attachedBottom:
            self.attachedBottom.setCornerY(self.y + self.height)

    def moove(self, posX: int, posY: int, scene):
        """Dinamically moove the coding block, making shadow block
        apear where it would snap if it is to be released

        Args:
            posX (int): the new X position
            posY (int): the new Y position
            scene (Scene): the scene where the block is stored
        """

        self.setX(posX)
        self.setY(posY)
        for b in scene.displayedBlocks:

            if self.shadowBlock and self.shadowBlock.attachedTop.id == b.id and not b.isNearAttachPoints(self):
                # deletes shadow block
                self.delete_Shadow()

            elif b.id != self.id and not self.shadowBlock and b.isNearAttachPoints(self):
                self.place_Shadow(b)

    def contains(self, x: int, y: int) -> bool:
        """Returns True if the point of coordinates (x,y) is in the block's hitbox

        Args:
            x (int): the x coordinated of the point
            y (int): the y coordinates of the point

        Returns:
            bool: if (x,y) in block
        """

        return x > self.x and x < self.x + self.width \
            and y > self.y and y < self.y + self.height

    def isNearAttachPoints(self, block) -> bool:
        """Check if attach points female are near to attach points male

        Args:
            block (Block): the block we check for attach points male

        Returns:
            Boolean
        """
        for pointF in self.attachPointsFemale:
            fX = pointF[0]*self.width + self.x
            fY = pointF[1]*self.height + self.y

            for pointM in block.attachPointsMale:
                mX = pointM[0]*block.width + block.x
                mY = pointM[1]*block.height + block.y

                if 0 <= mY-fY < block.height and abs(fX-mX) < block.width/2:
                    return True
        return False

    def attach(self, block):
        """attaches a block under itself

        Args:
            b (Block): the block we attach
        """
        # Note: make it also work for other clip points
        block.setCornerX(self.x)
        block.setCornerY(self.y + self.height)

        if self.attachedBottom and self.attachedBottom.id != block.id:  # change here
            block_under1 = self.attachedBottom
            self.disatach(block_under1)

            self.attachedBottom = block
            block.attachedTop = self

            block_under2 = block.attachedBottom

            # attach the previous block under to block
            block_under1.setCornerX(block.x)
            block_under1.setCornerY(block.y + block.height)

            block.attachedBottom = block_under1
            block_under1.attachedTop = block

            # continue attaching chain
            if block_under2:
                block.attach(block_under2)

        else:
            self.attachedBottom = block
            block.attachedTop = self

    def place_Shadow(self, block):
        """Places a shadow block at the clip position of the block

        Args:
            block (Block): the block the shadow is placed on
        """
        self.shadowBlock = Block(
            self.x, self.y, self.width, self.height, "shadow", self.canvas)
        block.attach(self.shadowBlock)
        self.shadowBlock.visual_Update()

    def disatach(self, b):
        """disatach itself from the block under

        Args:
            b (Block): the block under
        """
        b.attachedTop = None
        self.attachedBottom = None

    def delete_Shadow(self):
        """deletes shadow block, and reattach blocks that
        were separated by the shadow block
        """
        under_Block = self.shadowBlock.attachedBottom
        upper_Block = self.shadowBlock.attachedTop

        # visually delete shadow block
        for objID in self.shadowBlock.canvasObjectsID:
            self.canvas.delete(objID)

        upper_Block.disatach(self.shadowBlock)
        self.shadowBlock = None

        if under_Block:
            upper_Block.attach(under_Block)

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
