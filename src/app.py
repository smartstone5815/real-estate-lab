import streamlit as st

def calculate_commercial_roi(purchase_price, deposit, monthly_rent, loan_amount, interest_rate):
    """상가 투자 수익률 계산 로직"""
    acquisition_tax = purchase_price * 0.046
    actual_investment = purchase_price - loan_amount - deposit + acquisition_tax
    annual_interest = loan_amount * interest_rate
    annual_income = monthly_rent * 12
    net_annual_cashflow = annual_income - annual_interest
    
    if actual_investment <= 0: return None
    roi = (net_annual_cashflow / actual_investment) * 100
    return {
        "actual_investment": actual_investment,
        "annual_cashflow": net_annual_cashflow,
        "roi": round(roi, 2)
    }

# --- 웹 화면 구성 ---
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

st.title("🏢 상가 투자 수익률 분석기")
st.info("터미널에서 입력하던 정보를 아래 입력창에 기입해 주세요.")

# 입력을 위한 레이아웃 분할
col_in1, col_in2 = st.columns(2)

with col_in1:
    st.subheader("💰 매수 및 자금 계획")
    # value=0으로 설정하면 빈 칸처럼 직접 입력을 유도할 수 있습니다.
    price = st.number_input("1. 매매가 (원 단위)", value=500000000, step=10000000, format="%d")
    loan = st.number_input("2. 대출금 (원 단위)", value=300000000, step=10000000, format="%d")
    rate = st.number_input("3. 대출 금리 (%)", value=5.0, step=0.1) / 100

with col_in2:
    st.subheader("📋 임대 운영 정보")
    depo = st.number_input("4. 보증금 (원 단위)", value=30000000, step=1000000, format="%d")
    rent = st.number_input("5. 월세 (원 단위)", value=2000000, step=100000, format="%d")
    v_rate = st.slider("6. 예상 공실률 (%)", 0, 30, 5) / 100

st.divider()

# 계산 버튼 (클릭 시 실행되는 터미널의 느낌을 줌)
if st.button("투자 수익률 분석 실행"):
    adjusted_rent = rent * (1 - v_rate)
    result = calculate_commercial_roi(price, depo, adjusted_rent, loan, rate)

    if result:
        st.success("✅ 분석이 완료되었습니다.")
        
        # 결과 표시 영역
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("실투자금 (내 현금)", f"{int(result['actual_investment']):,} 원")
        res_col2.metric("연간 순수익 (공실 반영)", f"{int(result['annual_cashflow']):,} 원")
        res_col3.metric("최종 수익률 (ROE)", f"{result['roi']}%")
        
        # 상세 요약
        st.write(f"ℹ️ **안내**: 취득세는 매매가의 4.6%인 **{int(price * 0.046):,}원**이 가산되었습니다.")
    else:
        st.error("오류: 실투자금이 0원 이하입니다. 매매가나 대출금 설정을 확인해 주세요.")