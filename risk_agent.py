from risk_data import get_financial_profile
from risk_prompt import risk_template
from langchain.chat_models import ChatOpenAI

def analyze_risk():
    df = get_financial_profile()
    table = df.to_string(index=False)

    llm = ChatOpenAI(temperature=0.3)
    prompt = risk_template.format(metrics_table=table)
    result = llm.predict(prompt)
    return df, result