import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

# 2. 사이드바
with st.sidebar:
    st.title("분석 메뉴")
    menu = st.radio("분석 대상을 선택하세요", ["상가 분석", "오피스텔 분석", "투자 리포트"])
    st.divider()
    st.info("v1.8.2: 상가 정밀 로직 모드")

# 3. 메인 화면 - 상가 분석 로직
if menu == "상가 분석":
    st.header("🏢 상가 투자 수익률 정밀 분석")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 초기 투자 비용")
        price = st.number_input("매매가격 (원)", value=500000000, step=10000000, format="%d")
        
        # [정교화 1] 상가 취득 부대비용 (취득세 4.6% + 중개/법무 약 0.4% = 약 5%)
        # 실제 현장에서는 매매가의 약 5%를 부대비용으로 잡습니다.
        acquisition_tax = int(price * 0.046)
        extra_fee = int(price * 0.004) # 중개보수 및 법무비용
        total_initial_cost = acquisition_tax + extra_fee
        
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        _, sub_col = st.columns([0.1, 0.9])
        with sub_col:
            loan_rate = st.number_input("└ 대출금리 (%)", value=5.0, step=0.1)
        
        # [요청 반영] 자기자금 계산 (매매가격 - 대출금 + 부대비용)
        # 진정한 의미의 자기자금은 부대비용까지 포함된 '내 주머니에서 나가는 총액'입니다.
        own_capital = price - loan + total_initial_cost
        st.write("")
        st.markdown(f"**💡 총 소요 자기자금: {own_capital:,} 원**")
        st.caption(f"└ 순수 매매잔금: {price-loan:,}원 / 부대비용: {total_initial_cost:,}원")
        
    with col2:
        st.subheader("📋 임대 및 운영 정보")
        deposit = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        monthly_rent = st.number_input("월세 (원)", value=2500000, step=100000, format="%d")
        
        # [정교화 2] 관리비 및 수선유지비 (월세의 3~5% 수준)
        maintenance_cost = st.slider("기타 운영경비 (월세의 %)", 0, 10, 3)
        vacancy_rate = st.slider("공실률 (%)", 0, 30, 5)

    st.divider()
    
    # 4. 정밀 계산 로직
    if st.button("전문가 리포트 생성", use_container_width=True):
        # 실투자금(현금흐름) = 총 자기자금 - 임대보증금
        actual_cash_needed = own_capital - deposit
        
        # 수입 계산
        gross_annual_rent = monthly_rent * 12
        effective_gross_income = gross_annual_rent * (1 - (vacancy_rate / 100))
        
        # 지출 계산
        annual_interest = loan * (loan_rate / 100)
        annual_op_cost = (monthly_rent * (maintenance_cost / 100)) * 12
        
        # 순수익
        annual_net_income = effective_gross_income - annual_interest - annual_op_cost
        roi = (annual_net_income / actual_cash_needed) * 100 if actual_cash_needed > 0 else 0

        # 5. 결과 대시보드
        st.subheader("📊 분석 결과 리포트")
        res1, res2, res3 = st.columns(3)
        res1.metric("실제 투입 현금", f"{actual_cash_needed:,} 원")
        res2.metric("연간 순수익", f"{int(annual_net_income):,} 원")
        res3.metric("최종 수익률", f"{roi:.2f} %")
        
        with st.expander("📌 세부 산출 근거"):
            st.write(f"- 취득세 및 교육세(4.6%): {acquisition_tax:,} 원")
            st.write(f"- 기타 부대비용(중개/법무): {extra_fee:,} 원")
            st.write(f"- 연간 이자 비용: {int(annual_interest):,} 원")
            st.write(f"- 연간 운영 경비: {int(annual_op_cost):,} 원")