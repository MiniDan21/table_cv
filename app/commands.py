import shutil
from pathlib import Path

from .files_utils import *
from process import run
from config import config, Config


def control_pictures():
    if not check_files(files_path=config.IMAGES_DIR):
        download_unpack(config.LINK_IMAGES_ZIP, path=Path(config.IMAGES_DIR))
        # Если установится, то распределить файлы по папкам
        for filename_obj in path_array(config.IMAGES_DIR):
            choose_and_move(filename_obj, Path(config.VIDEOS_DIR), 
                            Path(config.IMAGES_DIR), Path(config.OTHER_DIR))
            
    results = run(image_files=path_array(config.IMAGES_DIR, string=True))
    for result in results:
        filename = str(Path(result.image_name).name)
        result.update_special_matrix_index()
        fill_xlsx_file(matrix=result.special_matrix, file_name=filename.split(".")[0] + ".xlsx")

    return "Завершение подпрограммы..."

    
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
            result = run(video_file=file_path)
        elif file_type == "image":
            result = run(image_file=file_path)
        result.update_special_matrix_index()
        fill_xlsx_file(result.special_matrix, file_name=filename.split(".")[0] + ".xlsx")

    else:
        return "Файл не найден в папках videos или images.\nПопробуйте установить специальной командой"
    
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
    
    return "Файл закрыт."


commands = {
    "1. Проверить на контрольных изображениях": control_pictures,
    "2. Указать путь к файлу для одиночной проверки": open_file,
    "3. Указать id ZIP-файла на Google Drive для скачивания": input_google_link,
    "4. Прочитать README": readme,
}