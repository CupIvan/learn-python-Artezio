#!/bin/env python

# Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь.
# Для ключей, для которых нет значений использовать None в качестве значения. Значения, для которых нет ключей игнорировать.
def make_map(keys, values):
	hash = {}
	for i in range(len(keys)):
		hash[keys[i]] = values[i] if i < len(values) else None
	return hash

print(make_map([1,2,3,4,5], [2,3,4]))
print(make_map([3,4,5], [1,2,2,3,4]))
