import shutil
from pathlib import Path

from .files_utils import *
from process import process_frame
from config import Config


config = Config()


def control_pictures():
    if not check_files(files_path=config.IMAGES_DIR):
        download_unpack(config.LINK_IMAGES_ZIP, path=Path(config.IMAGES_DIR))

        # Если установится, то распределить файлы по папкам
        try:
            for filename_obj in path_array(config.IMAGES_DIR):
                choose_and_move(filename_obj, Path(config.VIDEOS_DIR), 
                                Path(config.IMAGES_DIR), Path(config.OTHER_DIR))
        except Exception as e:
            print(e)
    result = process_frame(image_files=path_array(config.IMAGES_DIR, string=True))
    return result

    
def open_file():
    filename = input("Укажите имя файла, который надо открыть\n>")
    filename_obj = Path(filename)
    file_path = None
    file_type = check_type(filename_obj)
    if file_type == "video":
        file_path = str(Path(config.VIDEOS_DIR, filename_obj))
    elif file_type == "image":
        file_path = str(Path(config.IMAGES_DIR, filename_obj))

    result = None
    if check_files(file_path=file_path):
        file_type = check_type(file_path)
        if file_type == "video":
            result = process_frame(video_file=file_path)
        elif file_type == "image":
            result = process_frame(image_file=file_path)
    else:
        return "Файл не найден в папках videos или images.\nПопробуйте установить специальной командой"
        
    if result:
        return result
    
    return "Завершение подпрограммы..."


def input_google_link():
    temp_dir = Path("Temp")
    id = input("Укажите id ZIP-файла на Google Drive\n>")
    download_unpack(config.GOOGLE_DRIVE_LINK.format(id), temp_dir)
    check_temp(temp_dir)
    for filename_obj in path_array(temp_dir):
        choose_and_move(filename_obj, Path(config.VIDEOS_DIR), 
                        Path(config.IMAGES_DIR), Path(config.OTHER_DIR))

    delete_file(temp_dir)
    return "Загрузка завершена."


def readme():
    with open(config.README_PATH, "r", encoding="utf-8") as file:
        print(file.read())


commands = {
    "1. Проверить на контрольных изображениях": control_pictures,
    "2. Указать путь к файлу для одиночной проверки": open_file,
    "3. Указать id ZIP-файла на Google Drive для скачивания": input_google_link,
    "4. Прочитать README": readme,
}