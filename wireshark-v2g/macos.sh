#!/bin/bash

mkdir /Applications/Wireshark.app/Contents/PlugIns/wireshark/3-6/v2gdecode
cp exiv2g.lua /Applications/Wireshark.app/Contents/PlugIns/wireshark/3-6/v2gdecode/
cp v2gsdp.lua /Applications/Wireshark.app/Contents/PlugIns/wireshark/3-6/v2gdecode/
cp v2gtp.lua /Applications/Wireshark.app/Contents/PlugIns/wireshark/3-6/v2gdecode/

echo "[*] Wireshark V2G Pathced!!"
echo "[*] Please Reload Plugin"