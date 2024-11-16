from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard(user_post: str):

    if user_post == 'user':
        return  ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Каталог"), KeyboardButton(text="Мои заказы")],
                    [KeyboardButton(text="Написать в поддержку")]
                ],
                resize_keyboard=True
            )
    
    elif user_post == 'admin':
        return  ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Каталог"), KeyboardButton(text="Заявки")],
                    [KeyboardButton(text="Админ панель")]
                ],
                resize_keyboard=True  
        )