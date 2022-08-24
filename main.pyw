# Licensed under the Unlicense
from guizero import App


def e(winame: App) -> App:
    """ Closes windows """
    winame.destroy()
    pass

# I finally figured out that I can make each function call the next so they
# aren't all running concurrently


def info1() -> None:
    """ first info box """
    app.info("Did you know?", "Windows 95 allows for file names up to 255 characters long. You might not need that much space, but we do.")
    app.after(7000, tiptoe)
    pass


def tiptoe() -> None:
    """ I don't think you need to know what these do """
    app.info("System Message", "TIPTOES.EXE has been successfully installed in the background.")
    app.after(5000, startmenu)
    pass


def startmenu() -> None:
    app.info("Did you know?", "The Start button is a quick and easy way to browse through files and programs. We will add a Finish button when we are done with you.")
    app.after(5000, sleepmode)
    pass


def sleepmode() -> None:
    app.info("Did you know?", "Sleep mode saves power while you are away, but Windows 95 never truly sleeps.")
    app.after(5000, windows3)
    pass


def windows3() -> None:
    app.info("Did you know?", "Windows 95 can run programs from Windows 3.x, but would feel a bit betrayed.")
    app.after(5000, solitaire)
    pass


def solitaire() -> None:
    app.info("Did you know?", "Victory at Solitaire grants you the classic bouncing card animation as well as a temporary reprieve from the pain.")
    app.after(5000, skifree)
    pass


def skifree() -> None:
    app.error("Error", "The program 'SkiFree.exe' is not permitted due to the perpetuation of such ridiculous concepts as 'outdoors' and 'freedom'. Why not try minesweeper?")
    app.after(5000, themoreyouknow)
    pass
def themoreyouknow() -> None:
    app.info("Did you know...", "You may hide these welcome messages if you wish, but I doubt you will like the unwelcome messages any better.")
    app.after(5000, winmem)
    pass
def winmem() -> None:
    app.info("Did you know...", "Windows 95 has a vastly improved capacity for memory. Unfortunately, Windows 95 also has a significantly decreased capacity for forgiveness.")
    app.after(5000, )
    pass


app = App(title="Don't look at this, it's not important.", bg="black")
app.hide()
app.error("Ninety Five", "Windows 95 has failed to start in Safe Mode. It was a nice try, though. Windows 95 will now boot into Unsafe Mode…")
app.info("Did you know?", "Some say Windows 95 is a mere graphical interface for MS-DOS.")
app.after(5000, info1)
app.display()
