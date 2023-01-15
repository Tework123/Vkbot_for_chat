from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_my_keyboard():
    key_board = VkKeyboard(inline=False)

    key_board.add_button('1 вариант', color=VkKeyboardColor.SECONDARY)
    key_board.add_button('2 вариант', color=VkKeyboardColor.SECONDARY)
    key_board.add_button('3 вариант', color=VkKeyboardColor.SECONDARY)
    return key_board.get_keyboard()