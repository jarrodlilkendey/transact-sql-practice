def read_query_from_file(path):
    with open(path, 'r') as query_file:
        query = query_file.read()
    return query