
def is_word_square(x: list[str]):
    for i in range(len(x)):
        sol_list = [y[i] for y in x]
        sol = ''.join(sol_list)
        if sol != x[i]:
            return False
    return True


def mount_ball(x: list[str], y: str):
    # print(x, y)
    l = len(x)
    i = 0
    while i < l:
        if x[i][l] != y[i]:
            return False
        i += 1
    return y


def solution(x: list[str]):
    max_length = len(x[0])
    sols = []
    for i, word in enumerate(x):
        sol = [word]

        i = 0
        grow = True
        while True:
            print(x[i])
            if i == -1:
                break

            if len(sol) == max_length:
                sols.append(sol)
                break
            if x[i] not in sol:
                zzz = mount_ball(sol, x[i])
                if zzz is not False:
                    sol.append(zzz)

            if i == len(x) - 1:
                grow = False

            if grow:
                i += 1
            else:
                i -= 1
    return sols


def recur(sol: list[str], x: list[str]):
    print(sol, x)


mem = {}


def rec_solution(sol: list[str], x: list[str]):
    if len(sol) == len(x[0]):
        # print(sol)
        return sol

    possible = []
    for word in x:
        if f"{sol},{word}" in mem and not mem[f"{sol},{word}"]:
            return False
        y = mount_ball(sol, word)
        if y:
            possible.append(y)

    if len(possible) == 0:
        return False

    sols = []
    for word in possible:
        rest = [item for item in x if item != word]
        z = rec_solution([*sol, word], rest)
        if z:
            if type(z[0]) is str:
                sols.append(z)
            else:
                sols.append(z[0])
        else:
            mem[f"{sol},{word}"] = False

    return sols


def main():
    y = ['AREA', 'BALL', 'DEAR',
         'LADY', 'LEAD', 'YARD']
    b = ['BALL', 'AREA', 'DEAR',
         'LADY', 'LEAD', 'YARD']
    x = rec_solution([], y)

    # x = solution(['BALL', 'AREA', 'DEAR', 'LADY', 'LEAD', 'YARD'])
    print("sol: ", x)


if __name__ == "__main__":
    main()
