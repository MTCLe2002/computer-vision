import tkinter

root = tkinter.Tk()
root.title("Computer Vison")

root_width = 1000
root_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - root_width / 2)
center_y = int(screen_height / 2 - root_height / 2)

# set window at center on the screen
root.geometry(f"{root_width}x{root_height}+{center_x}+{center_y}")

# don't allow window resizing
root.resizable(False, False)

# change icon window
root.iconbitmap(
    "C:/Users/mtcle/OneDrive/WorkSpace/computer-vision/data/external/image/icon.ico"
)

hello = tkinter.Label(root, text="Hello Word")
hello.pack()
root.mainloop()
