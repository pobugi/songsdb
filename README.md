# songsdb
Django learning project (lazy queries)

query examples:

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

