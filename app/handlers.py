from .events import ContactCreated, ContactUpdated, ContactDeleted
from .policy import policies, PhoneNumberLongEnough


class CreateContactHandler:

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    @policies(PhoneNumberLongEnough())
    def __call__(self, cmd):
        self.repo.create(cmd.name, cmd.phone)
        self.bus.publish(ContactCreated(name=cmd.name, phone=cmd.phone))


class UpdateContactHandler:

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def __call__(self, cmd):
        self.repo.update(cmd.name, cmd.phone)
        self.bus.publish(ContactUpdated(name=cmd.name, phone=cmd.phone))


class DeleteContactHandler:

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def __call__(self, cmd):
        self.repo.delete(cmd.name)
        self.bus.publish(ContactDeleted(name=cmd.name))


class ReadContactHandler:

    def __init__(self, repo, bus):
        self.repo = repo
        self.bus = bus

    def __call__(self, cmd):
        return self.repo.read(cmd.name)


class ContactEventsHandler:

    def __call__(self, event):
        print(event)
