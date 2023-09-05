from libqtile import bar, widget
from libqtile.config import Screen
from libqtile import qtile
from .utils import parse_titles

screens = [
    Screen(
        bottom=bar.Bar(
            [
                # apps
                widget.TextBox("APPS",
                               mouse_callbacks={
                                   "Button1": lambda: qtile.cmd_spawn("rofi -show drun -show-icons")
                               },
                               foreground="#2d394e",
                               background="#a7c080",
                               fontsize=14,
                               font="Hack Nerd Font Bold"),
                widget.GroupBox(
                    disable_drag=True,
                    rounded=False,
                    highlight_method="block",
                    urgent_alert_method="block",
                    block_highlight_text_color="#2d394e",
                    background="#475258",
                    active="#9da9a0",
                    inactive="#2d394e",
                    highlight_color=["#2d394e", "#2d394e"],
                    this_current_screen_border="#a7c080",
                    this_screen_border="#a7c080",
                    other_current_screen_border="#dbbc7f",
                    other_screen_border="#dbbc7f",
                    urgent_border="#e67e80",
                    urgent_text="#e67e80",
                    fontsize=14,
                    font="Hack Nerd Font"),
                widget.WindowTabs(
                    foreground="#809185",
                    fontsize=14,
                    parse_text=parse_titles,
                ),
                # system tray
                widget.Systray(
                    background="#475258"
                ),
                # time
                widget.Clock(
                    format="%I:%M:%S %p",
                    background="#475258",
                    foreground="#9da9a0",
                    fontsize=14,
                ),
                # layout
                widget.CurrentLayout(
                    background="#475258",
                    foreground="#9da9a0",
                    fontsize=14,
                ),
                # keyboard layout
                widget.KeyboardLayout(
                    configured_keyboards=['fr', 'gb'],
                    option='grp:alt_space_toggle',
                    fontsize=14,
                    font="Hack Nerd Font Bold",
                    background="#475258",
                    foreground="#9da9a0"
                ),
                # exit
                widget.TextBox("LOGOUT",
                               mouse_callbacks={
                                   "Button1": lambda: qtile.cmd_spawn("xfce4-session-logout")
                               },
                               foreground="#2d394e",
                               background="#e67e80",
                               fontsize=14,
                               font="Hack Nerd Font Bold")
            ],
            24,
            background="#343f44",
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
                    highlight_method="block",
                    urgent_alert_method="block",
                    block_highlight_text_color="#2d394e",
                    background="#475258",
                    active="#9da9a0",
                    inactive="#2d394e",
                    highlight_color=["#2d394e", "#2d394e"],
                    this_current_screen_border="#a7c080",
                    this_screen_border="#a7c080",
                    other_current_screen_border="#dbbc7f",
                    other_screen_border="#dbbc7f",
                    urgent_border="#e67e80",
                    urgent_text="#e67e80",
                    fontsize=14,
                    font="Hack Nerd Font"),
                widget.WindowName(
                    foreground="#809185",
                    fontsize=14,
                ),
            ],
            24,
            background="#343f44",
        ),
    )
]
