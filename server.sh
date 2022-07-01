#!/bin/bash

V2GPATH=/Users/dhjeong/Desktop/EV-Charging-Research/EVS-Research/v2gdecoder-web/V2Gdecoder/target/V2Gdecoder-jar-with-dependencies.jar

echo "[*] Find Running V2GServer"
result=`ps -ef | grep V2Gdecoder-jar | awk '{print $2}'`
cmd=`kill -9 $result`

echo "[*] V2GServer Build"
cd V2Gdecoder

if [ -f "$V2GPATH" ]; then
    echo "[*] V2GServer Already Builded."
else
    echo "[*] V2GServer Build Start..."
    mvn compile assembly:single
fi

echo "[*] V2GServer Starting.."
java -jar ./target/V2Gdecoder-jar-with-dependencies.jar -w &

echo "[*] WebServer Starting.."
cd ../
python3 main.py
