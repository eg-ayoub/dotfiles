"""Hooks for Qtile."""
import time

from libqtile import hook, qtile
from libqtile.utils import send_notification
from libqtile.log_utils import logger

from .utils import run_local, run

@hook.subscribe.screen_change
def reconfigure_on_randr(_):
    """Run when screens are plugged/unplugged."""
    send_notification("Reconfiguring", "Reconfiguring Qtile due to screen change")

@hook.subscribe.restart
def restart():
    """Runs before qtile restarts."""
    send_notification("Qtile restart", "Qtile is restarting")
    run_local(script="pre_restart.sh")

@hook.subscribe.startup_complete
def start():
    """Run after qtile starts or restarts."""
    send_notification("Qtile started", "Qtile has started")
    run_local(script="post_start.sh")

@hook.subscribe.startup_once
def autostart():
    """Run when qtile starts for the first time."""
    send_notification("Qtile started", "Welcome to Qtile")
    run_local(script="autostart.sh")
