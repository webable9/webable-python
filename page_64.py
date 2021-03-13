# 클래스는 현대 프로그래밍 언어에서 빼놓을 수 없는 필수 기능이다
from dataclasses import dataclass


@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area())
# dataclass 데코레이션을 이용해 클래스를 선언했다. 물론 dataclass를 선언하지 않아도 클래스 구현에는 문제가 없다.
# 그러나 선언하게 되면 여러 가지 내부 함수의 기능도 자동으로 구현해주기 때문에 편리하게 활용할수 있다.
