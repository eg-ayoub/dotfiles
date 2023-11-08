"""Hooks for Qtile."""

import os
import subprocess

from libqtile import hook
from libqtile.utils import send_notification

@hook.subscribe.screen_change
def restart_on_randr(_):
    """Run when screens are plugged/unplugged."""
    send_notification("Restarting Qtile", "Restarting Qtile due to screen change")

@hook.subscribe.startup_once
def autostart():
    """Run when qtile starts."""
    send_notification("Qtile started", "Qtile has started")
    autostart_script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([autostart_script])
