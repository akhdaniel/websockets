#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets
import simplejson

async def time(websocket, path):
    while True:
        now = datetime.datetime.now().timestamp() 
        value = random.randrange(50,150)
        data = [
    		now,    
    		value,       
		]
        await websocket.send(simplejson.dumps(data))
        print(data)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

