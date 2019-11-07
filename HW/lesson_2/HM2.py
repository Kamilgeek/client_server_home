import csv, chardet, re

os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

param_name_to_result_list = {
    'Изготовитель ОС': os_prod_list,
    'Название ОС': os_name_list,
    'Код продукта': os_code_list,
    'Тип системы': os_type_list
}
regex_pattern = re.compile(
    r"(Изготовитель ОС|Название ОС|Код продукта|Тип системы):\s+(.+)"
)


def get_data(file_name):
    with open(file_name) as file:
        data = file.read()

    result = re.findall(regex_pattern, data)

    for param_name, param_value in result:
        param_name_to_result_list[param_name].append(param_value)


def write_to_csv(writing_file_name):
    writing_file_name.decode('utf8').encode('utf8')
    for file_name in [f"info_{i}.txt" for i in range(1, 4)]:
        get_data(file_name)

    main_data = [tuple(param_name_to_result_list.keys())] + list(
        zip(*param_name_to_result_list.values())
    )

    with open(writing_file_name, 'W') as file:
        writer = csv.writer(file)
        writer.writerow(main_data)

if __name__== 'client':
    write_to_csv('main_data.csv')

