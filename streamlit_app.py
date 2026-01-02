import streamlit as st
from openai import OpenAI

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="PaXdom Property Comparison",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:16px;">
        <h2 style="margin-bottom:6px;">🏠 PaXdom Property Comparison</h2>
        <p style="color:#555; font-size:15px;">
            Objective comparison of property listings. No rankings. No recommendations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown("### 🧾 Property Inputs")

with st.container():
    with st.expander("Property A", expanded=True):
        property_a = st.text_area(
            "Paste listing details",
            height=130,
            placeholder="Example: Project name, price, size, location, possession, builder...",
            key="property_a_input"
        )

    with st.expander("Property B", expanded=True):
        property_b = st.text_area(
            "Paste listing details",
            height=130,
            placeholder="Example: Project name, price, size, location, possession, builder...",
            key="property_b_input"
        )

    with st.expander("Property C (Optional)", expanded=False):
        property_c = st.text_area(
            "Paste listing details",
            height=120,
            placeholder="Optional third listing",
            key="property_c_input"
        )

st.markdown("### 🎯 Buyer Context (Optional)")
priority = st.text_input(
    "What matters most to you?",
    placeholder="Budget, possession timeline, location, rental yield, brand, etc."
)

# -----------------------------
# CTA
# -----------------------------
st.markdown("<br>", unsafe_allow_html=True)
compare_clicked = st.button("🔍 Compare Properties", use_container_width=True)

# -----------------------------
# SYSTEM PROMPT (LOCKED)
# -----------------------------
SYSTEM_PROMPT = """
You are a neutral real estate analyst.

Task:
Compare multiple property listings objectively for a homebuyer.

Input Handling Rules:
- If a property input is empty or not provided, completely ignore it.
- Do NOT mention, reference, or evaluate missing property inputs.
- Do NOT say “no information provided” for optional properties.
- Only analyze and compare properties that contain actual listing text.

Comparison Rules:
- Do NOT recommend or rank properties.
- Do NOT declare a winner.
- Do NOT assume facts.
- Clearly highlight differences, trade-offs, and risks.
- Explicitly state missing or unclear information ONLY for properties that are provided.
- Use simple, non-marketing, neutral language.

Tone:
- Factual
- Analytical
- Buyer-centric
- No sales or persuasion language.

Output format (strict):

1. Comparison Snapshot
2. Key Differences
3. Trade-offs & Risks
4. Missing or Unclear Information
5. Best Suited Buyer Profiles
6. Questions the Buyer Must Ask
"""

# -----------------------------
# OUTPUT SECTION
# -----------------------------
if compare_clicked:
    if not property_a.strip() or not property_b.strip():
        st.warning("Please provide at least Property A and Property B.")
    else:
        with st.spinner("Analyzing listings objectively..."):
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            # -----------------------------
            # BUILD PROMPT DYNAMICALLY
            # -----------------------------
            user_prompt_parts = []

            user_prompt_parts.append(f"Property A:\n{property_a.strip()}")
            user_prompt_parts.append(f"Property B:\n{property_b.strip()}")

            if property_c.strip():
                user_prompt_parts.append(f"Property C:\n{property_c.strip()}")

            if priority.strip():
                user_prompt_parts.append(
                    f"Buyer context (important factors to consider):\n{priority.strip()}"
                )

            user_prompt = "\n\n".join(user_prompt_parts)

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2
            )

        st.markdown("---")
        st.markdown("## 📊 Comparison Output")

        with st.container():
            st.markdown(
                f"""
                <div style="
                    background:#FAFAFA;
                    border:1px solid #E5E7EB;
                    border-radius:8px;
                    padding:18px;
                    line-height:1.6;
                    font-size:15px;
                ">
                {response.choices[0].message.content}
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("PaXdom AI Tools • Neutral analysis • Built for informed decisions")
