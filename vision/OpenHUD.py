import asyncio
import vision.handy as handy
import vision.vision as vision
import websockets

buffer = handy.buffer

async def handler(websocket):
    print("server loaded")
    while True:
        if buffer.click !=0:
            await websocket.send(buffer.click)
            buffer.click=0

        if buffer.stream !=0:
            await websocket.send(buffer.stream)
            buffer.stream=0
            print("send")

        if buffer.labels !=0:
            await websocket.send(buffer.labels)
            buffer.labels=0
            print("send")
        msg = await websocket.recv()    
        print(msg)
  
async def main():    
    async with websockets.serve(handler, "localhost", 8989):
        await asyncio.Future()  # run forever
    

if __name__ == "__main__":

    asyncio.run(main())