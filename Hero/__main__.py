import asyncio
import importlib
import sys
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from config import BANNED_USERS
from Hero import LOGGER, app, userbot
from Hero.core.call import Veer
from Hero.plugins import ALL_MODULES
from Hero.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Hero").error(
            "Atleast add a pyrogram string"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Hero").warning(
            "Spotify Client Id & Secret not added"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Hero.plugins" + all_module)
    LOGGER("Hero.plugins").info(
        "Modules Imported Successfully"
    )
    await userbot.start()
    await Veer.start()
    try:
        await Veer.stream_call(
            "https://telegra.ph/file/8d5db123638c2f6bb6ce4.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Hero").error(
            "[ERROR] - \n\nFirstly open telegram and turn on voice chat in Logger Group"
        )
        sys.exit()
    except:
        pass
    await Veer.decorators()
    LOGGER("Hero").info("Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Hero").info("Stopping Music Bot")
