import TKinterModernThemes as TKMT
import tkinter as tk

import TKinterModernThemes.examples.allwidgets as demo1
import TKinterModernThemes.examples.switch as demo2
import TKinterModernThemes.examples.togglebutton as demo3
import TKinterModernThemes.examples.accentbutton as demo4

demos = [demo1, demo2, demo3, demo4]
names = ["All Widgets Demo", "Slide Switch Demo", "Toggle Button Demo", "Accent Button Demo"]

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        super().__init__("Example TKMT Launcher")

        #vars
        self.themeoptions = ['Pick a Theme', "Park", "Azure", "Sun-Valley"]
        self.modeoptions = ['Pick a Mode', "Light", "Dark"]
        self.themeoptionvar = tk.StringVar()
        self.modeoptionvar = tk.StringVar()

        self.usecommandargs = tk.BooleanVar(value=True)
        self.usethemeconfigfile = tk.BooleanVar(value=True)

        self.buttonframe = self.addLabelFrame("Examples")
        for i in range(0, len(demos)):
            self.buttonframe.Button(text=names[i], command=self.runDemo, args=(demos[i],))

        self.menuframe = self.addLabelFrame("Config", col=1)
        self.menuframe.OptionMenu(self.themeoptions, self.themeoptionvar, command=self.flipSwitches)
        self.menuframe.OptionMenu(self.modeoptions, self.modeoptionvar, command=self.flipSwitches)
        self.menuframe.SlideSwitch("Use Command Parameters", self.usecommandargs, row=2)
        self.menuframe.SlideSwitch("Use Theme Config File", self.usethemeconfigfile)
        self.run()

    def runDemo(self, demo):
        theme = self.themeoptionvar.get()
        if theme == self.themeoptions[0]:
           theme = ""
        mode = self.modeoptionvar.get()
        if mode == self.modeoptions[0]:
           mode = ""
        demo.App(theme, mode, self.usecommandargs.get(), self.usethemeconfigfile.get(), topLevel=True)


    def flipSwitches(self, _):
        self.usecommandargs.set(False)
        self.usethemeconfigfile.set(False)

def run():
    App()

if __name__ == "__main__":
    run()