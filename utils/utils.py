from typing import List, Tuple, Dict


def convert_tuple_list_to_dict(list: List[Tuple[int, str, str, str]]) -> List[Dict[str, int|str]]:
    all_dates = []
    for data in list:
        d = dict()
        
        d["id"] = data[0]
        d["nome"] = data[1]
        d["email"] = data[2]
        d["telefone"] = data[3]

        all_dates.append(d)
    return all_dates


if __name__=="__main__":
    teste = [
        (2, 'Maria Joaquina', 'maria@gmail.com', '74999104444'),
        (2, 'Maria Joaquina', 'maria@gmail.com', '74999104444'),
        (2, 'Maria Joaquina', 'maria@gmail.com', '74999104444')
    ]

    print(convert_tuple_list_to_dict(teste))
