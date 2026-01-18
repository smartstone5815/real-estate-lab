import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="smartstone5815 / real-estate-lab", page_icon="🏠", layout="wide")

# 2. 모든 디자인 오류를 수정한 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경 흰색 및 글자색 진한 검정으로 고정 */
    .stApp { background-color: #ffffff; color: #1f2328; }
    
    /* 제목 및 부제목 가독성 강화 */
    h1, h2, h3, p, span, label { color: #1f2328 !important; font-weight: 600 !important; }
    
    /* 입력창(Number Input) 디자인 수정: 배경은 연회색, 글자는 검정 */
    div[data-baseweb="input"] { background-color: #f6f8fa !important; border-radius: 6px !important; }
    input { color: #1f2328 !important; }
    
    /* 버튼 스타일 */
    .stButton>button {
        width: 100%; background-color: #1f883d !important; color: white !important;
        border: 1px solid rgba(27,31,36,0.15); border-radius: 6px; padding: 10px;
    }
    
    /* 사이드바 배경 및 구분선 */
    [data-testid="stSidebar"] { background-color: #f6f8fa !important; border-right: 1px solid #d0d7de; }
    </style>
    """, unsafe_allow_html=True)

# --- 계산 로직 ---
def calculate_commercial_roi(purchase_price, deposit, monthly_rent, loan_amount, interest_rate):
    acquisition_tax = purchase_price * 0.046
    actual_investment = purchase_price - loan_amount - deposit + acquisition_tax
    annual_interest = loan_amount * interest_rate
    annual_income = monthly_rent * 12
    net_annual_cashflow = annual_income - annual_interest
    if actual_investment <= 0: return None
    roi = (net_annual_cashflow / actual_investment) * 100
    return {"actual_investment": actual_investment, "annual_cashflow": net_annual_cashflow, "roi": round(roi, 2)}

# --- 사이드바 ---
with st.sidebar:
    st.markdown("### 📂 Navigation")
    menu = st.radio("분석 메뉴를 선택하세요", ["🏢 상가 분석", "🏠 오피스텔 분석", "📊 리포트"], index=0)
    st.divider()
    st.caption("smartstone5815 / v1.2.0")

# --- 메인 화면 ---
st.title("🏠 smartstone5815 / real-estate-lab")

if menu == "🏢 상가 분석":
    st.subheader("🏢 상가 투자 수익률 분석기")
    col1, col2 = st.columns(2)
    with col1:
        price = st.number_input("매매가 (원)", value=500000000, step=10000000)
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000)
        rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1) / 100
    with col2:
        depo = st.number_input("보증금 (원)", value=30000000, step=1000000)
        rent = st.number_input("월세 (원)", value=2000000, step=100000)
        v_rate = st.slider("예상 공실률 (%)", 0, 30, 5) / 100

    if st.button("Run Analysis"):
        res = calculate_commercial_roi(price, depo, rent * (1 - v_rate), loan, rate)
        if res:
            st.divider()
            c1, c2, c3 = st.columns(3)
            c1.metric("실투자금", f"{int(res['actual_investment']):,}원")
            c2.metric("연 순수익", f"{int(res['annual_cashflow']):,}원")
            c3.metric("최종 수익률", f"{res['roi']}%")