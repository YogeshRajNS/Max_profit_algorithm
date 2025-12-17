import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(layout="wide", page_title="Max Profit")

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Base Styles */
body {
    background: radial-gradient(circle at top, #0b1220, #020617);
    color: #e5e7eb;
}

.block-container {
    padding-top: 2rem;
}

/* Base Card Style */
.card {
    background: linear-gradient(180deg, #020617, #020617);
    border: 1px solid #1e293b;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 0 25px rgba(0,0,0,0.6);
    margin-bottom: 1rem;
}

.muted {
    color: #94a3b8;
    font-size: 14px;
}

.highlight {
    color: #facc15;
    font-weight: 700;
}

.big {
    font-size: 38px;
    font-weight: 800;
    color: #facc15;
}

ul.muted {
    padding-left: 20px;
}

/* --- CRITICAL NEW CSS OVERRIDES FOR SINGLE LEFT CARD --- */

/* 1. Remove padding/margin from the Streamlit element that wraps the entire column */
/* This is often a generic wrapper like st-emotion-cache-x... */
[data-testid="stVerticalBlock"] > div:first-child { 
    gap: 0px !important; /* Removes gap between elements in the column */
}

/* 2. Target the number input and remove its default margin/padding */
.stNumberInput {
    padding-top: 0px !important;
    margin-top: -10px !important; /* Adjust negative margin to pull it up */
    margin-bottom: 10px !important;
}

/* 3. Target the button and remove its default margin */
.stButton {
    margin-top: 5px !important; /* Keep a little space below the input */
    margin-bottom: 0px !important;
}

/* 4. Ensure the number input field itself is styled */
.st-emotion-cache-12tqulq {
    background-color: #0b1220 !important;
    border-color: #1e293b !important;
}

/* --- END OF CRITICAL NEW CSS OVERRIDES --- */

</style>
""", unsafe_allow_html=True)

# ---------------- LOGIC ----------------
def max_profit_all_solutions(n):
    dp = [-1] * (n + 1)
    solutions = [set() for _ in range(n + 1)] 

    dp[0] = 0
    solutions[0].add((0, 0, 0))

    for t in range(1, n + 1):
        current_best_solutions = set()
        
        # 1. Commercial Park (Time: 10, Profit: 2000)
        if t >= 10 and dp[t-10] != -1:
            profit = dp[t-10] + (n - t) * 2000
            
            if profit > dp[t]:
                dp[t] = profit
                current_best_solutions = {(T, P, C+1) for T, P, C in solutions[t-10]}
            elif profit == dp[t]:
                current_best_solutions.update((T, P, C+1) for T, P, C in solutions[t-10])

        # 2. Theatre (Time: 5, Profit: 1500)
        if t >= 5 and dp[t-5] != -1:
            profit = dp[t-5] + (n - t) * 1500
            
            if profit > dp[t]:
                dp[t] = profit
                current_best_solutions = {(T+1, P, C) for T, P, C in solutions[t-5]}
            elif profit == dp[t]:
                current_best_solutions.update((T+1, P, C) for T, P, C in solutions[t-5])

        # 3. Pub (Time: 4, Profit: 1000)
        if t >= 4 and dp[t-4] != -1:
            profit = dp[t-4] + (n - t) * 1000
            
            if profit > dp[t]:
                dp[t] = profit
                current_best_solutions = {(T, P+1, C) for T, P, C in solutions[t-4]}
            elif profit == dp[t]:
                current_best_solutions.update((T, P+1, C) for T, P, C in solutions[t-4])

        if current_best_solutions:
            solutions[t] = current_best_solutions
            
    max_profit = max(dp)
    result = []

    for t in range(n + 1):
        if dp[t] == max_profit:
            for T, P, C in solutions[t]:
                result.append({"Theatre": T, "Pub": P, "Commercial": C})

    return max_profit, result


# ---------------- TITLE ----------------
st.markdown("## 🏗 Available Properties")

# ---------------- PROPERTY CARDS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="card">
    <h4>🎭 Theatre</h4>
    <div class="muted">Build Time</div> 5 units<br>
    <div class="muted">Land</div> 2×1<br><br>
    <div class="muted">Earning / Unit</div>
    <span class="highlight">$1,500</span><br>
    <div class="muted">Efficiency</div>
    <span class="highlight">$300 / time</span>
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="card">
    <h4>🍺 Pub</h4>
    <div class="muted">Build Time</div> 4 units<br>
    <div class="muted">Land</div> 1×1<br><br>
    <div class="muted">Earning / Unit</div>
    <span class="highlight">$1,000</span><br>
    <div class="muted">Efficiency</div>
    <span class="highlight">$250 / time</span>
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="card">
    <h4>🏢 Commercial Park</h4>
    <div class="muted">Build Time</div> 10 units<br>
    <div class="muted">Land</div> 3×1<br><br>
    <div class="muted">Earning / Unit</div>
    <span class="highlight">$2,000</span><br>
    <div class="muted">Efficiency</div>
    <span class="highlight">$200 / time</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT + OUTPUT ----------------
left, right = st.columns([1, 1.2])

with left:
    # START OF THE SINGLE LEFT CARD WRAPPER
    # st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # 1. Time Input Section
    st.markdown("<h4>⏱ Time Input</h4>", unsafe_allow_html=True)
    
    # Interactive elements must be called directly, outside the container for optimal layout control
    n = st.number_input("Total Time Units (n)", min_value=0, value=12, label_visibility="collapsed")
    run = st.button("📊 Calculate Maximum Profit", type="primary")

    # Add a visual separator (line break)
    st.markdown("<hr style='border: 1px solid #1e293b; margin: 15px 0;'>", unsafe_allow_html=True)

    # 2. Rules Section (Static text)
    st.markdown("<h4>📜 Rules</h4>", unsafe_allow_html=True)
    st.markdown("""
    <ul class="muted">
        <li>Only one building at a time</li>
        <li>Land is unlimited</li>
        <li>Earnings start after construction</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # END OF THE SINGLE LEFT CARD WRAPPER
    st.markdown("</div>", unsafe_allow_html=True)


with right:
    if run:
        profit, sols = max_profit_all_solutions(n)
        num_ways = len(sols)

        # Max Profit Card (Separate card for the header)
        st.markdown(f"""
<div class="card" style="text-align:center;">
    <div class="muted">MAXIMUM PROFIT FOR {n} TIME UNITS</div>
    <div class="big">${profit:,}</div>
    <div class="muted">Number of ways to achieve this profit:</div>
    <div class="highlight">{num_ways}</div>
</div>
""", unsafe_allow_html=True)

        # Solutions List (Separate card for each solution)
        for idx, s in enumerate(sols, 1):
            
            total_units = s['Theatre']*5 + s['Pub']*4 + s['Commercial']*10
            
            # Conditionally build the content list HTML
            content_html = ""
            if s['Theatre'] > 0:
                content_html += f"🎭 Theatre × <span class='highlight'>{s['Theatre']}</span><br>"
            if s['Pub'] > 0:
                content_html += f"🍺 Pub × <span class='highlight'>{s['Pub']}</span><br>"
            if s['Commercial'] > 0:
                content_html += f"🏢 Commercial Park × <span class='highlight'>{s['Commercial']}</span><br>"

            # Use st.html() for guaranteed HTML rendering for each solution card
            st.html(f"""
<div class="card">
    <h4>📊 Solution {idx}</h4>
    {content_html}
    <div style="margin-top:10px;" class="muted">Total Time Units Used: <span class='highlight'>{total_units}</span></div>
</div>
""")