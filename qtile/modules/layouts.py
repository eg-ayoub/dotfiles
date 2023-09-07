from libqtile import layout
from libqtile.config import Match
from .utils import get_config

config = get_config()

layouts = [
    layout.MonadTall(
        margin=config["layout"]["mtall"]["margin"],
        border_focus=config["layout"]["colors"]["focus"],
        border_normal=config["layout"]["colors"]["normal"],
        ratio=config["layout"]["mtall"]["ratio"],
        max_ratio=config["layout"]["mtall"]["max_ratio"],
        min_ratio=config["layout"]["mtall"]["min_ratio"],
    ),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(title='pinentry'),  # GPG key password entry
    Match(title='RPCSX'),  # RPCSX
    Match(title='SDL Guide'),  # RPCSX
])
