import os
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

from ..logger import get_logger





class PURVI(Client):
    def __init__(self):
        LOGGER = get_logger(__name__)
        LOGGER.info("Starting bot...")

        super().__init__(
            name="PURVIMUSIC",
            api_id=int(os.getenv("API_ID")),
            api_hash=os.getenv("API_HASH"),
            bot_token=os.getenv("BOT_TOKEN"),
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=int(os.getenv("LOGGER_ID")),
                text=f"<u><b>» {self.mention} ʙᴏᴛ sᴛᴀʀᴛᴇᴅ :</b></u>\n\nɪᴅ : <code>{self.id}</code>\nɴᴀᴍᴇ : {self.name}\nᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
                parse_mode=ParseMode.HTML,
            )
        except:
            LOGGER(__name__).error(
                "Bot failed to access the log group/channel. Make sure your bot is added to the group."
            )

        a = await self.get_chat_member(int(os.getenv("LOGGER_ID")), self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot to admin in the log group/channel."
            )

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
        
