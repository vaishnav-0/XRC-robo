import sys
import cv2
import os
from stream import RealsenseStream
import numpy as np
import json
from transport import Transport
import asyncio  
from queue import Queue
from threading import Thread
  
# Object that signals shutdown
_sentinel = object()


sockets = []

q = Queue()

def stream_to_clients(queue):
    while 1:
        data = queue.get()
        # print(data if data else "No data")
        for ws in sockets:
            asyncio.run(ws.send(data))
        if data is _sentinel:
            q.put(_sentinel)
            break

if __name__ == "__main__":
    print("SUBPROCESS_READY")
    stream = RealsenseStream()
    try:
        stream_t = Thread(target = stream.start_stream, args =(q,), daemon=True)
        Thread(target = stream_to_clients, args =(q,)).start()
        stream_t.start()
        Transport(sys.argv[1], lambda ws:sockets.append(ws))
        
    except Exception as er:
            print(er)
    finally:
        stream.stop_stream()
