# Функция для записи текстового файла

def writing_file(user_string: str, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as flow:
        flow.writelines(user_string)
