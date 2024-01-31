#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__ == '__main__':
    def find_duplicate_pair_index(tuple_data):
        for i in range(len(tuple_data) - 1):
            if tuple_data[i] == tuple_data[i + 1]:
                return i, i + 1
        return None

    my_tuple = (2, 2, 3, 5, 8, 9)
    result = find_duplicate_pair_index(my_tuple)

    if result:
        index1, index2 = result
        print(f"Найдена пара одинаковых соседних элементов на позициях {index1} и {index2}")
    else:
        print("В кортеже нет пары одинаковых соседних элементов.")
