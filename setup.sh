#!/bin/bash

echo -e " ╔═╗┌─┐┌┐┌╔╗ ┌─┐┌┬┐"
echo -e " ╚═╗├─┤│││╠╩╗│ │ │ "
echo -e " ╚═╝┴ ┴┘└┘╚═╝└─┘ ┴ "
echo -e "------Bot By san------"
sleep 2

clear
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3 python3-pip
#pip3 install python-telegram-bot==12.0.0 // Install jika python3 eror
sudo apt install git -y

#Buat folder Bot
mkdir -p san/bot

#Ke direktori Bot
cd san/bot

#Ambil file bot dan instal
git clone https://github.com/Paper890/Bot.git
pip install -r requirements.txt

