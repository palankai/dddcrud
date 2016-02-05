from .commands import CreateContact, ReadContact, UpdateContact, DeleteContact
from .events import ContactCreated, ContactUpdated, ContactDeleted

from .handlers import (
    CreateContactHandler, UpdateContactHandler, DeleteContactHandler,
    ReadContactHandler
)
from .handlers import ContactEventsHandler

def register_commands(repo, bus, evt_bus):
    bus.register([CreateContact], CreateContactHandler(repo, evt_bus))
    bus.register([ReadContact], ReadContactHandler(repo, evt_bus))
    bus.register([UpdateContact], UpdateContactHandler(repo, evt_bus))
    bus.register([DeleteContact], DeleteContactHandler(repo, evt_bus))


def register_events(bus):
    bus.register(
        [ContactCreated, ContactUpdated, ContactDeleted],
        ContactEventsHandler()
    )
