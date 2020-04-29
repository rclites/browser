with open('salary.txt', 'r') as salary:
    with open('salary_year.txt', 'w') as salary_year:
        for line in salary:
            yearly = int(line) * 12
            salary_year.write(f'{yearly}\n')
