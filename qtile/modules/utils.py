"""Utils for qtile"""

import gi
import tomli

gi.require_version('Gtk', '3.0')
from functools import cache
from pathlib import Path

from gi.repository import Gtk


def find_icon(appname):
    """Find icon for appname"""
    icon_theme = Gtk.IconTheme.get_default()

    # normal attempt
    icon = icon_theme.lookup_icon(appname, 48, 0)
    if icon:
        return icon.get_filename()

    # attempt with capitalized appname
    appname = appname.capitalize()
    icon = icon_theme.lookup_icon(appname, 48, 0)
    if icon:
        return icon.get_filename()

    return appname

def parse_titles(text):
    """Parse title and handle bold"""
    ret = []
    titles = text.split(" | ")
    for title in titles:
        if title.startswith("<b>"):
            ret.append("<b>" + parse_title(title[3:-4]) + "</b>")
        else:
            ret.append(parse_title(title))
    return " | ".join(ret)


def parse_title(title):
    """Parse title to get shorter program name"""
    for prg in ["- Visual Studio Code", "- Google Chrome", "- Opera", "- Slack"]:
        if prg in title:
            title = title[:-len(prg)]
            title = title[:20]
            return title + prg
    return title

def _deep_update(dest, upd):
    """Update nested dict"""
    for k, val in upd.items():
        if isinstance(val, dict):
            dest[k] = _deep_update(dest.get(k, {}), val)
        else:
            dest[k] = val
    return dest

@cache
def get_config():
    """Get config"""
    default_config_path = Path.home() / ".config/qtile/defaults.toml"
    if not default_config_path.is_file():
        raise FileNotFoundError("Default config not found")
    config = tomli.loads(default_config_path.read_text(encoding="utf-8"))
    config_path = Path.home() / ".config/qtile/config.toml"
    if config_path.is_file():
        config = _deep_update(config, tomli.loads(config_path.read_text(encoding="utf-8")))
    return config
