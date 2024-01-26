import tkinter
import unittest

from my_deck_construction_frame.frame.my_deck_construction_frame import MyDeckConstructionFrame


class TestMyDeckConstructionFrame(unittest.TestCase):

    def test_my_deck_construction_frame(self):
        root = tkinter.Tk()
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.deiconify()

        window = MyDeckConstructionFrame(root)
        window.pack(fill=tkinter.BOTH, expand=1)

        toggle_button = tkinter.Button(root, text="Toggle Visibility", command=window.toggle_visibility)
        toggle_button.place(x=800, y=400)

        root.mainloop()


if __name__ == '__main__':
    unittest.main()