from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from docker_bot import docker_crud
from docker_bot.keyboards import get_main_keyboard
from docker_bot.main import docker_client
from docker_bot.states import MainStates


async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    # containers = docker_crud.get_containers(docker_client)
    # print(containers)
    keyboard = await get_main_keyboard()
    await message.answer("What do you want to do?", reply_markup=keyboard)
    # await state.set_state(MainStates.)

async def list_containers(message: Message, state: FSMContext) -> None:
    containers = docker_crud.get_containers(docker_client)
    # response = "List of containers:\n" + "\n".join(containers)
    response = "List of containers:\n"
    response += "\n".join([f"{container.name} ({container.short_id})" for container in containers])
    await message.answer(response)
    await start(message, state)


async def enter_id(message: Message, state: FSMContext) -> None:
    await message.answer("Enter container id:")
    await state.set_state(MainStates.get_container)


async def get_container(message: Message, state: FSMContext) -> None:
    container_id = message.text
    try:
        container = docker_crud.get_container(docker_client, container_id)
    except Exception as e:
        await message.answer(f"Error: {e}")
        await start(message, state)
        return
    response = f"Container: {container.name} ({container.short_id})\n"
    response += f"Status: {container.status}"
    await message.answer(response)
    await start(message, state)

async def enter_id_delete(message: Message, state: FSMContext) -> None:
    await message.answer("Enter container id:")
    await state.set_state(MainStates.delete_container)

async def delete_container(message: Message, state: FSMContext) -> None:
    container_id = message.text
    try:
        docker_crud.delete_container(docker_client, container_id)
    except Exception as e:
        await message.answer(f"Error: {e}")
        await start(message, state)
        return
    await message.answer("Container deleted")
    await start(message, state)

async def enter_id_restart(message: Message, state: FSMContext) -> None:
    await message.answer("Enter container id:")
    await state.set_state(MainStates.restart_container)

async def restart_container(message: Message, state: FSMContext) -> None:
    container_id = message.text
    try:
        docker_crud.restart_container(docker_client, container_id)
    except Exception as e:
        await message.answer(f"Error: {e}")
        await start(message, state)
        return
    await message.answer("Container restarted")
    await start(message, state)

async def enter_id_logs(message: Message, state: FSMContext) -> None:
    await message.answer("Enter container id:")
    await state.set_state(MainStates.get_logs)

async def get_logs(message: Message, state: FSMContext) -> None:
    container_id = message.text
    try:
        logs = docker_crud.get_logs(docker_client, container_id)
    except Exception as e:
        await message.answer(f"Error: {e}")
        await start(message, state)
        return
    await message.answer(logs)
    await start(message, state)

async def enter_id_stop(message: Message, state: FSMContext) -> None:
    await message.answer("Enter container id:")
    await state.set_state(MainStates.stop_container)

async def stop_container(message: Message, state: FSMContext) -> None:
    container_id = message.text
    try:
        docker_crud.stop_container(docker_client, container_id)
    except Exception as e:
        await message.answer(f"Error: {e}")
        await start(message, state)
        return
    await message.answer("Container stopped")
    await start(message, state)
