# {}로 둘러쌓여 있으며 각각의 요소는 Key : Value 형태로 작성
# {Key1 : Value1, Key2 : Value2, Key3 : Value3}

dic = {"name": "장준호", "phone": "010-4308-3135", "birth": "0605"}
dic["name"]

# Value에 list를 넣을 수도 있음
a = {1: [1, 2, 3]}
a[1]

# dictionary 쌍 추가
a = {1: "a"}
a[2] = "b"
a["c"] = (
    "charlie"  # c라는 변수를 key로 활용하고 싶다면, c='c'처럼 미리 변수를 hashable하게 고정해야함
)

# key를 사용해 value 얻기
grade = {"pey": 10, "alice": 99}
grade["pey"]
grade["alice"]

# key가 중복될 경우

a[1]  # 1이라는 key가 중복될 때는 하나를 제외한 다른 value를 무시함

# key가 될 수 있는 자료형
a = {
    [1, 2]: "a"
}  # list 자료형은 mutable(변할 수 있는) 자료이기 때문에 key로 활용할 수 없음.
b = {(1, 2): "a"}  # tuple, int, 문자열 자료형은 immutable값 이므로 key로 활용 가능
print(b)  # {(1, 2): 'a'}

# Dictionary 관련 함수
# .keys()
a = {1: "first", 2: "second", 3: "third"}
a.keys()  # dict_keys([1, 2, 3]) 반환
# a의 key 만을 모아 dict_keys 객체를 반환

for k in a.keys():
    print(k)

# key를 list로 반환하는 방법 >> list(a.keys())
a = {1: "first", 2: "second", 3: "third"}
k = list(a.keys())
k[2]
a[k[2]]

# value list 만들기 >> .values()
a = {1: "first", 2: "second", 3: "third"}
a.values()  # dict_values 객체를 반환
list(a.values())

# key, value 쌍 얻기 >> .items()
a = {1: "first", 2: "second", 3: "third"}
a.items()  # 각각의 key와 value를 tuple로 묶은 값을 dict_items 객체로 리턴
k = list(a.items())
k[0]  # (3, 'third') 리턴

# key : value 쌍 모두 지우기 >> .clear()
a = {1: "first", 2: "second", 3: "third"}
a.clear()
print(a)  # 비어있는 dictionary {}로 리턴

# key로 value를 얻는 다른 방법 >> .get(key)
a = {1: "first", 2: "second", 3: "third"}
a[1]  # 'first' 리턴
a.get(1)  # 'first' 리턴

a[4]  # error 발생
a.get(4)  # None 리턴
print(a.get(4))  # None

# .get(key, default_value)
a = {1: "first", 2: "second", 3: "third"}
a.get(
    1, "fail"
)  # 1이라는 값이 key에 없을 시 default값인 'fail'을 리턴하지만 1이 key에 있으므로 그에 해당하는 value를 리턴
a.get("name", "fail")  # 'name'이라는 key가 없으므로 지정된 default 값인 'fail'을 리턴

# 해당 key가 dictionary에 있는지 조사 >> in
a = {1: "first", 2: "second", 3: "third"}
1 in a  # 1이 dictionary a의 key 중 하나이므로 True를 리턴
4 in a  # 4는 key가 아니므로 False를 리턴

a = list(1, 2, 3, 4, 5)
