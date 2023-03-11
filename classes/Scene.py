if __name__ == "__main__":
    from CodingBlock import Block
elif __name__[:8] == "classes.":
    from classes.CodingBlock import Block

levels = {"test": [Block(200, 490, 200, 50, "fire_ball"),
                   Block(700, 500, 200, 50, "ice_ahnilator"),
                   Block(1200, 70, 200, 50, "sledkhjgb"),
                   Block(500, 200, 200, 50, "checker")],

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

        self.loadLevel(levelName)

    def loadLevel(self, levelName: str) -> None:
        """Loads a level

        Args:
            levelName (str): the level name
        """
        if levels.get(levelName):
            # reset variables
            self.displayedBlocks = []
            self.focusedBlock = None

            # update variables to new level
            self.displayedObjects = levels[levelName]
            for obj in self.displayedObjects:

                if type(obj) == Block:
                    self.displayedBlocks.append(obj)
