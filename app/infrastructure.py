import collections


class CommandDispatcher:

    def __init__(self):
        self.handlers = dict()
        self.event_bus = None

    def register(self, cmd_type, handler):
        if cmd_type in self.handlers:
            raise HandlerRedefinedError()
        self.handlers[cmd_type] = handler

    def handle(self, cmd):
        t = type(cmd)
        if t not in self.handlers:
            raise NoRegisteredHandlerError()
        handler = self.handlers[t]
        policies = getattr(handler, 'policies', [])
        for policy in policies:
            if not policy.is_satisfied(cmd):
                print('PolicyError: %s(%s)' % (policy, cmd))
                return
        return handler(cmd)


class EventDispatcher:

    def __init__(self):
        self.handlers = collections.defaultdict(list)

    def register(self, event_type, handler):
        self.handlers[event_type].append(handler)

    def handle(self, event):
        for handler in self.handlers[type(event)]:
            handler(event)


class CommandBus:

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def register(self, commands, handler):
        for command in commands:
            self.dispatcher.register(command, handler)

    def handle(self, command):
        return self.dispatcher.handle(command)


class EventBus:

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def register(self, events, handler):
        for event in events:
            self.dispatcher.register(event, handler)

    def handle(self, event):
        self.dispatcher.handle(event)

    def publish(self, event):
        self.handle(event)


class UnitOfWork:

    def __enter__(self):
        raise NotImplementedError('enter')

    def __exit__(self, type, value, traceback):
        raise NotImplementedError('exit')

    def commit(self):
        raise NotImplementedError('commit')

    def rollback(self):
        raise NotImplementedError('rollback')

    @property
    def contacts(self):
        raise NotImplementedError('contacts')


class UnitOfWorkManager:

    def start(self):
        return UnitOfWork()


class ContactRepository:

    def create(self, name, phone):
        raise NotImplementedError('create')

    def read(self, name):
        raise NotImplementedError('read')

    def update(self, name, phone):
        raise NotImplementedError('update')

    def delete(self, name):
        raise NotImplementedError('delete')


class HandlerRedefinedError(Exception):
    pass


class NoRegisteredHandlerError(Exception):
    pass


class MapperRedefinedError(Exception):
    pass


class UnknownReaderError(Exception):
    pass


class RejectedMessageError(Exception):
    pass


class ShortPhoneNumberError(Exception):
    pass
