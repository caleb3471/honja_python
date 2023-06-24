root_num = 1/2

def pita(num1, num2):
    pita_out = (num1**2 + num2**2) ** root_num
    return pita_out



width = float(input("밑변의 길이를 입력하세요 : "))
high = float(input("높이의 길이를 입력하세요 : "))

print("빗변의 길이는 {:.1f} 입니다.".format(pita(width, high)))