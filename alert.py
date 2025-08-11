import sys

def alert(message):
    # ANSI escape codes for red bold text + beep sound
    print(f"\033[91m\033[1m⚠ ALERT: {message}\033[0m\a", file=sys.stderr)

alert("Disk usage exceeded threshold!")
