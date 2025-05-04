import sys

"""
    A função lê os nomes das cidades e suas faixas de CEP e retorna uma lista de cidades e o índice da linha.
"""
def read_ceps_from_file(lines):

    cities=[]
    i=0

    # Ler os nomes das cidades e suas faixas de CEP
    while lines[i] != '--':
        city_name, start_cep, dest_cep = lines[i].split(',')
        cities.append((city_name, start_cep, dest_cep))
        i+=1

    return cities, i

"""
    A função lê os custos entre as cidades e retorna um grafo com os custos e o índice da linha.
"""
def build_graph_from_costs(lines, i):
    graph = {}

    while lines[i] != '--':

        # Ler os nomes das cidades e o custo entre elas
        start_city, dest_city, cost = lines[i].split(',')

        # Criar um grafo para armazenar os custos entre as cidades
        graph.setdefault(start_city, []).append((dest_city, cost))
        graph.setdefault(dest_city, []).append((start_city, cost))
        i+=1
    
    return graph, i

"""
    Verifica se o CEP está dentro da faixa de CEPs da cidade e retorna o nome da cidade correspondente.
"""
def get_city_from_cep(cities, cep):
    for city, start_cep, dest_cep in cities:
        # Verifica se o CEP está dentro da faixa de CEPs da cidade
        if start_cep <= cep <= dest_cep:
            return city
    return None

"""
    Encontra o menor caminho de menor custo entre duas cidades em um grafo utilizando o algoritmo de Dijkstra.
"""
def find_shortest_path_with_cost(graph, start_city, dest_city):

    # Inicializa a fila
    queue = [(0, start_city, [])]
    visited = set()

    while queue:

        # Remover o elemento com menor custo
        queue.sort(key=lambda x: x[0])
        cost, curr_city, path = queue.pop(0)

        if curr_city in visited:
            continue

        visited.add(curr_city)

        # Atualizar o caminho
        path = path + [curr_city]

        if curr_city == dest_city:
            return path, cost

        # Verificar os vizinhos da cidade atual
        for neighbor, weight in graph.get(curr_city, []):
            if neighbor not in visited:
                queue.append((cost + float(weight ), neighbor, path))

    return [], sys.maxsize

try:
    with open('custos.txt') as f:
        # Ler o arquivo e dividir as linhas
        lines = f.read().strip().split('\n')
    
        cities, i = read_ceps_from_file(lines)
                
        # Ler o arquivo e criar um grafo com os custos entre as cidades
        graph, i = build_graph_from_costs(lines, i+1)
            
        # Ler a linha que contém os CEPs de origem e destino
        start_cep, dest_cep = lines[i+1].split(',')

        city_1 = get_city_from_cep(cities, start_cep)
        city_2 = get_city_from_cep(cities, dest_cep)

        # Calcular o menor caminho entre as cidades
        if city_1 and city_2:
            path, cost = find_shortest_path_with_cost(graph, city_1, city_2)
            print(f"Menor caminho entre {city_1} e {city_2}: {path} com custo total {cost}")

except FileNotFoundError:
    print(f"Erro: O arquivo 'custos.txt' não foi encontrado.")
    exit()

