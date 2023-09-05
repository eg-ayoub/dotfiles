from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.MonadTall(margin=8, border_focus='#a7c080',
                     border_normal='#343f44', ratio=0.6,
                     max_ratio=0.8, min_ratio=0.2),
    #layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(),
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
