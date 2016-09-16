__author__ = 'maria slanova'

import networkx as nx
import pandas as pd
import csv


def edge_list_to_graph():
    """
    :return: Weighted graph, where each node represents an airport
    """
    filename = raw_input('Enter a file name: ')
    df = pd.read_csv(filename, names=['node1', 'node2'])
    df.groupby('node1')['node2'].size()
    df['count'] =df.groupby('node1')['node2'].transform(pd.Series.value_counts)
    df = df.drop_duplicates(subset=['node1', 'node2'], take_last=True)
    matrix = df.drop_duplicates(subset=['node1', 'node2'], take_last=True)
    matrix.to_csv('temp/out.csv', sep=',', encoding='utf-8', header=True, index=False)
    with open("temp/out.csv") as f:
        next(f)
        graph = nx.read_edgelist(f, delimiter=",", data=[("count", float)], create_using=nx.DiGraph())

    return graph


def dictionary():
    """
    :return: A dictionary representation of a weighted graph
    """
    data_dict = {}
    with open('temp/out.csv', 'r') as data_file:
        data = csv.DictReader(data_file, delimiter=",")
        for row in data:
            item = data_dict.get(row["node2"], dict())
            item[row["node1"]] = int(row["count"])
            data_dict[row["node2"]] = item

    return data_dict
