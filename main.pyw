from guizero import App, Text, PushButton, Window


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
    """ I don't think you need to know what this does """
    app.info("System Message", "TIPTOES.EXE has been successfully installed.")
    pass


app = App(title="Don't look at this, it's not important.")
app.hide()
app.error("ERROR", "Windows 95 has failed to start in Safe Mode. It was a nice try, though. Windows 95 will now boot into Unsafe Mode…")
app.info("Did you know?", "Some say Windows 95 is a mere graphical interface for MS-DOS.")
app.after(5000, info1)
app.display()
