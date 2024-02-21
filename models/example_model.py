# models/example_model.py

import sys
import os

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "C:/Users/mtcle/OneDrive/WorkSpace/computer-vision/src",
        "src",
    )
)

from src.example import hello


def use_example():
    result = hello()
    return result
