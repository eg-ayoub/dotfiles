from libqtile import layout
from libqtile.config import Match
from .utils import get_config

config = get_config()

layouts = [
    layout.Bsp(),
    # layout.MonadTall(
    #     margin=config["layout"]["mtall"]["margin"],
    #     border_focus=config["layout"]["colors"]["focus"],
    #     border_normal=config["layout"]["colors"]["normal"],
    #     ratio=config["layout"]["mtall"]["ratio"],
    #     max_ratio=config["layout"]["mtall"]["max_ratio"],
    #     min_ratio=config["layout"]["mtall"]["min_ratio"],
    # ),
    # layout.MonadWide(
    #     margin=config["layout"]["mtall"]["margin"],
    #     border_focus=config["layout"]["colors"]["focus"],
    #     border_normal=config["layout"]["colors"]["normal"],
    #     ratio=config["layout"]["mtall"]["ratio"],
    #     max_ratio=config["layout"]["mtall"]["max_ratio"],
    #     min_ratio=config["layout"]["mtall"]["min_ratio"],
    # ),
    layout.Max(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(title='pinentry'),  # GPG key password entry
    Match(title='RPCSX'),  # RPCSX
    Match(title='SDL Guide'),  # RPCSX
])
