from models.telefonbok import Telefonbok

from tuiFabricator.TuiFabricator import TuiFabricator
from tuiFabricator.QueryResponse import QueryResponse
from tuiFabricator.QueryDescriptor import QueryDescriptor


class ExitHelper:
    exitCondition = [True]

    def exit(self):
        self.exitCondition[0] = False


class Program:

    def __init__(self):
        self.telefonbok = Telefonbok()

    def add(self, args):
        name = args[0]
        number = args[1]
        self.telefonbok.add(name, number)

    def lookup(self, args):
        name = args[0]
        self.telefonbok.lookup(name)

    def alias(self, args):
        origin = args[0]
        alias = args[1]
        self.telefonbok.alias(origin, alias)

    def change(self, args):
        name = args[0]
        number = args[1]
        self.telefonbok.change(name, number)

    def save(self, args):
        filename = args[0]
        self.telefonbok.save(filename)

    def load(self, args):
        filename = args[0]
        self.telefonbok.load(filename)


def run():
    program = Program()
    exit_helper = ExitHelper()

    command_definitions = [
        QueryResponse("add", 2, [None, None], program.add),
        QueryResponse("lookup", 1, [None], program.lookup),
        QueryResponse("alias", 2, [None, None], program.alias),
        QueryResponse("change", 2, [None, None], program.change),
        QueryResponse("save", 1, [None], program.save),
        QueryResponse("load", 1, [None], program.load),
        QueryResponse("quit", 0, [], exit_helper.exit)
    ]

    query_definition = QueryDescriptor()
    query_definition.showPrompt = True
    query_definition.prompt = "telebok>"

    tui = TuiFabricator(query_definition, command_definitions)
    tui.query_repeat(exit_helper.exitCondition)


run()
