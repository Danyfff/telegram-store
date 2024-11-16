from aiogram import Router
from aiogram.types import Message 
from aiogram.filters import Command
from database.db_creater import db
from keyboards import reply

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):

    user_id = int(message.from_user.id)
    user_post = db.get_user_post(user_id)

    if not db.get_user(user_id):
        db.create_user(user_id)
        
    await message.answer(
        f"Привет, {message.from_user.first_name}", 
        reply_markup=reply.main_keyboard(user_post)
    )