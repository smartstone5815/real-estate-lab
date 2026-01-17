def calculate_commercial_roi(purchase_price, deposit, monthly_rent, loan_amount, interest_rate):
    """
    상가 투자 수익률 계산 함수
    """
    # 1. 취득세 (상가 기준 4.6%)
    acquisition_tax = purchase_price * 0.046
    
    # 2. 실투자금 (매매가 - 대출금 - 보증금 + 취득세)
    actual_investment = purchase_price - loan_amount - deposit + acquisition_tax
    
    # 3. 연간 이자 비용
    annual_interest = loan_amount * interest_rate
    
    # 4. 연간 순영업소득 (NOI) - 관리비/공실은 우선 제외한 기초 버전
    annual_income = monthly_rent * 12
    net_annual_cashflow = annual_income - annual_interest
    
    # 5. 수익률 계산 (ROE: 자기자본 수익률)
    roi = (net_annual_cashflow / actual_investment) * 100
    
    if actual_investment <= 0: return None
    roi = (net_annual_cashflow / actual_investment) * 100

    return {
        "actual_investment": actual_investment,
        "annual_cashflow": net_annual_cashflow,
        "roi": round(roi, 2)
    }

# --- 사용자 입력 부분 ---
print("=== 🏢 상가 투자 수익률 계산기 ===")
try:
    # 콤마(,)가 포함된 입력도 처리할 수 있게 문자열로 받아 처리
    price = int(input("1. 매매가(원)를 입력하세요: ").replace(',', ''))
    depo = int(input("2. 보증금(원)을 입력하세요: ").replace(',', ''))
    rent = int(input("3. 월세(원)를 입력하세요: ").replace(',', ''))
    loan = int(input("4. 대출금(원)을 입력하세요: ").replace(',', ''))
    rate = float(input("5. 대출금리(%)를 입력하세요 (예: 5.5): ")) / 100

    # 공실률 입력 받기 (기본값 5%)
    v_input = input("6. 예상 공실률(%) (미입력시 5%): ")
    vacancy_rate = float(v_input) / 100 if v_input else 0.05

    # 공실률이 반영된 실제 월세 수입 적용
    adjusted_rent = rent * (1 - vacancy_rate)

    result = calculate_commercial_roi(price, depo, adjusted_rent, loan, rate)

    if result:
        print("\n" + "="*40)
        print(f"▶ 적용 공실률: {vacancy_rate*100}%")
        print(f"▶ 실투자금: {result['actual_investment']:,}원")
        print(f"▶ 연간 순수익(공실반영): {result['annual_cashflow']:,}원")
        print(f"▶ 최종 수익률(ROE): {result['roi']}%")
        print("="*40)
    else:
        print("경고: 실투자금이 0보다 작거나 같습니다. 입력값을 확인하세요.")

except ValueError:
    print("오류: 숫자와 소수점만 사용하여 정확히 입력해 주세요.")



print(result)