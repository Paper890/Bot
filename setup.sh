#!/bin/bash
# Warna teks
red="\e[31m"
green="\e[32m"
yellow="\e[33m"
blue="\e[34m"
purple="\e[35m"
cyan="\e[36m"
NC="\e[0m"

clear
echo -e "
░██████╗░█████╗░███╗░░██╗░░░██████╗░░█████╗░████████╗
██╔════╝██╔══██╗████╗░██║░░░██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░███████║██╔██╗██║░░░██████╦╝██║░░██║░░░██║░░░
░╚═══██╗██╔══██║██║╚████║░░░██╔══██╗██║░░██║░░░██║░░░
██████╔╝██║░░██║██║░╚███║██╗██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░"
echo -e""
echo -e "${yellow}UPDATE PACKAGE VPS${NC}"
sleep 2
clear
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3 python3-pip
sudo apt install git -y
echo -e "${yellow} UPDATE SELESAI ${NC}"

#Buat folder Bot
mkdir -p san/bot

#Ke direktori Bot
cd san/bot

#Ambil file bot dan instal
git clone https://github.com/Paper890/Bot.git

cd
cd san/bot/Bot
pip install -r requirements.txt

#Fungsi jalankan Bot di background
cd
cd /etc/systemd/system/
wget https://raw.githubusercontent.com/Paper890/Bot/main/bot.service
cd
clear
