from requests import get, post, delete

# print(get('http://127.0.0.1:8080/api/jobs').json())
# print(get('http://127.0.0.1:8080/api/jobs/1').json())
# print(get('http://127.0.0.1:8080/api/jobs/999').json())
# # # print(get('http://127.0.0.1:8080/api/jobs/q').json())
# print(post('http://127.0.0.1:8080/api/jobs', json={}).json())
# #
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'title': 'Заголовок'}).json())
# #
# print(post('http://127.0.0.1:8080/api/jobs',
#            json={'team_leader': 'Заголовок',
#                  'job': 'Текст новости',
#                  'collaborators': "3, 4",
#                  "work_size": 99,
#                  "is_finished": False}).json())
#
# # print(delete('http://127.0.0.1:8080/api/jobs/999').json())
# # новости с id = 999 нет в базе
# print(delete('http://127.0.0.1:8080/api/jobs/a').json())
# # В ЖИЗНИ МНОГО ЧТО МОЖНО ПЕРЕПУТАТЬ, НО КАК МОЖНО ПЕРЕПУТАТЬ ЦИФРУ С БУКВОЙ?
# print(delete('http://127.0.0.1:8080/api/jobs/1').json())
# # вот так пишут люди
# print(get('http://127.0.0.1:8080/api/jobs').json())
# # ОТ ВАМ НЕБОЛЬШОЙ РАССКАЗ
# # Жена приехала домой после длительной командировки.
# # Я, уходя на работу утром, сказал ей: — Не включай мой компьютер.
# # То, что ты увидишь, может тебе не понравиться!
# # Прихожу домой вечером, а она злая. Спрашиваю: — Что случилось?
# # Она говорит: — Ну включила я твой комп. Лазила целый день, думала там ***** или переписки с любовницей.
# # А там ничего! — И это тебе не понравилось? — Ну, да! — Я же предупреждал!
#
#
# print(post('http://127.0.0.1:8080/api/jobs/1', json={}).json())
# # НУ ты особенный, что ты передаёщь
# print(post('http://127.0.0.1:8080/api/jobs/1',
#            json={'job': '1234567890'}).json())
# # Ну ты опять что-ли особенный
# print(post('http://127.0.0.1:8080/api/jobs/6',
#            json={"id": 6,
#                  'team_leader': 2345676543,
#                  'job': 'Текст 234234234',
#                  'collaborators': "3, 4"}).json())
# # НУ Вот
# # Ты неперь не особенный
# print(get('http://127.0.0.1:8080/api/jobs').json())

# Напечатать всё
print(get("http://127.0.0.1:8080/api/v2/users").json())
# Напечатать только одного
print(get("http://127.0.0.1:8080/api/v2/users/1").json())
# Удалить кого-то
print(delete("http://127.0.0.1:8080/api/v2/users/1").json())
# НУ и вот ещё
print(post('http://127.0.0.1:8080/api/jobs/6',
           json={"id": 6,
                 'team_leader': 2345676543,
                 'job': 'Текст 234234234',
#                'collaborators': "3, 4"}).json())
