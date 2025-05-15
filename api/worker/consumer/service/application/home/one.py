import json
from api.worker.config.worker import HOME_FILES


def one_application_home_service(lang: str):
    try:
        file_path = HOME_FILES / f'home_{lang}.json'
        with open(file_path, 'r', encoding='utf-8') as open_file:
            result = json.load(open_file)

        return result
    except Exception as e:
        print(e)
        pass
