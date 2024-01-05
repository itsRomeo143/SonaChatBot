from pyrogram import filters
from pyrogram.types import Message

from SonaChatBot import OWNER, dev
from SonaChatBot.database.chats import get_served_chats
from SonaChatBot.database.users import get_served_users


@dev.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(cli: dev, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""𝘼𝙡𝙡 𝙎𝙩𝙖𝙩𝙨 𝙊𝙛 𝘽𝙤𝙩 {(await cli.get_me()).mention} :

➻ **𝘾𝙝𝙖𝙩𝙨 :** {chats}
➻ **𝙐𝙨𝙚𝙧𝙨 :** {users}"""
    )
