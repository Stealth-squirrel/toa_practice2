import copy

def stable_matching(h_prefs, s_prefs, quotas):
    free_students = list(s_prefs.keys())  #студенты, которых еще не взяли
    h_s = {h:[] for h in h_prefs.keys()}  # {hospital: [students]}
    s_h = {s:None for s in s_prefs.keys()}  # {student: hospital}
    # распределение студентов по рангам для каждой больницы
    hospital_rankings = {h: {s: i for i, s in enumerate(prefs)} for h, prefs in h_prefs.items()}

    while free_students:
        s = free_students.pop(0) # берем первого свободного студента
        prefs = copy.deepcopy(s_prefs[s])  # предпочтения выбранного студента

        while prefs: 
          h = prefs.pop(0)  # берем наиболее предпочитаемую больницу
          if len(h_s[h]) < quotas[h]: # проверяем, остались ли в больнице места
            h_s[h].append(s)  # если да, то создаем пару
            s_h[s] = h
            break
          
          else:  # если мест в больнице нет, проверяем, можно ли заменить кого-то
            worst = max(h_s[h], key=lambda x: hospital_rankings[h][x])
            if hospital_rankings[h][s] < hospital_rankings[h][worst]:  # новый студент лучше наименее предпочтительного для больницы студента
                h_s[h].remove(worst)
                h_s[h].append(s) # нанием студента вместо наименее предпочтительного
                s_h[s] = h
                s_h[worst] = None
                free_students.append(worst)  # худший снова свободен
                break
    return s_h, h_s

# пример
students_prefs = {
    'S0': ['H0', 'H1'],
    'S1': ['H1', 'H0'],
    'S2': ['H0', 'H1'],
    'S3': ['H1', 'H0']
}
hospitals_prefs = {
    'H0': ['S0', 'S1', 'S2', 'S3'],
    'H1': ['S1', 'S0', 'S2', 'S3']
}
quotas = {'H0': 2, 'H1': 1}

s_h, h_s = stable_matching(hospitals_prefs, students_prefs, quotas)

print("Распределение студентов:")
for s, h in s_h.items():
    print(f"  {s} -> {h if h else 'Не распределён'}")

print("\nСостав больниц:")
for h, s in h_s.items():
    print(f"  {h} (квота {quotas[h]}): {s}")