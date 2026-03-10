import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ==========================================
# 页面配置 (可选，让页面更宽敞)
# ==========================================
st.set_page_config(page_title="Number Systems", page_icon="🔢 ", layout="wide")

# ==========================================
# 初始化 Session State (给 3D 螺旋用)
# ==========================================
if 'euler_t_3d' not in st.session_state:
    st.session_state['euler_t_3d'] = 2.0


def set_t(val):
    st.session_state['euler_t_3d'] = float(val)


# ==========================================
# 主体内容
# ==========================================
st.header("🌌 Topic 1: Evolution of Number Systems")

# 4 个核心标签页
tab1, tab2, tab3, tab4 = st.tabs([
    "1. The Evolution (History)",
    "2. Complex Logic (Rotation)",
    "3. Polar Coordinates",
    "4. Euler's Formula"
])

# ---------------------------------------------------------
# TAB 1: 数字发展史 (History)
# ---------------------------------------------------------
with tab1:
    st.subheader("🌌 Topic 1: The Drama of Numbers")
    st.caption("A journey from a simple line to a 2D plane.")

    chapter = st.select_slider(
        "📜 The Timeline:",
        options=[
            "1. Hunters (N)",
            "2. Accountants (Z)",
            "3. Broken Numbers (Q)",
            "4. The Murderous Root (Irrationals)",
            "5. The Ghosts (Transcendental)",
            "6. The Cartesian Revolution",
            "7. The Impossible Dimension (Complex)"
        ],
        value="1. Hunters (N)"
    )

    st.markdown("---")

    c_story, c_vis = st.columns([1.3, 2])
    fig1 = go.Figure()

    if "1." in chapter:
        with c_story:
            st.subheader("🦕 1. Survival (The Ray)")
            st.info("""
            **Ch 1. The Hunters (Natural Numbers $\mathbb{N}$)**
            * **Who/Origin**: Prehistoric humans and ancient shepherds.
            * **Motivation**: Survival. Needed to count sheep or warriors.
            * **The Story**: Counting started with notches on bones. They only knew "one, two, three, many."
            * **The Impact**: Created **Addition**. 
                * *Fatal Flaw*: Couldn't understand "debt" (negative apples).
            """)
        fig1.add_shape(type="line", x0=0, y0=0, x1=5.5, y1=0, line=dict(color="gray", width=2))
        x_vals = [1, 2, 3, 4, 5]
        fig1.add_trace(go.Scatter(x=x_vals, y=[0] * 5, mode='markers+text', text=x_vals, textposition="top center",
                                  marker=dict(size=15, color='#00ADB5'), name='N'))
        fig1.update_layout(title="1D: The Ray", xaxis=dict(range=[-0.5, 6], showgrid=False), yaxis=dict(visible=False))

    elif "2." in chapter:
        with c_story:
            st.subheader("💸 2. Debt (The Line)")
            st.info("""
            **Ch 2. The Accountants (Integers $\mathbb{Z}$)**
            * **Who**: Brahmagupta (India, 628 AD).
            * **Motivation**: Commerce. Distinguishing "earned" vs "owed".
            * **The Story**: Defined **"Fortunes"** (+) and **"Debts"** (-). Europeans rejected this for 1000 years as "absurd".
            * **The Impact**: The Ray became a **Line**, allowing algebraic symmetry.
            """)
        fig1.add_shape(type="line", x0=-5.5, y0=0, x1=5.5, y1=0, line=dict(color="gray", width=2))
        x_vals = [-3, -2, -1, 0, 1, 2, 3]
        fig1.add_trace(
            go.Scatter(x=x_vals, y=[0] * len(x_vals), mode='markers+text', text=x_vals, textposition="top center",
                       marker=dict(size=15, color='#FF2E63'), name='Z'))
        fig1.update_layout(title="1D: The Line", xaxis=dict(range=[-4, 4], showgrid=False), yaxis=dict(visible=False))

    elif "3." in chapter:
        with c_story:
            st.subheader("🍰 3. Sharing (Density)")
            st.info("""
            **Ch 3. The Broken Numbers (Rationals $\mathbb{Q}$)**
            * **Who**: Egyptians & Pythagoreans.
            * **Motivation**: Fair distribution (taxes, food).
            * **The Story**: "Fraction" means "Broken". Pythagoras believed **"All is Ratio"** (Music 1:2, 2:3).
            * **The Impact**: The line became **"dense"**. They thought fractions filled every gap.
            """)
        fig1.add_shape(type="line", x0=-3, y0=0, x1=3, y1=0, line=dict(color="gray", width=2))
        fig1.add_trace(go.Scatter(x=[-2, -1, 0, 1, 2], y=[0] * 5, mode='markers', marker=dict(size=8, color='gray')))
        fig1.add_trace(
            go.Scatter(x=[-1.5, -0.5, 0.5, 1.5], y=[0] * 4, mode='markers+text', text=["-3/2", "-1/2", "1/2", "3/2"],
                       textposition="top center", marker=dict(size=12, color='#FDB827'), name='Q'))
        fig1.update_layout(title="1D: Filling Gaps", xaxis=dict(range=[-3, 3], showgrid=False),
                           yaxis=dict(visible=False))

    elif "4." in chapter:
        with c_story:
            st.subheader("💀 4. The Monster (√2)")
            st.error("""
            **Ch 4. The Murderous Root (Irrationals $\mathbb{R \setminus Q}$)**
            * **Who**: Hippasus (500 BC).
            * **Motivation**: Geometric precision.
            * **The Story**: Proved $\sqrt{2}$ isn't a fraction. This broke the Pythagorean creed. **Legend says he was drowned for this secret.**
            * **The Impact**: First Crisis of Math. Revealed "holes" in the number line.
            """)
        fig1.add_shape(type="line", x0=0, y0=0, x1=3, y1=0, line=dict(color="gray", width=2))
        fig1.add_trace(go.Scatter(x=[0, 1, 1, 0], y=[0, 0, 1, 0], mode='lines', line=dict(color='green', dash='dot'),
                                  name='Geometry'))
        r = np.sqrt(2)
        fig1.add_trace(go.Scatter(x=[r], y=[0], mode='markers+text', text=["√2"], textposition="top center",
                                  marker=dict(size=15, color='purple', symbol='diamond')))
        fig1.update_layout(title="1D: Geometry fills the Line", xaxis=dict(range=[-0.5, 2.5], showgrid=False),
                           yaxis=dict(visible=False))

    elif "5." in chapter:
        with c_story:
            st.subheader("👻 5. The Outlaws (π, e)")
            st.info("""
            **Ch 5. The Ghosts (Transcendental)**
            * **Who**: Liouville, Hermite.
            * **Motivation**: Distinguishing constants of nature.
            * **The Story**: $\pi$ and $e$ are **"Outlaws"**. They aren't solutions to ANY algebra equation.
            * **The Impact**: Proved "Squaring the Circle" is impossible.
            """)
        fig1.add_shape(type="line", x0=2, y0=0, x1=4, y1=0, line=dict(color="gray", width=2))
        fig1.add_trace(go.Scatter(x=[np.e], y=[0], mode='markers+text', text=["e"], textposition="top center",
                                  marker=dict(size=15, color='#E056FD')))
        fig1.add_trace(go.Scatter(x=[np.pi], y=[0], mode='markers+text', text=["π"], textposition="top center",
                                  marker=dict(size=15, color='#E056FD')))
        fig1.update_layout(title="1D: The Line is Complete", xaxis=dict(range=[2, 4], showgrid=False),
                           yaxis=dict(visible=False))

    elif "6." in chapter:
        with c_story:
            st.subheader("🪰 6. The Cartesian Revolution")
            st.warning("""
            **Ch 6. The Fly (Cartesian Grid)**
            * **Who**: René Descartes (1637).
            * **Motivation**: Linking Algebra & Geometry.
            * **The Story**: Sick in bed, he watched a **fly** on the ceiling. Realized he could track it with TWO numbers (x, y).
            * **The Impact**: Born of **Analytic Geometry**. Numbers jumped from 1D Line to **2D Plane**.
            """)
        for i in range(-2, 3):
            fig1.add_shape(type="line", x0=i, y0=-2, x1=i, y1=2, line=dict(color="rgba(255,255,255,0.1)", width=1))
            fig1.add_shape(type="line", x0=-2, y0=i, x1=2, y1=i, line=dict(color="rgba(255,255,255,0.1)", width=1))
        fig1.add_shape(type="line", x0=-2, y0=0, x1=2, y1=0, line=dict(color="white", width=2))
        fig1.add_shape(type="line", x0=0, y0=-2, x1=0, y1=2, line=dict(color="white", width=2))
        fig1.add_trace(
            go.Scatter(x=[1.5], y=[1.0], mode='markers+text', text=["The Fly (x,y)"], textposition="top right",
                       marker=dict(size=15, color='#FDB827', symbol='x')))
        fig1.update_layout(title="2D: The Grid is Born", xaxis=dict(range=[-2, 2], showgrid=False),
                           yaxis=dict(range=[-2, 2], showgrid=False, visible=True))

    elif "7." in chapter:
        with c_story:
            st.subheader("🧠 7. The Complex Plane")
            st.error("""
            **Ch 7. The Impossible Dimension ($\mathbb{C}$)**
            * **Who**: Cardano, Gauss.
            * **Motivation**: Solving $x^2 = -1$.
            * **The Story**: Cardano called $\sqrt{-1}$ **"mental torture"**. Gauss fixed it by standing the axis up. **$i$ points Sideways.**
            * **The Impact**: **Rotation** entered math.
            """)
        fig1.add_shape(type="line", x0=-2, y0=0, x1=2, y1=0, line=dict(color="white", width=2))
        fig1.add_shape(type="line", x0=0, y0=-2, x1=0, y1=2, line=dict(color="cyan", width=2))
        fig1.add_annotation(x=0.2, y=1, ax=1, ay=0, xref="x", yref="y", axref="x", ayref="y", arrowcolor="cyan",
                            arrowwidth=2, arrowhead=2, text="Rotate 90°")
        fig1.add_trace(go.Scatter(x=[0], y=[1], mode='markers+text', text=["i"], textposition="top right",
                                  marker=dict(size=15, color='cyan')))
        fig1.update_layout(title="2D: The Complex Plane", xaxis=dict(range=[-2, 2], showgrid=True),
                           yaxis=dict(range=[-2, 2], showgrid=True, visible=True))

    fig1.update_layout(height=400, template="plotly_dark", margin=dict(l=20, r=20, t=40, b=20),
                       plot_bgcolor='rgba(0,0,0,0)')
    with c_vis:
        st.plotly_chart(fig1, use_container_width=True)

    if "7." in chapter:
        st.markdown("---")
        st.subheader("💡 Interesting Fact: Cardano's 'Mental Torture'")
        col_img, col_txt = st.columns([1, 2])
        with col_img:
            try:
                st.image("cardano.jpg", caption="Ars Magna (1545)", use_container_width=True)
            except:
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Cardano-Ars.jpg/400px-Cardano-Ars.jpg",
                    caption="Ars Magna (Web)", use_container_width=True)
        with col_txt:
            st.markdown(r"""
            In Chapter 37 of *Ars Magna*, Cardano posed this "impossible" problem:
            > **"Divide 10 into two parts such that their product is 40."**
            $$ x(10 - x) = 40 \implies x^2 - 10x + 40 = 0 $$
            He found: **$x = 5 \pm \sqrt{-15}$**. 
            He wrote them as `5 p: R m 15` and `5 m: R m 15`, calling them "useless" but noting that they mathematically worked!
            """)

# ---------------------------------------------------------
# TAB 2: 虚数的诞生 (Rotation Logic)
# ---------------------------------------------------------
with tab2:
    st.subheader("Thought Experiment: Unlocking Dimensions")
    st.markdown(
        r"**Core Logic**: If $\times (-1)$ is a half-turn rotation (180°), then $\times i$ is a quarter-turn rotation (90°).")

    story_step = st.select_slider(
        "Drag slider to witness the evolution:",
        options=[
            "1. Start: Real 1",
            "2. Observe: x (-1) (180°)",
            "3. Dilemma: Finding √-1",
            "4. Breakthrough: Define i (90°)",
            "5. Verify: i² (-1)",
            "6. Evolve: i³ (-i)",
            "7. Cycle: i⁴ (1)"
        ],
        value="1. Start: Real 1"
    )

    col1, col2 = st.columns([1, 2])
    val = 2.5

    with col1:
        if "1." in story_step:
            st.info("Everything starts at **1** on the Real Axis.\n\nDirection: Right ($0^{\circ}$)")
        elif "2." in story_step:
            st.write("When calculating $1 \\times (-1)$, the point jumps to the left.")
            st.info("**Geometric Essence**:\nThis isn't 'debt', this is a **180° Rotation**.")
        elif "3." in story_step:
            st.error("""**The Problem**: We need a number $x$ that, when multiplied twice, equals -1 ($180^{\circ}$).
            $$ x \cdot x = -1 $$
            But on the number line:
            * $0^{\circ}$ twice is still $0^{\circ}$.
            * $180^{\circ}$ twice is $360^{\circ}$ (back to start).
            **No solution on the 1D line!**""")
        elif "4." in story_step:
            st.success("""**The Solution**: Since we need $180^{\circ}$, let's **split it in two**. Each step rotates **90°**.
            $$ i = \\text{Rotation of } 90^{\circ} $$
            **Welcome to the Complex Plane!**""")
        elif "5." in story_step:
            st.warning("""**Verification**: If $i$ is 90° rotation... Then $i \\times i$ is rotating 90° twice.
            $$ 90^{\circ} + 90^{\circ} = 180^{\circ} $$
            **Look! It lands exactly on -1.** So $i^2 = -1$ is a geometric necessity.""")
        elif "6." in story_step:
            st.write("Continuing the rotation...")
            st.latex(r"i^3 = i^2 \cdot i = -1 \cdot i = -i")
            st.info("Now we are at $270^{\circ}$, the bottom of the imaginary axis.")
        elif "7." in story_step:
            st.write("One last rotation...")
            st.latex(r"i^4 = i^3 \cdot i = -i \cdot i = -i^2 = 1")
            st.success(
                "We have rotated a full circle ($360^{\circ}$) and returned to the start. **This is the power of cycles.**")

    with col2:
        fig2 = go.Figure()
        fig2.add_shape(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="gray", width=2))
        fig2.add_shape(type="line", x0=0, y0=-4, x1=0, y1=4, line=dict(color="gray", width=2))
        fig2.add_annotation(x=4.2, y=0, text="Real", showarrow=False)
        fig2.add_annotation(x=0, y=4.2, text="Imag", showarrow=False)

        theta_circle = np.linspace(0, 2 * np.pi, 100)
        fig2.add_trace(go.Scatter(x=val * np.cos(theta_circle), y=val * np.sin(theta_circle), mode='lines',
                                  line=dict(dash='dot', color='rgba(255,255,255,0.2)'), hoverinfo='skip'))

        current_x, current_y = val, 0
        color = "#00ADB5"
        label = "1"

        if "2." in story_step:
            current_x, current_y = -val, 0
            color = "#FF2E63"
            label = "-1"
            t = np.linspace(0, np.pi, 50)
            fig2.add_trace(
                go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='orange', dash='dash')))
        elif "3." in story_step:
            current_x, current_y = val, 0
            label = "?"
            color = "gray"
            fig2.add_annotation(x=0, y=1, text="Dead End!", font=dict(color="red", size=20), showarrow=False)
        elif "4." in story_step:
            current_x, current_y = 0, val
            color = "#6610f2"
            label = "i"
            t = np.linspace(0, np.pi / 2, 50)
            fig2.add_trace(
                go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
        elif "5." in story_step:
            current_x, current_y = -val, 0
            color = "#FF2E63"
            label = "i² = -1"
            t = np.linspace(0, np.pi, 50)
            fig2.add_trace(
                go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
            fig2.add_trace(
                go.Scatter(x=[0], y=[val], mode='markers+text', marker=dict(color='gray', size=10), text=["i"],
                           textposition="top right"))
        elif "6." in story_step:
            current_x, current_y = 0, -val
            color = "#FDB827"
            label = "i³ = -i"
            t = np.linspace(0, 3 * np.pi / 2, 100)
            fig2.add_trace(
                go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
            fig2.add_trace(go.Scatter(x=[0, -val], y=[val, 0], mode='markers', marker=dict(color='gray', size=8)))
        elif "7." in story_step:
            current_x, current_y = val, 0
            color = "#00ADB5"
            label = "i⁴ = 1"
            t = np.linspace(0, 2 * np.pi, 100)
            fig2.add_trace(
                go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
            fig2.add_trace(
                go.Scatter(x=[0, -val, 0], y=[val, 0, -val], mode='markers', marker=dict(color='gray', size=8)))

        fig2.add_trace(go.Scatter(
            x=[0, current_x], y=[0, current_y],
            mode='lines+markers+text',
            marker=dict(size=15, symbol="arrow-bar-up", angleref="previous", color=color),
            line=dict(width=5, color=color), text=[None, label], textposition="top center"
        ))
        fig2.update_layout(xaxis_range=[-4, 4], yaxis_range=[-4, 4], height=500, width=500, showlegend=False,
                           title="Complex Plane Evolution", plot_bgcolor='rgba(0,0,0,0)', template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------------
# TAB 3: 极坐标 (Polar Radar)
# ---------------------------------------------------------
with tab3:
    st.subheader("Polar Coordinates: Redefining Position with 'Angle' & 'Distance'")
    st.markdown(
        r"""In Polar form, we don't say "Go right 3, up 4". We say: > **"Face direction $\theta$, walk distance $r$."**""")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("### 🕹️ Radar Control")
        r_val = st.slider("Modulus r", 0.0, 5.0, 3.0, step=0.1)
        theta_deg = st.slider("Argument θ°", 0, 360, 45)
        theta_rad = np.radians(theta_deg)
        x = r_val * np.cos(theta_rad)
        y = r_val * np.sin(theta_rad)
        st.latex(rf"z = {r_val} \cdot e^{{i \cdot {theta_deg}^\circ}}")
        st.markdown("---")
        st.write("**Translate to Cartesian:**")
        st.latex(rf"x = {r_val} \cos({theta_deg}^\circ) = {x:.2f}")
        st.latex(rf"y = {r_val} \sin({theta_deg}^\circ) = {y:.2f}")
        st.info(f"💡 Complex Number: {x:.2f} + {y:.2f}i")

    with col2:
        fig3 = go.Figure()
        for i in range(1, 6):
            t = np.linspace(0, 2 * np.pi, 100)
            fig3.add_trace(go.Scatter(x=i * np.cos(t), y=i * np.sin(t), mode='lines',
                                      line=dict(color='rgba(255,255,255,0.1)', width=1), showlegend=False,
                                      hoverinfo='skip'))
        fig3.add_trace(go.Scatter(x=[0, x], y=[0, 0], mode='lines', line=dict(color='#00ADB5', width=4, dash='solid'),
                                  name='Real Projection'))
        fig3.add_trace(go.Scatter(x=[x, x], y=[0, y], mode='lines', line=dict(color='#FF2E63', width=2, dash='dot'),
                                  name='Imag Projection'))
        fig3.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines+markers',
                                  marker=dict(size=12, color='black', symbol='arrow-bar-up', angleref='previous'),
                                  line=dict(color='red', width=5), name='Polar Vector z'))
        arc_t = np.linspace(0, theta_rad, 50)
        fig3.add_trace(
            go.Scatter(x=0.5 * np.cos(arc_t), y=0.5 * np.sin(arc_t), mode='lines', line=dict(color='orange', width=3),
                       name='Angle θ'))
        fig3.update_layout(xaxis_range=[-5.5, 5.5], yaxis_range=[-5.5, 5.5], width=600, height=600,
                           xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), showlegend=True,
                           template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------------
# TAB 4: 欧拉公式 (Euler's Formula)
# ---------------------------------------------------------
with tab4:
    st.subheader("Decoding God's Formula: From Growth to Perfect Rotation")

    physics_step = st.radio(
        "Select Experiment:",
        ["1. Mechanism: Bending the Line (Birth of e)",
         "2. Tool: Wrapping the Radius (Essence of Radians)",
         "3. Dimension Up: The 3D Helix"],
        horizontal=True
    )

    col1, col2 = st.columns([1.2, 2])

    if physics_step == "1. Mechanism: Bending the Line (Birth of e)":
        with col1:
            st.markdown("### Where does $e$ and $i$ come from?")
            growth_type = st.radio("Accelerator Type:",
                                   ["Real Growth (Compound Interest)", "Imaginary Growth (Rotation Force)"])
            if growth_type == "Real Growth (Compound Interest)":
                st.info(
                    r"""**History**: In 1683, Jacob Bernoulli asked: > If bank interest is 100%, and I split the year into $n$ parts... $$ \text{Total} = (1 + \frac{1}{n})^n $$ **Limit is $e \approx 2.718...$**""")
            else:
                st.success(
                    r"""**Imaginary Version**: If we apply growth from the **side ($i$)**: $$ (1 + \frac{i}{n})^n $$ **Result**: Energy used to "change direction". Draws a **Unit Circle**.""")
            n_val = st.slider("Split Steps (n)", 1, 1000, 10)
            if growth_type == "Real Growth (Compound Interest)":
                current_val = (1 + 1 / n_val) ** n_val
                st.metric("Current Result", f"{current_val:.5f}", delta=f"Distance to e: {np.e - current_val:.5f}",
                          delta_color="inverse")
            else:
                st.caption("Max out n to see the polygon become a circle!")

        with col2:
            fig4 = go.Figure()
            if growth_type == "Real Growth (Compound Interest)":
                step_val = (1 + 1 / n_val)
                path_y = [(step_val) ** i for i in range(n_val + 1)]
                path_x = list(range(n_val + 1))
                fig4.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', name='Compound Growth',
                                          line=dict(color='#00ADB5', width=3), marker=dict(size=6)))
                fig4.add_shape(type="line", x0=0, y0=np.e, x1=n_val, y1=np.e,
                               line=dict(color="#FF2E63", dash="dash", width=2), name="e Limit")
                fig4.add_annotation(x=n_val, y=np.e, text=f"e ≈ {np.e:.3f}", showarrow=True, arrowhead=1, ax=-40,
                                    ay=-40, font=dict(color="#FF2E63", size=14))
                fig4.update_layout(title=f"Approaching e: (1 + 1/{n_val})^{n_val}", xaxis_title="Steps (n)",
                                   yaxis_title="Value", yaxis=dict(range=[0.8, 3.0]),
                                   xaxis=dict(range=[-0.5, n_val + 0.5]), template="plotly_dark", height=450)
            else:
                step = 1 + (1j * np.pi / n_val)
                z = 1 + 0j
                path_x, path_y = [1], [0]
                for _ in range(n_val):
                    z = z * step
                    path_x.append(z.real)
                    path_y.append(z.imag)
                theta = np.linspace(0, np.pi, 50)
                fig4.add_trace(
                    go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='gray', dash='dot'),
                               name='Perfect Circle'))
                fig4.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines', name='Actual Path',
                                          line=dict(color='#FF2E63', width=3)))
                fig4.add_trace(
                    go.Scatter(x=[0, path_x[-1]], y=[0, path_y[-1]], mode='lines', line=dict(color='white', width=2)))
                fig4.update_layout(title=f"Imaginary Growth: n={n_val}", xaxis_range=[-1.5, 1.5], yaxis_range=[0, 1.5],
                                   height=450, template="plotly_dark")
            st.plotly_chart(fig4, use_container_width=True)

    elif physics_step == "2. Tool: Wrapping the Radius (Essence of Radians)":
        with col1:
            st.markdown("### Why use Radians?")
            wrap_val = st.slider("Wrap the Red Radius onto Circle:", 0.0, 3.2, 1.0, step=0.1)
            st.info(f"**Arc Length**: {wrap_val:.1f} radius lengths.\n**Angle**: {wrap_val:.1f} radians.")
        with col2:
            fig4 = go.Figure()
            theta = np.linspace(0, 2 * np.pi, 100)
            fig4.add_trace(
                go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='rgba(255,255,255,0.2)'),
                           showlegend=False))
            fig4.add_trace(
                go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='gray', dash='dash'), name='Radius r=1'))
            arc_t = np.linspace(0, wrap_val, 50)
            fig4.add_trace(
                go.Scatter(x=np.cos(arc_t), y=np.sin(arc_t), mode='lines', line=dict(color='#FF2E63', width=6),
                           name='Wrapped Radius'))
            fig4.add_trace(go.Scatter(x=[1, 1], y=[0, wrap_val], mode='lines', line=dict(color='#FF2E63', dash='dot'),
                                      name='Straight Radius'))
            fig4.update_layout(xaxis_range=[-1.2, 2], yaxis_range=[-0.5, 3.5], height=450,
                               title="Radians = Curved Radius", template="plotly_dark")
            st.plotly_chart(fig4, use_container_width=True)

    elif physics_step == "3. Dimension Up: The 3D Helix":
        with col1:
            st.markdown(r"### $$ e^{it} = \cos(t) + i\sin(t) $$")
            st.caption("Student: *'How does a circle become a wave?'*")
            st.markdown("""
            When you pull a 2D circle through **Time**, it becomes a **3D Helix**.
            * 🟡 **Yellow Shadow (Real):** $\cos(t)$ - A wave viewed from the side.
            * 🔴 **Pink Shadow (Imaginary):** $\sin(t)$ - A wave viewed from the top.
            """)
            st.divider()

            st.write("**Jump to specific time:**")
            cols = st.columns(4)
            cols[0].button("0", on_click=set_t, args=(0.0,))
            cols[1].button("π/2", on_click=set_t, args=(np.pi / 2,))
            cols[2].button("π", on_click=set_t, args=(np.pi,))
            cols[3].button("2π", on_click=set_t, args=(2 * np.pi,))

            t_3d = st.slider("Time Flow (t)", 0.0, 4 * np.pi, key='euler_t_3d')

            if abs(t_3d - np.pi) < 0.1:
                st.error(
                    "🌟 **Moment of Truth**: When t = π, the helix rotates exactly half a circle and lands on Real -1! ($e^{i\pi} = -1$)")

        with col2:
            t_range = np.linspace(0, 4 * np.pi, 300)
            x_helix = t_range
            y_helix = np.cos(t_range)
            z_helix = np.sin(t_range)

            fig4 = go.Figure()
            fig4.add_trace(
                go.Scatter3d(x=x_helix, y=y_helix, z=z_helix, mode='lines', line=dict(color='#00ADB5', width=5),
                             name='e^it (Helix)'))
            fig4.add_trace(go.Scatter3d(x=x_helix, y=np.ones_like(t_range) * 2, z=z_helix, mode='lines',
                                        line=dict(color='#FF2E63', width=3), opacity=0.5, name='Sin(t) Proj'))
            fig4.add_trace(go.Scatter3d(x=x_helix, y=y_helix, z=np.ones_like(t_range) * -2, mode='lines',
                                        line=dict(color='#FDB827', width=3), opacity=0.5, name='Cos(t) Proj'))

            cur_x, cur_y, cur_z = t_3d, np.cos(t_3d), np.sin(t_3d)
            fig4.add_trace(
                go.Scatter3d(x=[cur_x], y=[cur_y], z=[cur_z], mode='markers', marker=dict(size=10, color='red')))
            fig4.add_trace(
                go.Scatter3d(x=[cur_x, cur_x, cur_x], y=[2, cur_y, cur_y], z=[cur_z, cur_z, -2], mode='lines',
                             line=dict(color='#FF2E63', dash='dash')))

            fig4.update_layout(
                scene=dict(xaxis_title='Time (t)', yaxis_title='Real', zaxis_title='Imag', aspectmode='manual',
                           aspectratio=dict(x=2, y=1, z=1), xaxis=dict(range=[0, 13]), yaxis=dict(range=[-2, 2]),
                           zaxis=dict(range=[-2, 2])), height=500, margin=dict(l=0, r=0, b=0, t=0),
                template="plotly_dark")
            st.plotly_chart(fig4, use_container_width=True)