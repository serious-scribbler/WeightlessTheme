# WeightlessTheme
The weightless theme is my personal lightweight theme for awesomewm

## Screenshots
This theme is still a work in progress, but here is a screenshot that showcases it's current state:
<img src="screenshots/screenshot1.png" />

## Getting Started
*coming soon*

## Requirements
I will write a better summary when the theme is in a more finished state.
- All required packages (not including awesome) are listed in requirements.txt
- You might need additional packages if you are not using Ubuntu

### Additional Requirements for other distros
If you are using a distro other than Ubuntu, you might also need to install the following packages:
- network-manager
- network-manager-gnome

## Recommendations
Here are some tools and settings I used to improve the look of some tools.
All mentioned config files can be found in the otherDotFiles directory.

### Ubuntu specific
My preferred shell is bash. Ubuntu uses dash as default, in order to change it to bash use
```sudo dpkg-reconfigure dash```

### gnome-terminal
- Add padding to the gnome-terminal by copying my *gtk.css* (from the otherDotFiles/gtk-3 directory) to *.config/gtk-3.0/*
- Set a shortcut for *"Hide and Show Menubar"* and hide it by default (**Preferences**>**General**>Show menubar by default...)
- Install the [Argonaut color scheme](https://mayccoll.github.io/Gogh/) and set it as default
- Set the background color to *#222222* (**Preferences**>**Your scheme**>**Colors**)
- In the same menu enable transparent background and adjust it to your liking
- Install the [Ubuntu Mono Nerd Font](https://github.com/ryanoasis/nerd-fonts) (**This is a requirement if you want to use the powerline-shell**)
  - Clone the repo, preferrably into /tmp because it's huge (11GB) and you only need one of the fonts
  - CD into the directory
  - Install the font using ```./install.sh "UbuntuMono"```
  - Change the font in gnome-terminal (**Preferences**>**Your scheme**>Text) to ```UbuntuMono Nerd Font Regular```
  - You might also want to increase the font size, this is a small font

### bash
Most of the improvements I have done can be replicated by copying my *.bashrc* file. I still included all steps in the following list for anyone who wants to use their own .bashrc.
- Create a *scripts* directory in your home directory (or somewhere else) and add it to *$PATH*
- Download [pfetch](https://github.com/dylanaraps/pfetch) into your scripts directory and add it to the end of your *.bashrc*
- [Install powerline-shell](https://github.com/b-ryan/powerline-shell)
  - Copy ```otherDotFiles/powerline/config.json``` to ```~/.config/powerline-shell/```
  - Copy ```otherDotFiles/powerline/weightless.py``` to ```~/powerlinethemes/```
- Add this alias ```alias ddir='du -h --max-depth=1'``` to *.bashrc* to allow the use of *ddir* to get the size of a directory
- Add the *cawm* alias to quickly cd into the awesome directory: ```alias cawm='cd ~/.config/awesome```

### Qt 5 Apps
Qt 5 can be customized by installing a theme.
- Install my [Inverse-Dark-Weightless](https://github.com/serious-scribbler/Inverse-Dark-Weightless) theme.<br>
  Instructions can be found in the readme of my repo.

