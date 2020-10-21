
class Actor:
    def __init__(self, actor_full_name: str):
        self.__colleagues = []
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.__actor_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_full_name < other.__actor_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            self.__colleagues.append(colleague.__actor_full_name)
            colleague.__colleagues.append(self.__actor_full_name)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague.__actor_full_name in self.__colleagues:
            return True
        else:
            return False




def main():
    actor1 = Actor('Bruce Lee')
    actor2 = Actor('Ezrea Miller')
    print(actor1)
    print(actor2)
    actor1.add_actor_colleague(actor2)

    print(actor1.check_if_this_actor_worked_with(actor2))
    print(actor2.check_if_this_actor_worked_with(actor1))
main()

