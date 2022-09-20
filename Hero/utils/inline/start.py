from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from Hero import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Aᴅᴅ Mᴇ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇs",
                url=f"https://t.me/He_Ro_Bots",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Aᴅᴅ Mᴇ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇs", url="https://t.me/He_Ro_Bots"
            ),
        ],
        [
            InlineKeyboardButton(text="Oᴡɴᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="Sᴜᴩᴩᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"{config.UPSTREAM_REPO}"
                )
        ],
     ]
    return buttons
