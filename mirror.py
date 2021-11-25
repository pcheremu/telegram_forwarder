# file: mirror.py
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import events
from telethon.tl.types import PeerChat, PeerChannel

from config import (API_ID, API_HASH, SESSION_STRING,
                    SOURCE_CHANNEL, TARGET_CHANNEL)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


@client.on(events.NewMessage(chats=[SOURCE_CHANNEL]))
async def handler_new_message(event):
    # print(event.message)
    try:
        # отправим сообщение в наш канал
        await client.send_message(TARGET_CHANNEL, event.message)
        # либо вместо переотправки можно репостнуть:
        #await client.forward_messages(TARGET_CHANNEL, event.message)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()