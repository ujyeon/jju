# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if st.button('Say hello'):
    st.write('쭈 안녕')



st.header('2. Radio button')
genre = st.radio('좋아하는 영화 장르를 선택해봐', ('코미디', 'SF', '액션'))

if genre == '코미디':
    st.write('유쾌하신 분이시군요')
elif genre == 'SF':
    st.write('스타워즈 아시나요')
else:
    st.write('미션 임파서블 보셨나요')



st.header('3. Checkbox')    # 😄
agree = st.checkbox('나랑 놀사람')
if agree:
    st.write('치킨먹으러 가장 💞')


st.header('4. Select box')
option = st.selectbox('주말에 어디로 놀러 갈래?', ('창원', '포항', '울산', '제주도'))
st.write('좋아', option, '에서 실컷 먹구 놀다 오자!!')

st.header('5. Multi select')
options = st.multiselect('좋아하는 음식을 모두 선택하세요', ['초밥', '회', '파스타', '피자', '떡볶이', '감자탕', '짬뽕', '우동'], ['회', '초밥'])
st.write('선호하는 음식:')
for i in options:
    st.write(i)



st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title =st.text_input('최애 영화를 입력하세요', '해리포터와 마법사의 돌')
st.write('당신이 가장 좋아하는 영화는', title, '이군요, 이번에 같이 봅시다')


st.subheader('**_number_input_**')
number = st.number_input('나이를 적어보세요', min_value=28, max_value=90, value=30, step=1)
st.write('당신의 나이는', number, '당신의 만나이는', number-1)


st.header('7. Date input')
ymd = st.date_input('우리 100일은 언제일까', datetime(2023, 10, 23))
st.write('100일은', ymd)

st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('몸무게가 어떻게 되세요?', 40, 130, 70)
st.write('My weight is', age, 'kg')

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('성인 이후 인생 최저, 최대 몸무게 구간을 선택하세요', 40.0, 130.0, (44.0, 70.0))
st.write('최대, 최저 몸무게:', values)


st.subheader('**_년 월 일 사이 구간_**')

slider_date = st.slider('휴가 신청기간을 선택하세요', datetime(2023,10,23), datetime(2023,12,31), value=(datetime(2023,10,23), datetime(2023,11,23)), format='YY/MM/DD')
st.write('휴가 신청기간:', slider_date)
st.write('휴가 시작일:', slider_date[0], '휴가 마지막일:', slider_date[1])






# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit0\4-1.input.py