def przelicz(kwota, kurs):
    return kwota * kurs

def main():
    print("Przelicznik walut - PLN na wybrane waluty")

    while True:
        print("\nPodaj kwotę w PLN lub wpisz 'q' aby zakończyć:")
        wejscie = input("PLN: ")

        if wejscie.lower() == 'q':
            print("Zakończono działanie programu.")
            break

        try:
            pln = float(wejscie)
        except ValueError:
            print("Błąd: podano nieprawidłową wartość.")
            continue

        print("Podaj aktualny kurs EUR:")
        try:
            kurs_eur = float(input("Kurs EUR: "))
        except ValueError:
            print("Błąd: nieprawidłowy kurs EUR.")
            continue

        print("Podaj aktualny kurs USD:")
        try:
            kurs_usd = float(input("Kurs USD: "))
        except ValueError:
            print("Błąd: nieprawidłowy kurs USD.")
            continue

        print("Podaj aktualny kurs GBP:")
        try:
            kurs_gbp = float(input("Kurs GBP: "))
        except ValueError:
            print("Błąd: nieprawidłowy kurs GBP.")
            continue

        print(f"\n{pln} PLN to:")
        print(f"- {przelicz(pln, kurs_eur):.2f} EUR")
        print(f"- {przelicz(pln, kurs_usd):.2f} USD")
        print(f"- {przelicz(pln, kurs_gbp):.2f} GBP")

if __name__ == "__main__":
    main()
