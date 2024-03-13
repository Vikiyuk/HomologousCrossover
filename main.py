import random
import numpy as np

def parent(n):
    parent = []
    for i in range(0, n):
        parent.append(random.randint(0, 1))
    while parent[n - 2] == 1 and parent[n - 1] == 1:
        parent[n - 2] = random.randint(0, 1)
        parent[n - 1] = random.randint(0, 1)
    return parent


def homologous_crossover(parent_a, parent_b, m, w, u):
    crossover_points = sorted(random.sample(range(0, len(parent_a) - 1), m))
    print("Crossover points:", crossover_points)
    offspring_a = []
    offspring_b = []
    offspring_a.extend(parent_a[:crossover_points[0]])
    offspring_b.extend(parent_b[:crossover_points[0]])
    for i in range(len(crossover_points) - 1):
        start = crossover_points[i]

        end = crossover_points[i + 1]
        substring_a = parent_a[start+1:end]
        substring_b = parent_b[start+1:end]
        print(substring_a,substring_b)
        if len(substring_a) >= w:
            number_of_1 = sum(1 for a, b in zip(substring_a[:w], substring_b[:w]) if a != b)
            DS = number_of_1 / len(substring_a)
            print(DS, number_of_1,substring_a[:w])
            if DS >= u:
                print("swap")
                substring_a, substring_b = substring_b, substring_a
        offspring_a.extend([parent_a[start]])
        offspring_a.extend(substring_a)
        offspring_b.extend([parent_b[start]])
        offspring_b.extend(substring_b)

    offspring_a.extend(parent_a[end:])
    offspring_b.extend(parent_b[end:])

    return offspring_a, offspring_b


nmb_of_parents = 5
parents_a = []
parents_b = []
for i in range(nmb_of_parents):
    parents_a.append(parent(10))
    parents_b.append(parent(10))
parent_a = parents_a[random.randint(0, len(parents_a) - 1)]
parent_b = parents_b[random.randint(0, len(parents_b) - 1)]
m = 3
w = 2
u = 0.4

offspring_a, offspring_b = homologous_crossover(parent_a, parent_b, m, w, u)
print("Parent A:", parent_a)
print("Parent B:", parent_b)
print("Offspring A:", offspring_a)
print("Offspring B:", offspring_b)
