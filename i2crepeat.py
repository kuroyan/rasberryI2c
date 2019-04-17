#!/usr/bin/python3

import smbus
#import time
from time import sleep
i2c = smbus.SMBus(1)
addr = 0x50 # AOC Address
p = 0x0
 
def protectOFF():
    i2c.write_i2c_block_data(addr,0x7b,[0xf0,0xf0,0xf0,0xf0])
 
def page(pg):
    ar=[0]
    ar[0] = pg
    i2c.write_i2c_block_data(addr,0x7f,ar)

def read(adr):
    data = i2c.read_i2c_block_data(addr, adr, 16 )
    for i in data:
        print('{:02x}'.format(i),end=" ")
    print("")

# main#
print( "page4 read enable. start any key" )
print( ">", end="")
key = input()
p=0x4
page(p)
protectOFF()
cnt = 0;
rad = 0x80
while 1:
    for i in range(8):
        try:
            read(rad)
        except KeyboardInterrupt:
            break
        rad += 0x10
    print("")
    cnt += 1;
    print("実行回数=", cnt )
    sleep(1)
    rad = 0x80

GPIO.cleanup()
