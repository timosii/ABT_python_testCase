import sys
import json
import argparse


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count = 0
    for el in data["game"]["rounds"]:
        count += len(el["questions"])

    print(count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    for el in data["game"]["rounds"]:
        for i in el["questions"]:
            correct_answers.append(i["correct_answer"])

    print(correct_answers)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    max_time = 0
    for el in data["game"]["rounds"]:
        if el["type"] == "classical":
            for i in el["questions"]:
                max_time = i["time_to_answer"] if i["time_to_answer"] > max_time else max_time
    
    print(max_time)


def main(filename):
    with open(filename) as f:
        data = json.load(f)  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    parser = argparse.ArgumentParser(description="Take filename")
    parser.add_argument('filename', type=str, help="filename for analysis")
    filename = parser.parse_args().filename
    # filename = "test.json"
    main(filename)
