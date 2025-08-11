from IPython.display import Javascript

def browser_alert(msg):
    display(Javascript(f'alert("{msg}")'))

browser_alert("Disk usage exceeded threshold!")
