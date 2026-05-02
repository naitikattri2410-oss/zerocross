def print_board(tic):
    print("Current Board:")
    for row in tic:
        print(" ".join(row))
    print()


def check_winner(tic):
    return (
        (tic[0][0] == tic[1][1] == tic[2][2] != '_') or
        (tic[0][0] == tic[0][1] == tic[0][2] != '_') or
        (tic[1][0] == tic[1][1] == tic[1][2] != '_') or
        (tic[2][0] == tic[2][1] == tic[2][2] != '_') or
        (tic[0][0] == tic[1][0] == tic[2][0] != '_') or
        (tic[0][1] == tic[1][1] == tic[2][1] != '_') or
        (tic[0][2] == tic[1][2] == tic[2][2] != '_') or
        (tic[0][2] == tic[1][1] == tic[2][0] != '_')
    )


def is_draw(tic):
    for row in tic:
        if '_' in row:
            return False
    return True


def main():
    tic = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print("game will start with X")
    c = 'X'

    while True:
        try:
            a = int(input("row: "))
            b = int(input("column: "))
        except ValueError:
            print("invalid input. try again.")
            continue

        # check weather thi input is valid
        if a > 3 or a < 1 or b > 3 or b < 1:
            print("invalid place.\n")
            continue

        if tic[a - 1][b - 1] != '_':
            print("not available..try again\n")
            continue

        tic[a - 1][b - 1] = c
        print_board(tic)

        # for winner 
        if check_winner(tic):
            print(f"{c} is winner")
            break

        # used to check if the game is draw
        if is_draw(tic):
            print("match is draw")
            break

        c = 'O' if c == 'X' else 'X'
main()
