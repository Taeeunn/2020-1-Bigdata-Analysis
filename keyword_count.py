import csv
f=open('data.csv', 'w', encoding='utf-8', newline='')
wr=csv.writer(f)

travel_list=['가나여행.txt','그리스여행.txt','나이지리아여행.txt','네덜란드여행.txt','네팔여행.txt','노르웨이여행.txt','뉴질랜드여행.txt','대만여행.txt',
             '덴마크여행.txt','독일여행.txt','두바이여행.txt','라오스여행.txt','러시아여행.txt', '룩셈부르크여행.txt', '마다가스카르여행.txt','멕시코여행.txt',
             '모나코여행.txt','모로코여행.txt','몰디브여행.txt','몰타여행.txt','몽골여행.txt','미국여행.txt','미얀마여행.txt','방글라데시여행.txt',
             '베트남여행.txt','벨기에여행.txt','볼리비아여행.txt','부탄여행.txt','불가리아여행.txt','사모아여행.txt','세르비아여행.txt','스웨덴여행.txt',
             '스위스여행.txt','스페인여행.txt','슬로바키아여행.txt','슬로베니아여행.txt','싱가포르여행.txt','아르헨티나여행.txt','아이슬란드여행.txt',
             '아일랜드여행.txt','아제르바이잔여행.txt','에스토니아여행.txt','에콰도르여행.txt','영국여행.txt','오스트리아여행.txt','우루과이여행.txt',
             '우즈베키스탄여행.txt','우크라이나여행.txt','이란여행.txt','이집트여행.txt','이탈리아여행.txt','인도네시아여행.txt','인도여행.txt','일본여행.txt',
             '조지아여행.txt','중국여행.txt','체코여행.txt','캐나다여행.txt','케냐여행.txt','콜롬비아여행.txt','쿠바여행.txt','쿠웨이트여행.txt',
             '크로아티아여행.txt','태국여행.txt','터키여행.txt','파라과이여행.txt','파키스탄여행.txt','팔라우여행.txt','페루여행.txt','포르투갈여행.txt',
             '폴란드여행.txt','프랑스여행.txt','핀란드여행.txt','필리핀여행.txt','헝가리여행.txt','호주여행.txt']


count=[0]*23

col_name=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U','V','W']
wr.writerow(col_name)

for m in range(0, len(travel_list)):
    data = open(travel_list[m], mode='rt', encoding='utf-8')
    count=[0]*23
    for i in range(0, 999):
        line_data = data.readline()
        if '가족여행' in line_data or '패밀리' in line_data:
            count[0]+=1
        if '신혼' in line_data or '커플' in line_data or '부부' in line_data or '허니문' in line_data:
            count[1] += 1
        if '우정' in line_data or '프렌드' in line_data or '친구' in line_data:
            count[2]+=1
        if '자유' in line_data or '배낭' in line_data:
            count[3]+=1
        if '패키지' in line_data or '가이드' in line_data or '투어' in line_data:
            count[4]+=1


        if '어학연수' in line_data or '유학' in line_data or '교환학생' in line_data:
            count[5]+=1
        if '워킹홀리데이' in line_data or '워홀' in line_data:
            count[6]+=1
        if '살기' in line_data or '거주' in line_data or '이민' in line_data:
            count[7]+=1
        if '휴가' in line_data or '방학' in line_data:
            count[8]+=1


        if '힐링' in line_data or '휴양' in line_data:
            count[9]+=1
        if '호캉스' in line_data or '호텔' in line_data or '리조트' in line_data:
            count[10]+=1
        if '액티비티' in line_data or '다이빙' in line_data or '번지' in line_data or '패러글라이딩' in line_data or '수영' in line_data \
                or '서핑' in line_data or '카약' in line_data or '요트' in line_data or '호핑' in line_data:
            count[11]+=1
        if '맛집' in line_data or '먹스타그램' in line_data or '먹방' in line_data or '음식' in line_data or '푸드' in line_data:
            count[12]+=1
        if '선물' in line_data or '기념품' in line_data or '쇼핑' in line_data or '지름신' in line_data:
            count[13]+=1
        if '플리마켓' in line_data or '시장' in line_data or '마켓' in line_data or '축제' in line_data or '페스티벌' in line_data:
            count[14]+=1
        if '바다' in line_data or '해변' in line_data or '비치' in line_data:
            count[15]+=1
        if '온천' in line_data or '스파' in line_data:
            count[16]+=1
        if '미술관' in line_data or '박물관' in line_data or '뮤지엄' in line_data or '유적' in line_data or '유산' in line_data or '문화' in line_data \
            or '궁' in line_data or '사원' in line_data:
            count[17]+=1
        if '캠핑' in line_data or '캠퍼밴' in line_data or '캠핑카' in line_data:
            count[18]+=1
        if '풍경' in line_data or '노을' in line_data or '야경' in line_data or '석양' in line_data or '일몰' in line_data or '오션뷰' in line_data \
                or '경치' in line_data or '하늘' in line_data:
            count[19]+=1
        if '등산' in line_data or '트래킹' in line_data or '하이킹' in line_data or '산책' in line_data or '순례길' in line_data:
            count[20]+=1
        if '자연' in line_data:
            count[21]+=1
        if '오로라' in line_data or '별' in line_data or '은하수' in line_data:
            count[22]+=1

    wr.writerow(count)

f.close()