import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pmt(rate, loan_term, present_value):
    '''
    Calculate Monthly Payment based on annual rate, loan_term, present value of loan
    rate: APR, annual rate
    loan_term: term of loan in years
    present_value: present value of loan
    '''
    r = rate/12
    n = loan_term*12
    p = present_value

    pay_int_to_n = (1+r)**n
    m = p*r*pay_int_to_n/(pay_int_to_n-1)

    return m

def principal_vs_interest_over_time(rate, loan_term, present_value):
    '''
    Calculate $$ of monthly payment allocated to principal and interest over
    the course of the loan based on annual rate, loan_term, present value of loan
    rate: APR, annual rate
    loan_term: term of loan in years
    present_value: present value of loan
    '''

    monthly_payment = pmt(rate, loan_term, present_value)
    number_of_payments = loan_term*12
    monthly_rate = rate/12
    total_principal = 0
    original_principal = present_value

    df = pd.DataFrame([], columns=['monthly_payment','interest','principal','value_after_payment','total_principal_paid'])
    for payment_month in range(number_of_payments):
        interest = present_value*monthly_rate
        principal = monthly_payment-interest
        #  update present value to new
        present_value = present_value - principal
        total_principal = total_principal + principal
        df.loc[payment_month,:] = [monthly_payment, interest, principal, present_value, total_principal]

    df = df.reset_index().rename({'index':'month'}, axis=1)
    df['interest_pct_payment'] = df['interest']/df['monthly_payment']
    df['principal_pct_payment'] = df['principal']/df['monthly_payment']
    df['percent_principal_paid_off'] = df['total_principal_paid']/original_principal

    return df

def plot_pct_of_payment_interest_vs_principal(df, interest_col='interest_pct_payment',\
        principal_col = 'principal_pct_payment'):

    fig, ax = plt.subplots(1,1, figsize=(12,8))
    ax.plot(df['month'], df['interest_pct_payment'], label='interest')
    ax.plot(df['month'], df['principal_pct_payment'], label='principal')
    # ax.plot(df['month'], df['value_after_payment'], label='remaining_loan_balance')
    fig.legend()
    ax.set_title('Percent of Monthly Payment Comprised of Interest vs Principal')
    ax.set_xlabel('Month')
    ax.set_ylabel('Percent')
    ax.set_yticklabels(['{:,.0%}'.format(x) for x in ax.get_yticks()])

    plt.show()

    return

def plot_principal_interest_percent_paid(df, month_col='month', \
        pct_paid_off_col='percent_principal_paid_off'):
    fig, ax = plt.subplots(1,1, figsize=(12,8))
    ax.plot(df[month_col]/12, df[pct_paid_off_col], label='Percent Principal Paid Off')
    halfway_there_mark = df[df[pct_paid_off_col]>=0.5].head(1)
    ax.scatter(halfway_there_mark[month_col]/12,halfway_there_mark[pct_paid_off_col], \
                label='Halfway: {} months'.format(halfway_there_mark[month_col].values[0]),\
                marker='*', color='darkorange', s=400)
    fig.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Percent')
    ax.set_title('Percent of Principal Paid Off')
    ax.set_yticklabels(['{:,.0%}'.format(x) for x in ax.get_yticks()])

    plt.show()

    return


if __name__=='__main__':

    rate = 0.03625
    loan_term = 15
    present_value=320000

    m = pmt(rate, loan_term, present_value)
    df = principal_vs_interest_over_time(rate, loan_term, present_value)

    plot_pct_of_payment_interest_vs_principal(df, interest_col='interest_pct_payment',\
            principal_col = 'principal_pct_payment')
    plot_principal_interest_percent_paid(df, month_col='month', \
            pct_paid_off_col='percent_principal_paid_off')
