import json

__data = []


def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    :param path: json file
    :return: Список кандидатов
    """
    global __data
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id: ID
    :return: Кандидат
    """
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }
    return {'not_found': 'Кандидата с таким ID не найдено'}


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    :param candidate_name: Имя
    :return: Кандидаты
    """
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    :param skill_name: Навый
    :return: Кандидаты
    """
    pass