# ID: 145459872
from string import digits


def decode_instructions(encoded: str) -> str:
    """
    Раскодирует сжатые инструкции для марсохода.
    
    Args:
        encoded: Сжатая строка инструкций
        
    Returns:
        Раскодированная строка команд
    """
    DIGITS_SET = set(digits)
    OPEN_BRACKET = '['
    CLOSE_BRACKET = ']'
    
    stack: list[tuple[str, int]] = []
    current_string, current_number = '', ''
    
    for char in encoded:
        if char in DIGITS_SET:
            current_number += char
        elif char == OPEN_BRACKET:
            # Сохраняем текущую строку и число в стек
            stack.append((current_string, int(current_number)))
            current_string, current_number = '', ''
        elif char == CLOSE_BRACKET:
            # Извлекаем из стека предыдущую строку и множитель
            prev_string, multiplier = stack.pop()
            current_string = prev_string + current_string * multiplier
        else:
            # Обычный символ (команда)
            current_string += char
    
    return current_string


if __name__ == '__main__':
    print(decode_instructions(input().strip()))
