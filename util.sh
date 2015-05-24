#bin/sh
apt-get install python-dev

apt-get install python-setuptools

apt-get install python-rpi.gpi

git clone https://github.com/doceme/py-spidev

cd py-spidev/

python setup.py install

git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git 

apt-get install python-smbus

apt-get install python-serial

usermod -a -G tty pi

usermod -a -G dialout pi

apt-get install arduino

git clone https://github.com/tino/pyFirmata.git

cd pyFirmata

python setup.py install
