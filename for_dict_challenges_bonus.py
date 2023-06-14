"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history() -> list:
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def content_maker(messages: list[dict]) -> str:
    # Создаем список сообщений с ID отправителя
    writer: list = [message['sent_by'] for message in messages if message['sent_by']]
    # Находим максимальную частоту вхождений
    max_writer: int = max(writer, key=writer.count)
    # Создаем список сообщений с максимальной частотой вхождений, удаляем дубликаты
    ids_max_writers: set = set([i for i in writer if writer.count(i) == writer.count(max_writer)])
    # Приводим полученный set к строке
    res: str = ', '.join(map(str, ids_max_writers))
    return f'User ID, который написал больше всех сообщений - {res}.'


def reply_maker(messages: list[dict]) -> str:
    # Создаем список с ID на которые отвечали
    reply_ids: list = [message['sent_by'] for message in messages if message['reply_for']]
    # Находим максимальную частоту вхождения
    max_replied: int = max(reply_ids, key=reply_ids.count)
    # Находим количество сообщений с максимальной частотой вхождений
    count_max_replied: int = reply_ids.count(max_replied)
    # Создаем список сообщений с максимальной частотой вхождений, удаляем дубликаты
    res: set = set([i for i in reply_ids if reply_ids.count(i) == count_max_replied])
    # Приводим полученный set к строке
    replied: str = ', '.join(map(str, res))
    return f'User ID, на сообщения которого больше всего отвечали - {replied}.'


def influencer(messages: list[dict]) -> str:
    # Создаем список с ID, которые были просмотрены
    users_seen: list = [message['sent_by'] for message in messages if message['seen_by']]
    # Находим максимальную частоту вхождения
    max_seen: int = max(users_seen, key=users_seen.count)
    # Находим количество сообщений с максимальной частотой вхождений
    count_max_seen: int = users_seen.count(max_seen)
    # Создаем список сообщений с максимальной частотой вхождений, удаляем дубликаты
    res: set = set([i for i in users_seen if users_seen.count(i) == count_max_seen])
    # Приводим полученный set к строке
    ids_seen_max: str = ', '.join(map(str, res))
    return f'User ID, сообщения которых видело больше всего уникальных пользователей - {ids_seen_max}.'


def when_they_chat(messages: list[dict]) -> str:
    # Создаем словарь-счетчик
    msg_count: dict = {
        'утром': 0,
        'днем': 0,
        'вечером': 0,
        }
    # В цикле определяем принадлежность к времени суток каждого сообщения
    for message in messages:
        if 0 <= message['sent_at'].hour < 12:
            msg_count['утром'] += 1
        elif 12 <= message['sent_at'].hour < 18:
            msg_count['днем'] += 1
        elif 18 <= message['sent_at'].hour < 24:
            msg_count['вечером'] += 1
    # Выбор ключа-ответа по максимальному количеству сообщений
    max_msg_by_hour: str = ', '.join([k for k, v in msg_count.items() if v == max(msg_count.values())])
    return f'В чате больше всего сообщений: {max_msg_by_hour}.'


def longest_thread(messages: list[dict]) -> str:
    # Создаем список сообщений, которые не являются ответами
    start_thread_list: list = [msg for msg in messages if not msg['reply_for']]
    # Создаем список сообщений, которые являются ответами
    etc_thread_list: list = [msg for msg in messages if msg['reply_for']]
    # Создаем список для подсчета длины треда
    max_thread: list = []
    # Создаем словарь-счетчик длины тредов
    threads: dict = {}
    # Проверяем каждое сообщение из сообщений, не являющихся ответами
    for start_msg in start_thread_list:
        # Создаем тред
        max_thread.append(start_msg['id'])
        # Записываем в переменную начало цепочки
        start_id: uuid = start_msg['id']
        # Записываем временную переменную для сравнения
        temp: uuid = start_msg['id']
        # Проверяем сообщения-ответы на соответствие последнему элементу цепочки
        for reply_msg in etc_thread_list:
            if reply_msg['reply_for'] == temp:
                max_thread.append(reply_msg['id'])
                temp = reply_msg['id']
        # Наполняем словарь-счетчик
        threads[start_id] = len(max_thread)
        max_thread = []
    # Находим самую большую длину треда
    longest_thread_value: int = max(threads.values())
    # Создаем список ID сообщений с самой большой длиной треда, преобразуем в строку
    longest_thread_id: str = ', '.join([str(k) for k, v in threads.items() if v == longest_thread_value])
    return f'ID сообщений, начавших самые длинные треды: {longest_thread_id}. Длина треда: {longest_thread_value}'


if __name__ == "__main__":
    generate_chat_history()
    print(content_maker(messages=generate_chat_history()))
    print(reply_maker(messages=generate_chat_history()))
    print(influencer(messages=generate_chat_history()))
    print(when_they_chat(messages=generate_chat_history()))
    print(longest_thread(messages=generate_chat_history()))
