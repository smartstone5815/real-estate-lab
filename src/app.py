import streamlit as st

# 1. 페이지 설정: 탭 제목만 설정
st.set_page_config(page_title="부동산 투자 분석 Lab", layout="wide")

# 2. GitHub 전문가 스타일 CSS: 가독성 및 UI 레이아웃 강제 교정
st.markdown("""
    <style>
    /* 배경 및 기본 텍스트 색상: GitHub의 깨끗한 흰색 바탕 */
    .stApp { background-color: #ffffff !important; color: #1f2328 !important; }
    
    /* [중요] 모든 제목, 라벨, 일반 텍스트를 진한 검정색으로 고정 */
    h1, h2, h3, label, p, span, .stMarkdown { color: #1f2328 !important; font-weight: 600 !important; }
    
    /* [중요] 입력창 내부 숫자 가독성: 배경은 흰색, 글자는 진한 검정 */
    input { 
        color: #1f2328 !important; 
        background-color: #ffffff !important;
        -webkit-text-fill-color: #1f2328 !important; 
    }
    
    /* 입력 박스 테두리: GitHub 스타일의 얇은 회색 선 */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #d0d7de !important;
        border-radius: 6px !important;
    }

    /* 사이드바: Navigation 텍스트 삭제 반영 및 연회색 배경 */
    [data-testid="stSidebar"] {
        background-color: #f6f8fa !important;
        border-right: 1px solid #d0d7de !important;
    }
    
    /* 사이드바 라디오 버튼에서 불필요한 아이콘/불렛 제거 효과 */
    [data-testid="stWidgetLabel"] p { font-size: 16px !important; }

    /* 버튼 스타일: GitHub Primary Green (#1f883d) */
    .stButton>button {
        background-color: #1f883d !important;
        color: #ffffff !important;
        border: 1px solid rgba(27,31,36,0.15) !important;
        border-radius: 6px !important;
        width: 100%;
    }

    /* GitHub 스타일의 구분 상자 */
    .gh-card {
        border: 1px solid #d0d7de;
        border-radius: 6px;
        padding: 24px;
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 사이드바 구성 (요청사항 반영) ---
with st.sidebar:
    st.write("") # 상단 여백
    # 'Navigation' 삭제, '분석대상' 명칭 변경, 아이콘 제거
    menu = st.radio(
        "분석대상",
        ["상가 분석", "오피스텔 분석", "투자 리포트"],
        index=0
    )
    st.divider()
    st.caption("v1.4.1 Production Ready")

# --- 4. 메인 화면 (상단 제목 라인 완전 삭제) ---
if menu == "상가 분석":
    st.header("🏢 상가 투자 수익률 분석")
    
    # GitHub Card 스타일 레이아웃
    st.markdown('<div class="gh-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💰 매수 계획**")
        price = st.number_input("매매가 (원)", value=500000000, step=10000000, format="%d")
        loan = st.number_input("대출금 (원)", value=300000000, step=10000000, format="%d")
        rate = st.number_input("대출 금리 (%)", value=5.0, step=0.1) / 100
    with col2:
        st.markdown("**📋 운영 계획**")
        depo = st.number_input("보증금 (원)", value=30000000, step=1000000, format="%d")
        rent = st.number_input("월세 (원)", value=2000000, step=100000, format="%d")
        v_rate = st.slider("공실률 (%)", 0, 30, 5) / 100
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("실행 분석 (Run Analysis)"):
        st.info("전문가용 분석 결과가 여기에 표시됩니다.")