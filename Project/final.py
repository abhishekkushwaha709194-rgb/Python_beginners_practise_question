import streamlit as st
import sympy as sp
from openai import OpenAI
import os
#here we put our api key
client = OpenAI(api_key="")

# xdefining x as mathematical variable 
x = sp.symbols('x')

# explanation through ai api 
def ai_explain(problem, result, operation):
    try:
        prompt = f"""
        Solve this {operation} problem step by step.

        Problem: {problem}
        Answer: {result}

        Explain clearly like a teacher in simple steps.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI explanation error: {e}"

#user interface
st.title("AI Calculus Solver")
st.caption("Use * for multiplication and ** for powers (e.g., x**2 + 3*x)")

operation = st.selectbox("Choose operation", ["Derivative", "Integral"])

#deravative 
if operation == "Derivative":
    expr_input = st.text_input("Enter expression")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)
            result = sp.diff(expr, x)

            st.success(f"Final Answer: {result}")

            #Ai explanation
            explanation = ai_explain(expr_input, result, operation)

            st.subheader("🤖 AI Explanation:")
            st.write(explanation)

        except Exception as e:
            st.error(f"Error: {e}")

#integration
elif operation == "Integral":
    expr_input = st.text_input("Enter expression")
    lower = st.text_input("Lower limit (optional)")
    upper = st.text_input("Upper limit (optional)")

    if st.button("Solve"):
        try:
            expr = sp.sympify(expr_input)

            if lower and upper:
                result = sp.integrate(expr, (x, float(lower), float(upper)))
            else:
                result = sp.integrate(expr, x)

            st.success(f"Final Answer: {result}")

            # 🔥 AI Explanation
            explanation = ai_explain(expr_input, result, operation)

            st.subheader("🤖 AI Explanation:")
            st.write(explanation)

        except Exception as e:
            st.error(f"Error: {e}")