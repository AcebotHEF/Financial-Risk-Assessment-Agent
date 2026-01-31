from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from risk_data import get_financial_profile
from risk_prompt import risk_template

# Load environment variables (API Key)
load_dotenv()

def analyze_risk():
    """
    Fetches financial data and generates an AI risk assessment using Gemini.
    """
    # 1. Get the data from your data module
    df = get_financial_profile()
    
    # Convert DataFrame to a string format the AI can read
    table = df.to_string(index=False)

    # 2. Initialize Gemini (Using the lighter 'flash' model for speed)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

    # 3. Create the Chain (Prompt -> LLM)
    chain = risk_template | llm

    # 4. Invoke the chain
    # We pass the dictionary matching the variable {metrics_table} in your template
    response = chain.invoke({"metrics_table": table})

    # Return the original dataframe (for the UI table) and the AI's text response
    return df, response.content