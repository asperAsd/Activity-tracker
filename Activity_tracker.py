import matplotlib.pyplot as plt
import time

activities = {}

def start_tracking(activity):
    start_time = time.time()
    input(f"Трекер запущен для '{activity}'. Нажмите Enter, чтобы остановить...")
    end_time = time.time()
    duration = end_time - start_time

    if activity in activities:
        activities[activity] += duration
    else:
        activities[activity] = duration

def generate_chart():
    if not activities:
        print("Нет данных для отображения.")
        return
    activities_names = list(activities.keys())
    durations = list(activities.values())
    plt.figure(figsize=(10, 8))
    plt.pie(durations, labels=activities_names, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Распределение времени по активностям')
    plt.legend(title="Активности", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    plt.show()

def main():
    while True:
        activity = input("Введите активность (или 'выход' для завершения): ")
        if activity.lower() == 'выход':
            break
        start_tracking(activity)

    generate_chart()

if __name__ == "__main__":
    main()
