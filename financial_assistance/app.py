import streamlit as st
import yfinance as yf
import os
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from custom_prompts import finance_prompts
from langchain.chat_models import ChatOpenAI
load_dotenv(find_dotenv(), override=True)

chat_gpt = ChatOpenAI(model='gpt-4', temperature=0.5, max_tokens=1024)

st.title('Financial Assistant')


def fetch_financial_data(ticker):
    ticker_info = yf.Ticker(ticker)
    return ticker_info.balance_sheet, ticker_info.income_stmt, ticker_info.cash_flow


ticker = st.text_input('Enter a symbol')
if ticker:
    balance_sheet, income_stmt, cash_flow = fetch_financial_data(ticker)
    st.write('Balance Sheet')
    messages = [
        SystemMessage(
            content="Consider yourself as an expert financial analyst"),
        HumanMessage(
            content=finance_prompts.get_balance_sheet_prompt(balance_sheet))
    ]
    reply = chat_gpt(messages=messages)
    st.write(balance_sheet)
    st.write(reply.content)
    st.write('Income Statement')
    messages = [
        SystemMessage(
            content="Consider yourself as an expert financial analyst"),
        HumanMessage(
            content=finance_prompts.get_income_stmnt_prompt(balance_sheet))
    ]
    reply = chat_gpt(messages=messages)
    st.write(income_stmt)
    st.write(reply.content)
    st.write('Cashflow Statement')
    messages = [
        SystemMessage(
            content="Consider yourself as an expert financial analyst"),
        HumanMessage(
            content=finance_prompts.get_cash_flow_prompt(cash_flow))
    ]
    reply = chat_gpt(messages=messages)
    st.write(cash_flow)
    st.write(reply.content)
    
