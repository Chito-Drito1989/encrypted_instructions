# ID: 145327026
def decode_instructions(encoded: str) -> str:
    """
    Раскодирует сжатые инструкции для марсохода.
    
    Args:
        encoded: Сжатая строка инструкций
        
    Returns:
        Раскодированная строка команд
    """
    stack: list = []
    current_string: str = ''
    current_number: str = ''
    
    for char in encoded:
        if char.isdigit():
            current_number += char
        elif char == '[':
            # Сохраняем текущую строку и число в стек
            stack.append((current_string, int(current_number) if current_number else 1))
            current_string = ''
            current_number = ''
        elif char == ']':
            # Извлекаем из стека предыдущую строку и множитель
            prev_string, multiplier = stack.pop()
            current_string = prev_string + current_string * multiplier
        else:
            # Обычный символ (команда)
            current_string += char
    
    return current_string


def main() -> None:
    """Основная функция для ввода и вывода данных."""
    try:
        encoded_instruction = input().strip()
        result = decode_instructions(encoded_instruction)
        print(result)
    except Exception as e:
        print(f'Ошибка при обработке входных данных: {e}')


if __name__ == '__main__':
    main()
