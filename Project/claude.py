import streamlit as st
import sympy as sp
from sympy import symbols, diff, integrate, latex, simplify, oo, sin, cos, tan, exp, ln, sqrt

# Page config
st.set_page_config(
    page_title="Calculus Solver",
    page_icon="∫",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=JetBrains+Mono:wght@300;400;600&display=swap');

    /* Root theme */
    :root {
        --bg: #0a0a0f;
        --card: #111118;
        --accent: #c8a96e;
        --accent2: #e8c98e;
        --text: #e8e4dc;
        --muted: #6b6880;
        --border: #2a2838;
        --glow: rgba(200, 169, 110, 0.15);
    }

    .stApp {
        background-color: var(--bg);
        color: var(--text);
        font-family: 'JetBrains Mono', monospace;
    }

    /* Hide default streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 2rem; max-width: 760px;}

    /* Title */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.2rem;
        font-weight: 900;
        color: var(--accent);
        text-align: center;
        letter-spacing: -0.02em;
        margin-bottom: 0.2rem;
        line-height: 1;
    }
    .sub-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        color: var(--muted);
        text-align: center;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 2.5rem;
    }

    /* Mode selector tabs */
    .stRadio > div {
        display: flex;
        gap: 0;
        background: var(--card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 4px;
        justify-content: center;
    }
    .stRadio label {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
        color: var(--muted) !important;
        padding: 8px 28px !important;
        border-radius: 6px !important;
        cursor: pointer !important;
    }
    .stRadio [data-checked="true"] label {
        background: var(--accent) !important;
        color: var(--bg) !important;
    }

    /* Input fields */
    .stTextInput input, .stSelectbox select {
        background: var(--card) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--text) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 1rem !important;
        padding: 12px 16px !important;
    }
    .stTextInput input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px var(--glow) !important;
    }

    /* Labels */
    .stTextInput label, .stSelectbox label, .stRadio label {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.75rem !important;
        color: var(--muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }

    /* Button */
    .stButton > button {
        background: var(--accent) !important;
        color: var(--bg) !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Playfair Display', serif !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        padding: 12px 40px !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        background: var(--accent2) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 24px var(--glow) !important;
    }

    /* Result card */
    .result-card {
        background: var(--card);
        border: 1px solid var(--border);
        border-left: 3px solid var(--accent);
        border-radius: 8px;
        padding: 1.5rem 1.8rem;
        margin-top: 1.5rem;
    }
    .result-label {
        font-size: 0.65rem;
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 0.2em;
        margin-bottom: 0.8rem;
        font-family: 'JetBrains Mono', monospace;
    }
    .result-expr {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: var(--text);
        word-break: break-all;
    }

    /* Error */
    .error-card {
        background: #1a0f0f;
        border: 1px solid #5a2020;
        border-left: 3px solid #c84040;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin-top: 1rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        color: #e88080;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 1px solid var(--border);
        margin: 1.5rem 0;
    }

    /* Hint text */
    .hint {
        font-size: 0.72rem;
        color: var(--muted);
        font-family: 'JetBrains Mono', monospace;
        margin-top: 0.4rem;
    }

    /* Columns spacing */
    .row-widget.stHorizontal {gap: 12px;}
</style>
""", unsafe_allow_html=True)


# ── Header ──────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">∫ Calculus</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Symbolic Solver · SymPy Engine</div>', unsafe_allow_html=True)

# ── Mode selector ────────────────────────────────────────────────────────────
mode = st.radio(
    "Operation",
    ["Derivative", "Integral"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Helpers ──────────────────────────────────────────────────────────────────
def parse_expr(expr_str, var):
    """Parse expression string safely with sympy."""
    local_dict = {
        'x': var, 'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
        'exp': sp.exp, 'ln': sp.ln, 'log': sp.log, 'sqrt': sp.sqrt,
        'pi': sp.pi, 'e': sp.E, 'abs': sp.Abs, 'asin': sp.asin,
        'acos': sp.acos, 'atan': sp.atan, 'sinh': sp.sinh,
        'cosh': sp.cosh, 'tanh': sp.tanh,
    }
    return sp.sympify(expr_str, locals=local_dict)


def render_result(label, expr):
    latex_str = latex(expr)
    st.markdown(f"""
        <div class="result-card">
            <div class="result-label">{label}</div>
            <div class="result-expr">{latex_str}</div>
        </div>
    """, unsafe_allow_html=True)
    # Also render with st.latex for proper math rendering
    st.latex(latex_str)


# ── Shared input ─────────────────────────────────────────────────────────────
x = symbols('x')

expression = st.text_input(
    "Expression",
    placeholder="e.g.  x**3 + sin(x)*exp(x)",
    help="Use Python/SymPy syntax"
)
st.markdown('<div class="hint">Supported: sin cos tan exp ln sqrt pi e abs asin acos atan sinh cosh tanh</div>',
            unsafe_allow_html=True)


# ── Derivative UI ─────────────────────────────────────────────────────────────
if mode == "Derivative":
    order = st.selectbox(
        "Order",
        [1, 2, 3, 4, 5],
        format_func=lambda n: f"{n}{'st' if n==1 else 'nd' if n==2 else 'rd' if n==3 else 'th'} derivative"
    )

    if st.button("Solve  →  d/dx"):
        if not expression.strip():
            st.markdown('<div class="error-card">⚠ Please enter an expression.</div>', unsafe_allow_html=True)
        else:
            try:
                expr = parse_expr(expression.strip(), x)
                result = diff(expr, x, order)
                result = simplify(result)
                label = f"d{'²' if order==2 else '³' if order==3 else str(order) if order>3 else ''}/dx{'²' if order==2 else '³' if order==3 else str(order) if order>3 else ''} of expression"
                render_result(label, result)
            except Exception as e:
                st.markdown(f'<div class="error-card">⚠ Error: {e}</div>', unsafe_allow_html=True)


# ── Integral UI ───────────────────────────────────────────────────────────────
else:
    st.markdown('<div class="hint" style="margin-bottom:0.6rem">Leave limits blank for indefinite integral</div>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        lower = st.text_input("Lower limit  (a)", placeholder="e.g.  0  or  -oo")
    with col2:
        upper = st.text_input("Upper limit  (b)", placeholder="e.g.  pi  or  oo")

    if st.button("Solve  →  ∫ dx"):
        if not expression.strip():
            st.markdown('<div class="error-card">⚠ Please enter an expression.</div>', unsafe_allow_html=True)
        else:
            try:
                expr = parse_expr(expression.strip(), x)

                # Determine definite vs indefinite
                has_lower = lower.strip() != ""
                has_upper = upper.strip() != ""

                if has_lower and has_upper:
                    # Definite integral
                    inf_map = {'oo': oo, 'inf': oo, '-oo': -oo, '-inf': -oo,
                               'pi': sp.pi, 'e': sp.E}
                    def parse_limit(s):
                        s = s.strip()
                        if s in inf_map:
                            return inf_map[s]
                        return sp.sympify(s)

                    a = parse_limit(lower)
                    b = parse_limit(upper)
                    result = integrate(expr, (x, a, b))
                    result = simplify(result)
                    render_result(f"Definite integral from {lower} to {upper}", result)

                elif not has_lower and not has_upper:
                    # Indefinite integral
                    result = integrate(expr, x)
                    result = simplify(result)
                    render_result("Indefinite integral  ( + C )", result)

                else:
                    st.markdown(
                        '<div class="error-card">⚠ Please provide BOTH limits or leave BOTH empty.</div>',
                        unsafe_allow_html=True
                    )

            except Exception as e:
                st.markdown(f'<div class="error-card">⚠ Error: {e}</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<div class="hint" style="text-align:center">Powered by SymPy · Streamlit</div>',
    unsafe_allow_html=True
)