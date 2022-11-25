import asyncio
import socketio

sioconm = socketio.AsyncClient()
sbtoken = input('Token > ')

async def send_message(message, type = 'shout'): 
    await sioconm.emit('message-send', {'text': message, 'type': type})
    # what ever you wanna do types are "quote, shout, and system"

@sioconm.event
async def connect():
    print('Connceted to shoutbox')
    await send_message('Hello World!', 'system') # example of sending a message (message text, message type)

@sioconm.on("message-receive")
async def on_message_receive(message): print(message.get('user').get('username'), message.get('text'))

@sioconm.event
async def disconnect(): print('Disconnected from shoutbox')

async def main():
    try:
        await sioconm.connect('wss://c.breached.vc/socket.io/?token=%s' % sbtoken)
        await sioconm.wait()
    except Exception as e: exit(e)

if __name__ == '__main__': asyncio.run(main())
