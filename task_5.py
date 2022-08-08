class Stationery:
    title: str

    def draw(self):
        print("Мы начинаем.")


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f"{self.title} пишет, подписывает, является хорошим подарком")


class Pencil(Stationery):
    title = "карандаш"

    def draw(self):
        print(f"{self.title} чертит, легко стирается, можно затачить")


class Handle(Stationery):
    title = "маркер"

    def draw(self):
        print(f"{self.title} пригоден для доски, можно рисовать, выделять")


if __name__ == '__main__':
    stationery = Stationery()
    stationery.draw()

    pen = Pen()
    pen.draw()

    pencil = Pencil()
    pencil.draw()

    handle = Handle()
    handle.draw()
