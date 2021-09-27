from django.db import connection, reset_queries
from time import perf_counter
import functools

def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()

        start_queries = len(connection.queries)

        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()

        end_queries = len(connection.queries)

        print("Function: {}".format(func.__name__))
        print("N of queries: {}".format(end_queries-start_queries))
        print("Finished in: {} s.".format(round(end-start, 2)))

        return result

    return inner_func