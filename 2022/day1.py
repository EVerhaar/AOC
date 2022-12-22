with open('calories.txt') as f:
    calories = f.readlines()

    total_calories = []
    current_calorie = 0

    for calorie in calories:
        calorie = calorie.strip()

        if not calorie == '':
            calorie = int(calorie)
            current_calorie += calorie
        else:
            total_calories.append(current_calorie)
            current_calorie = 0
    total_calories.append(current_calorie)
    
    highest_calorie = 0
    for c in total_calories:
        if c > highest_calorie:
            highest_calorie = c
    
    print(highest_calorie)

    total_calories.sort(reverse=True)
    top3 = 0
    for calorie in total_calories[:3]:
        top3 += calorie

    print(top3)