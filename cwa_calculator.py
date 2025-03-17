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
    (75, 3),
    (80, 2),
    (65, 3),
    (90, 1),
]

cwa = calculate_cwa(grades_list)
print(f"CWA: {cwa:.2f}")
