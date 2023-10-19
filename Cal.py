# asdf
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "0으로 나눌 수 없습니다."
        return x / y

# 계산기 객체 생성
calc = Calculator()

while True:
    print("사칙연산을 선택하세요:")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")

    choice = input("선택 (1/2/3/4/5):")

    if choice == '5':
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        if choice == '1':
            print("결과: ", calc.add(num1, num2))
        elif choice == '2':
            print("결과: ", calc.subtract(num1, num2))
        elif choice == '3':
            print("결과: ", calc.multiply(num1, num2))
        elif choice == '4':
            result = calc.divide(num1, num2)
            print("결과: ", result)
        else:
            print("잘못된 선택입니다.")
    else:
        print("잘못된 선택입니다.")
