n = int(input())
c = list(map(int, input().split()))
q = int(input())

queries = list()

for qi in range(q):
    query = input()
    queries.append(query)


def count_clients(clients: list, queries_list: list) -> None:
    for q_str in queries_list:
        parsed_query = q_str.split()
        event = parsed_query[0]

        if event == 'COUNT':
            start = int(parsed_query[1]) - 1
            end = int(parsed_query[2])
            print(sum((clients[start:end])))

            continue

        tower = int(parsed_query[1]) - 1
        d = 1 if event == 'ENTER' else -1
        clients[tower] += d


count_clients(c, queries)
