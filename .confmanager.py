### import
import os
import time

### space
space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print (space)

### editor
editor = "vim"

### print list config
print ("0  alacritty")
print ("1  dunst")
print ("2  herbstluftwm")
print ("3  picom")
print ("4  qutebrowser")
print ("5  rofi")
print ("6  startpage")
print ("7  vim")
print ("8  zsh")

### input
a = int(input("\nthis is "))

### rules

# alacritty
if a == 0:
    os.system (editor + " $HOME/.config/alacritty/alacritty.yml")

# dinst
elif a == 1:
    os.system (editor + " $HOME/.config/dunst/dunstrc")

# herbstluftwm
elif a == 2:
	os.system (editor + " $HOME/.config/herbstluftwm/autostart")

# picom
elif a == 3:
	os.system (editor + " $HOME/.config/picom/picom.conf")

# qutebrowser
elif a == 4:
	print (space, "\n\n0 config\n1 quickmarks\n")
	b2 = int(input("this is "))

	# quteconf
	if b2 == 0:
		os.system (editor + " $HOME/.config/qutebrowser/config.py")

	# quickmarks
	elif b2 == 1:
		os.system (editor + " $HOME/.config/qutebrowser/quickmarks")

# rofi
elif a == 5:
	os.system (editor + " $HOME/.config/rofi/config.rasi")

# startpage
elif a == 6:
	os.system (editor + " $HOME/.startpage/index.html")

# vim
elif a == 7:
    os.system (editor + " $HOME/.vimrc")

# zsh
elif a == 8:
	os.system (editor + " $HOME/.zshrc")

### exit conf
time.sleep(0.5)
os.system("xdotool key super+w")
