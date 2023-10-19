# 간단한 계산기 함수
def calculator():
    try:
        # 사용자로부터 숫자 입력
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        operator = input("사칙연산 연산자를 입력하세요 (+, -, *, /): ")
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        # 연산 수행
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("0으로 나눌 수 없습니다.")
                return
            result = num1 / num2
        else:
            print("유효한 연산자를 입력하세요.")
            return

        print(f"결과: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("올바른 숫자를 입력하세요.")

# 계산기 실행
while True:
    calculator()
    again = input("다시 계산하시겠습니까? (y/n): ")
    if again.lower() != 'y':
        break
