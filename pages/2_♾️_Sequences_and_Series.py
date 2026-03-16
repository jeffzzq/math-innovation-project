import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math
import scipy.stats as stats

# ==========================================
# 页面配置 (让页面变成宽屏，更适合展示数学公式和图表)
# ==========================================
st.set_page_config(page_title="Sequences & Series", page_icon="♾️", layout="wide")


def show_sequence_page():
    st.header("🌌 Topic 2: The Rhythm of Infinity (Sequences & Series)")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Decompressing Sigma (How it works)",
        "2. Arithmetic (AP) and Geometric (GP) Progression",
        "3. Hall of Fame (The Logic)",
        "4. Pascal to Normal",
        "5. Taylor Series (Expansion)"
    ])

    # ==========================================
    # TAB 1: Sigma 慢动作拆解
    # ==========================================
    with tab1:
        st.subheader("Step 1: The Difference between Sequence & Series")
        st.markdown("Before we start calculating, we must distinguish two words:")

        c_def1, c_def2 = st.columns(2)
        with c_def1:
            st.info("""
                **Sequence ($T_n$)**
                An ordered **list** of items.
                * "How big is the slice at step $n$?"
                * Example: $1, 2, 4, 8...$
                """)
        with c_def2:
            st.success("""
                **Series ($S_n$)**
                The **total sum** of the items so far.
                * "How much cake have we eaten in total?"
                * Example: $1 + 2 + 4 + 8...$
                """)

        st.markdown("---")

        st.subheader("Step 2: Visual Experiment")
        st.write("Let's look at a specific Sequence: **Halving the Cake**.")

        col_vis_ctrl, col_vis_plot = st.columns([1, 2])

        with col_vis_ctrl:
            n_cuts = st.slider("Number of Cuts (n)", 1, 8, 3)
            st.write(f"At step **n={n_cuts}**, we add a slice of size:")
            st.latex(rf"T_{{{n_cuts}}} = \frac{{1}}{{{2 ** n_cuts}}}")

        with col_vis_plot:
            fig = go.Figure()
            fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1, line=dict(color="gray", width=2))

            x_curr, y_curr, w, h, direction = 0, 0, 1, 1, 0
            colors = ['#FF2E63', '#08D9D6', '#252A34', '#EAEAEA']
            terms_latex = []

            for i in range(n_cuts):
                denom = 2 ** (i + 1)
                terms_latex.append(rf"\frac{{1}}{{{denom}}}")

                if direction == 0:
                    w = w / 2
                    fig.add_shape(type="rect", x0=x_curr, y0=y_curr, x1=x_curr + w, y1=y_curr + h,
                                  fillcolor=colors[i % 4], line=dict(color="black", width=1), opacity=0.9)
                    if i < 4: fig.add_annotation(x=x_curr + w / 2, y=y_curr + h / 2, text=f"T{i + 1}", showarrow=False,
                                                 font=dict(size=14, color="white"))
                    x_curr += w
                    direction = 1
                else:
                    h = h / 2
                    fig.add_shape(type="rect", x0=x_curr, y0=y_curr, x1=x_curr + w, y1=y_curr + h,
                                  fillcolor=colors[i % 4], line=dict(color="black", width=1), opacity=0.9)
                    if i < 4: fig.add_annotation(x=x_curr + w / 2, y=y_curr + h / 2, text=f"T{i + 1}", showarrow=False,
                                                 font=dict(size=14, color="white"))
                    y_curr += h
                    direction = 0

            fig.update_layout(width=400, height=300, xaxis=dict(visible=False), yaxis=dict(visible=False),
                              margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        st.subheader("Step 3: The Problem (Calculation)")
        st.write("Now, if we want to calculate the **Total Area (Series)**, we have to add them up:")

        long_sum_str = " + ".join(terms_latex)
        st.latex(rf"S_{{{n_cuts}}} = {long_sum_str}")

        if n_cuts >= 5:
            st.error(f"😫 **It's getting too long!** Imagine if n=100. Writing this out is impossible.")
        else:
            st.warning("It's manageable now, but what if n=100?")

        st.markdown("---")

        st.subheader("Step 4: The 'Lazy' Solution ($\sum$)")
        st.markdown("""
            Mathematicians are famously lazy. They hate writing long strings of numbers.
            So, they invented a **Compression Machine** called **Sigma**.
            """)

        c_sigma_vis, c_sigma_exp = st.columns([1, 1.5])

        with c_sigma_vis:
            st.markdown("#### The Anatomy")
            st.latex(r"\sum_{Start}^{End} Rule")
            st.caption("It acts like a 'Loop' in coding.")

        with c_sigma_exp:
            st.markdown("#### How to read it:")
            st.markdown(f"""
                1.  **$\sum$**: "Sum everything up..."
                2.  **$k=1$ (Bottom)**: "...starting from slice #1..."
                3.  **${n_cuts}$ (Top)**: "...stopping at slice #{n_cuts}..."
                4.  **$1/2^k$ (Right)**: "...using this formula for each slice."
                """)

        st.markdown("#### The Result:")
        st.latex(
            rf"S_{{{n_cuts}}} = \sum_{{k=1}}^{{{n_cuts}}} \frac{{1}}{{2^k}} = {sum([1 / 2 ** i for i in range(1, n_cuts + 1)]):.6f}")

    # ==========================================
    # TAB 2: AP 和 GP
    # ==========================================
    with tab2:
        st.header("🧬 Topic 3: The Limit of Growth")
        st.caption("From Discrete Progressions to the Continuous Constant (e)")

        st.subheader("1. The Rhythm: Linear vs. Exponential")
        st.write("First, let's see how Arithmetic (AP) and Geometric (GP) sequences behave.")

        c_input, c_vis = st.columns([1, 2])

        with c_input:
            st.info("🐢 **Arithmetic (AP)**")
            a_ap = st.number_input("Start (a)", value=1, key="ap_a_final")
            d = st.number_input("Common Difference (d)", value=2, key="ap_d_final")

            st.markdown("---")

            st.error("🚀 **Geometric (GP)**")
            a_gp = st.number_input("Start (a)", value=1.0, key="gp_a_final")
            r_val = st.number_input("Common Ratio (r)", value=1.5, step=0.1, key="gp_r_final")

            st.markdown("---")
            n_steps = st.slider("Number of Terms (n)", 5, 30, 15)

        with c_vis:
            n_vals = np.arange(1, n_steps + 1)
            ap_vals = a_ap + (n_vals - 1) * d
            gp_vals = a_gp * (r_val ** (n_vals - 1))

            fig_growth = go.Figure()
            fig_growth.add_trace(go.Scatter(x=n_vals, y=ap_vals, mode='lines+markers', name='AP (Linear)',
                                            line=dict(color='#00ADB5', width=3)))
            fig_growth.add_trace(go.Scatter(x=n_vals, y=gp_vals, mode='lines+markers', name='GP (Exponential)',
                                            line=dict(color='#FF2E63', width=3)))

            fig_growth.update_layout(
                title="Growth Rate Comparison",
                xaxis_title="Term (n)",
                yaxis_title="Value",
                template="plotly_dark",
                height=400,
                margin=dict(l=20, r=20, t=40, b=20),
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_growth, use_container_width=True)

        st.divider()
        st.subheader("2. The Logic Behind the Formulas")
        st.write("For students who struggle with formulas: Don't memorize, **visualize**.")

        st.markdown("#### 🐢 Arithmetic Sum ($S_n$) : The Symmetry Trick")
        with st.expander("Show Derivation: How young Gauss added 1 to 100", expanded=True):
            st.info("💡 **Concept:** List the numbers forward and backward. The sum of each pair is constant.")
            st.markdown(r"""
            Let's sum an AP:
            $$ S_n = a + (a+d) + (a+2d) + \dots + L $$
            **Step 1:** Write it forward and then backward.
            $$ S_n = a \quad + (a+d) \quad + \dots + L $$
            $$ S_n = L \quad + (L-d) \quad + \dots + a $$
            **Step 2:** Add them vertically. Notice $a+L = (a+d)+(L-d)$.
            $$ 2S_n = (a+L) + (a+L) + \dots + (a+L) $$
            Since there are $n$ pairs:
            $$ 2S_n = n(a+L) $$
            $$ \boxed{S_n = \frac{n}{2}(a + L)} $$
            """)

        st.markdown("#### 🚀 Geometric Sum ($S_n$) : The Cancellation Trick")
        with st.expander("Show Derivation: The 'Shift and Destroy' Method", expanded=True):
            st.error(
                "💡 **Concept:** Multiply the whole sequence by $r$ to shift it, then subtract to cancel the middle.")
            st.markdown(r"""
            Let's sum a GP:
            $$ S_n = a + ar + ar^2 + \dots + ar^{n-1} $$
            **Step 1:** Multiply by $r$ (every term shifts one step right).
            $$ rS_n = ar + ar^2 + ar^3 + \dots + ar^n $$
            **Step 2:** Subtract ($S_n - rS_n$).
            $$ \begin{aligned} S_n &= a + \color{red}{ar + ar^2 + \dots + ar^{n-1}} \\ - (rS_n &= \quad \color{red}{ar + ar^2 + \dots + ar^{n-1}} + ar^n) \\ \hline S_n(1-r) &= a - ar^n \end{aligned} $$
            **Step 3:** Solve for $S_n$.
            $$ \boxed{S_n = \frac{a(1-r^n)}{1-r}} $$
            """)

        st.divider()
        st.subheader("🧪 3. The Discovery of 'e' (1683)")
        st.markdown("""
        ### 📜 The Story of "Maximum Greed"
        In 1683, **Jacob Bernoulli** studied compound interest. He wanted to know:
        > *"If a bank offers **100% interest** per year on **$1**, how rich can I get if I compound it **infinitely often**?"*
        """)

        c_e_lab, c_e_fig = st.columns([1, 1.5])

        with c_e_lab:
            st.info("👇 **Compounding Experiment**")
            steps_e = [1, 2, 4, 12, 52, 365, 8760, 100000]
            labels_e = ["Yearly", "6-Months", "Quarterly", "Monthly", "Weekly", "Daily", "Hourly", "Continuously"]

            sel_label = st.select_slider("Change Frequency (n)", options=labels_e, value="Yearly")
            n_val_e = steps_e[labels_e.index(sel_label)]
            e_approx = (1 + 1 / n_val_e) ** n_val_e

            st.write(f"**Frequency (n):** {n_val_e}")
            st.latex(rf"\left( 1 + \frac{{1}}{{{n_val_e}}} \right)^{{{n_val_e}}}")
            st.metric("Final Amount", f"${e_approx:.6f}", delta=f"{e_approx - np.e:.6f} from e")

            if n_val_e == 1:
                st.warning("Just $2.00. Not very greedy.")
            elif n_val_e >= 365:
                st.success("You are hitting the 'Growth Wall'!")

        with c_e_fig:
            x_e = np.linspace(1, 100, 200)
            y_e = (1 + 1 / x_e) ** x_e

            fig_e = go.Figure()
            fig_e.add_trace(go.Scatter(x=x_e, y=y_e, mode='lines', name='Money', line=dict(color='#00ADB5', width=4)))
            fig_e.add_hline(y=np.e, line_dash="dash", line_color="#FF2E63",
                            annotation_text="The Wall (e ≈ 2.718)", annotation_position="bottom right")

            curr_x = min(n_val_e, 100)
            fig_e.add_trace(go.Scatter(x=[curr_x], y=[(1 + 1 / curr_x) ** curr_x], mode='markers',
                                       marker=dict(size=12, color='#FDB827'), name='Your Choice'))

            fig_e.update_layout(title="The Limit of Growth", template="plotly_dark", height=320,
                                margin=dict(l=10, r=10, t=40, b=10), plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_e, use_container_width=True)

        st.markdown("""
        #### 🧐 The Conclusion
        Bernoulli realized that even with "infinite greed," you cannot grow your money to infinity. 
        The sequence is bounded by a mathematical constant: **$e$**. 
        This constant $e$ is the foundation of **natural growth**—from bacteria colonies to radioactive decay.
        """)
        st.caption(
            "**Fun Fact:** Although Bernoulli discovered it, the letter **'e'** was chosen by **Leonhard Euler** 50 years later. ")

    # ==========================================
    # TAB 3: 名人堂
    # ==========================================
    with tab3:
        st.subheader("🏛️ The Hall of Fame: Rigorous Proofs")
        st.caption("Detailed mathematical derivation of three legendary series.")

        series_choice = st.selectbox(
            "Select a Derivation:",
            ["1. Harmonic Series (Oresme's Inequality Proof)",
             "2. The Basel Problem (Euler's Product Formula)",
             "3. Fibonacci Sequence (Deriving the Golden Ratio)"]
        )

        st.markdown("---")
        c1, c2 = st.columns([1.8, 1.5])

        if "Harmonic" in series_choice:
            with c1:
                st.markdown("### 🧱 1. The Harmonic Series")
                st.markdown("**Claim:** The sum $S = \sum_{n=1}^{\infty} \\frac{1}{n}$ diverges to infinity.")
                st.markdown("#### 📝 Step-by-Step Proof (Nicole Oresme, 1350)")
                st.write("We group the terms into blocks of powers of 2 ($2^k$ terms per block).")
                st.markdown("**Step 1: Expand the series**")
                st.latex(
                    r"S = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \dots")
                st.markdown("**Step 2: Group terms (Inequality Strategy)**")
                st.write("Replace each term in a group with the *smallest* term in that group:")
                st.latex(
                    r"S > 1 + \frac{1}{2} + \underbrace{\left(\frac{1}{4} + \frac{1}{4}\right)}_{\text{was } 1/3+1/4} + \underbrace{\left(\frac{1}{8} + \dots + \frac{1}{8}\right)}_{\text{was } 1/5 \dots 1/8} + \dots")
                st.markdown("**Step 3: Calculate the Sum of Groups**")
                st.latex(r"Group 2: \frac{1}{4} + \frac{1}{4} = \frac{2}{4} = \frac{1}{2}")
                st.latex(r"Group 3: \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}")
                st.markdown("**Step 4: Final Logic**")
                st.latex(r"S > 1 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \dots = \infty")
                st.error("Since we can add $1/2$ infinitely many times, the sum must be Infinite.")
                
            with c2:
                st.write("**Visualizing the Lower Bound:**")
                x_vals = [1, 2, 4, 8, 16, 32]
                y_lower = [1, 1.5, 2.0, 2.5, 3.0, 3.5]
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=x_vals, y=y_lower, mode='lines+markers', name='Lower Bound (1 + k/2)',
                                         line=dict(color='#FF2E63', width=3)))
                fig.update_layout(title="Divergence via Grouping", xaxis_title="Number of Terms (n)",
                                  yaxis_title="Sum Value", xaxis_type="log", template="plotly_dark", height=500)
                st.plotly_chart(fig, use_container_width=True)


        elif "Basel" in series_choice:

            with c1:

                st.markdown("### 👑 2. The Basel Problem")

                st.markdown("**Claim:** $\sum_{n=1}^{\infty} \\frac{1}{n^2} = \\frac{\pi^2}{6}$")

                st.markdown("#### 📝 Step-by-Step Proof (Euler, 1734)")

                st.markdown("**Step 1: Maclaurin Series Expansion**")

                st.write("We know the series for $\sin(x)$:")

                st.latex(r"\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots")

                st.write("Divide by $x$ to remove the constant term:")

                st.latex(r"\frac{\sin(x)}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \dots \quad \text{--- (Eq 1)}")

                st.markdown("**Step 2: Infinite Product Formula**")

                st.write("The roots of $\sin(x)/x$ are $\pm \pi, \pm 2\pi, \pm 3\pi \dots$")

                st.write("In formal mathematics, Euler expressed this as an infinite product using the $\prod$ symbol:")

                st.latex(r"\frac{\sin(x)}{x} = \prod_{n=1}^{\infty} \left( 1 - \frac{x^2}{n^2 \pi^2} \right)")

                st.write(
                    "But to understand Euler's genius, we must **expand these brackets out** to see what's inside:")

                st.latex(

                    r"\frac{\sin(x)}{x} = \left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{4\pi^2}\right)\left(1-\frac{x^2}{9\pi^2}\right)\dots \quad \text{--- (Eq 2)}")

                st.markdown("**Step 3: Extract the $x^2$ Coefficient**")

                st.write(
                    "Imagine multiplying out those infinite brackets. To create an $x^2$ term, you must pick the $x^2$ fraction from *one* bracket, and multiply it by the $1$ from *all the other* brackets. Adding all these possibilities together gives:")

                st.latex(

                    r"\text{Coeff of } x^2 = -\frac{1}{\pi^2} - \frac{1}{4\pi^2} - \frac{1}{9\pi^2} - \dots = -\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}")

                st.markdown("**Step 4: Equate Coefficients**")

                st.write("Compare $x^2$ coefficient from Eq 1 ($-1/6$) and Eq 2:")

                st.latex(r"-\frac{1}{6} = -\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}")

                st.success(r"Multiply by $-\pi^2$:  $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$")

                st.info("📺 **Video Resources:**")

                st.markdown(

                    "[▶️ 3Blue1Brown: The Basel Problem Visualized](https://www.youtube.com/watch?v=d-o3eB9sfls)")

            with c2:

                st.write("**Visualizing Convergence:**")

                n_b = 50

                x_b = np.arange(1, n_b + 1)

                y_b = np.cumsum(1 / (x_b ** 2))

                target = (np.pi ** 2) / 6

                fig = go.Figure()

                fig.add_trace(

                    go.Scatter(x=x_b, y=y_b, mode='lines', name='Partial Sum', line=dict(color='#00ADB5', width=3)))

                fig.add_shape(type="line", x0=0, y0=target, x1=n_b, y1=target, line=dict(color="#FF2E63", dash="dash"))

                fig.add_annotation(x=n_b / 2, y=target - 0.1, text="Target: π²/6 ≈ 1.6449", font=dict(color="#FF2E63"))

                fig.update_layout(title="Approaching π²/6", xaxis_title="n", template="plotly_dark", height=500)

                st.plotly_chart(fig, use_container_width=True)




        elif "Fibonacci" in series_choice:

            # ---------------------------------------------------------

            # PART 1: Basic Derivation (Left Col) & Ratio Graph (Right Col)

            # ---------------------------------------------------------

            with c1:

                st.markdown("### 🌻 3. Fibonacci & Golden Ratio")

                st.markdown("**Claim:** The ratio of consecutive terms converges to $\phi \\approx 1.618$.")

                st.markdown("#### 📝 Step-by-Step Derivation")

                st.markdown("**Step 1: The Recursive Definition**")

                st.latex(r"F_{n+1} = F_n + F_{n-1}")

                st.markdown("**Step 2: Construct the Ratio**")

                st.write("Divide the whole equation by $F_n$:")

                st.latex(r"\frac{F_{n+1}}{F_n} = \frac{F_n}{F_n} + \frac{F_{n-1}}{F_n} = 1 + \frac{F_{n-1}}{F_n}")

                st.markdown("**Step 3: Define the Limit**")

                st.write("Let $L = \lim_{n \\to \infty} \\frac{F_{n+1}}{F_n}$.")

                st.latex(r"L = 1 + \frac{1}{L}")

                st.markdown("**Step 4: Solve the Quadratic**")

                st.write("Multiply by $L$: $L^2 = L + 1 \implies L^2 - L - 1 = 0$.")

                st.latex(r"L = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2(1)} = \frac{1 \pm \sqrt{5}}{2}")

                st.success(r"Taking the positive root: $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.61803$")

            with c2:

                st.write("**Visualizing Ratio Convergence:**")

                fibs = [1, 1]

                for i in range(15): fibs.append(fibs[-1] + fibs[-2])

                ratios = [fibs[i] / fibs[i - 1] for i in range(1, len(fibs))]

                fig_ratio = go.Figure()

                fig_ratio.add_trace(go.Scatter(

                    x=list(range(1, len(ratios) + 1)), y=ratios, mode='lines+markers',

                    name='Ratio Fn/Fn-1', line=dict(color='#FDB827', width=3)

                ))

                fig_ratio.add_shape(type="line", x0=1, y0=1.618, x1=15, y1=1.618, line=dict(dash='dash', color='white'))

                fig_ratio.add_annotation(x=8, y=1.618, text="φ (1.618)", ay=-30, font=dict(color="white"))

                fig_ratio.update_layout(

                    title="Oscillation Damping", xaxis_title="n", yaxis_title="Ratio",

                    template="plotly_dark", height=400, margin=dict(l=0, r=0, b=0, t=40)

                )

                st.plotly_chart(fig_ratio, use_container_width=True)

            # ---------------------------------------------------------

            # PART 2: Mind-Blowing Extra (Full Screen Width)

            # ---------------------------------------------------------

            # Stepping outside c1 and c2 so these take up the whole screen

            st.divider()

            st.markdown("### 🤯 Mind-Blowing Extra: The Two Spirals of Fibonacci")

            st.write(
                "When people think of the Fibonacci sequence, they immediately picture the classic 'Conch Shell' shape. But mathematically, there are actually **two entirely different spirals** at play.")

            # Create two new columns just for the explanation

            col_conch, col_helix = st.columns(2)

            with col_conch:

                st.markdown("#### 🐚 1. The Geometric Conch (Nature)")

                st.write(
                    "This is the spiral we see in sunflowers, snail shells, and galaxies. It's built by drawing quarter-circles inside squares with Fibonacci-length sides. **It lives entirely in our flat, 2D real world.**")

                # Plotting the classic Conch Golden Spiral

                theta_conch = np.linspace(0, 4 * np.pi, 200)

                r_conch = ((1 + np.sqrt(5)) / 2) ** (2 * theta_conch / np.pi)

                fig_conch = go.Figure()

                fig_conch.add_trace(go.Scatter(

                    x=r_conch * np.cos(theta_conch), y=r_conch * np.sin(theta_conch),

                    mode='lines', line=dict(color='#FDB827', width=4), name="Golden Spiral"

                ))

                fig_conch.update_layout(

                    xaxis=dict(scaleanchor="y", scaleratio=1, visible=False),

                    yaxis=dict(visible=False), height=350, template="plotly_dark", margin=dict(l=0, r=0, b=0, t=30)

                )

                st.plotly_chart(fig_conch, use_container_width=True)

            with col_helix:

                st.markdown("#### 🌌 2. The Algebraic Helix (Hidden Dimension)")

                st.write("What if we want to calculate the **1.5th** Fibonacci number? We must use Binet's formula:")

                st.latex(r"F_n = \frac{\phi^n - (-0.618)^n}{\sqrt{5}}")

                st.write(
                    "Notice the negative number. Raising a negative number to a decimal power (like $1.5$) requires taking a **square root of a negative**. This forces the sequence to spawn **Imaginary Numbers ($i$)**!")

                st.write(
                    "To connect the dots, the sequence leaps off the 1D number line into the **3D Complex Plane**. The integers we know (1, 1, 2, 3...) are simply the exact moments this 3D helix crashes down into our 'Real' reality.")

            # Full-width 3D Plot representing the Algebraic Helix (placed below the two text columns)

            n_continuous = np.linspace(-2.0, 5.5, 500)

            phi_val = (1 + np.sqrt(5)) / 2

            psi_val = (1 - np.sqrt(5)) / 2

            real_vals = (phi_val ** n_continuous - np.cos(np.pi * n_continuous) * (
                        np.abs(psi_val) ** n_continuous)) / np.sqrt(5)

            imag_vals = (-np.sin(np.pi * n_continuous) * (np.abs(psi_val) ** n_continuous)) / np.sqrt(5)

            n_ints = np.arange(-2, 6)

            int_real = (phi_val ** n_ints - np.cos(np.pi * n_ints) * (np.abs(psi_val) ** n_ints)) / np.sqrt(5)

            int_imag = np.zeros_like(n_ints)

            fig_fib = go.Figure()

            # 3D Helix

            fig_fib.add_trace(go.Scatter3d(

                x=n_continuous, y=real_vals, z=imag_vals, mode='lines',

                line=dict(color='#00ADB5', width=6), name="Continuous Complex Helix"

            ))

            # Real Integers (Red Dots)

            fig_fib.add_trace(go.Scatter3d(

                x=n_ints, y=int_real, z=int_imag, mode='markers+text',

                marker=dict(size=8, color='#FF2E63'), text=[f"F({n})" for n in n_ints],

                textposition="top center", name="Real Integers (Our World)"

            ))

            # The "Real" Floor Shadow

            fig_fib.add_trace(go.Scatter3d(

                x=n_continuous, y=real_vals, z=np.zeros_like(real_vals), mode='lines',

                line=dict(color='#FF2E63', width=2, dash='dash'), opacity=0.4,

                name="Shadow on the Real Floor"

            ))

            fig_fib.update_layout(

                scene=dict(xaxis_title='Index (n)', yaxis_title='Real Value', zaxis_title='Imaginary Value',

                           aspectmode='manual', aspectratio=dict(x=2.5, y=1, z=1)),

                height=550, margin=dict(l=0, r=0, b=0, t=0), template="plotly_dark",

                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)

            )

            st.plotly_chart(fig_fib, use_container_width=True)

            # ---------------------------------------------------------

            # PART 3: Resources

            # ---------------------------------------------------------

            st.info("📺 **Video Resources:**")

            st.markdown("[▶️ Numberphile: The Golden Ratio](https://www.youtube.com/watch?v=ghxQA3vvhsk)")



    # ==========================================
    # TAB 4: Pascal to Normal
    # ==========================================
    with tab4:
        st.header("🧱 The Binomial Engine: Logic & Derivation")

        col_top_left, col_top_right = st.columns([1.3, 2.0])

        with col_top_left:
            st.subheader("1. The Logic of $(a+b)^n$")
            n_rows_pascal = st.slider("Power (n)", 0, 12, 5, key='n_slider_final_fix')
            p_val = st.slider("Probability (p)", 0.0, 1.0, 0.5, 0.05, key='p_slider_final_fix')

            with st.expander("📖 DEEP DIVE: Where does the formula come from?", expanded=True):
                st.markdown("""
                **Don't just memorize the formula. Visualize the brackets.**
                Imagine calculating $(a+b)^3$:
                $$(a+b)(a+b)(a+b)$$
                To get $a^2b$, you need to choose **'b'** from exactly **1** bracket, and **'a'** from the other **2**.
                **The Answer is:** Combinations! $\\binom{3}{1} = 3$.
                """)

        with col_top_right:
            st.subheader("The Visual Architecture")
            fig_tri = go.Figure()
            for r in range(n_rows_pascal + 1):
                row_coeffs = [math.comb(r, k) for k in range(r + 1)]
                xs = np.linspace(-r / 2, r / 2, r + 1)
                ys = [-r] * (r + 1)

                if r < n_rows_pascal:
                    base_color = 'rgba(0, 173, 181, 0.3)'
                    text_col = 'rgba(255, 255, 255, 0.5)'
                    size = 20
                else:
                    base_color = '#FDB827'
                    text_col = 'black'
                    size = 35

                fig_tri.add_trace(go.Scatter(
                    x=xs, y=ys, mode='markers+text',
                    text=[str(c) for c in row_coeffs],
                    textfont=dict(color=text_col, size=12 if r < n_rows_pascal else 16, family="Arial Black"),
                    marker=dict(size=size, color=base_color, symbol='hexagon', line=dict(width=1, color='white')),
                    showlegend=False, hoverinfo='text',
                    hovertext=[f"Row {r}, Term {k + 1}<br>Value: {c}" for k, c in enumerate(row_coeffs)]
                ))

            fig_tri.update_layout(height=400, xaxis=dict(visible=False), yaxis=dict(visible=False),
                                  plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=10, b=0),
                                  title=f"Pascal's Triangle (Row 0 to {n_rows_pascal})", template="plotly_dark")
            st.plotly_chart(fig_tri, use_container_width=True)

            c1, c2 = st.columns(2)
            c1.metric(label=f"Sum of Row {n_rows_pascal}", value=f"{2 ** n_rows_pascal}", help="(1+1)^n")
            c2.metric(label="Shallow Diagonals", value="Fibonacci", help="1, 1, 2, 3, 5...")

            st.markdown("---")
            st.caption("Visualizing the Limit (Normal Curve)")
            x_k = np.arange(0, n_rows_pascal + 1)
            probs = stats.binom.pmf(x_k, n_rows_pascal, p_val)
            fig_dist = go.Figure()
            fig_dist.add_trace(go.Bar(x=x_k, y=probs, name='Binomial', marker_color='#FDB827'))
            mu = n_rows_pascal * p_val
            sigma = math.sqrt(n_rows_pascal * p_val * (1 - p_val))
            if sigma > 0:
                x_smooth = np.linspace(0, n_rows_pascal, 200)
                y_smooth = stats.norm.pdf(x_smooth, mu, sigma)
                fig_dist.add_trace(go.Scatter(x=x_smooth, y=y_smooth, mode='lines', name='Normal',
                                              line=dict(color='#00ADB5', width=3)))
            fig_dist.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0), template="plotly_dark",
                                   plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_dist, use_container_width=True)

        st.divider()

        st.subheader("2. Term Finder & General Term")
        tf_col1, tf_col2 = st.columns([1, 2])
        with tf_col1:
            k_term = st.number_input(f"Find the k-th term (1 to {n_rows_pascal + 1})", min_value=1,
                                     max_value=n_rows_pascal + 1, value=1, key='k_term_final')
            r_idx = k_term - 1
            coeff = math.comb(n_rows_pascal, r_idx)
        with tf_col2:
            st.markdown(f"**Target:** The **{k_term}-th** term (so $r={r_idx}$).")
            st.latex(rf"T_{{r+1}} = \binom{{n}}{{r}} a^{{n-r}} b^r")
            st.caption("We use $r+1$ because we start counting from $r=0$ (the 1st term).")
            st.latex(
                rf"\binom{{{n_rows_pascal}}}{{{r_idx}}} = \frac{{{n_rows_pascal}!}}{{{r_idx}!({n_rows_pascal}-{r_idx})!}} = {coeff}")

        st.divider()
        st.subheader("3. Newton's Infinite Series (The Logic)")
        st.markdown("#### Step 1: Newton's Generalization")
        st.write(
            "Newton discovered that the Combinations formula $\\binom{n}{r}$ works for **any number** (fractions/negatives) if written in this specific form:")
        st.latex(r"\binom{n}{r} = \frac{n(n-1)(n-2)\dots(n-r+1)}{r!}")
        st.caption("""
            * **Term 0 ($r=0$):** Value is **1**.
            * **Term 1 ($r=1$):** Value is $\\frac{n}{1!} = n$.
            * **Term 2 ($r=2$):** Value is $\\frac{n(n-1)}{2!}$.
            """)

        st.divider()
        st.markdown("#### Step 2: Expanding $(1+ax)^n$")
        st.write(
            "Now, we substitute these coefficients into the Binomial structure. We replace $x$ with the term **$(ax)$**:")
        st.latex(
            r"""(1+ax)^n = \underbrace{1}_{\binom{n}{0}} + \underbrace{n}_{\binom{n}{1}}(ax) + \underbrace{\frac{n(n-1)}{2!}}_{\binom{n}{2}}(ax)^2 + \underbrace{\frac{n(n-1)(n-2)}{3!}}_{\binom{n}{3}}(ax)^3 + \dots""")
        st.info(
            "Notice how the factorials ($2!, 3!$) and the falling powers ($n(n-1)$) match the General Combinations formula above.")

        st.divider()
        st.markdown("#### Step 3: Does it work? (Convergence)")
        conv_c1, conv_c2 = st.columns([1, 1])
        with conv_c1:
            st.warning("⚠️ **The Golden Rule**")
            st.markdown("Since the series goes on forever, it is only valid if the terms shrink to zero.")
            st.latex(r"|ax| < 1")
        with conv_c2:
            st.markdown("**What happens?**")
            st.write("✅ **Converges:** If $|ax| < 1$, the sum is real.")
            st.write("💥 **Diverges:** If $|ax| \ge 1$, the sum explodes to infinity.")

    # ==========================================
    # TAB 5: Taylor Series
    # ==========================================
    with tab5:
        st.subheader("Taylor Series: From Formula to Polynomial")
        st.markdown("### 📜 The Origin Story: The Calculator's Secret")
        st.info("""
        **How does a calculator compute $\sin(35^\circ)$ or $e^2$?**
        Deep down, computers are "dumb". They technically **only** know how to do **Arithmetic** (+, -, $\\times$, $\div$). 
        They don't have a magic "Sine" button inside the chip.
        **The Solution (Brook Taylor, 1715):**
        He discovered that **ANY** smooth, curvy function (like waves or exponents) can be translated into an **infinite string of simple polynomials**.
        * **The Mission**: Turn complex functions into simple arithmetic ($x^n$).
        * **The Logic**: If we add enough simple terms ($x, x^2, x^3...$), the polynomial eventually "hugs" the curve perfectly.
        """)
        st.markdown("---")

        col_ctrl, col_plot = st.columns([1.2, 2.5])

        with col_ctrl:
            func_type = st.radio("Function:", ["Sin(x)", "Cos(x)", "e^x"])
            n_terms = st.slider("Precision (Terms)", 1, 8, 3)

            st.markdown("---")
            st.write("### 1. General Formula (Sigma)")

            if func_type == "Sin(x)":
                st.latex(r"\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}")
                terms_idx = range(n_terms)
                powers = [2 * i + 1 for i in terms_idx]
                facts = [math.factorial(p) for p in powers]
                signs = [(-1) ** i for i in terms_idx]
            elif func_type == "Cos(x)":
                st.latex(r"\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}")
                terms_idx = range(n_terms)
                powers = [2 * i for i in terms_idx]
                facts = [math.factorial(p) for p in powers]
                signs = [(-1) ** i for i in terms_idx]
            else:
                st.latex(r"\sum_{n=0}^{\infty} \frac{x^n}{n!}")
                terms_idx = range(n_terms)
                powers = [i for i in terms_idx]
                facts = [math.factorial(p) for p in powers]
                signs = [1 for i in terms_idx]

            st.write("### 2. Step-by-Step Expansion")
            raw_terms = []
            for i in range(n_terms):
                p = powers[i]
                s = signs[i]
                sign_str = "+" if s > 0 else "-"
                if i == 0: sign_str = "" if s > 0 else "-"
                raw_terms.append(rf"{sign_str} \frac{{x^{{{p}}}}}{{{p}!}}")

            raw_latex = " ".join(raw_terms) + " \dots"
            st.latex(raw_latex)

            st.write("### 3. Final Polynomial")
            final_terms = []
            for i in range(n_terms):
                p = powers[i]
                s = signs[i]
                coef = 1 / math.factorial(p)
                sign_char = "+" if s > 0 else "-"
                if i == 0 and s > 0: sign_char = ""

                if coef == 1:
                    val_str = ""
                else:
                    val_str = rf"\frac{{1}}{{{math.factorial(p)}}}"

                final_terms.append(rf"{sign_char} {val_str} x^{{{p}}}")

            final_latex = " ".join(final_terms) + " \dots"
            st.latex(final_latex)

        with col_plot:
            fig_taylor = go.Figure()
            x_vals = np.linspace(-10, 10, 400)

            if func_type == "Sin(x)":
                y_true = np.sin(x_vals)
            elif func_type == "Cos(x)":
                y_true = np.cos(x_vals)
            else:
                y_true = np.exp(x_vals)

            fig_taylor.add_trace(go.Scatter(x=x_vals, y=y_true, mode='lines', line=dict(color='gray', dash='dash'),
                                            name='True Function'))

            y_approx = np.zeros_like(x_vals)
            for i in range(n_terms):
                p = powers[i]
                s = signs[i]
                y_approx += s * (x_vals ** p) / math.factorial(p)

            y_limit = [-3, 3] if "x" in func_type else [-5, 10]

            fig_taylor.add_trace(go.Scatter(x=x_vals, y=y_approx, mode='lines', line=dict(color='#00ADB5', width=3),
                                            name=f'Approximation'))
            fig_taylor.update_layout(xaxis_title="x", yaxis_title="y", yaxis=dict(range=y_limit),
                                     template="plotly_dark", height=450)
            st.plotly_chart(fig_taylor, use_container_width=True)

        st.markdown("---")
        with st.expander("💎 The Grand Finale: Euler's Formula Proof (Detailed Expansion)"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**1. Maclaurin Series for $e^x$:**")
                st.latex(
                    r"e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \frac{x^5}{5!} + \dots")
                st.markdown("**2. Let $x = ix$:**")
                st.latex(
                    r"e^{ix} = 1 + \frac{ix}{1!} + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + \dots")
            with c2:
                st.markdown("**3. Evaluate Powers of $i$:**")
                st.caption(r"$i^2=-1, \quad i^3=-i, \quad i^4=1$")
                st.latex(
                    r"e^{ix} = 1 + i\frac{x}{1!} - \frac{x^2}{2!} - i\frac{x^3}{3!} + \frac{x^4}{4!} + i\frac{x^5}{5!} \dots")
                st.markdown("**4. Group Terms:**")
                st.latex(
                    r"e^{ix} = \underbrace{\left( 1 - \frac{x^2}{2!} + \frac{x^4}{4!} \dots \right)}_{\cos(x)} + i \underbrace{\left( \frac{x}{1!} - \frac{x^3}{3!} + \dots \right)}_{\sin(x)}")
            st.success(r"Conclusion: $e^{ix} = \cos(x) + i\sin(x)$")


# ==========================================
# 执行运行 (这是最关键的启动代码)
# ==========================================
if __name__ == "__main__":
    show_sequence_page()