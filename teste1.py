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
    Verifica se o CEP está dentro da faixa de CEPs e retorna o nome da cidade.
"""
def get_city_from_cep(cities, cep):
    for city, start_cep, dest_cep in cities:
        # Verifica se o CEP está dentro da faixa de CEPs da cidade
        if start_cep <= cep <= dest_cep:
            return city
        
    return None

try:
    with open('cidades.txt') as f:
        # Ler o arquivo e dividir as linhas
        lines = f.read().strip().split('\n')

        cities, i = read_ceps_from_file(lines)

        # Ler a linha que contém o CEP a ser buscado
        cep = lines[i+1]

        city = get_city_from_cep(cities, cep)
        print(city) 

except FileNotFoundError:
    print(f"Erro: O arquivo 'cidades.txt' não foi encontrado.")
    exit()
