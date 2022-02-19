import os
from Canvas import Canvas


def clearBMPs():
    for file in os.listdir():
        if file.endswith(".bmp"):
            os.remove(file)
            print(f"File {file} removed!")


if __name__ == "__main__":
    line = [(3, 2), (4, 2), (5, 3), (6, 3), (7, 4), (8, 4)]
    clearBMPs()
    c = Canvas()
    c.showImageWithPaint()
    print("All done!")