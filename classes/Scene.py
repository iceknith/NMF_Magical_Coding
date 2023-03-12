if __name__ == "__main__":
    from CodingBlock import Block
    from Buttons import Button
if __name__ == "classes.Scene":
    from classes.CodingBlock import Block
    from classes.Buttons import Button


def levels():
    return \
        {"test": [Block(900, 350, 200, 50, "fire_ball"),
                  Block(700, 500, 200, 50, "ice_ahnilator"),
                  Block(1000, 70, 200, 50, "checker"),
                  Block(700, 200, 200, 50, "checker"),
                  Button(50, 100, 200, 50, "Change Level",
                         ("level transition", "editor")),
                  Button(50, 250, 200, 50, "Fire Ball",
                         ("block creation", (200, 50, "fire_ball")))
                  ],

         "editor": [Block(200, 490, 200, 50, "fire_ball"),
                    Block(300, 48, 200, 50, "fire_ball"),
                    Block(400, 500, 200, 50, "checker"),
                    Block(500, 200, 200, 50, "checker"),
                    Block(700, 500, 200, 50, "ice_ahnilator"),
                    Block(150, 126, 200, 50, "ice_ahnilator"),
                    Block(400, 1000, 200, 50, "ice_ahnilator"),
                    Block(1200, 70, 200, 50, "sledkhjgb"),
                    Block(300, 489, 200, 50, "sledkhjgb"),
                    Block(700, 73, 200, 50, "sledkhjgb")]}


class Scene:
    """Stores, indexes and load every displayed object
    """

    def __init__(self, levelName: str) -> None:
        # variables definition
        self.displayedObjects = []

        self.displayedBlocks = []
        self.focusedBlock = None

        self.displayedButtons = []

        # define levels
        self.levels = levels()

        # load level
        self.loadLevel(levelName)

    def loadLevel(self, levelName: str) -> None:
        """Loads a level

        Args:
            levelName (str): the level name
        """
        if self.levels.get(levelName):
            # reset variables
            self.displayedBlocks = []
            self.displayedButtons = []
            self.focusedBlock = None

            # update variables to new level
            self.displayedObjects = self.levels[levelName]

            for obj in self.displayedObjects:

                if type(obj) == Block:
                    self.displayedBlocks.append(obj)

                elif type(obj) == Button:
                    self.displayedButtons.append(obj)

    def add_Object(self, obj) -> None:
        """adds an object to the current scene

        Args:
            obj (Button/Block): the object to add
        """
        self.displayedObjects.append(obj)

        if type(obj) == Block:
            self.displayedBlocks.append(obj)
        elif type(obj) == Button:
            self.displayedButtons.append(obj)

    def delete_Object(self, obj) -> None:
        """deletes an object from the current scene

        Args:
            obj (Button/Block): the object to delete
        """
        self.displayedObjects.remove(obj)

        if type(obj) == Block:
            self.displayedBlocks.remove(obj)

            if self.focusedBlock == obj:
                self.focusedBlock = None

        elif type(obj) == Button:
            self.displayedButtons.remove(obj)
