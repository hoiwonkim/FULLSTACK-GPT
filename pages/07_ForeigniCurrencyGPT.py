# 필요한 라이브러리 및 모듈 불러오기
from langchain.schema import SystemMessage
import streamlit as st
import requests
from typing import Type
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from langchain.agents import initialize_agent, AgentType
from sklearn.linear_model import LinearRegression
import numpy as np
from datetime import datetime, timedelta

# Streamlit의 secrets 기능을 사용하여 API 키 불러오기
openai_api_key = st.secrets["OPENAI_API_KEY"]
open_exchange_rates_api_key = st.secrets["OPEN_EXCHANGE_RATES_API_KEY"]

# ChatOpenAI 객체 생성 및 llm 변수에 할당
llm = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo-1106", openai_api_key=openai_api_key)

# 환율 정보 검색 도구 클래스 정의
class ExchangeRateToolArgsSchema(BaseModel):
    base_currency: str = Field(description="기준 통화. 예: USD, EUR")
    target_currency: str = Field(description="대상 통화. 예: KRW, JPY")

class ExchangeRateTool(BaseTool):
    name = "ExchangeRateTool"
    description = "기준 통화와 대상 통화 간의 환율을 확인하는 도구입니다."
    args_schema: Type[ExchangeRateToolArgsSchema] = ExchangeRateToolArgsSchema

    def _run(self, base_currency, target_currency):
        # USD를 기준 통화로 사용
        r = requests.get(
            f"https://openexchangerates.org/api/latest.json?app_id={open_exchange_rates_api_key}&base=USD"
        )
        data = r.json()

        # NZD로 환산하는 로직
        if base_currency == "NZD":
            nzd_rate = self._convert_to_nzd(data['rates'], target_currency)
            return f"The current exchange rate of {target_currency} against NZD is {nzd_rate}."
        else:
            # 다른 통화에 대한 처리
            if 'rates' not in data:
                return f"API response does not contain 'rates' data. Response: {data}"
            
            rate = data['rates'].get(target_currency)
            if rate is None:
                return f"Cannot find exchange rate information for {target_currency}."

            return f"The current exchange rate of {target_currency} against {base_currency} is {rate}."
    
    def _convert_to_nzd(self, rates, target_currency):
        nzd_to_usd = rates['NZD']
        target_to_usd = rates.get(target_currency)

        if target_to_usd is None:
            return f"{target_currency}에 대한 환율 정보를 찾을 수 없습니다."

        return target_to_usd / nzd_to_usd

# 환율 변동 예측 및 거래 추천 도구 클래스 정의
class CurrencyTradeRecommendationTool(BaseTool):
    name = "CurrencyTradeRecommendationTool"
    description = "환율 변동을 예측하고 어떤 통화를 거래할지 추천하는 도구입니다."
    args_schema: Type[ExchangeRateToolArgsSchema] = ExchangeRateToolArgsSchema

    def _run(self, base_currency, target_currency):
        # 지난 일주일 간의 환율 데이터 가져오기
        historical_rates = self._get_historical_rates(base_currency, target_currency)

        # 추세 분석
        trend = self._analyze_trend(historical_rates)

        # 추세에 따른 거래 추천
        recommendation = "상승 추세입니다. 매수를 추천합니다." if trend > 0 else "하락 추세입니다. 매도를 추천합니다."
        return recommendation

    def _get_historical_rates(self, base_currency, target_currency):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        dates = [start_date + timedelta(days=i) for i in range(7)]
        rates = []
        for date in dates:
            formatted_date = date.strftime('%Y-%m-%d')
            r = requests.get(
                f"https://openexchangerates.org/api/historical/{formatted_date}.json?app_id={open_exchange_rates_api_key}&base=USD"
            )
            data = r.json()
            if 'rates' not in data or target_currency not in data['rates']:
                continue  # API 응답에 'rates'가 없거나, 대상 통화 정보가 없는 경우 건너뛰기
            rates.append(data['rates'][target_currency] / data['rates']['NZD'])  # USD 대비 환율을 NZD로 환산

        return rates

    def _analyze_trend(self, rates):
        X = np.arange(len(rates)).reshape(-1, 1)
        y = rates
        model = LinearRegression().fit(X, y)
        return model.coef_[0]

# 에이전트 초기화
agent = initialize_agent(
    llm=llm,
    verbose=True,
    agent=AgentType.OPENAI_FUNCTIONS,
    handle_parsing_errors=True,
    tools=[
        ExchangeRateTool(),
        CurrencyTradeRecommendationTool(),
    ],
    agent_kwargs={
        "system_message": SystemMessage(
            content="""
            당신은 금융 분석가입니다.
            
            외환 시장을 분석하고 환율 예측에 기반한 통화 거래에 대한 추천을 제공합니다.
        """
        )
    },
)

# Streamlit 페이지 구성
st.set_page_config(
    page_title="PAYTHON",
    page_icon="💼",
)

st.markdown(
    """
    # ForeignCurrency
            
    FCC에 오신 것을 환영합니다.
            
    거래하고자 하는 기준 통화와 대상 통화의 이름을 입력하십시오.
"""
)

# 기준 통화와 대상 통화 입력 받기
base_currency = st.text_input("기준 통화를 입력하세요", value="NZD")
target_currency = st.text_input("대상 통화를 입력하세요 (예: KRW, JPY, AUD)")

# 입력값이 모두 존재할 경우 에이전트 호출
if base_currency and target_currency:
    input_data = {"input": {"base_currency": base_currency, "target_currency": target_currency}}
    result = agent.invoke(input_data)
    st.write(result["output"].replace("$", "\$"))
