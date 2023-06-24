pi = 3.141592


def trans_volume(num1):
    float_num = float(num1)
    volume = (4/3)*pi*(float_num**3)
    return volume

def trans_surface(num1):
    float_num = float(num1)
    surface = 4 * pi * (float_num**2)
    return surface


num = input("구의 반지름을 입력하세요 : ")
print("= 구의 부피는 {:f} 입니다.".format(trans_volume(num)))
print("= 구의 겉넓이는 {:f} 입니다.".format(trans_surface(num)))
    
 
