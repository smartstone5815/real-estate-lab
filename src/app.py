import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="smartstone5815 / real-estate-lab",
    page_icon="🏠",
    layout="wide" # 사이드바가 있으므로 wide가 더 보기 좋습니다.
)

# 2. GitHub 스타일 커스텀 CSS
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1 {
        font-weight: 600 !important;
        color: #1f2328 !important;
        border-bottom: 1px solid #d0d7de;
        padding-bottom: 12px;
    }
    /* 사이드바 스타일 커스텀 */
    [data-testid="stSidebar"] {
        background-color: #f6f8fa;
        border-right: 1px solid #d0d7de;
    }
    /* 버튼 스타일 */
    .stButton>button {
        width: 100%;
        background-color: #1f883d !important;
        color: white !important;
        border-radius: 6px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 상가 분석 로직 함수 ---
def calculate_commercial_roi(purchase_price, deposit, monthly_rent, loan_amount, interest_rate):
    acquisition_tax = purchase_price * 0.046
    actual_investment = purchase_price - loan_amount - deposit + acquisition_tax
    annual_interest = loan_amount * interest_rate
    annual_income = monthly_rent * 12
    net_annual_cashflow = annual_income - annual_interest
    if actual_investment <= 0: return None
    roi = (net_annual_cashflow / actual_investment) * 100
    return {"actual_investment": actual_investment, "annual_cashflow": net_annual_cashflow, "roi": round(roi, 2)}

# --- 3. 사이드바 메뉴 구성 ---
with st.sidebar:
    st.title("📂 Navigation")
    st.markdown("---")
    # 메뉴 선택 (라디오 버튼)
    menu = st.radio(
        "분석 도구를 선택하세요",
        ["🏢 상가 분석", "🏠 오피스텔 분석 (준비중)", "📊 투자 요약 리포트"],
        index=0
    )
    st.divider()
    st.caption("Owner: smartstone5815")
    st.caption("v1.1.0 Update")

# --- 4. 메뉴별 화면 출력 ---
st.title("🏠 smartstone5815 / real-estate-lab")

if menu == "🏢 상가 분석":
    st.markdown("### 🏢 상가 투자 수익률 분석기")
    
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        st.markdown("**💰 자금 계획**")
        price = st.number_input("매매가 (원)", value=500000000, step=10000000, format="%d")
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1) / 100
    with col_in2:
        st.markdown("**📋 운영 정보**")
        depo = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        rent = st.number_input("월세 (원)", value=2000000, step=100000, format="%d")
        v_rate = st.slider("예상 공실률 (%)", 0, 30, 5) / 100

    if st.button("Run Analysis"):
        result = calculate_commercial_roi(price, depo, rent * (1 - v_rate), loan, rate)
        if result:
            st.divider()
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("실투자금", f"{int(result['actual_investment']):,} 원")
            res_col2.metric("연간 순수익", f"{int(result['annual_cashflow']):,} 원")
            res_col3.metric("최종 수익률", f"{result['roi']}%")
        else:
            st.error("실투자금 설정을 확인해 주세요.")

elif menu == "🏠 오피스텔 분석 (준비중)":
    st.markdown("### 🏠 오피스텔 투자 분석 (Coming Soon)")
    st.info("주거용/업무용 세금 체계를 반영한 업데이트가 곧 진행될 예정입니다.")
    st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?ixlib=rb-1.2.1&auto=format&fit=crop&w=1353&q=80", caption="오피스텔 분석 모듈 준비중")

else:
    st.markdown("### 📊 투자 요약 리포트")
    st.write("다양한 매물의 수익률을 한눈에 비교할 수 있는 대시보드입니다.")