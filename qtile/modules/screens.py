from libqtile import bar, qtile
from libqtile.config import Screen
from qtile_extras import widget

from .utils import get_config, parse_title, find_icon

config = get_config()

bar_progs = [
        (find_icon("alacritty"), "alacritty", "terminal"),
        # (find_icon("vscode"), "code", "code"),
        (find_icon("chrome"), "google-chrome-stable", "chrome"),
        (find_icon("slack"), "slack", "slack"),
        (find_icon("logseq"), "logseq", "logseq"),
]

screens = [
    Screen(
        top=bar.Bar(
            [
                # apps
                widget.Image(
                    filename="~/.config/qtile/assets/icon.png",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show drun -show-icons")
                    }
                ),
                widget.Spacer(
                    length=4,
                ),
                widget.Sep(),
                widget.Sep(),
                # shortcuts
                widget.LaunchBar(progs=bar_progs),
                widget.Sep(),
                widget.Sep(),
                # windows
                widget.TaskList(
                    rounded=False,
                    highlight_method="block",
                    theme_mode="fallback",
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    background=config["bar"]["colors"]["background"]["normal"],
                    border=config["bar"]["colors"]["this"],
                    urgent_border=config["bar"]["colors"]["urgent"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["normal"],
                    parse_text=parse_title,
                ),
                # groups
                widget.GroupBox(
                    disable_drag=True,
                    rounded=False,
                    padding=config["bar"]["main"]["gbox"]["padding"],
                    highlight_method="block",
                    urgent_alert_method="border",
                    background=config["bar"]["colors"]["background"]["normal"],
                    # text colors for group
                    active=config["bar"]["colors"]["foreground"]["bright"],
                    inactive=config["bar"]["colors"]["foreground"]["normal"],
                    # this and other group highlight
                    highlight_color=[
                        config["bar"]["colors"]["fallback"],
                        config["bar"]["colors"]["fallback"]
                    ],
                    # current screen
                    this_current_screen_border=config["bar"]["colors"]["this"],
                    this_screen_border=config["bar"]["colors"]["this"],
                    # other screen
                    other_current_screen_border=config["bar"]["colors"]["other"],
                    other_screen_border=config["bar"]["colors"]["other"],
                    # urgent
                    urgent_border=config["bar"]["colors"]["urgent"],
                    urgent_text=config["bar"]["colors"]["urgent"],
                    # font
                    fontsize=config["bar"]["main"]["gbox"]["font"]["size"],
                    font=config["bar"]["main"]["gbox"]["font"]["normal"]
                ),
                widget.Sep(),
                widget.Sep(),
                # system tray
                widget.Systray(
                    background=config["bar"]["colors"]["background"]["normal"],
                ),
                widget.Sep(),
                widget.Sep(),
                # time
                widget.Clock(
                    format="%I:%M",
                    background=config["bar"]["colors"]["background"]["normal"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    font=config["bar"]["main"]["font"]["normal"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                ),
                # keyboard layout
                widget.KeyboardLayout(
                    configured_keyboards=['fr', 'us altgr-intl'],
                    option='grp:alt_space_toggle',
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["bold"],
                    background=config["bar"]["colors"]["background"]["normal"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                ),
                # layout
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=config["bar"]["colors"]["background"]["normal"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                ),
                widget.Spacer(
                    length=6,
                ),
                # exit
                widget.TextBox("",
                               mouse_callbacks={
                                   "Button1": lambda: qtile.cmd_spawn("xfce4-session-logout")
                               },
                               foreground=config["bar"]["colors"]["exit"],
                               fontsize=config["bar"]["main"]["font"]["size"],
                               font=config["bar"]["main"]["font"]["bold"])
            ],
            config["bar"]["main"]["height"],
            background=config["bar"]["colors"]["background"]["normal"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
            top=bar.Bar(
            [
                # apps
                widget.Image(
                    filename="~/.config/qtile/assets/icon.png",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show drun -show-icons")
                    }
                ),
                widget.Spacer(
                    length=4,
                ),
                widget.Sep(),
                widget.Sep(),
                # shortcuts
                widget.LaunchBar(progs=bar_progs),
                widget.Sep(),
                widget.Sep(),
                # windows
                widget.TaskList(
                    rounded=False,
                    highlight_method="block",
                    theme_mode="fallback",
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    background=config["bar"]["colors"]["background"]["normal"],
                    border=config["bar"]["colors"]["this"],
                    urgent_border=config["bar"]["colors"]["urgent"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["normal"],
                    parse_text=parse_title,
                ),
                # groups
                widget.GroupBox(
                    disable_drag=True,
                    rounded=False,
                    padding=config["bar"]["main"]["gbox"]["padding"],
                    highlight_method="block",
                    urgent_alert_method="border",
                    background=config["bar"]["colors"]["background"]["normal"],
                    # text colors for group
                    active=config["bar"]["colors"]["foreground"]["bright"],
                    inactive=config["bar"]["colors"]["foreground"]["normal"],
                    # this and other group highlight
                    highlight_color=[
                        config["bar"]["colors"]["fallback"],
                        config["bar"]["colors"]["fallback"]
                    ],
                    # current screen
                    this_current_screen_border=config["bar"]["colors"]["this"],
                    this_screen_border=config["bar"]["colors"]["this"],
                    # other screen
                    other_current_screen_border=config["bar"]["colors"]["other"],
                    other_screen_border=config["bar"]["colors"]["other"],
                    # urgent
                    urgent_border=config["bar"]["colors"]["urgent"],
                    urgent_text=config["bar"]["colors"]["urgent"],
                    # font
                    fontsize=config["bar"]["main"]["gbox"]["font"]["size"],
                    font=config["bar"]["main"]["gbox"]["font"]["normal"]
                )
            ],
            config["bar"]["secondary"]["height"],
            background=config["bar"]["colors"]["background"]["normal"],
        ),
    )
]
