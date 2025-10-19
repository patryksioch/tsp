from math import sqrt
def greedytrasa(lines):
    tab=[1]
    dlugosc=0
    mini = float('inf')
    pkt = 0
    w = 0
    opkt = lines.pop(0)
    while len(lines) > 0:
        mini = float('inf')
        for i in range(len(lines)):
            d = sqrt((int(lines[i][1]) - int(opkt[1])) ** 2 + (int(lines[i][2]) - int(opkt[2])) ** 2)
            if d < mini:
                mini = d
                pkt = int(lines[i][0])
                w = i
        tab.append(pkt)
        dlugosc+=mini
        opkt = lines.pop(w)
    return tab , dlugosc
