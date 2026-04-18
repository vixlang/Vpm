from .base import Command as Command
from . import cmd_add, cmd_del
from .utils import log as log


cmd_list: list[type[Command]] = [
    cmd_add.AddCmd,
    cmd_del.DelCmd,
]
