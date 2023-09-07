from libqtile.config import ScratchPad, DropDown, Key, Group
from libqtile.command import lazy
from .keys import keys, mod, terminal
from .utils import get_config

config = get_config()

group_names = config["groups"]["names"]
group_shortcuts_azerty = config["groups"]["shortcuts"]["azerty"]
group_shortcuts_qwerty = config["groups"]["shortcuts"]["qwerty"]

groups = [
    ScratchPad(
        "dropdown",
        [
            DropDown(
                "terminal",
                terminal,
                width=config["scratch"]["term"]["width"],
                height=config["scratch"]["term"]["height"],
                opacity=config["scratch"]["term"]["opacity"],
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
