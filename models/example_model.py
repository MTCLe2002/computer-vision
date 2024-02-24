import sys

sys.path.append("src/features")
# sys.path.append("src/data")
# sys.path.append("src/models")
# sys.path.append("src/visualization")

import window_features
import tkinter as tk

root = tk.Tk()
window_features.CenterOnScreen(root=root, root_width=1000, root_height=600)

window_features.iconChange(
    root=root,
    link_folder_icon="C:/Users/mtcle/OneDrive/WorkSpace/computer-vision/data/external/image/icon.ico",
)

root.mainloop()
