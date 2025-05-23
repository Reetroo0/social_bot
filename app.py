import asyncio
from config import bot, dp ,logger
from misc.pgSQL import pgConnect
from misc.keyboards import main_menu
from handlers import start, survey, UnCompSurvey, profile


async def main():
    # Подключение хендлеров
    dp.include_routers(start.router)
    dp.include_routers(survey.router)
    dp.include_routers(UnCompSurvey.router)
    dp.include_routers(profile.router)
    
    # Подключение к БД
    pgConnect()

    # Уведомление запуске бота
    await bot.send_message(chat_id=618425933, text='Бот запущен', reply_markup=main_menu)

    # Запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logger.info("Бот запущен")
    asyncio.run(main())