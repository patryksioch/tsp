from math import sqrt
lines = open("berlin52.txt","r").readlines()[1:]
for i in range(len(lines)):
    lines[i]=lines[i].rstrip().split()
def greedytrasa(lines):
    startx = int(lines[0][1])
    starty = int(lines[0][2])
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
        if len(lines) == 1:
            ostatnie = lines[0]
            x = int(ostatnie[1])
            y = int(ostatnie[2])
    d = sqrt((x - startx) ** 2 + (y - starty) ** 2)
    dlugosc +=d
    return round(dlugosc, 2) , tab

print(greedytrasa(lines))
