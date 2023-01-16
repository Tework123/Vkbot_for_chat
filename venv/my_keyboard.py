from vk_api.keyboard import VkKeyboard, VkKeyboardColor


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
def get_keyboard_one():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Погода', color=VkKeyboardColor.PRIMARY)
    return key_board.get_keyboard()


# клавиатура "материалы"
def get_keyboard_two():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Добавить', color=VkKeyboardColor.PRIMARY)  # по сообщению
    key_board.add_button('Получить', color=VkKeyboardColor.PRIMARY)  # хз
    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_openlink_button('Твоя ссылочка на диск',
                                  'https://disk.yandex.ru/client/disk/%D0%9F-48%2C%20%D0%9F-42')  # по сообщению дает клаву

    return key_board.get_keyboard()
