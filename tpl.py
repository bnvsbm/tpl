habit_info = ('Reading', True, 7, 30)

weekly_habits = (1, 1, 0, 1, 1, 0, 1)


print(len(weekly_habits))
print(weekly_habits[0])
print(weekly_habits[3])
print(weekly_habits[0:3])
print(weekly_habits[5:7])

weekly_habits = weekly_habits + (1,)

print(weekly_habits.count(1))
print(weekly_habits.count(0))

for day in weekly_habits:
    print(day)

print('Habits completed')