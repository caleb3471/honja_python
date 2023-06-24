import datetime

while(True):
    
    question = input("입력 : ")
    if question == "종료":
        break
    elif question in "안녕":
        print("안녕하세요.")
    elif question == "지금 몇 시야":
        print("지금은 {}시 입니다.".format(datetime.datetime.now().hour))
    else:
        print(question)
    
    
        
        