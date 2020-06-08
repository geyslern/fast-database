'''
Author: Regis Santos - rg3915

Insere dados no banco de dados PostgreSQL de várias formas diferentes.
Gera um benchmark para ver o método mais rápido.

Requisitos:

* Instale PostgreSQL
* Gere os dados CSV previamente com
    create_database.py ou
    create_database_with_click.py

Como rodar este programa:

$ python insert_data_benchmark.py --rows 10000
'''
import click
import csv
import django
import os
import subprocess
import timeit
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myproject.core.models import Product


@click.command()
@click.option(
    '--rows',
    default='1000',
    prompt='Quantidade de linhas',
    help='Quantidade de linhas do CSV.'
)
def main(rows):
    logfile = 'time_log.txt'
    home = str(Path.home())
    filename = f'{home}/dados/produtos_{rows}.csv'

    data = csv_to_list(filename)

    time = insert_data_with_bulk_create(items=data)
    print(time)
    timelog(int(rows), time, logfile, 'Django bulk_create')


def insert_data_with_bulk_create(items):
    aux_list = []
    tic = timeit.default_timer()
    for item in items:
        obj = Product(title=item['title'], quantity=item['quantity'])
        aux_list.append(obj)
    Product.objects.bulk_create(aux_list)
    toc = timeit.default_timer()
    time = toc - tic
    return round((time), 3)


def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrderedDict.
    Créditos para Rafael Henrique
    https://bit.ly / 2FLDHsH
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def timelog(total_items, _time, logfile, resource):
    total_items = f'{total_items:,}'.replace(',', '.')
    space = ' ' * (10 - len(total_items))
    time = round((_time), 3)
    subprocess.call(f"printf '{total_items} {space} -> {time}s\t --> Inserindo {total_items} registros com {resource}.\n' >> {logfile}", shell=True)


# def insert_data_with_bulk_create(items):
#     print(f'Total: {items}')


if __name__ == '__main__':
    main()