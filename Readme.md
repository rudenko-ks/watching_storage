# Диспетчерский пульт охраны банка "Dvmn"
Сайт позволяет производить мониторинг посещения хранилища cотрудниками банка

## Установка и запуск

Python3 должен быть уже установлен. 
1. Клонируйте репозиторий
```
git clone https://github.com/rudenko-ks/watching_storage.git
```
2. Создайте виртуальное окружение
```
python -m venv .venv
source .venv/bin/activate
```
3. Используйте `pip` (или `pip3`, если конфликт с Python2) для установки зависимостей
```
pip install -r requirements.txt
```
4. Запустите сервер командой
```
python main.py
```
## Использование

1. Главная страница отображает сотрудников с активными пропусками и располагается по адресу http://localhost:8000/
2. Выбор любого из сотрудников кликом по нему откроет страницу со всеми его посещениями хранилища.
3. При нажатии "Список пользователей в хранилище" загрузится страница со всеми сотрудниками, находящихся в данный момент в хранилище

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков  [dvmn.org](https://dvmn.org/).