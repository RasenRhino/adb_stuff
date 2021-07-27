#! /bin/bash
cat ip.txt | while read IP
do
echo $IP
command adb connect $IP:5555;
done

