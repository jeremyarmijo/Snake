import tabulate

def file_body(file):
    copy = list(file.copy())
    copy.remove(copy[0])
    for i in range(0, len(copy)):
        copy[i] = copy[i].split(",")
    return copy

def set_score_board(path):
    file = []
    with open(path, "r") as file_content:
        for line in file_content:
            file.append(line.replace("\n", ""))
    if len(file) > 1:
        copy_file = file_body(file)
        print(tabulate.tabulate(copy_file, list(file[0].split(",")), tablefmt="grid"))
    else:
        print("No score registred")