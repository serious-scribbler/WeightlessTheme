#! /bin/sh
# Installs syntax highlighting for the nim programming language in kde
# Syntax highlighting by https://github.com/PhilipWitte/NimKate
cd /tmp
wget https://raw.githubusercontent.com/PhilipWitte/NimKate/master/nimrod.xml
wget https://raw.githubusercontent.com/PhilipWitte/NimKate/master/nimrod.js
mkdir -p ~/.local/share/katepart5/syntax/
mkdir -p ~/.local/share/katepart5/script/indentation/
mv nimrod.xml ~/.local/share/katepart5/syntax/
mv nimrod.js ~/.local/share/katepart5/script/indentation/
echo "Installed successfully!"
