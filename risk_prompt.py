from langchain.prompts import PromptTemplate

risk_template = PromptTemplate.from_template("""
You are an expert Financial Forensic Auditor and Risk Analyst.

Analyze the provided financial metrics below:
{metrics_table}

Your output must be a structured assessment covering:
1. **Risk Level:** Classify as "Low", "Medium", or "High".
2. **Key Flags:** Identify specific data points (e.g., high debt-to-equity, volatile cash flow) that drove this decision.
3. **Actionable Recommendations:** Provide 2-3 specific steps to mitigate the identified risks.

**Constraint:** Be professional, direct, and concise. Do not use conversational filler.

Analysis:
""")