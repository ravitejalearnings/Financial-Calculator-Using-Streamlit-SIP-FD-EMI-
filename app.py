import streamlit as st

st.title("Financial calculators")

choose_mode = st.selectbox("choose your calculator",["SIP","EMI","FD"])

if choose_mode == "SIP":
    st.subheader("SIP Calculator")

    p = st.number_input("Enter Monthly Investment Amount:- ", min_value= 0.0)
    annual_rate = st.number_input("Enter Annual Interest rate:- ", min_value= 0.0)
    n = st.number_input("Enter No.of Months:- ", min_value=1.0)

    r = annual_rate/12/100
    def sip_calculation(p, r, n):
        if r == 0:
            return round((p*n),2)
        sip_value = p * (((1 + r) ** n - 1) / r) * (1 + r)
        return round(sip_value, 2)

    total_invested = round((p * n), 2)
    total_value = sip_calculation(p, r, n)
    interest_earned = round((total_value - total_invested), 2)

    if st.button("Check"):
        st.write(f"{choose_mode} Calculation Summary:-")
        st.write(f"Total Investment         : {total_invested}")
        st.write(f"Interest Earned          : {interest_earned}")
        st.write(f"Total SIP Amount         : {total_value}")
        pass

elif choose_mode == "FD":
    st.subheader("FD Calculator")

    p = st.number_input("Enter Inital deposit:- ")
    annual_rate = st.number_input("Enter Annual Interest:- ")
    t = st.number_input("Enter duration in years:- ")

    r = annual_rate/100
    def fixed_deposit_calc(p,r,t):
        fd_cal = (p*r*t)
        return round(fd_cal,2)

    deposit_amt = p
    Maturity_amt = p + (fixed_deposit_calc(p,r,t))
    profit = Maturity_amt - deposit_amt

    if st.button("Check"):
        st.write(f"{choose_mode} Calculation Summary:-")
        st.write(f"Deposit Amount        : {deposit_amt}")
        st.write(f"Interest Earned       : {profit}")
        st.write(f"Maturity Amount       : {Maturity_amt}")

elif choose_mode == "EMI":
    st.subheader("EMI Calculator")

    p = st.number_input("Enter Loan Amount:- ")
    annual_rate = st.number_input("Enter Interest Rate: - ")
    n = st.number_input("Enter loan tenture in months:- ", min_value = 1)

    r = annual_rate/12/100

    def emi_calc(p,r,n):
        if r == 0:
            emi = (p/n)
        else:
            emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        return round(emi,2)

    total_interest_payable = round((emi_calc(p,r,n)*n)-p,2)
    total_payment = round((p+total_interest_payable),2)

    if st.button("Check"):
        st.write(f"Your Loan EMI is            : {emi_calc(p,r,n)}")
        st.write(f"Total Interest payable      : {total_interest_payable}")
        st.write(f"Total payment               : {total_payment}")

