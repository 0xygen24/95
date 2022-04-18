from guizero import App


# Licensed under the Unlicense
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

app = App(title="Don't look at this, it's not important.", bg="black")
app.hide()
app.error("ERROR", "Windows 95 has failed to start in Safe Mode. It was a nice try, though. Windows 95 will now boot into Unsafe Mode…")
app.info("Did you know?", "Some say Windows 95 is a mere graphical interface for MS-DOS.")
app.after(5000, info1)
app.display()
