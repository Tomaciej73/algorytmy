def foo1(imie, nazwisko):
    print(imie[0].upper() + "." + nazwisko[0].upper() + nazwisko[1:])


def foo2(imie, nazwisko, foo1):
    foo1(imie, nazwisko)


foo2("jan", "kowalski", foo1)
