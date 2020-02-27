# Pi-Py-Flick-right_left
Simple program for gesture control using flick lib
# Hardware used
All programs have been tested on a Raspberry Pi 4b - 4gb
For etching the OS use BalenaEtcher

Requirements :-
1> Raspberry pi 3/4
2> Class 10 SDCARD with an Operating system (Preferably Raspbian or Ubuntu) 
3> Flick HAT or Large (Preferably HAT)
4> Raspberry Pi Case (optional)
5> HDMI to HDMI cable (Raspberry Pi 3)
6> HDMI to Micro-HDMI cabe (Raspberry Pi 4)
7> Power Supply (mirco-usb for Rpi3 and type-c for Rpi4) (The official one is recommended)
8>A Keyboard and Mouse (wired or wireless)
# Step1
Enable i2c and gpio on your raspi-os (it can be in any os even ubuntu or kali)
If the os is anything other than raspbian, be sure to run it as root or give appropriate permissions
# Step2
Install pip3 by running "sudo apt install python3-pip"
Install keyboard library "sudo pip3 install keyboard"
Finally install the flicklibrary with :-
sudo git clone https://github.com/PiSupply/Flick.git 
sudo cd Flick/flick 
sudo python setup.py install 
# Step3
Clone this repository into Flick/flick
git clone https://https://github.com/ZeroAMU/Pi-Py-Flick-right_left.git
# Step4
Move leftright.py and keyboard.py to Flick/flick
Then, if on ubuntu or any non raspbian os run the following code:-
pip3 install RPi-GPIO
# Step5
Run this code
sudo python3 leftright.py
Let it be running in the background 

# Possible problems

Indentation error :-
Rectify this by replacing space indents with tab indents

No module found errors:-
Try installing flicklib keyboard and RPi-GPIO properly

No access to i2c :-
Go to the config file and find dtparam=i2c..... and uncomment it.
Then goto etc/module.conf and add i2c-dev

#                                                            Thank you
