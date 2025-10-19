from generator import opeen, generuj_dane
from greedy import  greedytrasa
def main():
    nazwa_pliku_danych = "dane.txt"
    liczba_punktow = 29
    generuj_dane(nazwa_pliku_danych, liczba_punktow)
    dane_punktow = opeen(nazwa_pliku_danych)
    obliczona_trasa, dlugosc_trasy = greedytrasa(dane_punktow)
    print(f"Obliczona trasa: {' -> '.join(map(str, obliczona_trasa))}")
    print(f"Całkowita długość trasy: {dlugosc_trasy:.2f}")

if __name__ == "__main__":
    main()