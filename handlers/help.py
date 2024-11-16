from aiogram import Router, F
from aiogram.types import Message 

router = Router()

@router.message(F.text == 'Написать в поддержку')
async def cmd_start(message: Message):
    await message.answer("Поддержка вас приветствует")