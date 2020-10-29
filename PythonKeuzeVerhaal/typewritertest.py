import sys
import time

restartText = "Do you want to restart? Y/N...\n\n"
for l in restartText:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.2)
