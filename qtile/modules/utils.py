"""Utils for qtile"""

import gi
import os
import subprocess
import sys
import tomli

gi.require_version('Gtk', '3.0')
from functools import cache
from pathlib import Path

from gi.repository import Gtk

from libqtile.utils import send_notification
from libqtile.log_utils import logger

BRI_DEVICE = "intel_backlight"
BRI_NID = None
brightness_notification_id = None
def notify_brightness(_ = None):
    """Send a notification with current brightness"""
    global brightness_notification_id
    # fetch brightness level:
    brightness = "0%"
    try:
        brightness=subprocess.check_output([
            "brightnessctl",
            "-m",
            "-d",
            BRI_DEVICE,
        ]).decode(sys.stdout.encoding).split(',')[3]
    except subprocess.CalledProcessError as exc:
        send_notification("Error", f"Failed to get brightness level: {exc!s}")
        return

    hint_args=["-h", f"int:value:{brightness}"]

    nid_args=[]
    if brightness_notification_id is not None:
        nid_args=["-r", str(brightness_notification_id)]

    timeout_args=["-t", "500"]

    try:
        brightness_notification_id=subprocess.check_output([
            "dunstify",
            *nid_args,
            *timeout_args,
            *hint_args,
            "-p",
            "Brightness",
            f"Changed {brightness}"
            ]).decode(sys.stdout.encoding)[:-1]
    except subprocess.CalledProcessError as exc:
        logger.warning("Failed to send notification for brightness, {}", exc)

def run_local(_ = None, script = None):
    """Run a script in config folder"""
    if not script:
        logger.warning("Please pass a script to run_local")
    run([os.path.expanduser(f"~/.config/qtile/scripts/{script}")])

def run(*args, **kwargs):
    """run a shell command."""
    try:
        ret = subprocess.run(*args, **kwargs)
        logger.warning(f"script returned {ret!s}")
    except subprocess.CalledProcessError as exc:
        logger.exception(exc)

def find_icon(appname):
    """Find icon for appname."""
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
    """Parse title and handle bold."""
    ret = []
    titles = text.split(" | ")
    for title in titles:
        if title.startswith("<b>"):
            ret.append("<b>" + parse_title(title[3:-4]) + "</b>")
        else:
            ret.append(parse_title(title))
    return " | ".join(ret)


def parse_title(title):
    """Parse title to get shorter program name."""
    for prg in ["- Visual Studio Code", "- Google Chrome", "- Opera", "- Slack", "- Vivaldi", "— Mozilla Firefox"]:
        if prg in title:
            title = title[:-len(prg)]
            title = title[:20]
            return title + prg
    return title

def _deep_update(dest, upd):
    """Update nested dict."""
    for k, val in upd.items():
        if isinstance(val, dict):
            dest[k] = _deep_update(dest.get(k, {}), val)
        else:
            dest[k] = val
    return dest

@cache
def get_config():
    """Read config files, overwrite values from the default."""
    default_config_path = Path.home() / ".config/qtile/defaults.toml"
    if not default_config_path.is_file():
        raise FileNotFoundError("Default config not found")
    config = tomli.loads(default_config_path.read_text(encoding="utf-8"))
    config_path = Path.home() / ".config/qtile/config.toml"
    if config_path.is_file():
        config = _deep_update(config, tomli.loads(config_path.read_text(encoding="utf-8")))
    return config
