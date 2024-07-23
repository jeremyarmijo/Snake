from scoreboard.set_scoreboard import set_score_board
from src.ascii_art import print_ascii_art

def check_flags(argv, info_flags):
    for i in range(0, len(argv)):
        if argv[i] == "-h":
            with open('extra/help.txt', "r") as f:
                print(f.read())
            info_flags[2] = False
        if argv[i] == "-s":
            print_ascii_art("Scores :", "slant")
            info_flags[2] = False
            set_score_board("scoreboard/scoreboard.csv")
        if argv[i] == "-rs":
            print_ascii_art("Scoreboard deleted.", "slant")
            info_flags[2] = False
            open('scoreboard/scoreboard.csv', 'w').close()
            with open('scoreboard/scoreboard.csv', "w") as f:
                f.write("Level,Name,Score\n")
        if argv[i] == "-l" and (i + 1) <= len(argv):
            try:
                level = int(argv[i + 1])
                info_flags[0] += level
                info_flags[2] = True
            except ValueError:
                print("Please enter an int")
                exit(1)
        if argv[i] == "-n" and (i + 1) <= len(argv):
            try:
                name = str(argv[i + 1])
                info_flags[1] = name
                info_flags[2] = True
            except ValueError:
                print("Please enter an int")
                exit(1)
    return info_flags