# Pi-Py-Flick-right_left
#simple program for gesture control using flick lib

#step 1
#enable i2c and gpio on your raspi-os
#it can be in any os even ubuntu or kali
#if its any thing other than raspbian, be sure to run it as root or give appropriate permissions

#step2
#install pip3 by running "sudo apt install python3-pip"
#install keyboard library "sudo pip3 install keyboard"
#finally install the flicklibrary
#"sudo git clone https://github.com/PiSupply/Flick.git
# sudo cd Flick/flick
# sudo python setup.py install"
 
#step3
#clone this repository into Flick/flick
#git clone https://https://github.com/ZeroAMU/Pi-Py-Flick-right_left.git

#step4
#move leftright.py to Flick/flick
#then if on ubuntu or any non raspbian os run "pip3 install RPi-GPIO"
#run "sudo python3 leftright.py"
#let it be running in the background 

#possible problems

#indentation error
#rectify by replacing space indents with tab indents

#no module found errors
#try installing flicklib keyboard and RPi-GPIO properly

#no access to i2c
#goto config file and find dtparam=i2c.....
#then uncomment it
#then goto etc/module.conf and add i2c-dev

#enjoy :-)
