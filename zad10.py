def foo(zdanie):
    zdanie = zdanie.replace(" ", "").replace(".", "").lower()
    if zdanie == zdanie[::-1]:
        print("Jest to palindrom")
    else:
        print("Nie jest to palindrom")


zdanie = "Kobyła ma mały bok."
foo(zdanie)
