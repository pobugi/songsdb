# songsdb
Django learning project (lazy queries)

Для запуска приложения:

1. Клонируйте репозиторий 
2. Перейдите в соответствующию директорию 
3. Создайте виртуальное окружение 
4. Установите зависимости: 
    Linux: pip3 install -r requirements.txt 
    Windows: pip install -r requirements.txt 
5. Выполните миграции: python/python3 manage.py migrate
6. Создайте администратора: python/python3 manage.py createsuperuser
7. Для заполнения БД тестовыми данными: python3 manage.py load_items
8. Запустите приложение: python/python3 manage.py runserver

Примеры lazy query:

    Song.objects
    Song.objects.all()

    Song.filter(...) or Song.exclude(...)

    name__exact="..."
    year__gt=10 (lt, gte, lte)
    name__contains="..."
    name__startswith="..."
    name__endswith="..."
    name__isnull=True


    .count()
    .get()

    rock = Genre.objects.filter(name__contains="Rock").get()
    rock.album_set.all()

