from guizero import App, TextBox, PushButton, Window


def e(winame: App) -> App:
    """ Closes windows """
    winame.destroy()


pass
app = App(title="Don't look at this, it's not important")
app.hide()
app.error("ERROR", "Windows 95 has failed to start in Safe Mode. It was a nice try, though. Windows 95 will now boot into Unsafe Mode… ")


app.display()
