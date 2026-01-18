import streamlit as st

# 1. 페이지 기본 설정 (GitHub의 정갈한 레이아웃을 위해 centered 사용)
st.set_page_config(
    page_title="smartstone5815 / real-estate-lab",
    page_icon="🏠",
    layout="centered"
)

# 2. GitHub 스타일 커스텀 CSS (디자인 요소 추가)
st.markdown("""
    <style>
    /* 배경색 및 폰트 */
    .stApp { background-color: #ffffff; }
    
    /* 제목 및 헤더: GitHub 리포지토리 상단 느낌 */
    h1 {
        font-weight: 600 !important;
        color: #1f2328 !important;
        border-bottom: 1px solid #d0d7de;
        padding-bottom: 12px;
        margin-bottom: 24px;
    }
    h3 { color: #1f2328; font-size: 1.2rem; }

    /* 입력창 디자인: GitHub 카드 스타일 */
    div.stNumberInput, div.stSlider {
        background-color: #f6f8fa;
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 10px;
    }

    /* 버튼 스타일: GitHub 'Success' 초록색 버튼 */
    .stButton>button {
        width: 100%;
        background-color: #1f883d !important;
        color: white !important;
        border-radius: 6px !important;
        border: 1px solid rgba(27, 31, 36, 0.15) !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
    }
    .stButton>button:hover {
        background-color: #1a7f37 !important;
    }

    /* 결과 메트릭 영역 */
    [data-testid="stMetricValue"] {
        color: #0969da !important; /* GitHub Link Blue 색상 */
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 계산 로직 (기존 기능 그대로 유지) ---
def calculate_commercial_roi(purchase_price, deposit, monthly_rent, loan_amount, interest_rate):
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
st.title("🏠 smartstone5815 / real-estate-lab")
st.caption("v1.0.0 • 부동산 투자 분석 실습용 저장소")

st.markdown("### 🏢 상가 투자 수익률 분석기")
st.info("GitHub 저장소 관리하듯 정밀하게 투자 수익률을 시뮬레이션 합니다.")

# 입력을 위한 레이아웃
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

st.write("") # 간격 조절

# 분석 실행 버튼
if st.button("Run Analysis (분석 실행)"):
    adjusted_rent = rent * (1 - v_rate)
    result = calculate_commercial_roi(price, depo, adjusted_rent, loan, rate)

    if result:
        st.divider()
        st.markdown("### 📊 분석 레포트")
        
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("실투자금", f"{int(result['actual_investment']):,} 원")
        res_col2.metric("연간 순수익", f"{int(result['annual_cashflow']):,} 원")
        res_col3.metric("최종 수익률", f"{result['roi']}%")
        
        st.write(f"💡 **분석 노트**: 취득세는 **{int(price * 0.046):,}원**으로 계산되었습니다.")
    else:
        st.error("오류: 실투자금이 0원 이하입니다. 설정을 확인해 주세요.")