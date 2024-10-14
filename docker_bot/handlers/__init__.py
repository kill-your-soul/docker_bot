from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter

from docker_bot.states import MainStates

from . import main


def setup_handlers() -> Router:
    router = Router()
    router.message.register(main.start, CommandStart())
    router.message.register(main.list_containers, F.text == "List containers")
    router.message.register(main.enter_id, F.text == "Get container")
    router.message.register(main.get_container, MainStates.get_container)
    router.message.register(main.enter_id_delete, F.text == "Delete container")
    router.message.register(main.delete_container, MainStates.delete_container)
    router.message.register(main.enter_id_restart, F.text == "Restart container")
    router.message.register(main.restart_container, MainStates.restart_container)
    router.message.register(main.enter_id_logs, F.text == "Get logs")
    router.message.register(main.get_logs, MainStates.get_logs)
    router.message.register(main.enter_id_stop, F.text == "Stop container")
    router.message.register(main.stop_container, MainStates.stop_container)
    return router
