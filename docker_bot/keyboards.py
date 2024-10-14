from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup


async def get_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="List containers")).add(KeyboardButton(text="Delete container")).add(
        KeyboardButton(text="Restart container"),
    ).add(KeyboardButton(text="Get logs")).add(KeyboardButton(text="Get container")).add(KeyboardButton(text="Stop container"))
    builder.adjust(3, 3)
    return builder.as_markup(one_time_keyboard=True, resize_keyboard=True)
