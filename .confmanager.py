### import
import os
import time

### space
space = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print (space)

### print list config
print ("0  alacritty")
print ("1  bash")
print ("2  bspwm")
print ("3  dunst")
print ("4  herbstluftwm")
print ("5  neofetch")
print ("6  picom")
print ("7  qutebrowser")
print ("8  rofi")
print ("9 startpage")
print ("10 zsh")

### input
a = int(input("\nthis is "))

### rules

# alacritty
if a == 0:
	os.system ("nano $HOME/.config/alacritty/alacritty.yml")

# bash
elif a == 1:
	os.system ("nano $HOME/.bashrc")

# bspwm
elif a == 2:
	print (space,"\n0 wm\n1 key\n")
	b1 = int(input("this is "))
	# wm
	if b1 == 0:
		os.system ("nano $HOME/.config/bspwm/bspwmrc")

	# key
	elif b1 == 1:
		os.system ("nano $HOME/.config/sxhkd/sxhkdrc")

# dinst
elif a == 3:
	os.system ("nano $HOME/.config/dunst/dunstrc")

# herbstluftwm
elif a == 4:
	os.system ("nano $HOME/.config/herbstluftwm/autostart")

# neofetch
elif a == 5:
	os.system ("nano $HOME/.config/neofetch/config.conf")

# picom
elif a == 6:
	os.system ("nano $HOME/.config/picom/picom.conf")

# qutebrowser
elif a == 7:
	print (space, "\n\n0 config\n1 quickmarks\n")
	b2 = int(input("this is "))

	# quteconf
	if b2 == 0:
		os.system ("nano $HOME/.config/qutebrowser/config.py")

	# quickmarks
	elif b2 == 1:
		os.system ("nano $HOME/.config/qutebrowser/quickmarks")

# rofi
elif a == 8:
	os.system ("nano $HOME/.config/rofi/config.rasi")

# startpage
elif a == 9:
	os.system ("nano $HOME/.startpage/index.html")

# zsh
elif a == 10:
	os.system ("nano $HOME/.zshrc")


### exit conf
time.sleep(0.5)
os.system("xdotool key super+w")