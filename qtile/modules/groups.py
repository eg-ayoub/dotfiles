from libqtile.config import ScratchPad, DropDown, Key, Group
from libqtile.command import lazy
from .keys import keys, mod, terminal

group_names = [
    "www", "irc", "dev", "dev.", "term",
    "log", "sys", "misc", "mov"
]

group_shortcuts_azerty = [
    'ampersand', 'eacute', 'quotedbl', 'apostrophe', 'parenleft',
    'minus', 'egrave', 'underscore', 'ccedilla'
]

group_shortcuts_qwerty = [
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9'
]

groups = [
    ScratchPad(
        "dropdown",
        [
            DropDown(
                "terminal",
                terminal,
                width=0.8,
                height=0.6,
                opacity=0.8,
            )
        ],
    ),
    *[Group(name) for name in group_names],
]

keys.extend([
    Key([mod], "space", lazy.group["dropdown"].dropdown_toggle("terminal"))
])

for index, group in enumerate(groups[1:]):
    keys.extend([
        # switch to group - QWERTY
        Key([mod],
            group_shortcuts_qwerty[index],
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # move focused to group - QWERTY
        Key([mod, "shift"],
            group_shortcuts_qwerty[index],
            lazy.window.togroup(group.name),
            desc="Switch to & move focused window to group {}".format(group.name)),

        # switch to group - AZERTY
        Key([mod],
            group_shortcuts_azerty[index],
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # move focused to group - AZERTY
        Key([mod, "shift"],
            group_shortcuts_azerty[index],
            lazy.window.togroup(group.name),
            desc="Switch to & move focused window to group {}".format(group.name)),
    ])
