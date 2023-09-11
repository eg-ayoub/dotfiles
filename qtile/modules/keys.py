from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# mod key
mod = "mod4"

# terminal
terminal = guess_terminal()

# shortcuts
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # move windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # resize windows - normal
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # resize windows - normal
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    # normalize window
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # resize windows - monad tall
    Key([mod, "control"], "p", lazy.layout.grow(), desc="Grow window"),
    Key([mod, "control"], "m", lazy.layout.shrink(), desc="Shrink window"),
    # terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # toggle between layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    # kill window
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    # restart qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # rofi launcher
    Key([mod], "d", lazy.spawn("rofi -show drun -show-icons"), desc="App launcher"),
    # pass
    Key([mod], "i", lazy.spawn("rofi-pass"), desc="Spawn a command using a prompt widget"),
    # vscode recents
    Key([mod], "o", lazy.spawn("rofi -show vscode-recent"), desc="VSCode recents"),    
    # vscode recents
    Key([mod], "v", lazy.spawn("xfce4-clipman-history"), desc="VSCode recents"),
    # screenshot
    Key([], "Print", lazy.spawn("xfce4-screenshooter"), desc="Take a screenshot")
]
