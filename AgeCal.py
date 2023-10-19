from datetime import date

# 사용자로부터 생년월일을 입력받는 함수
def get_birthdate():
    year = int(input("태어난 년도를 입력하세요 (예: 2000): "))
    month = int(input("태어난 월을 입력하세요 (1-12): "))
    day = int(input("태어난 일을 입력하세요 (1-31): "))
    return year, month, day

# 나이를 계산하는 함수
def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

# 생년월일 입력받기
year, month, day = get_birthdate()

# 나이 계산
age = calculate_age(year, month, day)

# 결과 출력
print("당신의 나이는", age, "세입니다.")
