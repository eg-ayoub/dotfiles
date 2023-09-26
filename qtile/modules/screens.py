from libqtile import bar
from qtile_extras import widget
from libqtile.config import Screen
from libqtile import qtile
from .utils import parse_titles, get_config

config = get_config()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # apps
                widget.TextBox("APPS",
                               mouse_callbacks={
                                   "Button1": lambda: qtile.cmd_spawn("rofi -show drun -show-icons")
                               },
                               foreground=config["bar"]["colors"]["foreground"]["dark"],
                               background=config["bar"]["colors"]["apps"],
                               fontsize=config["bar"]["main"]["font"]["size"],
                               font=config["bar"]["main"]["font"]["bold"]),
                widget.GroupBox(
                    disable_drag=True,
                    rounded=False,
                    padding=config["bar"]["main"]["gbox"]["padding"],
                    highlight_method="block",
                    urgent_alert_method="block",
                    block_highlight_text_color=config["bar"]["colors"]["foreground"]["dark"],
                    background=config["bar"]["colors"]["background"]["bright"],
                    active=config["bar"]["colors"]["foreground"]["bright"],
                    inactive=config["bar"]["colors"]["fallback"],
                    highlight_color=[
                        config["bar"]["colors"]["fallback"],
                        config["bar"]["colors"]["fallback"]
                    ],
                    this_current_screen_border=config["bar"]["colors"]["this"],
                    this_screen_border=config["bar"]["colors"]["this"],
                    other_current_screen_border=config["bar"]["colors"]["other"],
                    other_screen_border=config["bar"]["colors"]["other"],
                    urgent_border=config["bar"]["colors"]["urgent"],
                    urgent_text=config["bar"]["colors"]["urgent"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["normal"]),
                widget.WindowTabs(
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["normal"],
                    parse_text=parse_titles,
                ),
                # system tray
                widget.Systray(
                    background=config["bar"]["colors"]["background"]["bright"],
                ),
                # time
                widget.Clock(
                    format="%I:%M",
                    background=config["bar"]["colors"]["background"]["bright"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    font=config["bar"]["main"]["font"]["normal"],
                    fontsize=config["bar"]["main"]["font"]["size"],
                ),
                widget.CurrentLayoutIcon(
                    scale=0.65,
                    background=config["bar"]["colors"]["background"]["bright"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                ),
                # keyboard layout
                widget.KeyboardLayout(
                    configured_keyboards=['fr', 'us'],
                    option='grp:alt_space_toggle',
                    fontsize=config["bar"]["main"]["font"]["size"],
                    font=config["bar"]["main"]["font"]["bold"],
                    background=config["bar"]["colors"]["background"]["bright"],
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                ),
                # exit
                widget.TextBox("LOGOUT",
                               mouse_callbacks={
                                   "Button1": lambda: qtile.cmd_spawn("xfce4-session-logout")
                               },
                               foreground=config["bar"]["colors"]["foreground"]["dark"],
                               background=config["bar"]["colors"]["exit"],
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
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    rounded=False,
                    padding=config["bar"]["secondary"]["gbox"]["padding"],
                    highlight_method="block",
                    urgent_alert_method="block",
                    block_highlight_text_color=config["bar"]["colors"]["foreground"]["dark"],
                    background=config["bar"]["colors"]["background"]["bright"],
                    active=config["bar"]["colors"]["foreground"]["bright"],
                    inactive=config["bar"]["colors"]["fallback"],
                    highlight_color=[
                        config["bar"]["colors"]["fallback"],
                        config["bar"]["colors"]["fallback"]
                    ],
                    this_current_screen_border=config["bar"]["colors"]["this"],
                    this_screen_border=config["bar"]["colors"]["this"],
                    other_current_screen_border=config["bar"]["colors"]["other"],
                    other_screen_border=config["bar"]["colors"]["other"],
                    urgent_border=config["bar"]["colors"]["urgent"],
                    urgent_text=config["bar"]["colors"]["urgent"],
                    fontsize=config["bar"]["secondary"]["font"]["size"],
                    font=config["bar"]["secondary"]["font"]["normal"]),
                widget.WindowTabs(
                    foreground=config["bar"]["colors"]["foreground"]["bright"],
                    fontsize=config["bar"]["secondary"]["font"]["size"],
                    font=config["bar"]["secondary"]["font"]["normal"],
                    parse_text=parse_titles,
                ),
            ],
            config["bar"]["secondary"]["height"],
            background=config["bar"]["colors"]["background"]["normal"],
        ),
    )
]
