from tkinter import *
from tkinter import messagebox
from time import time
import classes.CodingBlock as cb


def gameLoop():
    """Runs a loop responsible of a stable fps count, and that handles task distribution
    input : None
    returns : None
    """
    # game loop private definitions
    waitingTime = 1/fps
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

            if fpsTimer >= 1:
                currentFPS = dynamicFPS
                dynamicFPS = 0
                fpsTimer = 0

                if currentFPS <= fps/2:
                    print("ALERT !!! fps too low")

            # update game
            update()

            # repaint
            repaint()


def update():
    b.setX(mouseX)
    b.setY(mouseY)


def repaint():
    # reset
    canvas.delete("all")

    # draw everything
    b.display(canvas)  # temporary
    canvas.create_text(
        50, 10, text=f"fps : {currentFPS} / {fps}", font=("Arial", 10, "bold"))
    root.update()


def closeWindow():
    if messagebox.askokcancel("Quit", "Do you want to quit ?"):
        # stop game loop
        global doGameContinue
        doGameContinue = False

        # destroy root
        root.destroy()


def mouseMovement(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y


if (__name__ == "__main__"):

    # window definition
    root = Tk()
    root.title("Magical System Programming")

    # adjust window size to screen size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")

    # root bindings
    root.protocol("WM_DELETE_WINDOW", closeWindow)
    root.bind("<Motion>", mouseMovement)

    # frame + canvas definition
    frame = Frame(root)
    canvas = Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    # game loop global definitions
    doGameContinue = True
    fps = 60
    currentFPS = 0

    # mouse definitions
    mouseX, mouseY = 0, 0

    # temporary
    b = cb.Block(screen_width/2, screen_height/2, 100, 100)

    # game loop call
    gameLoop()
