import asyncio

import handlers
from aiogram import Bot, Dispatcher
from core.config import settings
from docker import DockerClient

from docker_bot import docker_crud

docker_client = DockerClient(base_url=settings.DOCKER_SOCKET_URL)

def setup_handlers(dp: Dispatcher) -> None:
    dp.include_router(handlers.setup_handlers())

async def main() -> None:
    print("Starting bot...")
    bot = Bot(settings.TOKEN)
    dp = Dispatcher()
    setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    # print("Starting main...")
    asyncio.run(main())
