import tkinter
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


class MainWindow:
    def __init__(self):
        self.view = None
        self.choose = None
        self.image = None

        self.build_widgets()

    def build_widgets(self):
        self.view = tkinter.Canvas(root, width=300, height=300, bg="white")
        self.view.pack()

        choose = tkinter.Button(root, text="Open", command=self.choose_file)
        choose.pack()

    def choose_file(self):
        path = askopenfilename()
        self.image = ImageTk.PhotoImage(Image.open(path))
        self.view.create_image(0, 0, image=self.image, anchor="nw")


root = tkinter.Tk()
window = MainWindow()
root.mainloop()

