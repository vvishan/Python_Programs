def correlation(series1, series2):
    def direction(a, b):
        if b > a: return 1
        if b < a: return -1
        return 0

    dirs1 = [direction(series1[i], series1[i+1]) for i in range(len(series1)-1)]
    dirs2 = [direction(series2[i], series2[i+1]) for i in range(len(series2)-1)]

    if all(d1 == 0 and d2 == 0 for d1, d2 in zip(dirs1, dirs2)):
        return "both"
    elif all(d1 == d2 for d1, d2 in zip(dirs1, dirs2)):
        return "together"
    elif all(d1 == -d2 for d1, d2 in zip(dirs1, dirs2)):
        return "opposite"
    else:
        return "neither"