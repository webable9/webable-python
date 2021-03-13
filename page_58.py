# 파이썬은 우너래 동적 타이핑 언어이기 때문에 제너릭이 필요 없다.
# 하지만 동적 타이핑의 장점이자 단점은 얼핏 사용하기엔 매우 편하지만 코드의 복잡도가 높아질수록 혼란을 가중시킨다는 점이다.
# 타입을 아예 명시하지 않으면 가독성를 낮추고 버그 발생 확률이 높아진다. 따라서 다음과 같이 타입을 명시할 수 있다.
from typing import TypeVar

T = TypeVar('T')
U = TypeVar('U')


def are_equal(a: T, b: U) -> bool:
    return a == b


are_equal(10, 10.0)