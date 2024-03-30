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
read -p "Enter your bot token: " BOT_TOKEN

export BOT_TOKEN=$BOT_TOKEN

echo -e "${green}UPDATE PACKAGE VPS${NC}"
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
wget https://raw.githubusercontent.com/Paper890/Bot/main/authorized_users.txt
#Fungsi jalankan Bot di background
echo "[Unit]
Description=Bot Service
After=network.target
[Service]
User=root
WorkingDirectory=/root/san/bot/Bot
ExecStart=/usr/bin/python3 main.py
Restart=always
[Install]
WantedBy=multi-user.target" >> /etc/systemd/system/bot.service

sudo systemctl daemon-reload
sudo systemctl start bot
sudo systemctl enable bot
