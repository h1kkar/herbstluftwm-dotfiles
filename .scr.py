import os
import time

os.system ("scrot $HOME/Изображения/rice.png")
time.sleep(1)
os.system ("notify-send Screenshot taken!")