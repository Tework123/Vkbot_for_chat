from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import wiki_parcer


# модуль генерации клавиатур

# клавиатура "начальная"

def get_keyboard_start_chat():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Отправить мем', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Получить расписание', color=VkKeyboardColor.PRIMARY)
    # сначала я должен загрузить это расписание

    return key_board.get_keyboard()


def get_keyboard_start_user():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('Получить расписание', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Получить материалы', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_button('Разное', color=VkKeyboardColor.PRIMARY)
    key_board.add_openlink_button('Твоя ссылочка на диск',
                                  'https://disk.yandex.ru/client/disk/%D0%9F-48%2C%20%D0%9F-42')

    return key_board.get_keyboard()

#клавиатура "получить материалы"
def get_keyboard_materials():
    key_board = VkKeyboard(inline=False)
    key_board.add_button('Староверов', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Менеджмент', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Материаловедение', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_button('Дубровский, Сучков', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Экология', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)

    return key_board.get_keyboard()

#клавиатура "выбор времени"
def get_keyboard_time():
    key_board = VkKeyboard(inline=False)
    key_board.add_button('за 2 недели', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('за 1 месяц', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('за 3 месяца', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_button('за 6 месяцев', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('за 1 год', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Назад.', color=VkKeyboardColor.PRIMARY)

    return key_board.get_keyboard()

# клавиатура "разное"
def get_keyboard_other():
    key_board = VkKeyboard(inline=False)
    key_board.add_button('Отправить мем', color=VkKeyboardColor.PRIMARY)
    key_board.add_button('Погода', color=VkKeyboardColor.PRIMARY)
    key_board.add_line()
    key_board.add_openlink_button('Случайная статья с википедии', wiki_parcer.wiki_parcer())
    key_board.add_button('Назад', color=VkKeyboardColor.PRIMARY)

    return key_board.get_keyboard()



