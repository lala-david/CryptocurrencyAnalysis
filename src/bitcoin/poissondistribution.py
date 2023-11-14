import streamlit as st
import math

def attacker_success_probability(q, z):
    # 공격자 블록 생성하지 못할 확률 
    # q는 공격자가 블록 생성할 확률 
    p = 1.0 - q
    # z (블록 생성 수)
    lambda_ = z * (q / p)
    # 확률의 총합을 저장  
    sum_ = 1.0
    for k in range(z+1):
        # 푸아송 분포의 확률 계산 
        poisson = math.exp(-lambda_)
        for i in range(1, k+1):
            poisson *= lambda_ / i
            # 공격자의 성공 확률을 계산하고 총합함 
        sum_ -= poisson * (1 - ((q / p) ** (z - k)))
    return sum_

st.title('🐸 공격자의 성공 확률')

q = st.number_input('공격자가 블록을 생성할 확률(q)', min_value=0.0, max_value=1.0, step=0.01)
z = st.number_input('블록 수(z)', min_value=0, max_value=100, step=1)

if st.button('계산'):
    result = attacker_success_probability(q, z)
    st.write('공격자의 성공 확률: {:.20f}'.format(result))

