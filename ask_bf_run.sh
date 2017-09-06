#!/bin/bash
echo "Do you change the DBFile in the script. Are you change?"
while true
do
        echo "Answer: Y/N"
        read REPLY
        if [ $REPLY == "Y" ] || [ $REPLY == "y" ]; then
                break
        elif [ $REPLY == "N" ] || [ $REPLY == "n" ]; then
                echo Aborted
                exit 0
        fi
done
echo Run command
