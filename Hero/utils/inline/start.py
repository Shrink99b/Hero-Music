from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Hero import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/saikostar_xd"),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/friends_masti_club_fmc"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/THE_DRAGON_NETWORK_OFFICIAL"),
            InlineKeyboardButton(
                text="sᴜᴩᴩᴏʀᴛ", url=f"https://t.me/friends_masti_club_fmc"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="ᴏᴡɴᴇʀ", url=f"https://t.me/saikostar_xd"
                )
        ],
     ]
    return buttons
