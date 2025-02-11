odd = [
    1,
    3,
    5,
    7,
    9,
]  # 리스트 자료형의 형태 리스트명[요소1, 요소2, 요소3, ...]처럼 대괄호로 묶고 요소를 콤마로 구분.

a = []  # 비어있는 리스트
b = [1, 2, 3]  # 숫자만 있는 리스트
c = ["life", "is", "too", "short"]  # 문자열만 있는 리스트
d = [1, 2, "life", "short"]  # 숫자와 문자가 같이 있는 리스트
e = [1, "life", [2, "short"]]  # 리스트 자체가 리스트에 포함된 리스트

a = (
    list()
)  # 비어있는 리스트는 list()로 생성할 수 있음, 어떠한 자료형이든 리스트에 포함될 수 있다.

# 리스트 인덱싱

a = [1, 2, 3]
a[0]  # 1이 반환됨
a[2]  # 3이 반환됨

a[0] + a[2]  # 1+3으로 4가 반환됨

# 문자열과 마찬가지로 a[-1]은 오른쪽으로부터 대응하는 요소를 반환함

a = [1, 2, 3, ["a", "b", "c"]]

a[0]  # 1
a[-1]  # ['a','b','c']
a[3]  # ['a','b','c']

# 리스트 안에 있는 리스트에서 추출
a = [1, 2, 3, ["a", "b", "c"]]
a[3][1]  # 'b' 가 반환됨

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
a[0:2]  # 0번째부터 2번째 전까지->[1,2] 반환
b = a[:2]  # 첫번째부터 2번째 전까지
c = a[2:]  # 2번쨰부터 끝까지

# 중첩된 리스트에서도 동일하게 작용
a = [1, 2, 3, ["a", "b", "c"], 4, 5]
a[2:5]  # [3,['a','b','c'],4,5] 반환
a[3][0]  # 'a'반환

# 리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
a + b  # [1,2,3,4,5,6]

a * 3  # [1,2,3,1,2,3,1,2,3]

# 리스트 길이 구하기 len() 함수 사용
a = [1, 2, 3]
len(a)  # 3을 반환

# 리스트 연산에서의 주의점
a = [1, 2, 3]  # 리스트 a에서 각 요소는 int 자료형으로 저장됨
b = ["hi", "bye"]  # 리스트 b에서 각 요소는 str 자료형으로 저장됨

a[2] + b[0]  # int + str 이므로 오류 발생
str(a[2]) + b[0]  # '3'이라는 문자로 바꾸므로 '3hi' 출력

# 리스트 값 수정
a = [1, 2, 3, 4]
a[2] = 5  # 2번째 요소값인 3이 5로 바뀜

# 리스트 값 삭제 del 함수 이용...del + 삭제할 객체
a = [1, 2, 3, 3, 4]
del a[2]  # 2번째 요소값인 3이 삭제됨

# del 함수와 슬라이싱 기법을 활용
a = [1, 2, 3, 4, 5, 6, 7]
del a[2:4]  # 2번째부터 4번째 전까지 2개의 요소값 삭제

# 리스트 관련 함수

# 리스트 요소 추가하기 .append()함수
a = [1, 2, 3]
a.append(4)  # 리스트의 맨 마지막에 괄호 안의 요소를 추가
del a[1]
print(a)

a.append([5, 6])  # 어떤 자료형이든 추가 가능

# 리스트 정렬 .sort()

a = [5, 1, 9, 3, 2]
a.sort()  # list a 를 [1,2,3,5,9]로 변형

b = ["b", "d", "e", "a", "c"]
b.sort()  # list b를 ['a','b','c','d','e']로 변환

# 리스트 뒤집기 .reverse()
# 리스트를 역순으로 변환, 정렬 후 역순으로 변환하는 것이 아닌 리스트 자체를 역순으로 변환

a = [1, 4, 2, 5, 3]
a.reverse()

# 인덱스 반환 .index()
# 괄호 안에 있는 요소의 인덱스 값(위치값) 리턴

a = [1, 3, 5, 7, 9]
a.index(3)  # 1 리턴

b = [1, 2, 3, 1, 5]
b.index(1)  # 가장 처음 나오는 요소의 인덱스 값 리턴

# list에 없는 요소를 넣으면 오류 발생생
b.index(0)  # ValueError: 0 is not in list

# list에 요소 삽입 .insert(a,b)
# a번째 자리에 b를 삽입

a = [0, 1, 3, 4, 5]
a.insert(2, 2)  # 2번째 요소값에 2 삽입

a.insert(6, [1, 2])  # list 역시 삽입 가능

# list 요소 제거 .remove(a) >> 첫번째로 등장한 a 요소 제거
a = [0, 1, 2, 3, 4]
a.remove(1)  # a=[0,2,3,4]

a = [0, 1, 2, 1, 3, 4]
a.remove(1)  # a=[0,2,1,3,4] >> 두번째로 등장하는 1은 삭제되지 않음

# list 요소 끄집어 내기 .pop()
a = [1, 2, 3, 4]
a.pop()  # 4를 리턴하고 list a에서 4를 삭제함
print(a)  # [1,2,3]

b = [1, 2, 3, 4]
b.pop(2)  # 2번째 요소(3)를 리턴하고 리스트에서 삭제
print(b)  # [1,2,4]

# 리스트에 포함된 요소의 개수 세기 .count()
a = ["1", "a", "b", "3", 1, 3, "a"]
a.count("a")  # 문자 'a'가 2개 있으므로 2를 리턴
a.count(1)  # 숫자 1이 1개 있으므로 1을 리턴

# 리스트 확장 .extend()
# extend()의 괄호 안에는 리스트형 자료만이 올 수 있음

a = [1, 2, 3]
a.extend([4])  # a==[1,2,3,4]
a.extend([5, 6])  # a==[1,2,3,4,5,6]

b = [7, 8, 9]
a.extend(b)  # 변수 b에 리스트형 자료가 저장되어 있으므로
# a==[1,2,3,4,5,6,7,8,9]

# .extend()의 다른 표현
a = [1, 2, 3]
a.extend([4, 5])

b = [1, 2, 3]
b += [4, 5]

print(a == b)  # a와 b는 동일하므로 True 출력
