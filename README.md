# WeightlessTheme
The weightless theme is my personal lightweight theme for awesomewm

## Features
*coming soon*

## Requirements
- All required packages (not including awesome) are listed in requirements.txt
- You might need additional packages if you are not using Ubuntu

## Recommendations
Here are some tools and settings I used to improve the look of some tools.
All mentioned config files can be found in the otherDotFiles directory.

## Ubuntu specific
My preferred shell is bash, Ubuntu uses dash as default in order to change it to bash use
```sudo dpkg-reconfigure dash```

### gnome-terminal
- Add padding to gnome by copying my *gtk.css* to *.config/gtk-3.0/*
- Set a shortcut for *"Hide and Show Menubar"* and hide it by default (**Preferences**>**General**>Show menubar by default...)
- Install the [Argonaut color scheme](https://mayccoll.github.io/Gogh/) and set it as default
- Set the background color to *#222222* (**Preferences**>**Your scheme**>**Colors**)
- In the same menu enable transparent background and adjust it to your liking

### bash
Most of the improvements I hae done can be replicated by copying my *.bashrc* file some of them require extra steps
- Create a scripts directory in your home directory (or somewhere else) and add it to *$PATH*
- Download [pfetch](https://github.com/dylanaraps/pfetch) into your scripts directory and add it to the end of your *.bashrc*

