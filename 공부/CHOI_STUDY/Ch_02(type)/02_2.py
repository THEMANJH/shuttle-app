name = '최장혁'
age = 22
print(f"{name}은 {age}살이다.")

print(f'{3.141592:#^10.5f}')

#문자의 개수 카운팅(.count)
a='apple'
number_of_p = a.count('p')

print(number_of_p)

# 원하는 코드를 선택(드래그) 후 shift + enter를 누르면 그 부분만 실행

#위치 알려주기 1. {.find} (처음 등장하는 문자의 위치만 나타냄)

a='python is the best choice'
print(a.find('i'))

#찾는 문자열이 존재하지 않을 때는 -1을 반환함

#위치 알려주기 2. {.index} (처음 등장하는 문자의 위치만 나타냄)

a='python is the best choice'
print(a.index('i'))

#찾는 문자열이 존재하지 않을 때는 오류를 발생시킴

#문자열 삽입 {.join} (문자열 사이에 다른 문자열을 삽입)

print(",".join("abcd"))     #a,b,c,d
print(",".join("ab,cd"))    #a,b,,,c,d
print(",".join(["a","b","c","d"]))  #a,b,c,d (리스트에도 사용 가능)

#소문자를 대문자로 바꾸기 {.upper}
a='hi'
print(a.upper())    #HI

#대문자를 소문자로 바꾸기 {.lower}
a='HI'
print(a.lower())    #hi

#왼쪽 공백 지우기 {.lstrip}
a=' hi '
print(a.lstrip())   #hi

#오른쪽 공백 지우기 {.rstrip}
a=' hi '
print(a.rstrip())   # hi

#양쪽 공백 지우기 {.strip}
a=' hi '
print(a.strip())    #hi

#문자열 바꾸기 {.replace}
a='You only live once'
print(a.replace('You','Humans'))    #Humans only live once

#문자열 나누기 {.split}
a='You only live once'
print(a.split())    #['You', 'only', 'live', 'once']
#위 처럼 .split()에 괄호 안에 아무 값도 넣어주지 않으면 공백(띄워쓰기, 탭, 엔터)을 기준으로 나눔
#만약 괄호 안에 값을 넣어주면 그 값을 기준으로 나눔

#위의 경우들을 반환값이고 변수에 그 값을 대입하는 게 아님
#따라서, 변수에 저장하고 싶다면 변수에 저장해야 함

