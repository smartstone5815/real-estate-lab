import streamlit as st

# 1. 페이지 설정 (탭 제목부터 전문가 느낌으로)
st.set_page_config(page_title="smartstone5815 / real-estate-lab", page_icon="📝", layout="wide")

# 2. GitHub UI 복제 수준의 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경: GitHub 특유의 깨끗한 흰색 */
    .stApp { background-color: #ffffff !important; color: #1f2328 !important; }
    
    /* 폰트: GitHub 사용 폰트 스택 */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif !important;
    }

    /* 상단 영역: GitHub Repository 헤더 느낌 */
    .repo-header {
        background-color: #f6f8fa;
        border-bottom: 1px solid #d0d7de;
        padding: 16px 32px;
        margin: -60px -32px 32px -32px;
    }

    /* 입력 상자: 검은색 배경 삭제, GitHub 스타일의 흰색/회색 조합 */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #d0d7de !important;
        border-radius: 6px !important;
        box-shadow: inset 0 1px 0 rgba(208,215,222,0.2) !important;
    }
    input { color: #1f2328 !important; } /* 글자색 진한 검정 */
    
    /* 사이드바: 설정(Settings) 페이지 느낌 */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #d0d7de !important;
    }
    
    /* 버튼: GitHub 'Primary' 버튼 (초록색) */
    .stButton>button {
        background-color: #1f883d !important;
        color: #ffffff !important;
        border: 1px solid rgba(27,31,36,0.15) !important;
        border-radius: 6px !important;
        padding: 5px 16px !important;
        font-weight: 500 !important;
        font-size: 14px !important;
    }
    .stButton>button:hover {
        background-color: #1a7f37 !important;
        border-color: rgba(27,31,36,0.15) !important;
    }

    /* 섹션 구분: GitHub 'Box' 레이아웃 */
    .gh-box {
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 24px;
        margin-bottom: 24px;
    }
    </style>
    
    <div class="repo-header">
        <span style="color: #0969da; font-size: 20px;">smartstone5815</span> 
        <span style="color: #6e7781; font-size: 20px;">/</span> 
        <span style="color: #1f2328; font-size: 20px; font-weight: 600;">real-estate-lab</span>
        <span style="margin-left: 10px; padding: 2px 8px; border: 1px solid #d0d7de; border-radius: 20px; font-size: 12px; color: #6e7781;">Public</span>
    </div>
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

# --- 3. 사이드바 (깔끔한 텍스트 메뉴) ---
with st.sidebar:
    st.write("") # 상단 여백
    menu = st.radio(
        "분석대상",
        ["상가 분석", "오피스텔 분석", "투자 리포트"],
        index=0
    )
    st.divider()
    st.caption("Last commit: Just now")

# --- 4. 메인 화면 ---
if menu == "상가 분석":
    st.subheader("상가 투자 수익률 분석기")
    
    # GitHub Box 스타일 컨테이너
    with st.container():
        st.markdown('<div class="gh-box">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💰 Capital Plan")
            price = st.number_input("매매가 (Purchase Price)", value=500000000, step=10000000)
            loan = st.number_input("대출금 (Loan)", value=300000000, step=10000000)
            rate = st.number_input("대출 금리 (Interest Rate, %)", value=5.0, step=0.1) / 100
        with col2:
            st.markdown("### 📋 Operations")
            depo = st.number_input("보증금 (Deposit)", value=30000000, step=1000000)
            rent = st.number_input("월세 (Monthly Rent)", value=2000000, step=100000)
            v_rate = st.slider("공실률 (Vacancy, %)", 0, 30, 5) / 100
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Run Analysis"):
        res = calculate_commercial_roi(price, depo, rent * (1 - v_rate), loan, rate)
        if res:
            st.markdown("### Analysis Result")
            st.markdown('<div class="gh-box" style="background-color: #f6f8fa;">', unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.metric("Net Investment", f"{int(res['actual_investment']):,}원")
            c2.metric("Annual Net Income", f"{int(res['annual_cashflow']):,}원")
            c3.metric("ROI (ROE)", f"{res['roi']}%")
            st.markdown('</div>', unsafe_allow_html=True)