import asyncio
from core.bot import PURVI

bot = PURVI()

async def init():
    await bot.start()
    print("Bot started. Press Ctrl+C to stop.")
    await asyncio.Event().wait()  # Keeps the bot running

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
  
