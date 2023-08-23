from start_bot import bot, dp
import logging
import asyncio

import handlers

handlers.register_handlers(dp)

logging.basicConfig(level=logging.INFO)
async def main():

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())