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
    writer = [message['sent_by'] for message in messages if message['sent_by']]
    max_writer: int = max(writer, key=writer.count)
    ids_max_writers: set = set([i for i in writer if writer.count(i) == writer.count(max_writer)])
    res: str = ', '.join(map(str, (set(ids_max_writers))))
    return f'User ID, который написал больше всех сообщений - {res}.'


def reply_maker(messages: list[dict]) -> str:
    reply_ids: list = [message['sent_by'] for message in messages if message['reply_for']]
    max_replied: int = max(reply_ids, key=reply_ids.count)
    count_max_replied: int = reply_ids.count(max_replied)
    res: list = [i for i in reply_ids if reply_ids.count(i) == count_max_replied]
    replied: str = ', '.join(map(str, (set(res))))
    return f'User ID, на сообщения которого больше всего отвечали - {replied}.'



def influencer(messages: list[dict]) -> str:
    users_seen: list = [message['sent_by'] for message in messages if message['seen_by']]
    max_seen: int = max(users_seen, key=users_seen.count)
    count_max_seen: int = users_seen.count(max_seen)
    res: list = [i for i in users_seen if users_seen.count(i) == count_max_seen]
    ids_seen_max: str = ', '.join(map(str, (set(res))))
    return f'User ID, сообщения которых видело больше всего уникальных пользователей - {ids_seen_max}.'


def when_they_chat(messages: list[dict]) -> str:
    msg_count: dict = {
        'утром': 0,
        'днем': 0,
        'вечером': 0,
        }
    for message in messages:
        if 0 <= message['sent_at'].hour < 12:
            msg_count['утром'] += 1
        elif 12 <= message['sent_at'].hour < 18:
            msg_count['днем'] += 1
        elif 18 <= message['sent_at'].hour < 24:
            msg_count['вечером'] += 1
    max_msg_by_hour: str = ', '.join([k for k, v in msg_count.items() if v == max(msg_count.values())])
    return f'В чате больше всего сообщений: {max_msg_by_hour}.'




if __name__ == "__main__":
    print(generate_chat_history())
    print(content_maker(messages=generate_chat_history()))
    print(reply_maker(messages=generate_chat_history()))
    print(influencer(messages=generate_chat_history()))
    print(when_they_chat(messages=generate_chat_history()))
