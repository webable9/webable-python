# 구조체는 메모리의 어느 영역에나 어떤 크기로든 할당할 수 있는 사실상 유일한 복합 자료형 이다.
from collections import namedtuple
from dataclasses import dataclass

MyStruct = namedtuple("MyStruct", "field1 field2 field3")

m = MyStruct("foo", "bar", "baz")

# 파이썬에는 구조체가 없을 뿐더러 클래스 또한 데이터 타입을 지정할 수 없어. 구조체외 같은 형태를 정의 하려면 Named Tuple을 사용해야 한다. 파이써 3.7부터 dataclass를 지원하며
# @dataclass 데코레이션(자바에서는 동일한 문법을 애노테이션이라 부른다)으로 타입 힌트와 함께 활용함으로써 다음과 같이 class를 이용해 구조체 형태로 정의할 수 있다.

@dataclass
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 10
