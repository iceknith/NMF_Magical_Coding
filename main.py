from tkinter import *
from tkinter import messagebox
from time import time
import classes.CodingBlock as cb
from classes.Keyboard_Handler import Keyboard
from classes.Mouse_Handler import Mouse
from classes.Scene import Scene


def gameLoop():
    """Runs a loop responsible of a stable fps count, and that handles task distribution
    input : None
    returns : None
    """
    # game loop private definitions
    waitingTime = 1 / fps
    previousTime = time()

    # fps variables definition
    global currentFPS
    dynamicFPS = 0
    fpsTimer = 0

    # game loop
    while doGameContinue:

        actualTime = time()
        deltaTime = actualTime - previousTime

        if deltaTime >= waitingTime:

            previousTime = time()

            # fps handling
            dynamicFPS += 1
            fpsTimer += deltaTime

            if fpsTimer > 1:
                currentFPS = dynamicFPS
                dynamicFPS = 0
                fpsTimer = 0

                if currentFPS <= fps / 2:
                    print("ALERT !!! fps too low")

            # update game
            update()

            # repaint
            repaint()


def update():
    #---block logic---#

    # block focusing logic
    if mouse.isLeftClick and gameScene.focusedBlock == None:

        # pass trough every block to see which one sould be focused
        for b in gameScene.displayedBlocks:
            if b.contains(mouse.x, mouse.y):
                gameScene.focusedBlock = b
                b.isFocused = True

    # if no click
    elif not mouse.isLeftClick and gameScene.focusedBlock:

        # unfocus block
        gameScene.focusedBlock.isFocused = False
        gameScene.focusedBlock = None

    # moves the blocks
    if gameScene.focusedBlock:
        gameScene.focusedBlock.moove(
            mouse.x, mouse.y, gameScene.displayedBlocks)

    #---button logic---#

    # button focussing and pressing logic
    for b in gameScene.displayedButtons:

        if b.contains(mouse.x, mouse.y):
            # focus block
            b.focus_Handler(mouse.isLeftClick)

            # click bock
            if b.isClicked and not mouse.isLeftClick:
                b.click_Handler(gameScene)

        elif b.isFocused:
            # unfocus block
            b.unfocus_Handler()


def repaint():
    # reset
    canvas.delete("all")

    # draw everything
    for b in gameScene.displayedObjects:
        b.display(canvas)

    canvas.create_text(
        50, 10, text=f"fps : {currentFPS} / {fps}", font=("Arial", 10, "bold")
    )
    root.update()


def closeWindow():
    if messagebox.askokcancel("Quit", "Do you want to quit ?"):
        # stop game loop
        global doGameContinue
        doGameContinue = False

        # destroy root
        root.destroy()


if __name__ == "__main__":

    # window definition
    root = Tk()
    root.title("Magical System Programming")

    # adjust window size to screen size
    screen_width = 1250  # root.winfo_screenwidth()
    screen_height = 750  # root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    # root bindings
    root.protocol("WM_DELETE_WINDOW", closeWindow)
    keyboard = Keyboard(root)
    mouse = Mouse(root)

    # frame + canvas definition
    frame = Frame(root)
    canvas = Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    # game loop global definitions
    doGameContinue = True
    fps = 60
    currentFPS = 0

    # initialise scene
    gameScene = Scene("test")

    # game loop call
    gameLoop()
