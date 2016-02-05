from collections import namedtuple


def parser(val):
    return val

FieldMap = namedtuple("FieldMap", ["field", "parser"])


def _msg(name, *args):
    names = []
    names.extend(args)
    m = namedtuple(name, names)
    m.msgtype = None
    return m


def cmd(name, *args):
    m = _msg(name, *args)
    m.msgtype = 'command'
    return m

def evt(name, *args):
    m = _msg(name, *args)
    m.msgtype = 'event'
    return m
