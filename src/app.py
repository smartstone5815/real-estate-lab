import streamlit as st

# 1. 페이지 설정 (최상단 라인 삭제 확인)
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

# 2. 마음에 들어하신 [화이트/라이트 그레이] 스타일 및 상단바 제거 CSS
st.markdown("""
    <style>
    /* [안전장치] Streamlit 기본 헤더 및 메뉴 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 전체 배경: 화이트 */
    .stApp { background-color: #ffffff !important; }
    
    /* 가독성: 모든 텍스트 진한 검정 고정 */
    h1, h2, h3, h4, label, p, span, div { 
        color: #1f2328 !important; 
        font-family: -apple-system, system-ui, sans-serif !important;
    }

    /* 사이드바: 라이트 그레이 */
    [data-testid="stSidebar"] {
        background-color: #f6f8fa !important;
        border-right: 1px solid #d0d7de !important;
    }

    /* 입력창: 흰색 배경 + 검정 숫자 (가독성 확보) */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #d0d7de !important;
        border-radius: 8px !important;
    }
    input {
        color: #1f2328 !important;
        -webkit-text-fill-color: #1f2328 !important;
    }

    /* 버튼: 마음에 들어하신 초록색 스타일 */
    .stButton>button {
        background-color: #2da44e !important;
        color: #ffffff !important;
        border: 1px solid rgba(27,31,36,0.15) !important;
        border-radius: 6px !important;
        width: 100%;
        height: 3em;
        font-weight: 600 !important;
    }

    /* 박스 구획 스타일 */
    .gh-card {
        border: 1px solid #d0d7de;
        border-radius: 8px;
        padding: 24px;
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 사이드바 (Navigation 글자 삭제 확인) ---
with st.sidebar:
    st.write("") # 상단 여백
    menu = st.radio(
        "분석대상",
        ["상가 분석", "오피스텔 분석", "투자 리포트"],
        index=0
    )
    st.divider()
    st.caption("v1.6.1 Verified")

# --- 4. 메인 화면 (헤더 라인 삭제 확인) ---
if menu == "상가 분석":
    # 최상단 제목 - 여기에 smartstone... 관련 텍스트가 없는지 다시 확인했습니다.
    st.subheader("상가 투자 수익률 분석기")
    
    st.markdown('<div class="gh-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 자금 계획")
        price = st.number_input("매매가 (원)", value=500000000, step=10000000, format="%d")
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1) / 100
        
    with col2:
        st.markdown("### 📋 운영 정보")
        depo = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        rent = st.number_input("월세 (원)", value=2000000, step=100000, format="%d")
        v_rate = st.slider("공실률 (%)", 0, 30, 5) / 100
        
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("분석 실행 (Run Analysis)"):
        st.success("데이터 로딩 완료")