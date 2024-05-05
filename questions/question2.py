def get_volume(x: list[int]):
    max_vol = min(x[0], x[len(x)-1])
    total_vol = 0

    for i in x[1:len(x)-1]:
        total_vol += max_vol - i

    return total_vol


def find_first_peak(x: list[int]) -> int:
    y = [x[0], 0]
    for i, z in enumerate(x):
        if z > y[0]:
            y[0] = z
            y[1] = i
        if z < y[0]:
            break
    return y[1]


def find_next_peak(st: int, x: list[int]):
    if st == len(x) -1:
        return False
    l = len(x)
    s = [x[st], st]
    y = [x[st+1], st+1, False]

    for i in range(st+1, l):
        if x[i] >= s[0]:
            return i
        else:
            if x[i] >= y[0]:
                y[0] = x[i]
                y[1] = i
                y[2] = True

    if not y[2]:
        return False
    return y[1]


def trap(x: list[int]):
    max_vol = 0
    peak_s = find_first_peak(x)
    peak_e = find_next_peak(peak_s, x)
    
    while peak_e:
        vol = get_volume(x[peak_s : peak_e + 1])
        max_vol += vol
        peak_s = peak_e
        peak_e = find_next_peak(peak_s, x)
        print(peak_e)
    print(max_vol)




def main():
    # trap([1, 3, 2, 4, 5, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2])
    # trap([4,2,0,3,2,5])
    trap([0,1,0,2,1,0,1,3,2,1,2,1])


if __name__ == "__main__":
    main()
