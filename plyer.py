from plyer import notification

notification.notify(
    title="Disk Alert",
    message="Disk usage exceeded 90%!",
    timeout=5  # seconds
)
