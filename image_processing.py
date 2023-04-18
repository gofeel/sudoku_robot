import cv2
import numpy as np

def solve(filename):
    board = get_sudoku_from_image(filename)
    return solve_sudoku(board)


def capture_image(filename, device=1):
    vid = cv2.VideoCapture(device)

    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    for _ in range(50):
        ret, frame = vid.read()
    cv2.imwrite(filename=filename, img=frame)
    vid.release()


def get_sudoku_from_image(filename):
    rrr = [[0] * 9 for _ in range(9)]
    model = cv2.ml.KNearest_load('KNN_Trained_Model.xml')

    img = cv2.imread(filename)
    im = img[210:690, 720:1200]
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt)>50:
            [x,y,w,h] = cv2.boundingRect(cnt)
            if h > 28 and h < 48:
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(10,10))
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
                xxx = round((x - 26)/53.0)
                yyy = round((y - 19)/53.0)
                rrr[yyy][xxx] = int((results[0][0]))
    return rrr


def solve_sudoku(board):
    puzzle = Sudoku(3, 3, board=board)
    solution = puzzle.solve()
    result = []
    for rn, row in enumerate(puzzle.board):
        for cn, cell in enumerate(row):
            if cell is None:
                result.append([rn, cn, solution.board[rn][cn]])
    return result
