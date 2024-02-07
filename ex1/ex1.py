import  argparse
from collections import namedtuple
import  os
import logging
import json

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='log/ex15_1.log', filemode='a', format=FORMAT, encoding='utf-8', style='{', level=logging.INFO)
logger = logging.getLogger('main')

parser = argparse.ArgumentParser(description="argument parser")
parser.add_argument('-p', metavar='path', type= str or None , nargs='*', default=None, help='Укажите путь к директории или файлу')
args = parser.parse_args()


def split_path(lst_path: str):
    fs_objects = []
    if lst_path is None:
        path_string = os.getcwd()
        logger.warning(f'Пустой ввод.Путь установлен по умолчанию {path_string}')
        abs_path, full_name = os.path.split(path_string)
        abs_parent, parent = os.path.split(abs_path)
        name = full_name
        expansion = False
        flag = True
    else:
        path_string = lst_path[0]
        '''
        Родительский каталог определяется на один уровень вверх.
        При необходимости укзать абсолютный путь до файла/каталога вместо parent берем abs_path
        '''
        abs_path, full_name = os.path.split(path_string)
        abs_parent, parent = os.path.split(abs_path)
        if '.' in full_name:
            name, expansion = full_name.split('.')
            flag = False
            logger.info(f'Выбран файл {full_name}.Абсолютный путь к файлу {abs_path}')
        else:
            name = full_name
            expansion = False
            flag = True
            logger.info(f'Выбран каталог {full_name}. Абсолютный путь к каталогу {abs_path}.')

    Obj_info = namedtuple('Obj_info', 'name expansion catalog home', defaults=['', '', False, ''])
    fs_objects.append(Obj_info(name=name, expansion=expansion, catalog=flag, home=parent))
    logger.info(f'Записаны данные {fs_objects}')  # Запись данных в логи
    with open('base.json', 'a') as file:  # Запись данных в файл
        json.dump(fs_objects, file)
        file.write('\n')
    return fs_objects

if __name__ == '__main__':
    print(split_path(args.p))

# pyton .\ex15_1.py -p C:\Work\PyCharm\PytoProject\venv\hw.exe