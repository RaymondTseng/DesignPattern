from abc import abstractmethod, ABC


class Group(ABC):
    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def change(self):
        pass

    @abstractmethod
    def plan(self):
        pass


class RequirementGroup(Group):

    def find(self):
        print("find requirement group")

    def add(self):
        print("add a requirement")

    def delete(self):
        print("delete a requirement")

    def change(self):
        print("change a requirement")

    def plan(self):
        print("set up a plan")


class PageGroup(Group):

    def find(self):
        print("find page group")

    def add(self):
        print("add a page")

    def delete(self):
        print("delete a page")

    def change(self):
        print("change a page")

    def plan(self):
        print("set up a plan")


class CodeGroup(Group):

    def find(self):
        print("find code group")

    def add(self):
        print("add a feature")

    def delete(self):
        print("delete a feature")

    def change(self):
        print("change a feature")

    def plan(self):
        print("set up a plan")


class Command(ABC):
    def __init__(self):
        # should be use setter function here
        self.rg = RequirementGroup()
        self.pg = PageGroup()
        self.cg = CodeGroup()

    @abstractmethod
    def execute(self):
        pass


class AddRequirementCommand(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        self.rg.find()
        self.rg.add()
        self.rg.plan()


class DeletePageCommand(Command):
    def __init__(self):
        super().__init__()

    def execute(self):
        self.pg.find()
        self.pg.delete()
        self.pg.plan()


class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def action(self):
        self.command.execute()


if __name__ == "__main__":
    invoker = Invoker()
    c = AddRequirementCommand()
    invoker.set_command(c)
    invoker.action()
    c = DeletePageCommand()
    invoker.set_command(c)
    invoker.action()
