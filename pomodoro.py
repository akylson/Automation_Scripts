import time

# определяем константы для времени помидора и перерыва
POMODORO_MINUTES = 25
BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15

# счетчик помидоров
pomodoro_count = 0

def run_pomodoro():
    global pomodoro_count

    # считаем время работы помидора
    for i in range(POMODORO_MINUTES, 0, -1):
        print(f"\rPomodoro: {i} minutes left.", end="")
        time.sleep(60)

    # инкрементируем счетчик помидоров и сообщаем об этом
    pomodoro_count += 1
    print(f"\nPomodoro completed. {pomodoro_count} pomodoros completed today.")

    # делаем перерыв
    if pomodoro_count % 4 == 0:
        print(f"Time for a long break ({LONG_BREAK_MINUTES} minutes).")
        for i in range(LONG_BREAK_MINUTES, 0, -1):
            print(f"\rLong break: {i} minutes left.", end="")
            time.sleep(60)
    else:
        print(f"Time for a break ({BREAK_MINUTES} minutes).")
        for i in range(BREAK_MINUTES, 0, -1):
            print(f"\rBreak: {i} minutes left.", end="")
            time.sleep(60)


if __name__ == '__main__':
    print("Starting Pomodoro timer...")
    while True:
        run_pomodoro()