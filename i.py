import streamlit as st 
  
st.title('조선 시대 화폐 가치 체감')
st.text('20209 김유진 한국사 프로젝트')

st.subheader('1냥 = 9만원')

import streamlit as st

def calculator():
    st.title("계산기")

    operation = st.radio("구매하고자 하는 물건을 선택하세요.", ('붓', '기와집', '노비', '말'))

    num2 = st.number_input("물건의 수량을 입력하세요(소수점x)")
    
    if operation == '붓':
        result = 9 * num2
        (result2) = 9 * result
        st.success(f'붓 {num2} 개를 사는 데에 {result} 냥이 필요합니다, 이는 {(result2)} 만원입니다.')
    elif operation == '기와집':
        result =  150 * num2
        (result2) = 9 * result
        st.success(f'기와집 {num2} 채를 사는 데에 {result} 냥이 필요합니다, 이는 {(result2)} 만원입니다.')
    elif operation == '노비':
        result = 8 * num2
        (result2) = 9 * result
        st.success(f'노비 {num2} 명을 고용하는 데에 {result} 냥이 필요합니다, 이는 {(result2)} 만원입니다.')
    elif operation == '말': 
        result = 40 * num2
        (result2) = 9 * result
        st.success(f'말 {num2} 마리를 사는 데에 {result} 냥이 필요합니다, 이는 {(result2)} 만원입니다.')
        
if __name__ == '__main__':
    calculator()
