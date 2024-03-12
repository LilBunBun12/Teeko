import turtle
import re


def rules():
    """Displays the rules of the Teeko game"""
    print('The Teeko board consists of twenty-five spaces arranged in a five-by-five grid. There are eight markers in a Teeko game, four black and four red. One player,\n"Black" plays the black markers, and the other, "Red", plays the red. Black moves first and places one marker on any space on the board.\nRed then places a marker on any unoccupied space; black does the same; and so on until all eight markers are on the board.\nThe object of the game is for either player to win by having all four of their markers in a straight line (vertical, horizontal, or diagonal)\nor on a square of four adjacent spaces. (Adjacency is horizontal, vertical, or diagonal, but does not wrap around the edges of the board.)\nIf neither player has won after the "drop" (when all eight pieces are on the board), then they move their pieces one at a time, with Black playing first.\nA piece may be moved only to an adjacent space.')


def score(player1Score, player2Score):
    """Displays the score of the two players"""
    print(f"Score:\nPlayer1: {player1Score}\nPlayer2: {player2Score}")


def displayInstructionBoard():
    """Displays the empty ascii board"""
    print("  1 2 3 4 5")
    for i in range(5):
        print(" " + " -" * 5)
        print(str(i + 1) + "| " * 6)
    print(" " + " -" * 5)


def instructions():
    """Displays the instructions"""
    print("This is how the cordnite system works for this game:")
    displayInstructionBoard()
    print("When you are inputing a cordinate it should be a number 1 through 5(thr row) followed by a space then followed by a number 1 through 5(the column)")
    print("Example of a correct input: 1 4")
    print("When all the pieces are down and you are moving your pieces, this is how it's going to work\nIt's going to first as the position of the piece you want to move\nThen what direction you want to move. Here is an example:")
    print("What piece would you want to move? Input: 3 2")
    print("What direction would you like to move it in?\n- Up\n- Up Right\n- Right\n- Down Right\n- Down\n- Down Left\n- Left\n- Up Left\nInput: Down Left")


def tryAgain(isTrue):
    """If it's a valid input, you do not try again. If it is an invalid input, you do try again"""
    if (isTrue):
        print("Invalid input >:( Try again")
        return True
    else:
        return False


def drawW(t):
    t.down()
    t.right(155)
    t.forward(100)
    t.left(130)
    t.forward(100)
    t.right(130)
    t.forward(100)
    t.left(130)
    t.forward(100)
    t.right(65)
    t.up()
    t.forward(30)
    t.right(90)


def drawI(t):
    t.down()
    t.forward(10)
    t.up()
    t.forward(20)
    t.down()
    t.forward(60)
    t.right(180)
    t.up()
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.left(90)


def drawN(t):
    t.down()
    t.right(180)
    t.forward(90)
    t.right(180)
    t.forward(100)
    t.right(155)
    t.forward(110)
    t.left(155)
    t.forward(100)
    t.up()


def winner(color):
    t = turtle.Turtle()
    t.color(color)
    t.up()
    t.right(180)
    t.forward(100)
    t.right(180)
    t.left(90)
    drawW(t)
    drawI(t)
    drawN(t)
    for i in range(2):
        t.circle(175)


def createEmptyBoard():
    mat = []
    for i in range(5):
        mat.append([])
        for j in range(5):
            mat[-1].append(" ")
    return mat


def printBoard(mat):
    print("  1 2 3 4 5")
    for i in range(5):
        print(" " + " -" * 5)
        print(str(i + 1), end="")
        for j in range(5):
            print("|" + mat[i][j], end="")
        print("|")
    print(" " + " -" * 5)


def isValidInput(string):
    return bool(re.match("[1-5] [1-5]", string))


def isPositionTaken(i, j, mat):
    return mat[i][j] != " "


def check(mat, r, c, mr, mc, letter):
    if (letter == " "):
        return False
    try:
        for i in range(4):
            if (mat[r][c] != letter):
                return False
            r += mr
            c += mc
        return True
    except:
        return False


def anyWin(mat):
    movement = [[1, 0], [0, 1], [1, 1], [-1, 1]]
    for i in range(5):
        for j in range(5):
            for k in range(4):
                if (check(mat, i, j, movement[k][0], movement[k][1], mat[i][j])):
                    if (mat[i][j] == "R"):
                        winner("red")
                    else:
                        winner("black")
                    return [True, i, j]

    return [False]


def openingstage(mat):
    players = "Player1(Black) Player2(Red)".split(" ")
    piece = ["B", "R"]
    for i in range(8):
        answer = input(
            f"{players[i % 2]} place a piece on the board. Input: ").strip()
        a = isValidInput(answer)
        if (a):
            b = isPositionTaken(int(answer[0]) - 1, int(answer[2]) - 1, mat)
        else:
            b = True
        while (tryAgain(not (a) or b)):
            answer = input("Your input: ").strip()
            a = isValidInput(answer)
            if (a):
                b = isPositionTaken(
                    int(answer[0]) - 1, int(answer[2]) - 1, mat)
            else:
                b = True
        r = int(answer[0]) - 1
        c = int(answer[2]) - 1
        mat[r][c] = piece[i % 2]
        printBoard(mat)
        ar = anyWin(mat)
        if (ar[0]):
            return True
    return False


def finalstage(mat):
    players = "Player1(Black) Player2(Red)".split(" ")
    piece = ["B", "R"]
    cnt = 0
    while (True):
        answer = input(
            f"{players[cnt % 2]} choose a piece on the board. Input: ").strip()
        curPiece = piece[cnt]
        a = isValidInput(answer)
        if (a):
            b = mat[int(answer[0]) - 1][int(answer[2]) - 1] == curPiece
        else:
            b = True
        while (tryAgain(not (a) or not (b))):
            answer = input("Your input: ").strip()
            a = isValidInput(answer)
            if (a):
                b = mat[int(answer[0]) - 1][int(answer[2]) - 1] == curPiece
            else:
                b = True
        direction = input(
            "What direction would you like to move it in?\n- Up\n- Up Right\n- Right\n- Down Right\n- Down\n- Down Left\n- Left\n- Up Left\nInput: ")
        momentum = [[-1, 0], [-1, 1], [0, 1], [1, 1],
                    [1, 0], [1, -1], [0, -1], [-1, -1]]
        index = "up,up right,right,down right,down,down left,left,up left".split(
            ",").index(direction.lower())
        a = 0 <= index
        if (a):
            b = mat[int(answer[0]) - 1 + momentum[index][0]
                    ][int(answer[2]) - 1 + momentum[index][1]] == " "
        else:
            b = True
        while (tryAgain(not (a) or not (b))):
            direction = input("Your input: ").strip()
            index = "up,up right,right,down right,down,down left,left,up left".split(
                ",").index(direction.lower())
            a = 0 <= index
            if (a):
                b = mat[int(answer[0]) - 1 + momentum[index][0]
                        ][int(answer[2]) - 1 + momentum[index][1]] == " "
            else:
                b = True
        mat[int(answer[0]) - 1 + momentum[index][0]
            ][int(answer[2]) - 1 + momentum[index][1]] = curPiece
        mat[int(answer[0]) - 1][int(answer[2]) - 1] = " "
        cnt = (cnt + 1) % 2
        if (anyWin(mat)[0]):
            print(anyWin(mat)[0])
            break
        printBoard(mat)


player1Score = 0
player2Score = 0
while (True):
    while (True):
        answer = input(
            f"Welcome to our Teeko game, Please enter one of the actions\n- Instructions\n- Rules\n- Start Game\nYour input: ").strip()
        a = answer.lower() == "instructions"
        b = answer.lower() == "rules"
        c = answer.lower() == "start game"
        while (tryAgain(not (a or b or c))):
            answer = input("Your input: ").strip()
            a = answer.lower() == "instructions"
            b = answer.lower() == "rules"
            c = answer.lower() == "start game"
        if (a):
            instructions()
        elif (b):
            rules()
        else:
            print("Game starting now!")
            break
        print()
    mat = createEmptyBoard()
    printBoard(mat)
    if (openingstage(mat)):
        break
    finalstage(mat)
    answer = input("Would you like to play again? Yes or no?").strip()
    a = answer.lower() == "yes"
    b = answer.lower() == "no"
    while (tryAgain(not (a or b))):
        answer = input("Your input: ").strip()
        a = answer.lower() == "yes"
        b = answer.lower() == "no"
    if (a):
        continue
    break
