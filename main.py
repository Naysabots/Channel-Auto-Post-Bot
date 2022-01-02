import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

# filters for auto post
FILTER_TEXT = bool(os.environ.get("FILTER_TEXT", True))
FILTER_AUDIO = bool(os.environ.get("FILTER_AUDIO", True))
FILTER_DOCUMENT = bool(os.environ.get("FILTER_DOCUMENT", True))
FILTER_PHOTO = bool(os.environ.get("FILTER_PHOTO", True))
FILTER_STICKER = bool(os.environ.get("FILTER_STICKER", True))
FILTER_VIDEO = bool(os.environ.get("FILTER_VIDEO", True))
FILTER_ANIMATION = bool(os.environ.get("FILTER_ANIMATION", True))
FILTER_VOICE = bool(os.environ.get("FILTER_VOICE", True))
FILTER_VIDEO_NOTE = bool(os.environ.get("FILTER_VIDEO_NOTE", True))
FILTER_CONTACT = bool(os.environ.get("FILTER_CONTACT", True))
FILTER_LOCATION = bool(os.environ.get("FILTER_LOCATION", True))
FILTER_VENUE = bool(os.environ.get("FILTER_VENUE", True))
FILTER_POLL = bool(os.environ.get("FILTER_POLL", True))
FILTER_GAME = bool(os.environ.get("FILTER_GAME", True))

# for copy buttons
REPLY_MARKUP = bool(os.environ.get("REPLY_MARKUP", False))

Bot = Client(
    "Channel Auto Post Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """Hello {}, I am a channel auto post telegram bot.

Made by @FayasNoushad"""
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
            InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
        ],
        [
            InlineKeyboardButton('Source Code', url='https://github.com/FayasNoushad/Channel-Auto-Post-Bot')
        ]
    ]
)


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )


@Bot.on_message(
    filters.channel & filters.command(run) (
        filters.text if FILTER_TEXT else None |
        filters.audio if FILTER_AUDIO else None |
        filters.document if FILTER_DOCUMENT else None |
        filters.photo if FILTER_PHOTO else None |
        filters.sticker if FILTER_STICKER else None |
        filters.video if FILTER_VIDEO else None |
        filters.animation if FILTER_ANIMATION else None |
        filters.voice if FILTER_VOICE else None |
        filters.video_note if FILTER_VIDEO_NOTE else None |
        filters.contact if FILTER_CONTACT else None |
        filters.location if FILTER_LOCATION else None |
        filters.venue if FILTER_VENUE else None |
        filters.poll if FILTER_POLL else None |
        filters.game if FILTER_GAME else None
    )
)
async def Autopost(bot, message):
    fromid = await bot.ask(message.chat.id, Translation.FROM_MSG)
    if fromid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    elif not fromid.text.startswith('@'):
        return await message.reply(Translation.USERNAME)
    toid = await bot.ask(message.chat.id, Translation.TO_MSG)
    if toid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    skipno = await bot.ask(message.chat.id, Translation.SKIP_MSG)
    if skipno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    limitno = await bot.ask(message.chat.id, Translation.LIMIT_MSG)
    if limitno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    await message.reply_text(
        text=Translation.DOUBLE_CHECK.format(fromid.text),
        reply_markup=reply_markup
    )
    SKIP = skipno.text
    FROM = fromid.text
    TO = toid.text
    LIMIT = limitno.text
    if re.match('-100\d+', TO):
        TO = int(TO)



Bot.run()
