from typing import Optional, Callable
from dados import dados

def get_option_callable(option:int=-1) -> Optional[Callable]:
    menu_options = {
        1:get_st_deviation,
        2:get_ordered_vehicles,
        3:get_5_biggest,
        4:get_5_lowest,
        5:filter_by_column,
        6:get_by_name,
    }
    try:
        if(option!=-1):
            try:
                return menu_options.get(option)
            except:
                return None
        print("""
            1. Apresentação do desvio padrão de uma coluna específica
            2. Apresentação dos veículos ordenados segundo uma das colunas específica
            3. Apresentação dos 5 veículos com os maiores valores de uma coluna específica
            4. Apresentação dos 5 veículos com os menores valores de uma coluna específica
            5. Apresentação da quantidade de carros para cada tipo de valor de uma coluna específica
            6. Exibir os todos os dados de um veículo fornecendo o nome do modelo.
        """)
        option = int(input("Selecione a opcao que deseja: "))
    except:
        print("Opcao invalida")
        return None
    return menu_options.get(option)

def get_selected_column() -> Optional[int]:
    print()
    columns = (
        "\t\tMarca",
        "\t\tModelo",
        "\t\tCombustivel",
        "\t\tPortas",
        "\t\tEstilo",
        "\t\tPotencia",
        "\t\tRPM",
        "\t\tConsumo cidade",
        "\t\tConsumo estrada",
        "\t\tPreco"
    )
    for item in columns: print(item)
    print()
    selection = "\t\t"+input("Selecione a coluna que deseja realizar a operacao: ")
    if selection in columns:
        return columns.index(selection)
    else:
        return None


def get_st_deviation() -> Optional[float]:

    selected_column = get_selected_column()
    values = [item[selected_column]for item in dados]
    try:
        return _st_deviation(values)
    except:
        return None

def _st_deviation(values: list) -> float:
    num_elements = len(values)
    average = 0
    for item in values: average+= item
    average = average/num_elements
    dif_sum = 0
    for item in values:
        dif_sum += (item - average)**2
    return (dif_sum/num_elements)**(1/2)

def _bubble_sort(values: list, column: int) -> list:
    n = len(values)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if values[j][column] > values[j + 1][column]:
                swapped = True
                values[j], values[j + 1] = values[j + 1], values[j]
        if not swapped:
            return values

def get_ordered_vehicles() :

    selected_column = get_selected_column()
    _bubble_sort(dados, selected_column)
    try:
        return dados 
    except:
        return None

def get_5_biggest() -> Optional[list]:
    return get_ordered_vehicles()[-5:][::-1]

def get_5_lowest() -> Optional[list]:
    return (get_ordered_vehicles()[:5])

def filter_by_column() -> int:

    selected_column = get_selected_column()
    unique_values = list(set([item[selected_column] for item in dados]))
    result = []
    for item in unique_values:
        value = 0
        for entry in dados:
            if entry[selected_column] == item: value +=1
        result.append((item, value))
    return result

def get_by_name() -> Optional[list]:

    name = input("Insira o modelo do carro: ")
    for item in dados:
        if item[1] == name:
            return item
    return None
