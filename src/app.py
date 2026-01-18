import streamlit as st

# 1. 페이지 설정 (표준 레이아웃)
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

# 2. 사이드바 구성 (군더더기 제거)
with st.sidebar:
    st.title("분석 메뉴")
    menu = st.radio(
        "분석 대상을 선택하세요",
        ["상가 분석", "오피스텔 분석", "투자 리포트"]
    )
    st.divider()
    st.info("v1.8.0: 로직 중심 모델")

# 3. 메인 화면 - 상가 분석 로직
if menu == "상가 분석":
    st.header("🏢 상가 투자 수익률 분석")
    
    # 입력 구역을 두 개의 컬럼으로 분리
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 투자 자금")
        price = st.number_input("매매가 (원)", value=500000000, step=10000000, format="%d")
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        loan_rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1)
        
    with col2:
        st.subheader("📋 운영 수익")
        deposit = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        monthly_rent = st.number_input("월세 (원)", value=2000000, step=100000, format="%d")
        vacancy_rate = st.slider("공실률 (%)", 0, 30, 5)

    # 계산 로직 (간단한 예시)
    st.divider()
    if st.button("수익률 계산하기", use_container_width=True):
        # 실투자금 = 매매가 - 대출금 - 보증금
        actual_investment = price - loan - deposit
        # 연간 이자 비용
        annual_interest = loan * (loan_rate / 100)
        # 연간 순수익 = (월세 * 12 * (1 - 공실률)) - 연간 이자
        annual_net_income = (monthly_rent * 12 * (1 - vacancy_rate/100)) - annual_interest
        # 수익률
        roi = (annual_net_income / actual_investment) * 100 if actual_investment > 0 else 0

        # 결과 출력
        res_col1, res_col2 = st.columns(2)
        res_col1.metric("실투자금", f"{actual_investment:,} 원")
        res_col2.metric("예상 수익률", f"{roi:.2f} %")