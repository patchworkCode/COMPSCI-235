
class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__director_full_name)


class TestDirectorMethods:

    def test_init(self):
        director1 = Director("Taika Waititi")
        assert repr(director1) == "<Director Taika Waititi>"
        director2 = Director("")
        assert director2.director_full_name is None
        director3 = Director(42)
        assert director3.director_full_name is None
def main():
    director1 = Director("Cameron Diaz")
    director2 = Director("Angelina Jolie")
    director3 = Director("Brad Pitt")
    print(director1 > director2)
    print(director1 > director3)
    print(director2 < director3)
main()