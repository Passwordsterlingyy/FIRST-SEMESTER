def calculate_cwa(grades):
    """
    Calculate the Cumulative Weighted Average (CWA).

    param grades: List of tuples [(grade, credit_hours), ...]


    Return: CWA (float)
    """
    total_weighted_score = sum(grade * credit for grade, credit in grades)
    total_credits = sum(credit for _, credit in grades)

    if total_credits == 0:
        return 0

    return total_weighted_score / total_credits


grades_list = [
    (82, 3), # Pure Math
    (67.5, 2), #Discrete mathematics
    (69.79, 2), #Circuit theory
    (71, 3), #Programming
    (68, 3), #IT
    (70, 2), #Commskills
    (75, 2) #Econs
]

cwa = calculate_cwa(grades_list)
print(f"CWA: {cwa:.2f}")
