import random
import matplotlib.pyplot as plt


def calculate_swa(scores, courses):
    total_weighted_scores = sum(
        scores[course] * weight for course, weight in courses.items())
    total_credits = sum(courses.values())
    return total_weighted_scores / total_credits


def generate_combinations(target_swa, courses):
    predictions = []
    for _ in range(5):
        while True:
            # Random scores between 50 and 90
            scores = {course: random.randint(50, 90) for course in courses}
            swa = calculate_swa(scores, courses)
            if round(swa, 2) == target_swa:  # Ensuring it meets the target SWA
                predictions.append(scores)
                break
    return predictions


def plot_results(predictions, courses):
    fig, ax = plt.subplots(figsize=(10, 6))
    course_names = list(courses.keys())
    x = range(len(course_names))

    for idx, scores in enumerate(predictions):
        y = [scores[course] for course in course_names]
        ax.plot(x, y, marker='o', linestyle='-', label=f'Score Set {idx+1}')

    ax.set_xticks(x)
    ax.set_xticklabels(course_names, rotation=45)
    ax.set_xlabel("Courses")
    ax.set_ylabel("Scores")
    ax.set_title(f"Predicted Score Distributions for SWA of {target_swa}")
    ax.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    courses = {
        "CSM 151": 3,
        "CSM 153": 2,
        "CSM 157": 3,
        "CSM 165": 3,
        "ENGL 157": 2,
        "MATH 161": 3,
    }

    target_swa = float(input("What is your target SWA?: "))
    predictions = generate_combinations(target_swa, courses)

    print("\nPredicted Score Combinations:")
    for idx, scores in enumerate(predictions):
        print(f"Score Set {idx+1}: {scores}")

    plot_results(predictions, courses)
