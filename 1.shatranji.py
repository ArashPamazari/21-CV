import cv2
import numpy as np


board_size = 800
square_size = board_size // 8


chessboard = np.ones((board_size, board_size, 3), dtype=np.uint8) * 255


for row in range(8):
    for col in range(8):
        x0 = col * square_size
        y0 = row * square_size
        x1 = x0 + square_size
        y1 = y0 + square_size


        if (row + col) % 2 == 0:
            chessboard[y0:y1, x0:x1] = [255, 255, 255]  # White
        else:
            chessboard[y0:y1, x0:x1] = [0, 0, 0]        # Black


cv2.imwrite("board.png", chessboard)
cv2.imshow("board.png", chessboard)
cv2.waitKey()
