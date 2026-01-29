import streamlit as st
import time
import random
from openai import OpenAI, RateLimitError

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Property Comparison",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# GLOBAL SAFE CSS (MATCH APP 1 & 3)
# -----------------------------
st.markdown("""
<style>
html, body, .stApp {
    background-color: #ffffff !important;
    color: #111827 !important;
}

h1, h2, h3 {
    color: #111827 !important;
}

/* Inputs */
textarea, input {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #D1D5DB !important;
}

/* Placeholder visibility */
textarea::placeholder,
input::placeholder {
    color: #6B7280 !important;
    opacity: 1 !important;
}

/* Button */
button {
    background-color: #111827 !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
}

/* Prevent scroll traps */
.main, .block-container {
    overflow: visible !important;
    max-height: none !important;
}

/* Markdown spacing */
.stMarkdown ul {
    padding-left: 1.2em;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:18px;">
        <h1>🏠 Property Comparison</h1>
        <p style="color:#555; font-size:15px; max-width:720px; margin:auto;">
            Objective comparison of property listings.
            No rankings. No recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown("### 🧾 Property Inputs")

with st.expander("Property A", expanded=True):
    property_a = st.text_area(
        label="",
        height=140,
        placeholder="Project name, price, size, location, possession, builder…",
        key="property_a_input"
    )

with st.expander("Property B", expanded=True):
    property_b = st.text_area(
        label="",
        height=140,
        placeholder="Project name, price, size, location, possession, builder…",
        key="property_b_input"
    )

with st.expander("Property C (Optional)", expanded=False):
    property_c = st.text_area(
        label="",
        height=130,
        placeholder="Optional third listing",
        key="property_c_input"
    )

st.markdown("### 🎯 Buyer Context (Optional)")
priority = st.text_input(
    label="",
    placeholder="Budget, possession timeline, location, rental yield, brand, etc."
)

st.markdown("<br>", unsafe_allow_html=True)

compare_clicked = st.button(
    "🔍 Compare Properties",
    use_container_width=True
)

# -----------------------------
# SYSTEM PROMPT (LOCKED – FINAL)
# -----------------------------
SYSTEM_PROMPT = """
You are a neutral real estate analyst.

Task:
Compare multiple property listings objectively for a homebuyer.

Input Handling Rules:
- Ignore any property input that is empty.
- Do NOT mention or reference missing properties.
- Analyze only listings that contain actual text.

Comparison Rules:
- Do NOT recommend or rank properties.
- Do NOT declare a winner.
- Do NOT assume facts.
- Clearly highlight differences, trade-offs, and risks.
- Explicitly state missing or unclear information ONLY for provided listings.
- Use simple, neutral, non-marketing language.

Tone:
- Factual
- Analytical
- Buyer-centric
- No persuasion

Output format (strict):

1. Comparison Snapshot
2. Key Differences
3. Trade-offs & Risks
4. Missing or Unclear Information
5. Best Suited Buyer Profiles
6. Questions the Buyer Must Ask
"""

# -----------------------------
# OPENAI CLIENT (SAFE)
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def compare_properties(prompt: str, retries=3) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.2,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()

        except RateLimitError:
            if attempt < retries - 1:
                time.sleep((2 ** attempt) + random.uniform(0.5, 1.5))
            else:
                raise

# -----------------------------
# OUTPUT SECTION
# -----------------------------
if compare_clicked:
    if not property_a.strip() or not property_b.strip():
        st.warning("Please provide at least Property A and Property B.")
    else:
        with st.spinner("Analyzing listings objectively…"):
            try:
                parts = [
                    f"Property A:\n{property_a.strip()}",
                    f"Property B:\n{property_b.strip()}"
                ]

                if property_c.strip():
                    parts.append(f"Property C:\n{property_c.strip()}")

                if priority.strip():
                    parts.append(
                        f"Buyer context (important factors):\n{priority.strip()}"
                    )

                user_prompt = "\n\n".join(parts)

                result = compare_properties(user_prompt)

                st.markdown("---")
                st.markdown("## 📊 Comparison Output")

                # ✅ SAFE OUTPUT (NO HTML)
                st.markdown(result)

            except RateLimitError:
                st.error(
                    "The tool is temporarily busy due to high usage. "
                    "Please wait a moment and try again."
                )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Neutral analysis • Built for clarity • No recommendations")
