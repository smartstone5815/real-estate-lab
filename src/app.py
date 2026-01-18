import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

# 2. 선택하신 다크톤 대시보드 스타일 CSS
st.markdown("""
    <style>
    /* 전체 배경: 나노바나나 이미지의 짙은 다크그레이 톤 */
    .stApp { 
        background-color: #0d1117 !important; 
    }
    
    /* 상단 메뉴 및 불필요한 요소 제거 */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* 사이드바: 본문보다 약간 더 어두운 톤으로 분리 */
    [data-testid="stSidebar"] {
        background-color: #010409 !important;
        border-right: 1px solid #30363d !important;
    }

    /* 텍스트 색상: 다크모드 전용 밝은 회색/화이트 */
    h1, h2, h3, h4, label, p, span, div { 
        color: #c9d1d9 !important; 
    }

    /* 입력 박스: 나노바나나 스타일의 다크 카드 디자인 */
    div[data-baseweb="input"] {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }
    
    /* [가독성] 입력창 숫자: 밝은 화이트로 선명하게 표시 */
    input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* 버튼: GitHub 스타일의 그린 버튼 */
    .stButton>button {
        background-color: #238636 !important;
        color: #ffffff !important;
        border: 1px solid rgba(240,246,252,0.1) !important;
        border-radius: 6px !important;
        padding: 12px !important;
        width: 100%;
        font-weight: 600 !important;
    }

    /* 중앙 카드 컨테이너 */
    .gh-main-card {
        border: 1px solid #30363d;
        border-radius: 6px;
        padding: 30px;
        background-color: #161b22;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 사이드바 (깔끔한 텍스트 메뉴) ---
with st.sidebar:
    st.write("")
    menu = st.radio(
        "분석대상",
        ["상가 분석", "오피스텔 분석", "투자 리포트"],
        index=0
    )
    st.divider()
    st.caption("v1.7.0 Dark Dashboard")

# --- 4. 메인 화면 (나노바나나 레이아웃 복제) ---
if menu == "상가 분석":
    st.title("🏠 상가 투자 수익률 분석기")
    st.write("") # 간격
    
    st.markdown('<div class="gh-main-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 💰 Capital Plan (자금 계획)")
        price = st.number_input("매매가 (원)", value=500000000, step=10000000, format="%d")
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1) / 100
        
    with col2:
        st.markdown("#### 📄 Operations (운영 정보)")
        depo = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        rent = st.number_input("월세 (원)", value=2000000, step=100000, format="%d")
        v_rate = st.slider("공실률 (%)", 0, 30, 5) / 100
    
    st.write("")
    if st.button("실행 분석 (Run Analysis)"):
        st.success("분석 결과 데이터가 준비되었습니다.")
    st.markdown('</div>', unsafe_allow_html=True)