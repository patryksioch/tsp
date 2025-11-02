from generator import opeen, generuj_dane
from greedy import  greedytrasa
def main():
    print("MENU GŁÓWNE")
    print("1. Wygeneruj plik tekstowy ")
    print("2. Wczytaj plik tekstowy")
    wybor = input("Wybierz opcje 1 lub 2 ")
    if wybor == "1":
        nazwa_pliku_danych = input("Podaj nazwe pliku np dane.txt : ")
        # nazwa_pliku_danych = "dane.txt"
        # liczba_punktow = 29
        liczba_punktow = int(input("Podaj liczbe punktów"))
        generuj_dane(nazwa_pliku_danych, liczba_punktow)
        dane_punktow = opeen(nazwa_pliku_danych)
        dlugosc_trasy, obliczona_trasa = greedytrasa(dane_punktow)
        print(f"Obliczona trasa: {' -> '.join(map(str, obliczona_trasa))}")
        print(f"Całkowita długość trasy: {dlugosc_trasy:.2f}")
    elif wybor =="2":
        nazwa_pliku_danych = input("Podaj nazwe pliku np dane.txt :")
        #nazwa_pliku_danych = "tsp250.txt"
        dane_punktow = opeen(nazwa_pliku_danych)
        dlugosc_trasy, obliczona_trasa = greedytrasa(dane_punktow)
        print(f"Obliczona trasa: {' -> '.join(map(str, obliczona_trasa))}")
        print(f"Całkowita długość trasy: {dlugosc_trasy:.2f}")
    else:
        print("Błąd cwelu wybierz 1 lub 2")
if __name__ == "__main__":
    main()