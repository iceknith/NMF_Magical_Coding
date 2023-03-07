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
    for b in blocks:
        if b.message == "Unknown":
            print(b.attachedBottom, b.attachedTop)
        if b.isFocused:
            b.moove(mouseX, mouseY, blocks)


def repaint():
    # reset
    canvas.delete("all")

    # draw everything
    for b in blocks:
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


def mouseMovement(event):
    global mouseX, mouseY
    mouseX, mouseY = event.x, event.y


def mouseLeftClick(event):
    for b in blocks:
        if b.contains(mouseX, mouseY):
            b.isFocused = True
            return


def mouseLeftRelease(event):
    for b in blocks:
        if b.isFocused:
            b.isFocused = False


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
    root.bind("<Motion>", mouseMovement)
    root.bind("<ButtonPress-1>", mouseLeftClick)
    root.bind("<ButtonRelease-1>", mouseLeftRelease)

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

    # initialise block list
    """blocks = [cb.Block(200, 490, 200, 50, "fire_ball"),
              cb.Block(300, 48, 200, 50, "fire_ball"),
              cb.Block(400, 500, 200, 50, "checker"),
              cb.Block(500, 200, 200, 50, "checker"),
              cb.Block(700, 500, 200, 50, "ice_ahnilator"),
              cb.Block(150, 126, 200, 50, "ice_ahnilator"),
              cb.Block(400, 1000, 200, 50, "ice_ahnilator"),
              cb.Block(1200, 70, 200, 50, "sledkhjgb"),
              cb.Block(300, 489, 200, 50, "sledkhjgb"),
              cb.Block(700, 73, 200, 50, "sledkhjgb")]"""

    blocks = [
        cb.Block(200, 490, 200, 50, "fire_ball"),
        cb.Block(700, 500, 200, 50, "ice_ahnilator"),
        cb.Block(1200, 70, 200, 50, "sledkhjgb"),
        cb.Block(500, 200, 200, 50, "checker"),
    ]

    # game loop call
    gameLoop()
    print("lucas est ici")