import os

try:
    from telethon.sessions import StringSession
    from telethon.sessions.string import StringSession
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sessions.string import StringSession
    from telethon.sync import TelegramClient


def generate_telethon_session():
    print("\nTelethon Session generator!\n")

    APP_ID = int(input("\nEnter API ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    os.system("CLS||clear")

    with TelegramClient(StringSession(), APP_ID, API_HASH) as StarkBots:
        print("\nSession sent in saved messages.")
        StarkBots.send_message("me", f"🔴 Don't share with anyone 🔴\n\n`{StarkBots.session.save()}`\n\n💁‍♂️ Join @SingleDevelopers✌️",)

generate_telethon_session()
