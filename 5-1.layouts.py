import streamlit as st

st.title('Unit 5. Layouts & Containers')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/layout')

# sidebar- with 사용하기 📧  📱  ☎︎
with st.sidebar:
    st.header('소통 방식')


add_selectbox = st.sidebar.selectbox('어디로 연락 드릴까요?',
                                    ('Email', '휴대전화', '오피스 번호'))



if add_selectbox == 'Email':
    st.sidebar.title('📧')
elif add_selectbox == '휴대전화':
    st.sidebar.title('📱')
else:
    st.sidebar.title('☎︎')





# columns  
# 고양이 https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb
# 개     https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb
# 부엉이 https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb

st.header('2. Columns')
col1, col2, col3 = st.columns(3)
with col1:
    st.text('고양이')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb')
with col2:
    st.text('강아지')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb')
    
with col3:
    st.text('올빼미')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb')


    
# tabs - width=200

st.header('3. Tabs')
tab1, tab2, tab3 = st.tabs(['고양이', '강아지', '올빼미'])

with tab1:
    st.caption('고양이')
    st.image('https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?auto=compress&cs=tinysrgb', width=200)

with tab2:
    st.caption('강아지')
    st.image('https://images.pexels.com/photos/3361739/pexels-photo-3361739.jpeg?auto=compress&cs=tinysrgb', width=200)
    
with tab3:
    st.caption('올빼미')
    st.image('https://images.pexels.com/photos/3737300/pexels-photo-3737300.jpeg?auto=compress&cs=tinysrgb', width=200)


    
# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit0\5-1.layouts.py