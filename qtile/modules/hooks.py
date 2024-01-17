"""Hooks for Qtile."""

from libqtile import hook
from libqtile.utils import send_notification
from libqtile.log_utils import logger

from .utils import run_local

@hook.subscribe.screen_change
def reconfigure_on_randr(_):
    """Run when screens are plugged/unplugged."""
    logger.info("Reconfigure Qtile on screen_change")
    send_notification("Reconfiguring", "Reconfiguring Qtile due to screen change")

@hook.subscribe.restart
def restart():
    """Runs when qtile restarts."""
    logger.info("Restarting Qtile")
    send_notification("Qtile restart", "Qtile is restarting")
    run_local(script="pre_start.sh")

@hook.subscribe.startup
def autostart():
    """Run when qtile starts or restarts."""
    logger.info("Started Qtile")
    send_notification("Qtile started", "Qtile has started")
    run_local(script="post_start.sh")
