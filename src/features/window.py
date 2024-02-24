import tkinter as tk


def CenterOnScreen(root, root_width, root_height):
    """set window open center screen
    root = name_root_window
        root_width = width of root
        root_height = height of root

        ex:
        import  tkinter as tk
        name_root = tk.Tk()
        window.CenterOnScreen(
            root = name_root,
            root_widht= 1000,
            root_height=600
            )
    """
    # self.x = root_width
    # self.y = root_height
    # self.root = root

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width / 2 - root_width / 2)
    center_y = int(screen_height / 2 - root_height / 2)

    root.geometry(f"{root_width}x{root_height}+{center_x}+{center_y}")


def iconChange(root, link_folder_icon):
    """change icon window of app
    root = name_root of window

    ex:
        import tkinter as tk
        name_root = tk.TK()

        window.iconChange(
            root=name_root,
            link_folder_icon = "dowload/data/icon.ico"
        )

    """
    root.iconbitmap(f"{link_folder_icon}")
