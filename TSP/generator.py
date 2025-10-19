import random

def generuj_dane(nazwa_pliku, ile_punktow):
    min_x = 40
    max_x = 2000
    min_y = 500
    max_y = 2500
    with open(nazwa_pliku, "w") as plik:
        plik.write(f"{ile_punktow}\n")
        for i in range(1, ile_punktow + 1):
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)
            linia_do_zapisu = f"{i} {x} {y}"
            plik.write(f"{linia_do_zapisu}\n")


def opeen(nazwa_pliku):
    with open(nazwa_pliku, 'r') as f:
        lines = f.readlines()
    dane = [line.strip().split() for line in lines[1:]]
    return dane

