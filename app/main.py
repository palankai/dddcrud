from .infrastructure import EventBus, CommandBus
from .infrastructure import EventDispatcher, CommandDispatcher
from .config import register_events, register_commands
from .commands import CreateContact, ReadContact
from .infrastructure import UnitOfWork, UnitOfWorkManager, ContactRepository
from .models import Contact


class FakeContactRepository(ContactRepository):

    def create(self, name, phone):
        pass

    def read(self, name):
        return Contact(name, 'FAKE')

    def update(self, name, phone):
        pass

    def delete(self, name):
        pass


class FakeUnitOfWork(UnitOfWork):

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    @property
    def contacts(self):
        return FakeContactRepository()


class FakeUnitOfWorkManager(UnitOfWorkManager):

    def start(self):
        return FakeUnitOfWork()

def main():
    uowm = FakeUnitOfWorkManager()
    uow = uowm.start()
    repo = uow.contacts

    cmd_dispatcher = CommandDispatcher()
    evt_dispatcher = EventDispatcher()
    cmd_bus = CommandBus(cmd_dispatcher)
    evt_bus = EventBus(evt_dispatcher)

    cmd_dispatcher.event_bus = evt_bus

    register_commands(repo, cmd_bus, evt_bus)
    register_events(evt_bus)

    create_contact = CreateContact('Csaba', '+44')
    cmd_bus.handle(create_contact)

    create_contact = CreateContact('Csaba', '+447922')
    cmd_bus.handle(create_contact)

    read_contact = ReadContact('Csaba')
    print(cmd_bus.handle(read_contact))


if __name__ == '__main__':
    main()
