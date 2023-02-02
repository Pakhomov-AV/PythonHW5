# Задание 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import Func_read_files as rf
import random

import Func_writing_file as wf


def cleared(comprssed_file, recovered_file):
    if input('Для очистки рабочих файлов введите 0.\n'
             'Для сохранения - другое число: ') == '0':
        cleared_data = ''
        cleared_file = comprssed_file
        wf.writing_file(cleared_data, cleared_file)
        cleared_file = recovered_file
        wf.writing_file(cleared_data, recovered_file)


def data_flow_generator(user_file: str):
    number_characters = random.randint(5, 20)
    simbol_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data_flow = ''
    for i in range(number_characters):
        simbol_flow = random.choice(simbol_str)
        number_repetitions = random.randint(1, 50)
        for j in range(number_repetitions):
            data_flow += simbol_flow
    import Func_writing_file as wf
    wf.writing_file(data_flow, user_file)
    return data_flow


def rle_encoding(data):
    encode_rle = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encode_rle += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encode_rle += str(count) + prev_char
    return encode_rle


def rle_decoding(data):
    decode_rle = ''
    count = ''
    for char in data:
        if char in data:
            if char.isdigit():
                count += char
            else:
                decode_rle += char * int(count)
                count = ''
    return decode_rle


work_file = 'files/f_data5_4_source.txt'
comprssed_file = 'files/f_data5_4_compressed.txt'
recovered_file = 'files/f_data5_4_recovered.txt'
cleared(comprssed_file, recovered_file)

way = input('Если Вы хотите сгенерировать новый поток данных, введите 1,\n'
            'если нет - введите любое другое число: ')
if way == '1':
    data_flow_generator(work_file)

incoming_stream = rf.read_file(work_file)

compressed_data = rle_encoding(incoming_stream)

wf.writing_file(compressed_data, comprssed_file)

restored_data = rle_decoding(compressed_data)

wf.writing_file(restored_data, recovered_file)

cleared(comprssed_file, recovered_file)
