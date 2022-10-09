from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="ᴩᴀᴜsᴇ ⏸",
            description=f"ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ʀᴇsᴜᴍᴇ ▶️",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="sᴋɪᴩ ⏯️",
            description=f"sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ ᴍᴏᴠᴇs ᴛᴏ ᴛʜᴇ ɴᴇxᴛ sᴛʀᴇᴀᴍ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ᴇɴᴅ ⏺",
            description="ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="sʜᴜғғʟᴇ 🔁",
            description="sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ sᴏɴɢs ɪɴ ᴩʟᴀʏʟɪsᴛ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ʟᴏᴏᴩ 🔂",
            description="ʟᴏᴏᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://te.legra.ph/file/336acd415a964479f5f37.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
