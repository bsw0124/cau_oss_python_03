import math

class line :
    def __init__(self,length = 0):  #line클래스에는__length필드가 있고, 초기값은0이다. 생성자를통해초기__length값을지정할수있다.
        self.__length = length  
    # 해당필드에접근하기위한메소드set_length와get_length가있다
    def set_length(self,length):
        self.__length = length

    def get_length(self):
        return self.__length
    

def area_square(length): #𝑙𝑒𝑛𝑔𝑡ℎ를매개변수로받아,𝑙𝑒𝑛𝑔𝑡ℎ2의정사각형의넓이를반환한다
    return length**2

def area_circle(length): #𝑙𝑒𝑛𝑔𝑡ℎ를매개변수로받아,𝑙𝑒𝑛𝑔𝑡ℎ2×𝜋의원의넓이를반환한다
    return length**2*math.pi

def area_regular_triangle(length): #𝑙𝑒𝑛𝑔𝑡ℎ를매개변수로받아,정삼각형의넓이를반환한다
    return 3*math.sqrt(4)*length**2