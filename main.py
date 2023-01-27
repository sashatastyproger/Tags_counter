from bs4 import BeautifulSoup
import requests


"""Функция парсит страницу. Записывает HTML-код в файл. Затем читает из этого файла
код и построчно заносит в список (не спрашивайте зачем это). Далее по логике, если строка
начинается с символа '<' - то это является тегом. Так подсчитывает их количество"""
def tags_counter(url: str) -> int:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    with open('text.txt', 'w') as file:
        file.write(soup.prettify())

    with open('text.txt', 'r') as file:
        page = file.readlines()

    global tags
    tags = []
    count_tags = 0
    for p in page:
        if p.strip().startswith('<'):
            tags.append(p.strip())
            count_tags += 1

    return count_tags


"""Тут считаем теги у которых есть атрибуты. Передаем сюда список тегов из функции выше.
Проверяем, если есть символ '=' - значит атрибут в теге имеется. Так же считаем все счетчиком"""
def tags_with_attrs(tags: list) -> int:
    count_tag_attrs = 0
    for tag in tags:
        if '=' in tag:
            count_tag_attrs += 1
    return count_tag_attrs


if __name__ == '__main__':
    url = input('На каком сайте посчитать теги? ->>> ')
    print(f'Страница имеет HTML-тегов ->>> {tags_counter(url)}')
    print(f'Из них HTML-теги с атрибутами ->>> {tags_with_attrs(tags)}')








