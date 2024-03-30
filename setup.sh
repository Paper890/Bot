#!/bin/bash


echo -e "      ...                                        ...     ..                       s    "
echo -e "   .x888888hx    :                             .=*8888x <"?88h.                   :8    "
echo -e "  d88888888888hxx                 u.    u.    X>  '8888H> '8888          u.      .88    "
echo -e " 8" ... `"*8888%`        u      x@88k u@88c. '88h. `8888   8888    ...ue888b    :888ooo "
echo -e "!  "   ` .xnxx.       us888u.  ^"8888""8888" '8888 '8888    "88>   888R Y888r -*8888888 "
echo -e "X X   .H8888888%:  .@88 "8888"   8888  888R   `888 '8888.xH888x.   888R I888>   8888    "
echo -e "X 'hn8888888*"   > 9888  9888    8888  888R     X" :88*~  `*8888>  888R I888>   8888    "
echo -e "X: `*88888%`     ! 9888  9888    8888  888R   ~"   !"`      "888>  888R I888>   8888    "
echo -e "'8h.. ``     ..x8> 9888  9888    8888  888R    .H8888h.      ?88  u8888cJ888   .8888Lu= "
echo -e " `88888888888888f  9888  9888   "*88*" 8888"  :"^"88888h.    '!    "*888*P"    ^%888*   "
echo -e "  '%8888888888*"   "888*""888"    ""   'Y"    ^    "88888hx.+"       'Y"         'Y"    "
echo -e "     ^"****""`      ^Y"   ^Y'                        ^"**""                             
                                                                                                                                                           
                                                                                     
sudo apt update -y
sudo apt upgrade -y
sudo apt install python3 python3-pip
pip3 install python-telegram-bot
#pip3 install python-telegram-bot==12.0.0 // Install jika python3 eror
sudo apt install git -y

#Buat folder Bot
mkdir -p san/bot

#Ke direktori Bot
cd san/bot

#Ambil file bot dan instal
git clone https://github.com/Paper890/Bot.git
pip install -r requirements.txt
