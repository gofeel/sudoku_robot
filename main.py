import cv2
import image_processing
import serial
from testing_tool.touch import TouchTestTool
from sudoku import Sudoku

# 시리얼 포트 설정
port = '/dev/ttyUSB0'  # 포트 번호는 사용자의 환경에 맞게 변경
baudrate = 115200
X = 130
width = 70
Y = 33
height = 150


def trans_point_coordinate(point):
    image_width = 1284
    image_height = 2778
    transformed_point = (X + point[0] * width / image_width, Y + height - point[1] * height / image_height)
    return transformed_point


def get_point_for_blank(x, y):
    # return (x * 128 + 92, y * 128 + 560)
    return (y * 140 + 92, x * 140 + 560)


def get_point_for_answer(v):
    return (v * 143 - 40, 2322)


def get_touches(result):
    points = []

    for x in result:
        points.append(trans_point_coordinate(get_point_for_blank(x[0], x[1])))
        points.append(trans_point_coordinate(get_point_for_answer(x[2])))

    return points


if __name__ == "__main__":
    fn = "sudoku.jpg"

    image_processing.capture_image(fn)
    board = image_processing.get_sudoku_from_image(fn)

    puzzle = Sudoku(3, 3, board=board)
    solution = puzzle.solve()
    result = []
    for rn, row in enumerate(puzzle.board):
        for cn, cell in enumerate(row):
            if cell is None:
                result.append([rn, cn, solution.board[rn][cn]])

    points = get_touches(result)

    sp = serial.Serial(port, baudrate, timeout=1, exclusive=False, dsrdtr=True)
    tool = TouchTestTool(sp)
    tool.init()
    for n, p in enumerate(points):
        tool.touch(p)
    tool.finish()
    sp.close()
