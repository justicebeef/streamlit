import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Lånekalkulator")

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

col1, col2 = st.columns(2)
home_value = col1.slider("Boligens verdi", min_value=1000000, value=5000000, max_value=13000000, step=100000)
deposit = col1.slider("Egenkapital", min_value=0, value=1000000, max_value=13000000, step=100000)
interest_rate = col2.slider(label="Rente ( % )",  min_value=1.5, max_value=8.0, value=5.5)
loan_term = col2.slider(label="Nedbetalingstid ( år )",  min_value=1, max_value=30, value=30)


# Calculate the repayments.
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

# Display the repayments.
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

# Endring
st.write("### Nedbetalingsplan")
col1, col2, col3 = st.columns(3)
col1.metric(label="Månedlig kostnad", value=f"{monthly_payment:,.0f} kr")
col2.metric(label=f"Totalkonstnad over {loan_term} år", value=f"{total_payments:,.0f} kr")
col3.metric(label="Rentekonstad", value=f"{total_interest:,.0f} kr")


# Create a data-frame with the payment schedule.
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)  # Calculate the year into the loan
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Display the data-frame as a chart.
st.write("### Nedbetalingsplan")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
interests_df = df[["Year", "Interest"]].groupby("Year").min()
data_df = df[["Year", "Remaining Balance", "Interest"]].groupby("Year").min()


st.line_chart(payments_df)

st.line_chart(interests_df)