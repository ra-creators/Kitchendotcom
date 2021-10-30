#!/bin/bash

PARAMS=('-m 6 -q 70 -mt -af -progress')

if [ $# -ne 0 ]; then
	PARAMS=$@;
fi

cd $(pwd)

shopt -s nullglob nocaseglob extglob

for FILE in **/img/gallery/**/*.@(jpg|jpeg|tif|tiff|png); do 
    	#echo $FILE
	cwebp $PARAMS "$FILE" -o "${FILE%.*}".webp;
	rm "$FILE"
done
