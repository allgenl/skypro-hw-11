import json
from main import path


def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    :param path: json file
    :return: Список кандидатов
    """
    with open(path, "r", encoding="utf-8") as file:
        all_candidates = json.load(file)
    return all_candidates


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id: ID
    :return: Кандидат
    """
    all_candidates = load_candidates_from_json("candidates.json")
    return all_candidates[candidate_id - 1]["name"]


def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    :param candidate_name: Имя
    :return: Кандидаты
    """
    pass


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    :param skill_name: Навый
    :return: Кандидаты
    """
    pass