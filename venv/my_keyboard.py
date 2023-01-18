from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import wiki_parcer
import pathlib
from pathlib import Path


# модуль генерации клавиатур

# клавиатура "начальная"
def get_keyboard_start():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Отправить мем', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Разное', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_button('Получить расписание', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Материалы', color=VkKeyboardColor.PRIMARY)
    # сначала я должен загрузить это расписание

    return key_board.get_keyboard()


# клавиатура "разное"
def get_keyboard_other():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Погода', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Погода', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_openlink_button('Случайная статья с википедии', wiki_parcer.wiki_parcer())

    return key_board.get_keyboard()


# клавиатура "материалы"
def get_keyboard_attach():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Добавить метку', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Получить', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_openlink_button('Твоя ссылочка на диск',
                                  'https://disk.yandex.ru/client/disk/%D0%9F-48%2C%20%D0%9F-42')

    return key_board.get_keyboard()


def get_keyboard_put():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Козловский', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Староверов', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_button('Диплом', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)

    return key_board.get_keyboard()
