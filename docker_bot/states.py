from aiogram.fsm.state import State, StatesGroup


class MainStates(StatesGroup):
    main = State()
    get_logs = State()
    get_container = State()
    delete_container = State()
    restart_container = State()
    stop_container = State()
