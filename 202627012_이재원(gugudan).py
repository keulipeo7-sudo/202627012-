def gugudan(num):
    if num < 2 or num > 9:
        print("2부터 9 사이의 숫자를 입력하세요.")
        return

    print(f"--- {num}단 ---")
    for i in range(1, 10):
        print(num, "x", i, "=", num * i)

num = int(input("몇단을 입력할까요? "))
gugudan(num)

