if __name__ == "__main__":
    from CodingBlock import Block
    from Buttons import Button
if __name__ == "classes.Scene":
    from classes.CodingBlock import Block
    from classes.Buttons import Button


def levels(canvas):
    return \
        {"test": [Block(900, 350, 200, 50, "fire_ball", canvas),
                  Block(700, 500, 200, 50, "ice_ahnilator", canvas),
                  Block(1000, 70, 200, 50, "checker", canvas),
                  Block(700, 200, 200, 50, "checker", canvas),
                  Button(50, 100, 200, 50, "Change Level",
                         ("level transition", "editor"), canvas),
                  Button(50, 250, 200, 50, "Fire Ball",
                         ("block creation", (200, 50, "fire_ball")), canvas)
                  ],

         "editor": [Block(200, 490, 200, 50, "fire_ball", canvas),
                    Block(300, 48, 200, 50, "fire_ball", canvas),
                    Block(400, 500, 200, 50, "checker", canvas),
                    Block(500, 200, 200, 50, "checker", canvas),
                    Block(700, 500, 200, 50, "ice_ahnilator", canvas),
                    Block(150, 126, 200, 50, "ice_ahnilator", canvas),
                    Block(400, 1000, 200, 50, "ice_ahnilator", canvas),
                    Block(1200, 70, 200, 50, "sledkhjgb", canvas),
                    Block(300, 489, 200, 50, "sledkhjgb", canvas),
                    Block(700, 73, 200, 50, "sledkhjgb", canvas)]}


class Scene:
    """Stores, indexes and load every displayed object
    """

    def __init__(self, levelName: str, canvas) -> None:
        # variables definition
        self.displayedBlocks = []
        self.focusedBlock = None

        self.displayedButtons = []

        # define levels
        self.levels = levels(canvas)

        # load level
        self.loadLevel(levelName, canvas)

    def loadLevel(self, levelName: str, canvas) -> None:
        """Loads a level

        Args:
            levelName (str): the level name
        """
        if self.levels.get(levelName):

            # reset variables
            self.displayedBlocks = []
            self.displayedButtons = []
            self.focusedBlock = None

            # clear displayed objects
            canvas.delete("all")

            for obj in self.levels[levelName]:
                # put object in the according category
                if type(obj) == Block:
                    self.displayedBlocks.append(obj)

                elif type(obj) == Button:
                    self.displayedButtons.append(obj)

                # display object
                obj.visual_Update()

    def add_Object(self, obj) -> None:
        """adds an object to the current scene

        Args:
            obj (Button/Block): the object to add
        """
        # put object in the according category
        if type(obj) == Block:
            self.displayedBlocks.append(obj)
        elif type(obj) == Button:
            self.displayedButtons.append(obj)

        # display Object
        obj.visual_Update()

    def delete_Object(self, obj) -> None:
        """deletes an object from the current scene

        Args:
            obj (Button/Block): the object to delete
        """
        if type(obj) == Block:
            self.displayedBlocks.remove(obj)

            if self.focusedBlock == obj:
                self.focusedBlock = None

        elif type(obj) == Button:
            self.displayedButtons.remove(obj)

        # stop delete it visually
        obj.delete_Visually()
