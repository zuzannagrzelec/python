# # def mnozenie(a, b):
# #     return a * b

# # wynik = mnozenie(5, 3)
# # print(wynik)
# waga=float(input("Podaj swoją wagę: "))
# print(f"Twoja waga w kg to: {waga}") 
def dochod_miesieczny(stawka_godzinowa, dni_dochodu):
    if dni_dochodu <= 0:
        raise ValueError("Liczba dni dochodu nie może być mniejsza lub równa 0")
    return stawka_godzinowa * dni_dochodu * 8

stawka_godzinowa = float(input("Podaj swoją stawkę godzinową: "))
dni_dochodu = int(input("Podaj liczbę dni dochodu: "))
dochod_miesieczny = dochod_miesieczny(stawka_godzinowa, dni_dochodu)
print(f"Twój dochód miesięczny wynosi: {dochod_miesieczny} zł")
if dochod_miesieczny > 10000:
    print("Jestes w 2 progu podatkowym")
else:
    print("Jestes w 1 progu podatkowym")