# 뭐로 할까
# 코엔엘파이?? 트위터..

from konlpy.tag import Kkma
# from konlpy.tag import Twitter
kkma = Kkma()

line_list = []

line_list = []
f = open('test.txt', 'r', encoding='utf-8')
content = f.read()

filtered_content = content.replace('.', '').replace(',','').replace("'","").replace('·', ' ').replace('=','').replace('\n','')
Okt_morphs = kkma.pos(filtered_content)  # 튜플반환
print(Okt_morphs)