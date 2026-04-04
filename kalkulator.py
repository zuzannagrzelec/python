def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def podziel(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b


def main():
    print("Kalkulator — wybierz działanie:")
    print("  1 — dodawanie")
    print("  2 — odejmowanie")
    print("  3 — mnożenie")
    print("  4 — dzielenie")
    wybor = input("Numer (1–4): ").strip()

    a = float(input("Pierwsza liczba: "))
    b = float(input("Druga liczba: "))

    if wybor == "1":
        wynik = dodaj(a, b)
        print(f"Wynik: {a} + {b} = {wynik}")
    elif wybor == "2":
        wynik = odejmij(a, b)
        print(f"Wynik: {a} - {b} = {wynik}")
    elif wybor == "3":
        wynik = pomnoz(a, b)
        print(f"Wynik: {a} * {b} = {wynik}")
    elif wybor == "4":
        try:
            wynik = podziel(a, b)
            print(f"Wynik: {a} / {b} = {wynik}")
        except ValueError as e:
            print(e)
    else:
        print("Nieprawidłowy wybór.")


if __name__ == "__main__":
    main()
