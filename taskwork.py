import sys
import time
import zmq
from libreria import *

context = zmq.Context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# send message

sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")
JsonRe = ""
while True:
    s = receiver.recv()
    print s
    JsonRe += s
    file = open("recivir.txt","w")
    file.write(JsonRe)
    file.close()

    time.sleep(int (10)*0.001)

    sender.send("")
    
