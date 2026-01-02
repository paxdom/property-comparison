Here is a **clean, production-ready `README.md`** for **App 2: Property Comparison**, written in the **same philosophy, tone, and structure** as your reference — but correctly aligned to the comparison use-case.

You can copy-paste this directly.

---

````md
# 🏠 Property Comparison by PaXdom Realty  
### A Neutral AI Tool for Comparing Real Estate Listings Objectively

**Property Comparison** is an AI-powered tool built by **PaXdom Realty** to help homebuyers objectively compare multiple property listings side by side.

It transforms raw, often inconsistent or marketing-heavy listing text into a **clear, structured comparison** — highlighting differences, trade-offs, risks, and missing information **without recommending or ranking properties**.

This tool is fully neutral: it does **not** declare winners, promote projects, or provide buying advice.  
Its sole purpose is **clarity, transparency, and informed decision-making**.

---

## Why PaXdom Built This Tool

At PaXdom Realty, we observed that buyers often struggle to compare properties because:
- Listings use different formats and vague language
- Pros and cons are rarely stated clearly
- Important details are missing or buried
- Comparisons are driven by emotion or broker bias

**Property Comparison** applies a neutral analytical lens so buyers can:
- See differences clearly  
- Understand trade-offs and risks  
- Identify missing or unclear information  
- Ask sharper questions before deciding  

---

## What the App Does (V1)

### Inputs
- **Property A**: Raw listing text  
- **Property B**: Raw listing text  
- **Property C (Optional)**: Additional listing  
- **Optional buyer context** (e.g. budget, possession, location, rental yield)

Listings can be pasted from:
- WhatsApp broker messages  
- Property portals  
- Brochures or PDFs (text)  

---

### Output (Fixed Structure)

The app produces a structured comparison with:

1. Comparison Snapshot  
2. Key Differences  
3. Trade-offs & Risks  
4. Missing or Unclear Information  
5. Best Suited Buyer Profiles  
6. Questions the Buyer Must Ask  

---

## Core Principles

- Neutral and factual  
- No rankings or winners  
- No recommendations  
- No marketing or persuasive language  
- Missing information is explicitly highlighted  

---

## What the App Does NOT Do

- ❌ Recommend or rank properties  
- ❌ Declare a “best” option  
- ❌ Replace legal, financial, or site due diligence  
- ❌ Analyze external links or PDFs (V1 is text-only)  
- ❌ Act as a sales or lead-generation tool  

---

## Technology Stack

- **Frontend**: Streamlit  
- **AI Model**: OpenAI (`gpt-4o-mini`)  
- **Language**: Python 3.11  

Chosen for:
- Low cost  
- High reliability  
- Predictable, controlled outputs  

---

## Running the App Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Set OpenAI API key

Create the file:

```
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "sk-xxxx"
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

---

## Cost Notes

Approximate usage cost:

* ₹0.20 – ₹0.50 per comparison
  (depending on number and length of listings)

---

## Product Philosophy

PaXdom Realty builds tools based on three principles:

1. **Clarity over persuasion**
2. **Transparency over conversion**
3. **Buyer trust over short-term sales**

This is a **decision-support tool**, not a sales funnel.

---

## Explore More PaXdom AI Tools

Discover the full ecosystem at:
**[https://www.paxdomrealty.com/ai-property-tools](https://www.paxdomrealty.com/ai-property-tools)**

---

## Disclaimer

This tool provides **informational analysis only**.

It does **not** constitute legal, financial, or investment advice.
Users must independently verify all information and consult professionals when required.

---

## License
