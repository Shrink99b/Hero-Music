import asyncio
import os
import shutil
from datetime import datetime
import requests
import urllib3
from pyrogram import filters
import config
from strings import get_command
from Hero import app
from Hero.misc import SUDOERS
from Hero.utils.database import (get_active_chats,
                                       remove_active_chat,
                                       remove_active_video_chat)

# Commands

REBOOT_COMMAND = get_command("REBOOT_COMMAND")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@app.on_message(filters.command(REBOOT_COMMAND) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    served_chats = await get_active_chats()
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f"{config.MUSIC_BOT_NAME} ʜᴀs ᴊᴜsᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ʜᴇʀsᴇʟғ ғᴏʀ ᴜᴩᴅᴀᴛɪɴɢ ᴛʜᴇ ʙᴏᴛ. sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪssᴜᴇs.\n\nʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 15-20 sᴇᴄᴏɴᴅs.",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except Exception:
            pass
    A = "downloads"
    B = "raw_files"
    C = "cache"
    try:
        shutil.rmtree(A)
        shutil.rmtree(B)
        shutil.rmtree(C)
    except:
        pass
    await response.edit(
        "ʀᴇsᴛᴀʀᴛ ᴩʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs."
    )
    os.system(f"kill -9 {os.getpid()} && bash start")
