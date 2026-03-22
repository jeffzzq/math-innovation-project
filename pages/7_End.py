import streamlit as st

# ------------------------------------------
# Page Configuration
# st.set_page_config(page_title="The Q.E.D. | The Math Roots", layout="centered")
# ------------------------------------------

st.title("∎ The Q.E.D.")
st.caption("*Quod Erat Demonstrandum — What was to be demonstrated.*")

st.markdown("""
We have traced the roots of reason from the mud of sheer necessity to the elegant axiomatization of the cosmos. You have witnessed the 'ghosts' of vanished quantities, the taming of infinity, and the rigorous mapping of chance. 

**But here lies a dangerous trap.**

After traveling through centuries of genius and madness, it is easy to believe that simply knowing the *story* is enough. It is easy to mistake the appreciation of the history for the mastery of the subject. 

Let us be absolutely clear: **Mathematics is not a spectator sport.**
""")

st.markdown("<br>", unsafe_allow_html=True)

# --- 1. Full-width History Block (气势磅礴的全宽展示) ---
st.info("""
#### ⚔️ The Bloody History of Reason
If you think math is a peaceful progression of truths, you haven't been paying attention. The foundations you stand on were built over the corpses of bitter rivalries and martyred geniuses:

* **The Calculus War:** Newton and Leibniz didn't just disagree; they accused each other of theft and plagiarism, splitting the mathematical world into two hostile camps for a century.
* **The War over Infinity:** Georg Cantor, who discovered that some infinities are bigger than others, was called a "scientific charlatan" and a "corrupter of youth" by Leopold Kronecker. The stress contributed to Cantor's multiple nervous breakdowns.
* **The Unrecognized Martyrs:**
    * **Niels Abel:** Proved the insolvability of the general quintic equation, yet his groundbreaking work was ignored by the French Academy and Gauss. He died penniless and in anonymity at 26, only to be recognized as a genius days too late.
    * **Évariste Galois:** Created Group Theory to unify algebra and geometry. His works were lost, declared "unintelligible" by Cauchy, and rejected by Poisson. He scribbled his final, revolutionary proofs on the eve of his death in a political duel at age 20.
* **The Hippasus Scandal:** Legend says the Pythagoreans drowned a man at sea just for proving that $\sqrt{2}$ is irrational—a truth that broke their religious belief in whole numbers.
""")

# --- 2. Symmetrical Argument Block (左右对称的灵魂拷问) ---
st.markdown("<br>", unsafe_allow_html=True)
col_e1, col_e2 = st.columns(2)

with col_e1:
    st.error("""
    #### 🚫 The Illusion of Shortcuts
    If these titans had to bleed, argue, be ignored, and lose their minds to define a single variable, **what makes you think you can master it in a weekend?** Their disputes weren't settled by 'vibes' or 'intuition.' They were settled by the exhausting, soul-crushing precision of the pen. There are absolutely no shortcuts waiting for us.
    """)

with col_e2:
    st.success("""
    #### ✏️ The Forge of Repetition
    The history provides the *why*, but only the pencil provides the *how*. 

    The formulas left behind are not museum artifacts to be admired—they are heavy tools. And you must learn to swing them. The roots of logic are deep, but they only grow when you water them with practice. 
    """)

st.markdown("---")

# --- 3. The Final Call to Action ---
st.markdown("""
<div style="text-align: center; padding: 40px; background-color: rgba(128, 128, 128, 0.05); border-radius: 10px;">
    <h3 style="color: gray; font-weight: normal; font-style: italic;">"The history of mathematics is profoundly heavy."</h3>
    <h1 style="margin-top: 10px; margin-bottom: 20px;">But the pencil in your hand is light.</h1>
    <p style="font-size: 1.1em; color: #555;">
        The chronicle is their legacy. The pencil is your weapon.<br>
        Use it until the logic is no longer a formula, but an instinct.<br>
        <b style="color: #ff4b4b; font-size: 1.2em;">Go back to the problems.</b>
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- 4. Interactive Button with the "Evil" Twist ---
col_btn1, col_btn2, col_btn3 = st.columns([1, 1.5, 1])
with col_btn2:
    if st.button("The Story is Over. Let's Get to Work. 🚀", use_container_width=True):
        st.balloons()  # 虚假的庆祝
        # 你的恶趣味暴击：从故事瞬间切换到考场现实
        st.toast("Pick up your pencil. Start your practice. Prepare for your exam.", icon="📝")