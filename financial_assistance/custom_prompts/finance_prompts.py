def get_balance_sheet_prompt(balance_sheet):
    return f'''
        Consider the balance_sheet specified in back ticks.
        ```{balance_sheet}```
        - Summarize the overall outlook of the company from the balance sheet
        - Identify the  yearly trend of the relevant data.
        - If possible identify the key ratios from the balance sheet.
        - Identify the risk factors the company might face based on the balance sheet.
    '''
def get_income_stmnt_prompt(income_stmnt):
    return f'''
        Consider the income_statement specified in back ticks.
        ```{income_stmnt}```
        - Summarize the overall outlook of the company from the income statement
        - Identify the  yearly trend of the relevant data.
        - If possible identify the key ratios from the income statement.
        - Identify the risk factors the company might face based on the  income statement.
        - Identify key income sources
        - If possible identify Where the company looses money
    '''
def get_cash_flow_prompt(cash_flow):
    return f'''
        Consider the cashflow_statement specified in back ticks.
        ```{cash_flow}```
        - Summarize the overall outlook of the company from the cashflow_statement 
        - Identify the  yearly trend of the relevant data.
        - Identify the risk factors the company might face based on the cashflow statement .
        - If possible identify Where the company looses money
    '''
#Please note that a comprehensive analysis would require additional information from the income statement and cash flow statement to assess the company's profitability, liquidity, and cash flow position.