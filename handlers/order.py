from aiogram import Router, F
from aiogram.types import Message 

router = Router()

@router.message(F.text == 'Заявки')
async def cmd_start(message: Message):
    await message.answer("Выводятся заявки")

@router.message(F.text == 'Мои заказы')
async def cmd_start(message: Message):
    await message.answer("Ваши заказы")