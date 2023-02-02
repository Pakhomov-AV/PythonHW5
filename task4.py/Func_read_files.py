# Функция для чтения файла

def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as flow:
        result = flow.read()
        return result
