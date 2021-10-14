class House:
    doors: int
    color: str

    def __init__(self, doors: int, color: str) -> None:
        self.doors = doors
        self.color = color

    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            print('Kolor nie może być ten sam')
            return

        self.color = new_color

    def __len__(self) -> int:
        return 100

    def __str__(self) -> str:
        return f'liczba drzwi: {self.doors}, kolor elewacji: {self.color}'




house1: House = House(doors=10, color='blue')
print(house1.doors)
print(house1.color)

print(len(house1))
print(house1)