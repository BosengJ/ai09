# calculator 모듈 : class 구현 버전

class Calc:
    def __init__(self):   # 생성자,  인스턴스 객체를 생성할 때 자동으로 호출, 인스턴스 멤버 초기화
        print('Calc 생성자가 호출됨')
        self.a = 0
        self.b = 0
        self.c = 0
        
    def add(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a + self.b
        print('add called!')
        return self.c

    def subtract(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a - self.b
        print('subtract called!')
        return self.c

    def multiply(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a * self.b
        print('multiply called!')
        return self.c

    def divide(self,a,b):
        self.a = a
        self.b = b
        self.c = self.a / self.b
        print('divide called')
        return self.c

if __name__ == '__main__':
    m1 = Calc()    # 인스턴스 생성
    ret = m1.add(10,20)  # 인스턴스 메서드 호출
    print(ret)

    ret = m1.subtract(10,20)
    print(ret)

    print('나는 모듈입니다 ',__name__)



