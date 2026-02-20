import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats  # <--- 新增：用于二项分布计算
from fractions import Fraction
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import scipy.integrate as integrate
import sympy as sp




# ==========================================
# 1. 配置与全局设置
# ==========================================
st.set_page_config(
    page_title="Matri-X: Mathematics Visualization",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. 功能模块 (已完成的课程)
# ==========================================

def render_topic_1_number_system():
    st.header("🌌 Topic 1: Evolution of Number Systems — Dynamic Vector Rotation")

    # 修改这里：增加一个 Tab，变成 4 个
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. The Evolution (History)",  # <--- 新增的
        "2. Complex Logic (Rotation)",  # 原本的 Tab 1
        "3. Polar Coordinates",  # 原本的 Tab 2
        "4. Euler's Formula"  # 原本的 Tab 3
    ])

    # --- TAB 1: From Number Line to Complex Plane (Story) ---
    # --- TAB 1: 数字发展史 (新增) ---
    # --- 放在 with tab1: 下面 ---
    with tab1:
        st.subheader("🌌 Topic 1: The Drama of Numbers")
        st.caption("A journey from a simple line to a 2D plane.")

        # 1. 顶部滑块
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

        # 2. 定义布局：左边故事，右边图表
        c_story, c_vis = st.columns([1.3, 2])
        fig = go.Figure()

        # === Ch 1: 自然数 ===
        if "1." in chapter:
            with c_story:
                st.subheader("🦕 1. Survival (The Ray)")
                st.info(f"""
                **Ch 1. The Hunters (Natural Numbers $\mathbb{{N}}$)**

                * **Who/Origin**: Prehistoric humans and ancient shepherds.
                * **Motivation**: Survival. Needed to count sheep or warriors.
                * **The Story**: Counting started with notches on bones. They only knew "one, two, three, many."
                * **The Impact**: Created **Addition**. 
                    * *Fatal Flaw*: Couldn't understand "debt" (negative apples).
                """)
            fig.add_shape(type="line", x0=0, y0=0, x1=5.5, y1=0, line=dict(color="gray", width=2))
            x_vals = [1, 2, 3, 4, 5]
            fig.add_trace(go.Scatter(x=x_vals, y=[0] * 5, mode='markers+text', text=x_vals, textposition="top center",
                                     marker=dict(size=15, color='#00ADB5'), name='N'))
            fig.update_layout(title="1D: The Ray", xaxis=dict(range=[-0.5, 6], showgrid=False),
                              yaxis=dict(visible=False))

        # === Ch 2: 整数 ===
        elif "2." in chapter:
            with c_story:
                st.subheader("💸 2. Debt (The Line)")
                st.info(f"""
                **Ch 2. The Accountants (Integers $\mathbb{{Z}}$)**

                * **Who**: Brahmagupta (India, 628 AD).
                * **Motivation**: Commerce. Distinguishing "earned" vs "owed".
                * **The Story**: Defined **"Fortunes"** (+) and **"Debts"** (-). Europeans rejected this for 1000 years as "absurd".
                * **The Impact**: The Ray became a **Line**, allowing algebraic symmetry.
                """)
            fig.add_shape(type="line", x0=-5.5, y0=0, x1=5.5, y1=0, line=dict(color="gray", width=2))
            x_vals = [-3, -2, -1, 0, 1, 2, 3]
            fig.add_trace(
                go.Scatter(x=x_vals, y=[0] * len(x_vals), mode='markers+text', text=x_vals, textposition="top center",
                           marker=dict(size=15, color='#FF2E63'), name='Z'))
            fig.update_layout(title="1D: The Line", xaxis=dict(range=[-4, 4], showgrid=False),
                              yaxis=dict(visible=False))

        # === Ch 3: 有理数 ===
        elif "3." in chapter:
            with c_story:
                st.subheader("🍰 3. Sharing (Density)")
                st.info(f"""
                **Ch 3. The Broken Numbers (Rationals $\mathbb{{Q}}$)**

                * **Who**: Egyptians & Pythagoreans.
                * **Motivation**: Fair distribution (taxes, food).
                * **The Story**: "Fraction" means "Broken". Pythagoras believed **"All is Ratio"** (Music 1:2, 2:3).
                * **The Impact**: The line became **"dense"**. They thought fractions filled every gap.
                """)
            fig.add_shape(type="line", x0=-3, y0=0, x1=3, y1=0, line=dict(color="gray", width=2))
            fig.add_trace(go.Scatter(x=[-2, -1, 0, 1, 2], y=[0] * 5, mode='markers', marker=dict(size=8, color='gray')))
            fig.add_trace(go.Scatter(x=[-1.5, -0.5, 0.5, 1.5], y=[0] * 4, mode='markers+text',
                                     text=["-3/2", "-1/2", "1/2", "3/2"], textposition="top center",
                                     marker=dict(size=12, color='#FDB827'), name='Q'))
            fig.update_layout(title="1D: Filling Gaps", xaxis=dict(range=[-3, 3], showgrid=False),
                              yaxis=dict(visible=False))

        # === Ch 4: 无理数 ===
        elif "4." in chapter:
            with c_story:
                st.subheader("💀 4. The Monster (√2)")
                st.error(f"""
                **Ch 4. The Murderous Root (Irrationals $\mathbb{{R \setminus Q}}$)**

                * **Who**: Hippasus (500 BC).
                * **Motivation**: Geometric precision.
                * **The Story**: Proved $\sqrt{{2}}$ isn't a fraction. This broke the Pythagorean creed. **Legend says he was drowned for this secret.**
                * **The Impact**: First Crisis of Math. Revealed "holes" in the number line.
                """)
            fig.add_shape(type="line", x0=0, y0=0, x1=3, y1=0, line=dict(color="gray", width=2))
            fig.add_trace(go.Scatter(x=[0, 1, 1, 0], y=[0, 0, 1, 0], mode='lines', line=dict(color='green', dash='dot'),
                                     name='Geometry'))
            r = np.sqrt(2)
            fig.add_trace(go.Scatter(x=[r], y=[0], mode='markers+text', text=["√2"], textposition="top center",
                                     marker=dict(size=15, color='purple', symbol='diamond')))
            fig.update_layout(title="1D: Geometry fills the Line", xaxis=dict(range=[-0.5, 2.5], showgrid=False),
                              yaxis=dict(visible=False))

        # === Ch 5: 超越数 ===
        elif "5." in chapter:
            with c_story:
                st.subheader("👻 5. The Outlaws (π, e)")
                st.info(f"""
                **Ch 5. The Ghosts (Transcendental)**

                * **Who**: Liouville, Hermite.
                * **Motivation**: Distinguishing constants of nature.
                * **The Story**: $\pi$ and $e$ are **"Outlaws"**. They aren't solutions to ANY algebra equation.
                * **The Impact**: Proved "Squaring the Circle" is impossible.
                """)
            fig.add_shape(type="line", x0=2, y0=0, x1=4, y1=0, line=dict(color="gray", width=2))
            fig.add_trace(go.Scatter(x=[np.e], y=[0], mode='markers+text', text=["e"], textposition="top center",
                                     marker=dict(size=15, color='#E056FD')))
            fig.add_trace(go.Scatter(x=[np.pi], y=[0], mode='markers+text', text=["π"], textposition="top center",
                                     marker=dict(size=15, color='#E056FD')))
            fig.update_layout(title="1D: The Line is Complete", xaxis=dict(range=[2, 4], showgrid=False),
                              yaxis=dict(visible=False))

        # === Ch 6: 笛卡尔坐标系 ===
        elif "6." in chapter:
            with c_story:
                st.subheader("🪰 6. The Cartesian Revolution")
                st.warning(f"""
                **Ch 6. The Fly (Cartesian Grid)**

                * **Who**: René Descartes (1637).
                * **Motivation**: Linking Algebra & Geometry.
                * **The Story**: Sick in bed, he watched a **fly** on the ceiling. Realized he could track it with TWO numbers (x, y).
                * **The Impact**: Born of **Analytic Geometry**. Numbers jumped from 1D Line to **2D Plane**.
                """)
            # 画网格
            for i in range(-2, 3):
                fig.add_shape(type="line", x0=i, y0=-2, x1=i, y1=2, line=dict(color="rgba(255,255,255,0.1)", width=1))
                fig.add_shape(type="line", x0=-2, y0=i, x1=2, y1=i, line=dict(color="rgba(255,255,255,0.1)", width=1))
            fig.add_shape(type="line", x0=-2, y0=0, x1=2, y1=0, line=dict(color="white", width=2))
            fig.add_shape(type="line", x0=0, y0=-2, x1=0, y1=2, line=dict(color="white", width=2))

            # 苍蝇 (用 'x' 代替 'bug')
            fig.add_trace(
                go.Scatter(x=[1.5], y=[1.0], mode='markers+text', text=["The Fly (x,y)"], textposition="top right",
                           marker=dict(size=15, color='#FDB827', symbol='x')))
            fig.update_layout(title="2D: The Grid is Born", xaxis=dict(range=[-2, 2], showgrid=False),
                              yaxis=dict(range=[-2, 2], showgrid=False, visible=True))

        # === Ch 7: 复数 (包含手稿图片) ===
        elif "7." in chapter:
            with c_story:
                st.subheader("🧠 7. The Complex Plane")
                st.error(f"""
                **Ch 7. The Impossible Dimension ($\mathbb{{C}}$)**

                * **Who**: Cardano, Gauss.
                * **Motivation**: Solving $x^2 = -1$.
                * **The Story**: Cardano called $\sqrt{{-1}}$ **"mental torture"**. Gauss fixed it by standing the axis up. **$i$ points Sideways.**
                * **The Impact**: **Rotation** entered math.
                """)

            # 复平面图
            fig.add_shape(type="line", x0=-2, y0=0, x1=2, y1=0, line=dict(color="white", width=2))
            fig.add_shape(type="line", x0=0, y0=-2, x1=0, y1=2, line=dict(color="cyan", width=2))
            fig.add_annotation(x=0.2, y=1, ax=1, ay=0, xref="x", yref="y", axref="x", ayref="y", arrowcolor="cyan",
                               arrowwidth=2, arrowhead=2, text="Rotate 90°")
            fig.add_trace(go.Scatter(x=[0], y=[1], mode='markers+text', text=["i"], textposition="top right",
                                     marker=dict(size=15, color='cyan')))
            fig.update_layout(title="2D: The Complex Plane", xaxis=dict(range=[-2, 2], showgrid=True),
                              yaxis=dict(range=[-2, 2], showgrid=True, visible=True))

        # === 关键步骤：把图画出来！(这是你之前漏掉的) ===
        fig.update_layout(height=400, template="plotly_dark", margin=dict(l=20, r=20, t=40, b=20),
                          plot_bgcolor='rgba(0,0,0,0)')
        with c_vis:
            st.plotly_chart(fig, use_container_width=True)

        # === 只有在 Ch 7 时才显示卡尔达诺手稿 (放在下面) ===
        if "7." in chapter:
            st.markdown("---")
            st.subheader("💡 Interesting Fact: Cardano's 'Mental Torture'")
            col_img, col_txt = st.columns([1, 2])

            with col_img:
                # 确保 cardano.jpg 在你文件夹里，否则用下面第二行的网址版
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
#虚数的诞生
    with tab2:
        st.subheader("Thought Experiment: Unlocking Dimensions")
        st.markdown(r"**Core Logic**: If $\times (-1)$ is a half-turn rotation (180°), then $\times i$ is a quarter-turn rotation (90°).")

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
        val = 2.5 # Fixed modulus

        with col1:
            if story_step == "1. Start: Real 1":
                st.info("Everything starts at **1** on the Real Axis.\n\nDirection: Right ($0^{\\circ}$)")
            elif story_step == "2. Observe: x (-1) (180°)":
                st.write("When calculating $1 \\times (-1)$, the point jumps to the left.")
                st.info("**Geometric Essence**:\nThis isn't 'debt', this is a **180° Rotation**.")
            elif story_step == "3. Dilemma: Finding √-1":
                st.error("""
                    **The Problem**:
                    We need a number $x$ that, when multiplied twice, equals -1 ($180^{\\circ}$).
                    $$ x \\cdot x = -1 $$
                    But on the number line:
                    * $0^{\\circ}$ twice is still $0^{\\circ}$.
                    * $180^{\\circ}$ twice is $360^{\\circ}$ (back to start).
                    **No solution on the 1D line!**
                    """)
            elif story_step == "4. Breakthrough: Define i (90°)":
                st.success("""
                    **The Solution**:
                    Since we need $180^{\\circ}$, let's **split it in two**.
                    Each step rotates **90°**.
                    $$ i = \\text{Rotation of } 90^{\\circ} $$
                    **Welcome to the Complex Plane!**
                    """)
            elif story_step == "5. Verify: i² (-1)":
                st.warning("""
                    **Verification**:
                    If $i$ is 90° rotation...
                    Then $i \\times i$ is rotating 90° twice.
                    $$ 90^{\\circ} + 90^{\\circ} = 180^{\\circ} $$
                    **Look! It lands exactly on -1.** So $i^2 = -1$ is a geometric necessity.
                    """)
            elif story_step == "6. Evolve: i³ (-i)":
                st.write("Continuing the rotation...")
                st.latex(r"i^3 = i^2 \cdot i = -1 \cdot i = -i")
                st.info("Now we are at $270^{\\circ}$, the bottom of the imaginary axis.")
            elif story_step == "7. Cycle: i⁴ (1)":
                st.write("One last rotation...")
                st.latex(r"i^4 = i^3 \cdot i = -i \cdot i = -i^2 = 1")
                st.success("We have rotated a full circle ($360^{\\circ}$) and returned to the start. **This is the power of cycles.**")

        with col2:
            fig = go.Figure()
            # Axes
            fig.add_shape(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="gray", width=2))
            fig.add_shape(type="line", x0=0, y0=-4, x1=0, y1=4, line=dict(color="gray", width=2))
            fig.add_annotation(x=4.2, y=0, text="Real", showarrow=False)
            fig.add_annotation(x=0, y=4.2, text="Imag", showarrow=False)
            # Circle orbit
            theta_circle = np.linspace(0, 2 * np.pi, 100)
            fig.add_trace(go.Scatter(x=val * np.cos(theta_circle), y=val * np.sin(theta_circle),
                                     mode='lines', line=dict(dash='dot', color='rgba(255,255,255,0.2)'),
                                     hoverinfo='skip'))
            # Dynamic Logic
            current_x, current_y = val, 0
            color = "#00ADB5"
            label = "1"
            if "2." in story_step:
                current_x, current_y = -val, 0
                color = "#FF2E63"
                label = "-1"
                t = np.linspace(0, np.pi, 50)
                fig.add_trace(go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='orange', dash='dash')))
            elif "3." in story_step:
                current_x, current_y = val, 0
                label = "?"
                color = "gray"
                fig.add_annotation(x=0, y=1, text="Dead End!", font=dict(color="red", size=20), showarrow=False)
            elif "4." in story_step:
                current_x, current_y = 0, val
                color = "#6610f2"
                label = "i"
                t = np.linspace(0, np.pi / 2, 50)
                fig.add_trace(go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
            elif "5." in story_step:
                current_x, current_y = -val, 0
                color = "#FF2E63"
                label = "i² = -1"
                t = np.linspace(0, np.pi, 50)
                fig.add_trace(go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
                fig.add_trace(go.Scatter(x=[0], y=[val], mode='markers+text', marker=dict(color='gray', size=10), text=["i"], textposition="top right"))
            elif "6." in story_step:
                current_x, current_y = 0, -val
                color = "#FDB827"
                label = "i³ = -i"
                t = np.linspace(0, 3 * np.pi / 2, 100)
                fig.add_trace(go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
                fig.add_trace(go.Scatter(x=[0, -val], y=[val, 0], mode='markers', marker=dict(color='gray', size=8)))
            elif "7." in story_step:
                current_x, current_y = val, 0
                color = "#00ADB5"
                label = "i⁴ = 1"
                t = np.linspace(0, 2 * np.pi, 100)
                fig.add_trace(go.Scatter(x=val * np.cos(t), y=val * np.sin(t), mode='lines', line=dict(color='#6610f2', width=3)))
                fig.add_trace(go.Scatter(x=[0, -val, 0], y=[val, 0, -val], mode='markers', marker=dict(color='gray', size=8)))

            fig.add_trace(go.Scatter(
                x=[0, current_x], y=[0, current_y],
                mode='lines+markers+text',
                marker=dict(size=15, symbol="arrow-bar-up", angleref="previous", color=color),
                line=dict(width=5, color=color),
                text=[None, label],
                textposition="top center"
            ))
            fig.update_layout(xaxis_range=[-4, 4], yaxis_range=[-4, 4], height=500, width=500, showlegend=False, title="Complex Plane Evolution", plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

    # --- TAB 3: Polar Radar (完整回归) ---
    with tab3:
        st.subheader("Polar Coordinates: Redefining Position with 'Angle' & 'Distance'")
        st.markdown(r"""In Polar form, we don't say "Go right 3, up 4". We say: > **"Face direction $\theta$, walk distance $r$."**""")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### 🕹️ Radar Control")
            r = st.slider("Modulus r", 0.0, 5.0, 3.0, step=0.1)
            theta_deg = st.slider("Argument θ°", 0, 360, 45)
            theta_rad = np.radians(theta_deg)
            x = r * np.cos(theta_rad)
            y = r * np.sin(theta_rad)
            st.latex(rf"z = {r} \cdot e^{{i \cdot {theta_deg}^\circ}}")
            st.markdown("---")
            st.write("**Translate to Cartesian:**")
            st.latex(rf"x = {r} \cos({theta_deg}^\circ) = {x:.2f}")
            st.latex(rf"y = {r} \sin({theta_deg}^\circ) = {y:.2f}")
            st.info(f"💡 Complex Number: {x:.2f} + {y:.2f}i")
        with col2:
            fig5 = go.Figure()
            for i in range(1, 6):
                t = np.linspace(0, 2 * np.pi, 100)
                fig5.add_trace(go.Scatter(x=i * np.cos(t), y=i * np.sin(t), mode='lines', line=dict(color='rgba(255,255,255,0.1)', width=1), showlegend=False, hoverinfo='skip'))
            fig5.add_trace(go.Scatter(x=[0, x], y=[0, 0], mode='lines', line=dict(color='#00ADB5', width=4, dash='solid'), name='Real Projection'))
            fig5.add_trace(go.Scatter(x=[x, x], y=[0, y], mode='lines', line=dict(color='#FF2E63', width=2, dash='dot'), name='Imag Projection'))
            fig5.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines+markers', marker=dict(size=12, color='black', symbol='arrow-bar-up', angleref='previous'), line=dict(color='black', width=5), name='Polar Vector z'))
            arc_t = np.linspace(0, theta_rad, 50)
            fig5.add_trace(go.Scatter(x=0.5 * np.cos(arc_t), y=0.5 * np.sin(arc_t), mode='lines', line=dict(color='orange', width=3), name='Angle θ'))
            fig5.update_layout(xaxis_range=[-5.5, 5.5], yaxis_range=[-5.5, 5.5], width=600, height=600, xaxis=dict(showgrid=False), yaxis=dict(showgrid=False), showlegend=True, template="plotly_dark", plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig5, use_container_width=True)

    # --- TAB 4: Euler's Formula (修复了折线图 + 保留了 3D 螺旋) ---
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

        # Sub-Tab 1: 增长机制
        if physics_step == "1. Mechanism: Bending the Line (Birth of e)":
            with col1:
                st.markdown("### Where does $e$ come from?")
                growth_type = st.radio("Accelerator Type:", ["Real Growth (Compound Interest)", "Imaginary Growth (Rotation Force)"])
                if growth_type == "Real Growth (Compound Interest)":
                    st.info(r"""**History**: In 1683, Jacob Bernoulli asked: > If bank interest is 100%, and I split the year into $n$ parts... $$ \text{Total} = (1 + \frac{1}{n})^n $$ **Limit is $e \approx 2.718...$**""")
                else:
                    st.success(r"""**Imaginary Version**: If we apply growth from the **side ($i$)**: $$ (1 + \frac{i}{n})^n $$ **Result**: Energy used to "change direction". Draws a **Unit Circle**.""")
                n_val = st.slider("Split Steps (n)", 1, 1000, 10)
                if growth_type == "Real Growth (Compound Interest)":
                    current_val = (1 + 1 / n_val) ** n_val
                    st.metric("Current Result", f"{current_val:.5f}", delta=f"Distance to e: {np.e - current_val:.5f}", delta_color="inverse")
                else:
                    st.caption("Max out n to see the polygon become a circle!")

            with col2:
                fig = go.Figure()
                if growth_type == "Real Growth (Compound Interest)":
                    # --- 修复：折线图 ---
                    step_val = (1 + 1/n_val)
                    path_y = [(step_val)**i for i in range(n_val + 1)]
                    path_x = list(range(n_val + 1))
                    fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', name='Compound Growth', line=dict(color='#00ADB5', width=3), marker=dict(size=6)))
                    fig.add_shape(type="line", x0=0, y0=np.e, x1=n_val, y1=np.e, line=dict(color="#FF2E63", dash="dash", width=2), name="e Limit")
                    fig.add_annotation(x=n_val, y=np.e, text=f"e ≈ {np.e:.3f}", showarrow=True, arrowhead=1, ax=-40, ay=-40, font=dict(color="#FF2E63", size=14))
                    fig.update_layout(title=f"Approaching e: (1 + 1/{n_val})^{n_val}", xaxis_title="Steps (n)", yaxis_title="Value", yaxis=dict(range=[0.8, 3.0]), xaxis=dict(range=[-0.5, n_val + 0.5]), template="plotly_white", height=450)
                else:
                    # 虚数圆
                    step = 1 + (1j * np.pi / n_val)
                    z = 1 + 0j
                    path_x, path_y = [1], [0]
                    for _ in range(n_val):
                        z = z * step
                        path_x.append(z.real)
                        path_y.append(z.imag)
                    theta = np.linspace(0, np.pi, 50)
                    fig.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='gray', dash='dot'), name='Perfect Circle'))
                    fig.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines', name='Actual Path', line=dict(color='#FF2E63', width=3)))
                    fig.add_trace(go.Scatter(x=[0, path_x[-1]], y=[0, path_y[-1]], mode='lines', line=dict(color='white', width=2)))
                    fig.update_layout(title=f"Imaginary Growth: n={n_val}", xaxis_range=[-1.5, 1.5], yaxis_range=[0, 1.5], height=450)
                st.plotly_chart(fig, use_container_width=True)

        # Sub-Tab 2: 弧度工具
        elif physics_step == "2. Tool: Wrapping the Radius (Essence of Radians)":
            with col1:
                st.markdown("### Why use Radians?")
                wrap_val = st.slider("Wrap the Red Radius onto Circle:", 0.0, 3.2, 1.0, step=0.1)
                st.info(f"**Arc Length**: {wrap_val:.1f} radius lengths.\n**Angle**: {wrap_val:.1f} radians.")
            with col2:
                fig = go.Figure()
                theta = np.linspace(0, 2 * np.pi, 100)
                fig.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='rgba(255,255,255,0.2)'), showlegend=False))
                fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='gray', dash='dash'), name='Radius r=1'))
                arc_t = np.linspace(0, wrap_val, 50)
                fig.add_trace(go.Scatter(x=np.cos(arc_t), y=np.sin(arc_t), mode='lines', line=dict(color='#FF2E63', width=6), name='Wrapped Radius'))
                fig.add_trace(go.Scatter(x=[1, 1], y=[0, wrap_val], mode='lines', line=dict(color='#FF2E63', dash='dot'), name='Straight Radius'))
                fig.update_layout(xaxis_range=[-1.2, 2], yaxis_range=[-0.5, 3.5], height=450, title="Radians = Curved Radius")
                st.plotly_chart(fig, use_container_width=True)

        # Sub-Tab 3: 3D 螺旋 (终极修复版)
        elif physics_step == "3. Dimension Up: The 3D Helix":

            # --- 1. 核心修复：把变量名统一为 'euler_t_3d' ---
            # 如果系统里没有这个变量，先创建一个默认值 2.0
            if 'euler_t_3d' not in st.session_state:
                st.session_state['euler_t_3d'] = 2.0

            # 定义一个简单的回调函数，专门用来改这个值
            def set_t(val):
                st.session_state['euler_t_3d'] = float(val)

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

                # --- 2. 按钮：点击时，直接修改 'euler_t_3d' ---
                cols[0].button("0", on_click=set_t, args=(0.0,))
                cols[1].button("π/2", on_click=set_t, args=(np.pi / 2,))
                cols[2].button("π", on_click=set_t, args=(np.pi,))
                cols[3].button("2π", on_click=set_t, args=(2 * np.pi,))

                # --- 3. 滑块：关键修改！ ---
                # 这里的 key 必须也是 'euler_t_3d'。
                # 这样滑块和按钮就“心意相通”了，动谁都会更新同一个值。
                # 注意：因为用了 key，所以不需要写 value=...，它会自动读取。
                t_3d = st.slider("Time Flow (t)", 0.0, 4 * np.pi, key='euler_t_3d')

                if abs(t_3d - np.pi) < 0.1:
                    st.error(
                        "🌟 **Moment of Truth**: When t = π, the helix rotates exactly half a circle and lands on Real -1! ($e^{i\pi} = -1$)")

            with col2:
                # --- 4. 绘图部分 (保持原样，只是把变量换成了 t_3d) ---
                t_range = np.linspace(0, 4 * np.pi, 300)
                x_helix = t_range
                y_helix = np.cos(t_range)
                z_helix = np.sin(t_range)

                fig = go.Figure()

                # 主螺旋
                fig.add_trace(
                    go.Scatter3d(x=x_helix, y=y_helix, z=z_helix, mode='lines', line=dict(color='#00ADB5', width=5),
                                 name='e^it (Helix)'))

                # 投影 (Sin - Pink)
                fig.add_trace(go.Scatter3d(x=x_helix, y=np.ones_like(t_range) * 2, z=z_helix, mode='lines',
                                           line=dict(color='#FF2E63', width=3), opacity=0.5, name='Sin(t) Proj'))

                # 投影 (Cos - Yellow)
                fig.add_trace(go.Scatter3d(x=x_helix, y=y_helix, z=np.ones_like(t_range) * -2, mode='lines',
                                           line=dict(color='#FDB827', width=3), opacity=0.5, name='Cos(t) Proj'))

                # 当前点
                cur_x, cur_y, cur_z = t_3d, np.cos(t_3d), np.sin(t_3d)
                fig.add_trace(
                    go.Scatter3d(x=[cur_x], y=[cur_y], z=[cur_z], mode='markers', marker=dict(size=10, color='red')))

                # 连接线
                fig.add_trace(
                    go.Scatter3d(x=[cur_x, cur_x, cur_x], y=[2, cur_y, cur_y], z=[cur_z, cur_z, -2], mode='lines',
                                 line=dict(color='#FF2E63', dash='dash')))

                fig.update_layout(
                    scene=dict(xaxis_title='Time (t)', yaxis_title='Real', zaxis_title='Imag', aspectmode='manual',
                               aspectratio=dict(x=2, y=1, z=1), xaxis=dict(range=[0, 13]), yaxis=dict(range=[-2, 2]),
                               zaxis=dict(range=[-2, 2])), height=500, margin=dict(l=0, r=0, b=0, t=0))
                st.plotly_chart(fig, use_container_width=True)

#Topic 3: Sequence and Series



def render_topic_3_sequence():
    st.header("🌌 Topic 3: The Rhythm of Infinity (Sequences & Series)")

    tab1, tab2, tab3, tab4, tab5= st.tabs([
        "1. Decompressing Sigma (How it works)",
        "2. Arithmetic (AP) and Geometric (GP) Progression",
        "3. Hall of Fame (The Logic)",
        "4. Pascal to Normal",
        "5. Taylor Series (Expansion)"
    ])

    # --- TAB 1: 排版优化 + Sigma 慢动作拆解 ---
    # --- TAB 1: 故事化引导 (完全重写) ---
    with tab1:
        # === 第一部分：概念引入 ===
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

        # === 第二部分：视觉实验 (切正方形) ===
        st.subheader("Step 2: Visual Experiment")
        st.write("Let's look at a specific Sequence: **Halving the Cake**.")

        col_vis_ctrl, col_vis_plot = st.columns([1, 2])

        with col_vis_ctrl:
            n_cuts = st.slider("Number of Cuts (n)", 1, 8, 3)
            st.write(f"At step **n={n_cuts}**, we add a slice of size:")
            st.latex(rf"T_{n_cuts} = \frac{{1}}{{{2 ** n_cuts}}}")

        with col_vis_plot:
            # 切方块动画
            fig = go.Figure()
            fig.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1, line=dict(color="gray", width=2))

            x_curr, y_curr, w, h, direction = 0, 0, 1, 1, 0
            colors = ['#FF2E63', '#08D9D6', '#252A34', '#EAEAEA']
            terms_latex = []  # 收集每一项，后面用

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
                              margin=dict(l=0, r=0, t=0, b=0))
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # === 第三部分：遇到的麻烦 (太长了) ===
        st.subheader("Step 3: The Problem (Calculation)")
        st.write("Now, if we want to calculate the **Total Area (Series)**, we have to add them up:")

        long_sum_str = " + ".join(terms_latex)
        st.latex(rf"S_{{{n_cuts}}} = {long_sum_str}")

        if n_cuts >= 5:
            st.error(f"😫 **It's getting too long!** Imagine if n=100. Writing this out is impossible.")
        else:
            st.warning("It's manageable now, but what if n=100?")

        st.markdown("---")

        # === 第四部分：懒人发明符号 + 解释 ===
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
#AP 和GP
        with tab2:
            st.header("🧬 Topic 3: The Limit of Growth")
            st.caption("From Discrete Progressions to the Continuous Constant (e)")

            # === 1. 互动实验：线性与指数的较量 ===
            st.subheader("1. The Rhythm: Linear vs. Exponential")
            st.write("First, let's see how Arithmetic (AP) and Geometric (GP) sequences behave.")

            c_input, c_vis = st.columns([1, 2])

            with c_input:
                st.info("🐢 **Arithmetic (AP)**")
                a_ap = st.number_input("Start (a)", value=1, key="ap_a_final")
                d = st.number_input("Common Difference (d)", value=2, key="ap_d_final")

                st.markdown("---")

                st.error("🚀 **Geometric (GP)**")
                a_gp = st.number_input("Start (a)", value=1, key="gp_a_final")
                r = st.number_input("Common Ratio (r)", value=1.5, step=0.1, key="gp_r_final")

                st.markdown("---")
                n_steps = st.slider("Number of Terms (n)", 5, 30, 15)

            with c_vis:
                # 计算数据
                n_vals = np.arange(1, n_steps + 1)
                ap_vals = a_ap + (n_vals - 1) * d
                gp_vals = a_gp * (r ** (n_vals - 1))

                # 绘制对比图
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

            # === 2. 深度推导：逻辑的魅力 (宽屏版) ===
            st.divider()
            st.subheader("2. The Logic Behind the Formulas")
            st.write("For students who struggle with formulas: Don't memorize, **visualize**.")

            # --- AP 推导 ---
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

            # --- GP 推导 ---
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
                Look at the middle! All terms except the very first and the very last vanish.

                $$ 
                \begin{aligned}
                S_n &= a + \color{red}{ar + ar^2 + \dots + ar^{n-1}} \\
                - (rS_n &= \quad \color{red}{ar + ar^2 + \dots + ar^{n-1}} + ar^n) \\
                \hline
                S_n(1-r) &= a - ar^n
                \end{aligned}
                $$

                **Step 3:** Solve for $S_n$.
                $$ \boxed{S_n = \frac{a(1-r^n)}{1-r}} $$
                """)

            # === 3. 历史与实验室：e 的诞生 ===
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

                # 频率滑块
                steps = [1, 2, 4, 12, 52, 365, 8760, 100000]
                labels = ["Yearly", "6-Months", "Quarterly", "Monthly", "Weekly", "Daily", "Hourly", "Continuously"]

                sel_label = st.select_slider("Change Frequency (n)", options=labels, value="Yearly")
                n_val = steps[labels.index(sel_label)]

                # 计算 e 的逼近值
                e_approx = (1 + 1 / n_val) ** n_val

                st.write(f"**Frequency (n):** {n_val}")
                st.latex(rf"\left( 1 + \frac{{1}}{{{n_val}}} \right)^{{{n_val}}}")
                st.metric("Final Amount", f"${e_approx:.6f}", delta=f"{e_approx - np.e:.6f} from e")

                if n_val == 1:
                    st.warning("Just $2.00. Not very greedy.")
                elif n_val >= 365:
                    st.success("You are hitting the 'Growth Wall'!")

            with c_e_fig:
                # 绘制逼近曲线
                x_e = np.linspace(1, 100, 200)
                y_e = (1 + 1 / x_e) ** x_e

                fig_e = go.Figure()
                fig_e.add_trace(
                    go.Scatter(x=x_e, y=y_e, mode='lines', name='Money', line=dict(color='#00ADB5', width=4)))

                # 画出 e 的渐近线
                fig_e.add_hline(y=np.e, line_dash="dash", line_color="#FF2E63",
                                annotation_text="The Wall (e ≈ 2.718)", annotation_position="bottom right")

                # 标记当前点
                curr_x = min(n_val, 100)
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

            st.caption("""
                **Fun Fact:** Although Bernoulli discovered it, the letter **'e'** was chosen by **Leonhard Euler** 50 years later. 
                Some say 'e' stands for "Exponential", others say it stands for "Euler". 
                """)
        # --- TAB 3: 名人堂 (硬核数学 + 视频资源) ---
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

            # === 1. 调和级数 (Oresme's Proof) ===
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
                    st.latex(
                        r"Group 3: \frac{1}{8} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}")

                    st.markdown("**Step 4: Final Logic**")
                    st.latex(r"S > 1 + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \dots = \infty")
                    st.error("Since we can add $1/2$ infinitely many times, the sum must be Infinite.")

                    # 🔥 视频链接 (绝对保留)
                    st.info("📺 **Video Resources:**")
                    st.markdown(
                        "[▶️ 3Blue1Brown: The Harmonic Series Paradox](https://www.youtube.com/watch?v=ly_J23__eHw)")
                    st.markdown(
                        "[▶️ Khan Academy: Proof of Divergence](https://www.khanacademy.org/math/calculus-all/cc-cal-series-tests/cc-cal-integral-test/v/harmonic-series-divergence)")

                with c2:
                    # 绘图：展示真实值 vs 这里的下界估计
                    st.write("**Visualizing the Lower Bound:**")
                    x_vals = [1, 2, 4, 8, 16, 32]
                    y_lower = [1, 1.5, 2.0, 2.5, 3.0, 3.5]  # 1 + k/2

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x_vals, y=y_lower, mode='lines+markers', name='Lower Bound (1 + k/2)',
                                             line=dict(color='#FF2E63', width=3)))

                    fig.update_layout(
                        title="Divergence via Grouping",
                        xaxis_title="Number of Terms (n)",
                        yaxis_title="Sum Value",
                        xaxis_type="log",  # 对数坐标更能体现指数分组
                        template="plotly_dark",
                        height=500
                    )
                    st.plotly_chart(fig, use_container_width=True)

            # === 2. 巴塞尔问题 (Euler's Proof) ===
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

                    st.markdown("**Step 2: Infinite Product Formula (The infinite product part is a bit advanced and not required by the syllabus, but it’s a fascinating piece of history. You can find more in-depth explanations in the videos listed.)**")
                    st.write("A polynomial $P(x)$ with roots $r_1, r_2$ can be written as $A(1-\\frac{x}{r_1})(1-\\frac{x}{r_2})\dots$")
                    st.write("The roots of $\sin(x)/x$ are $\pm \pi, \pm 2\pi, \pm 3\pi \dots$. So:")
                    st.latex(
                        r"\frac{\sin(x)}{x} = \left(1-\frac{x}{\pi}\right)\left(1+\frac{x}{\pi}\right)\left(1-\frac{x}{2\pi}\right)\left(1+\frac{x}{2\pi}\right)\dots")
                    st.write("Use difference of squares $(1-a)(1+a) = 1-a^2$:")
                    st.latex(
                        r"\frac{\sin(x)}{x} = \left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{4\pi^2}\right)\left(1-\frac{x^2}{9\pi^2}\right)\dots \quad \text{--- (Eq 2)}")

                    st.markdown("**Step 3: Extract the $x^2$ Coefficient**")
                    st.write("In Eq 2, to get the $x^2$ term, we sum the $-1/k^2\pi^2$ terms:")
                    st.latex(
                        r"\text{Coeff of } x^2 = -\frac{1}{\pi^2} - \frac{1}{4\pi^2} - \frac{1}{9\pi^2} - \dots = -\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}")

                    st.markdown("**Step 4: Equate Coefficients**")
                    st.write("Compare $x^2$ coefficient from Eq 1 ($-1/6$) and Eq 2:")
                    st.latex(r"-\frac{1}{6} = -\frac{1}{\pi^2} \sum_{n=1}^{\infty} \frac{1}{n^2}")
                    st.success(r"Multiply by $-\pi^2$:  $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$")

                    # 🔥 视频链接 (绝对保留)
                    st.info("📺 **Video Resources:**")
                    st.markdown(
                        "[▶️ 3Blue1Brown: The Basel Problem Visualized](https://www.youtube.com/watch?v=d-o3eB9sfls)")
                    st.markdown("[▶️ Numberphile: Pi squared over 6](https://www.youtube.com/watch?v=0A6e9p8e20Y)")

                with c2:
                    # 绘图：收敛速度
                    st.write("**Visualizing Convergence:**")
                    n_b = 50
                    x_b = np.arange(1, n_b + 1)
                    y_b = np.cumsum(1 / (x_b ** 2))
                    target = (np.pi ** 2) / 6

                    fig = go.Figure()
                    fig.add_trace(
                        go.Scatter(x=x_b, y=y_b, mode='lines', name='Partial Sum', line=dict(color='#00ADB5', width=3)))
                    fig.add_shape(type="line", x0=0, y0=target, x1=n_b, y1=target,
                                  line=dict(color="#FF2E63", dash="dash"))
                    fig.add_annotation(x=n_b / 2, y=target - 0.1, text="Target: 1.6449...", font=dict(color="#FF2E63"))

                    fig.update_layout(title="Approaching π²/6", xaxis_title="n", template="plotly_dark", height=500)
                    st.plotly_chart(fig, use_container_width=True)

            # === 3. 斐波那契 (Deriving Golden Ratio) ===
            elif "Fibonacci" in series_choice:
                with c1:
                    st.markdown("### 🌻 3. Fibonacci & Golden Ratio")
                    st.markdown("**Claim:** The ratio of consecutive terms converges to $\phi \\approx 1.618$.")

                    st.markdown("#### 📝 Step-by-Step Derivation")

                    st.markdown("**Step 1: The Recursive Definition**")
                    st.latex(r"F_{n+1} = F_n + F_{n-1}")
                    st.write("Sequence: $1, 1, 2, 3, 5, 8, 13, 21 \dots$")

                    st.markdown("**Step 2: Construct the Ratio**")
                    st.write("Divide the whole equation by $F_n$:")
                    st.latex(r"\frac{F_{n+1}}{F_n} = \frac{F_n}{F_n} + \frac{F_{n-1}}{F_n} = 1 + \frac{F_{n-1}}{F_n}")

                    st.markdown("**Step 3: Define the Limit**")
                    st.write("Let $L = \lim_{n \\to \infty} \\frac{F_{n+1}}{F_n}$.")
                    st.write("Notice that $\\frac{F_{n-1}}{F_n}$ is just the reciprocal ($1/L$). So:")
                    st.latex(r"L = 1 + \frac{1}{L}")

                    st.markdown("**Step 4: Solve the Quadratic**")
                    st.write("Multiply by $L$: $L^2 = L + 1 \implies L^2 - L - 1 = 0$.")
                    st.write("Using Quadratic Formula:")
                    st.latex(r"L = \frac{-(-1) \pm \sqrt{(-1)^2 - 4(1)(-1)}}{2(1)} = \frac{1 \pm \sqrt{5}}{2}")
                    st.success(r"Taking the positive root: $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.61803$")

                    # 🔥 视频链接 (绝对保留)
                    st.info("📺 **Video Resources:**")
                    st.markdown("[▶️ Numberphile: The Golden Ratio](https://www.youtube.com/watch?v=ghxQA3vvhsk)")
                    st.markdown(
                        "[▶️ TED-Ed: The magic of Fibonacci numbers](https://www.youtube.com/watch?v=SjSHVDfXHQ4)")

                with c2:
                    # 绘图：比值震荡收敛
                    st.write("**Visualizing Ratio Convergence:**")
                    fibs = [1, 1]
                    for i in range(15): fibs.append(fibs[-1] + fibs[-2])
                    ratios = [fibs[i] / fibs[i - 1] for i in range(1, len(fibs))]

                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=list(range(1, len(ratios) + 1)), y=ratios, mode='lines+markers',
                                             name='Ratio Fn/Fn-1', line=dict(color='#FDB827', width=3)))
                    fig.add_shape(type="line", x0=1, y0=1.618, x1=15, y1=1.618, line=dict(dash='dash', color='white'))
                    fig.add_annotation(x=8, y=1.618, text="φ (1.618)", ay=-30)

                    fig.update_layout(title="Oscillation Damping", xaxis_title="n", yaxis_title="Ratio",
                                      template="plotly_dark", height=500)
                    st.plotly_chart(fig, use_container_width=True)

# --- TAB 4: 杨辉三角 (保持之前修复好的版本) ---

    # -----------------------------------------------------------
    # TAB 4: The Architecture of Chance (Fixed Layout)
    # -----------------------------------------------------------
    with tab4:
        st.header("🧱 The Binomial Engine: Logic & Derivation")

        # ==================================================
        # PART 1: TOP SECTION (Split Layout)
        # Left: Basic Setup & Logic | Right: Visuals
        # ==================================================
        col_top_left, col_top_right = st.columns([1.3, 2.0])

        # --- LEFT: CONTROLS & LOGIC ---
        with col_top_left:
            st.subheader("1. The Logic of $(a+b)^n$")

            n_rows = st.slider("Power (n)", 0, 12, 5, key='n_slider_final_fix')
            p_val = st.slider("Probability (p)", 0.0, 1.0, 0.5, 0.05, key='p_slider_final_fix')

            # [保留] Deep Dive 解释
            with st.expander("📖 DEEP DIVE: Where does the formula come from?", expanded=True):
                st.markdown("""
                **Don't just memorize the formula. Visualize the brackets.**

                Imagine calculating $(a+b)^3$:
                $$(a+b)(a+b)(a+b)$$

                To get $a^2b$, you need to choose **'b'** from exactly **1** bracket, and **'a'** from the other **2**.

                **The Question is:** How many ways can we choose 1 'b' from 3 brackets?
                **The Answer is:** Combinations! $\\binom{3}{1} = 3$.
                """)

        # --- RIGHT: VISUALIZATIONS ---
        with col_top_right:
            st.subheader("The Visual Architecture")

            # 1. Triangle Plot
            fig_tri = go.Figure()
            for r in range(n_rows + 1):
                row_coeffs = [math.comb(r, k) for k in range(r + 1)]
                xs = np.linspace(-r / 2, r / 2, r + 1)
                ys = [-r] * (r + 1)

                # 样式
                if r < n_rows:
                    base_color = 'rgba(0, 173, 181, 0.3)'
                    text_col = 'rgba(0, 0, 0, 0.3)'
                    size = 20
                else:
                    base_color = '#FDB827'
                    text_col = 'white'
                    size = 35

                fig_tri.add_trace(go.Scatter(
                    x=xs, y=ys, mode='markers+text',
                    text=[str(c) for c in row_coeffs],
                    textfont=dict(color=text_col, size=12 if r < n_rows else 16, family="Arial Black"),
                    marker=dict(size=size, color=base_color, symbol='hexagon', line=dict(width=1, color='white')),
                    showlegend=False, hoverinfo='text',
                    hovertext=[f"Row {r}, Term {k + 1}<br>Value: {c}" for k, c in enumerate(row_coeffs)]
                ))

            fig_tri.update_layout(height=400, xaxis=dict(visible=False), yaxis=dict(visible=False),
                                  plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=10, b=0),
                                  title=f"Pascal's Triangle (Row 0 to {n_rows})")
            st.plotly_chart(fig_tri, use_container_width=True)

            # 2. Hidden Patterns
            c1, c2 = st.columns(2)
            c1.metric(label=f"Sum of Row {n_rows}", value=f"{2 ** n_rows}", help="(1+1)^n")
            c2.metric(label="Shallow Diagonals", value="Fibonacci", help="1, 1, 2, 3, 5...")

            # 3. Normal Curve (保留!)
            st.markdown("---")
            st.caption("Visualizing the Limit (Normal Curve)")
            x_k = np.arange(0, n_rows + 1)
            probs = stats.binom.pmf(x_k, n_rows, p_val)
            fig_dist = go.Figure()
            fig_dist.add_trace(go.Bar(x=x_k, y=probs, name='Binomial', marker_color='#FDB827'))
            mu = n_rows * p_val
            sigma = math.sqrt(n_rows * p_val * (1 - p_val))
            if sigma > 0:
                x_smooth = np.linspace(0, n_rows, 200)
                y_smooth = stats.norm.pdf(x_smooth, mu, sigma)
                fig_dist.add_trace(go.Scatter(x=x_smooth, y=y_smooth, mode='lines', name='Normal',
                                              line=dict(color='#00ADB5', width=3)))
            fig_dist.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0))
            st.plotly_chart(fig_dist, use_container_width=True)

        st.divider()

        # ==================================================
        # PART 2: TERM FINDER (Full Width / Expanded)
        # ==================================================
        st.subheader("2. Term Finder & General Term")

        # 使用较宽的布局
        tf_col1, tf_col2 = st.columns([1, 2])

        with tf_col1:
            k_term = st.number_input(f"Find the k-th term (1 to {n_rows + 1})", min_value=1, max_value=n_rows + 1,
                                     value=1, key='k_term_final')
            r_idx = k_term - 1
            coeff = math.comb(n_rows, r_idx)

        with tf_col2:
            # [保留] 详细解释
            st.markdown(f"**Target:** The **{k_term}-th** term (so $r={r_idx}$).")
            st.latex(rf"T_{{r+1}} = \binom{{n}}{{r}} a^{{n-r}} b^r")
            st.caption("We use $r+1$ because we start counting from $r=0$ (the 1st term).")
            st.latex(rf"\binom{{{n_rows}}}{{{r_idx}}} = \frac{{{n_rows}!}}{{{r_idx}!({n_rows}-{r_idx})!}} = {coeff}")

        st.divider()
        # ==================================================
        # ==================================================
        # PART 3: NEWTON'S INFINITE EXPANSION (Fixed Layout & Logic)
        # ==================================================
        st.subheader("3. Newton's Infinite Series (The Logic)")

        # --- Step 1: 牛顿的发现 (The Discovery) ---
        # 直接全宽显示，防止重叠，并解释来源
        st.markdown("#### Step 1: Newton's Generalization")
        st.write(
            "Newton discovered that the Combinations formula $\\binom{n}{r}$ works for **any number** (fractions/negatives) if written in this specific form:")

        # 展示核心公式：组合数是如何计算的
        st.latex(r"\binom{n}{r} = \frac{n(n-1)(n-2)\dots(n-r+1)}{r!}")

        st.caption("""
            * **Term 0 ($r=0$):** Value is **1**.
            * **Term 1 ($r=1$):** Value is $\\frac{n}{1!} = n$.
            * **Term 2 ($r=2$):** Value is $\\frac{n(n-1)}{2!}$.
            """)

        st.divider()

        # --- Step 2: 套用到 (1+ax) (The Expansion) ---
        st.markdown("#### Step 2: Expanding $(1+ax)^n$")
        st.write(
            "Now, we substitute these coefficients into the Binomial structure. We replace $x$ with the term **$(ax)$**:")

        # 【关键修复】把长公式拿出来独占一行，解决重叠问题
        st.latex(r"""
            (1+ax)^n = \underbrace{1}_{\binom{n}{0}} + \underbrace{n}_{\binom{n}{1}}(ax) + \underbrace{\frac{n(n-1)}{2!}}_{\binom{n}{2}}(ax)^2 + \underbrace{\frac{n(n-1)(n-2)}{3!}}_{\binom{n}{3}}(ax)^3 + \dots
            """)

        st.info(
            "Notice how the factorials ($2!, 3!$) and the falling powers ($n(n-1)$) match the General Combinations formula above.")

        st.divider()

        # --- Step 3: 收敛性 (Convergence) ---
        # 这里内容短，可以用分栏
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
    # --- TAB 5: Taylor Series (通项 + 详细展开) ---
    with tab5:
        st.subheader("Taylor Series: From Formula to Polynomial")

        # --- 🆕 新增：泰勒级数的起源与作用 ---
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
        # ------------------------------------

        col_ctrl, col_plot = st.columns([1.2, 2.5])

        with col_ctrl:
            func_type = st.radio("Function:", ["Sin(x)", "Cos(x)", "e^x"])
            n_terms = st.slider("Precision (Terms)", 1, 8, 3)
            # 注意：这里n_terms设小一点，因为要显示详细展开，太长会换行难看

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
            else:  # e^x
                st.latex(r"\sum_{n=0}^{\infty} \frac{x^n}{n!}")
                terms_idx = range(n_terms)
                powers = [i for i in terms_idx]
                facts = [math.factorial(p) for p in powers]
                signs = [1 for i in terms_idx]

            st.write("### 2. Step-by-Step Expansion")
            st.caption("Substitute n=0, n=1, n=2...")

            # 动态生成“中间步骤” LaTeX
            # 格式: (x^1)/1! - (x^3)/3! ...
            raw_terms = []
            for i in range(n_terms):
                p = powers[i]
                s = signs[i]
                sign_str = "+" if s > 0 else "-"
                # 第一项不显示 + 号
                if i == 0: sign_str = "" if s > 0 else "-"

                raw_terms.append(rf"{sign_str} \frac{{x^{{{p}}}}}{{{p}!}}")

            raw_latex = " ".join(raw_terms) + " \dots"
            st.latex(raw_latex)

            st.write("### 3. Final Polynomial")
            # 动态生成“最终结果” LaTeX
            # 格式: x - 0.166x^3 ...
            final_terms = []
            for i in range(n_terms):
                p = powers[i]
                s = signs[i]
                coef = 1 / math.factorial(p)

                sign_char = "+" if s > 0 else "-"
                if i == 0 and s > 0: sign_char = ""

                # 分数形式优化显示
                if coef == 1:
                    val_str = ""
                else:
                    val_str = rf"\frac{{1}}{{{math.factorial(p)}}}"

                final_terms.append(rf"{sign_char} {val_str} x^{{{p}}}")

            final_latex = " ".join(final_terms) + " \dots"
            st.latex(final_latex)

        with col_plot:
            # 绘图部分
            fig_taylor = go.Figure()
            x_vals = np.linspace(-10, 10, 400)

            # True Function
            if func_type == "Sin(x)":
                y_true = np.sin(x_vals)
            elif func_type == "Cos(x)":
                y_true = np.cos(x_vals)
            else:
                y_true = np.exp(x_vals)

            fig_taylor.add_trace(go.Scatter(x=x_vals, y=y_true, mode='lines', line=dict(color='gray', dash='dash'),
                                            name='True Function'))

            # Calc Approx
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

        # --- 欧拉公式证明 (详细展开版) ---
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
# THE GRAND TALE: THE MAGNUM OPUS EDITION (绝对详尽版)
# ==========================================
def render_calculus_grand_story():
    st.title("📜 The Calculus Saga: The 2000-Year War on Infinity")
    st.markdown("### *From the Mind of God to the Measure of Man.*")

    # --- 0. 序章：神学与动机 (The Theological Spark) ---
    with st.expander("✨ Prologue: The Mind of God (17th Century Context)", expanded=True):
        c1, c2 = st.columns([2, 1])
        with c1:
            st.write("""
            **Why was Calculus invented? Calculus wasn't just born for calculation; it was born from a pursuit of the Divine Order.**

            In the 17th Century, science was not separate from religion. The "Heavens" (Stars) were literally believed to be the realm of God. 
            Scientists believed the universe was a machine designed by a perfect Creator. To discover the mathematical laws of the universe was to **read the mind of God**.
            """)
            st.markdown(
                "> *\"Nature and nature's laws lay hid in night; God said **'Let Newton be'** and all was light.\"* — Alexander Pope")

            st.write("""
            **The Great Conflict:**
            * **The Church (Ptolemy):** Earth is the center. Humans are special.
            * **The Rebels (Copernicus/Kepler):** The Sun is the center. The math is elegant.

            To prove the Sun was the center, they needed to predict planetary motion with **perfect accuracy**. Old geometry failed. They needed a new math.
            """)
        with c2:
            st.image("kepler.jpg",
                     caption="Kepler: 'I am thinking God's thoughts after Him.'")

    st.divider()

    # --- 1. 核心直觉 (The Intuition) ---
    st.markdown("### 1. The Artifact: The Trinity of Change")
    st.info(
        "Before we walk through history, hold the core concept in your hand. Calculus unites three things that seem separate.")

    # 交互滑块
    t_val = st.slider("Time / Position (t)", 0.0, 4.0, 2.0)
    x = np.linspace(0, 4.5, 200)
    y = x ** 2 / 4
    slope = t_val / 2
    area_val = (t_val ** 3) / 12

    fig = go.Figure()
    # 积分
    x_area = np.linspace(0, t_val, 100)
    y_area = x_area ** 2 / 4
    fig.add_trace(go.Scatter(x=x_area, y=y_area, fill='tozeroy', mode='none', name=f'Accumulation (Area/Integral)',
                             fillcolor='rgba(0, 173, 181, 0.3)'))
    # 路径
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Path (Function)', line=dict(color='yellow', width=3)))
    # 微分
    x_tan = np.linspace(max(0, t_val - 1), min(4.5, t_val + 1), 20)
    y_tan = slope * (x_tan - t_val) + (t_val ** 2 / 4)
    fig.add_trace(go.Scatter(x=x_tan, y=y_tan, mode='lines', name=f'Velocity (Slope/Derivative)',
                             line=dict(color='#FF2E63', width=4)))
    # 点
    fig.add_trace(go.Scatter(x=[t_val], y=[t_val ** 2 / 4], mode='markers', marker=dict(size=15, color='#FDB827')))
    fig.update_layout(template="plotly_dark", height=350, margin=dict(t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- 历史长卷：七大篇章 (完全对应文章结构) ---
    st.markdown("### 🎬 The Chronicles")

    tabs = st.tabs([
        "I. The Ancient Fog",
        "II. The Four Needs",
        "III. The Giants",
        "IV. The Birth",
        "V. The Crisis",
        "VI. The Rigor",
        "VII. Modern Horizons"
    ])

    # ==========================================
    # ERA I: 古希腊 (芝诺与阿基米德)
    # ==========================================
    # ==========================================
    # ERA I: 古希腊 (芝诺与阿基米德) [深度重制版]
    # ==========================================
    with tabs[0]:
        st.subheader("🏛️ Era I: The Fear of Infinity (450 BC - 250 BC)")
        st.markdown("""
            **The Context:**
            The Ancient Greeks loved geometry because it was static and perfect. But **Motion** and **Infinity** terrified them.

            **Why did Zeno create these paradoxes?**
            Zeno wasn't trying to say "movement doesn't exist" (he could walk to prove that). 
            He was a student of **Parmenides**, who believed **"All is One"** and change is an illusion. 
            Zeno created these 4 paradoxes to prove that if you assume space/time are divisible (many), logic breaks down.
            """)

        st.divider()

        # --- 芝诺的四大悖论 (使用子标签页详细展示) ---
        st.markdown("### 🐢 Zeno's Four Paradoxes")
        z_tab1, z_tab2, z_tab3, z_tab4 = st.tabs([
            "1. The Dichotomy (Space)",
            "2. Achilles (Motion)",
            "3. The Arrow (Time)",
            "4. The Stadium (Relativity)"
        ])

        # 1. 二分法悖论
        with z_tab1:
            col_d1, col_d2 = st.columns([1.5, 1])
            with col_d1:
                st.markdown("**The Paradox of Infinite Divisibility**")
                st.write("""
                    **The Argument:**
                    To reach the wall, you must first walk halfway ($1/2$).
                    To walk the remaining half, you must walk half of that ($1/4$).
                    Then $1/8$, then $1/16$...

                    **The Trap:**
                    You have to complete an **Infinite** number of tasks in a **Finite** amount of time. 
                    Zeno argued this is logically impossible. Therefore, you can never even start moving.
                    """)
                st.latex(r"Distance = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots = 1")

            with col_d2:
                # 可视化：无穷级数逼近
                steps = st.slider("Steps taken", 1, 10, 4)
                d_vals = [1 / (2 ** i) for i in range(1, steps + 1)]
                cum_sum = np.cumsum(d_vals)

                fig_d = go.Figure()
                fig_d.add_trace(go.Bar(x=list(range(1, steps + 1)), y=d_vals, name="Step Size"))
                fig_d.add_trace(
                    go.Scatter(x=list(range(1, steps + 1)), y=cum_sum, name="Total Distance", line=dict(color='red')))
                fig_d.update_layout(height=250, title="Approaching 1", margin=dict(t=30, b=10), showlegend=False)
                st.plotly_chart(fig_d, use_container_width=True)

        # 2. 阿基里斯追乌龟
        with z_tab2:
            col_a1, col_a2 = st.columns([1.5, 1])
            with col_a1:
                st.markdown("**The Paradox of the Race**")
                st.write("""
                    **The Argument:**
                    Achilles (fastest runner) races a Tortoise (slowest). Tortoise gets a head start (e.g., 100m).

                    1. By the time Achilles reaches the 100m mark, the Tortoise has moved a little (say, 10m).
                    2. By the time Achilles runs that 10m, the Tortoise moves a bit more (1m).
                    3. By the time Achilles runs that 1m, the Tortoise moves 0.1m...

                    **The Trap:**
                    Whenever Achilles reaches where the Tortoise *was*, the Tortoise has moved further.
                    Achilles gets infinitely close, but logically **never passes** it.
                    """)
            with col_a2:
                # 可视化：追及问题
                t = np.linspace(0, 15, 100)
                y_achilles = 10 * t
                y_tortoise = 50 + 2 * t  # 50m head start, slow speed

                fig_race = go.Figure()
                fig_race.add_trace(go.Scatter(x=t, y=y_achilles, name="Achilles"))
                fig_race.add_trace(go.Scatter(x=t, y=y_tortoise, name="Tortoise"))
                fig_race.update_layout(title="When do they intersect?", xaxis_title="Time", yaxis_title="Distance",
                                       height=250, margin=dict(t=30, b=10))
                st.plotly_chart(fig_race, use_container_width=True)
                st.caption("Calculus solves this by finding the intersection point of two functions.")

        # 3. 飞矢不动
        with z_tab3:
            col_ar1, col_ar2 = st.columns([1.5, 1])
            with col_ar1:
                st.markdown("**The Paradox of the Instant**")
                st.write("""
                    **The Argument:**
                    Consider an arrow flying through the air.
                    1. Look at any single **Instant** (snapshot of time, $t=0$).
                    2. At that exact instant, the arrow is not moving (it occupies a space equal to itself).
                    3. Time is made of instants.
                    4. If it's motionless at *every* instant, it is motionless for the *whole* time.

                    **The Trap:**
                    This challenged the concept of **Velocity**. How can you move if you are frozen in every frame?
                    """)
            with col_ar2:
                # 可视化：时间切片
                fig_arrow = go.Figure()
                fig_arrow.add_trace(go.Scatter(x=[2], y=[1], mode='markers+text',
                                               marker=dict(size=20, symbol="arrow-right", color="red"),
                                               text=["Frozen?"], textposition="top center"))
                fig_arrow.update_xaxes(range=[0, 4], title="Position")
                fig_arrow.update_yaxes(showticklabels=False)
                fig_arrow.update_layout(title="Snapshot at t=2.0s", height=250, margin=dict(t=30, b=10))
                st.plotly_chart(fig_arrow, use_container_width=True)
                st.caption("Calculus definition: $v = dx/dt$. It's a ratio of limits, not a state at a point.")

        # 4. 游行队伍 (游标悖论)
        with z_tab4:
            st.markdown("**The Paradox of Relativity & Discrete Time**")
            st.write("""
                **The Argument:**
                Imagine three rows of soldiers:
                * Row A: Standing still.
                * Row B: Moving Right (Speed 1).
                * Row C: Moving Left (Speed 1).

                Relative to A, B moves 1 unit.
                Relative to C, B moves **2 units**.

                **The Trap:**
                Zeno argued: If time has a "smallest unit" (an atom of time), then B passed two units of C in one unit of time. 
                This implies "Half the time is equal to Double the time".
                It proves that **Motion is Relative** and challenges the idea of "Absolute Time".
                """)

        st.info("""
            **What happened next?**
            These paradoxes froze Greek math. They decided to banish "Infinity" to avoid these logical traps.
            It wasn't until **Newton (Calculus)** and **Cauchy (Limits)** that we could mathematically solve Zeno.
            * We proved: Infinite sums can equal a finite number (Convergent Series).
            * We proved: Instantaneous velocity is a limit, not a static state.
            """)

        st.divider()

        # --- 阿基米德部分 ---
        st.markdown("### 📐 Archimedes: The First 'Hacker'")

        c_arch1, c_arch2 = st.columns([1.5, 1])
        with c_arch1:
            st.write("""
                **Archimedes (287 BC)** didn't solve Zeno's philosophy. He just found a way to work around it.

                **The Method of Exhaustion:**
                He wanted to find the area of a circle (to calculate Pi). He didn't have integration.
                So he sandwiched the circle between two polygons:
                1. An **Inner Polygon** (Area < Circle).
                2. An **Outer Polygon** (Area > Circle).

                He doubled the sides: 6, 12, 24, 48, 96...

                **The Logic:**
                He proved that the difference between the polygon and the circle could be made **"smaller than any given magnitude"**. 
                He didn't use the word "Limit", but he used the logic of limits.
                """)
            st.success(
                "**Impact:** This was the direct ancestor of **Integration**. 2000 years later, Newton would use this same idea but with algebra instead of geometry.")

        with c_arch2:
            # 阿基米德可视化 (保留并优化)
            n = st.slider("Polygon Sides (Approximation)", 3, 96, 6)
            th = np.linspace(0, 2 * np.pi, n + 1)

            fig_arch = go.Figure()
            # 圆
            fig_arch.add_trace(
                go.Scatter(x=np.cos(np.linspace(0, 2 * np.pi, 100)), y=np.sin(np.linspace(0, 2 * np.pi, 100)),
                           line=dict(color='white'), name="True Circle"))
            # 内接多边形
            fig_arch.add_trace(
                go.Scatter(x=np.cos(th), y=np.sin(th), fill="toself", name="Inner Polygon", line=dict(color='#00ADB5')))

            fig_arch.update_layout(height=280, margin=dict(t=20, b=20), title=f"Approximating Pi with {n} sides",
                                   template="plotly_dark", showlegend=False)
            st.plotly_chart(fig_arch, use_container_width=True)

        # ==========================================
        # ERA II: 四大需求 (深度交互版)
        # ==========================================
        with tabs[1]:
            st.subheader("🔥 Era II: The Four Impossible Problems (1600s)")
            st.write("""
            By the 17th Century, the Scientific Revolution was stalling. 
            Old mathematics (Geometry & Algebra) hit a wall against four specific problems from the real world.
            """)

            # 使用子标签页详细展开
            p_tab1, p_tab2, p_tab3, p_tab4 = st.tabs([
                "1. Velocity (Motion)",
                "2. Tangents (Optics)",
                "3. Maxima (Warfare)",
                "4. Area (Cosmos)"
            ])

            # --- 问题 1: 瞬时速度 (The Velocity Problem) ---
            with p_tab1:
                c1, c2 = st.columns([1.5, 1])
                with c1:
                    st.markdown("#### 🚀 The Motion Crisis")
                    st.info("**Challenge:** How to find speed at a specific *instant*?")
                    st.write("""
                    Galileo proved that falling objects accelerate ($d = t^2$). 
                    * **Average Speed** is easy: $Distance / Time$.
                    * **Instantaneous Speed** is impossible for old math.

                    **The Trap:**
                    To find the speed at exactly $t=1$, you need to measure distance in **0 seconds**.
                    $$ v = \\frac{\Delta d}{\Delta t} = \\frac{0}{0} $$
                    **Result:** Meaningless. This required the invention of the **Limit**.
                    """)
                with c2:
                    # 可视化：割线逼近切线 (Secant approaching Tangent)
                    st.caption("Visualizing the 'Crash' of 0/0")
                    delta_t = st.slider("Time Interval (Δt)", 0.01, 2.0, 1.0, key="vel_dt")
                    t_fixed = 1.0

                    # 绘制曲线 d = t^2
                    t_plot = np.linspace(0, 3, 100)
                    d_plot = t_plot ** 2

                    # 绘制割线
                    t2 = t_fixed + delta_t
                    d1, d2 = t_fixed ** 2, t2 ** 2
                    slope = (d2 - d1) / (t2 - t_fixed)

                    fig_vel = go.Figure()
                    fig_vel.add_trace(go.Scatter(x=t_plot, y=d_plot, name="Distance Curve"))
                    # 割线
                    x_sec = [t_fixed, t2]
                    y_sec = [d1, d2]
                    fig_vel.add_trace(
                        go.Scatter(x=x_sec, y=y_sec, mode="lines+markers", name=f"Avg Speed: {slope:.2f}"))

                    fig_vel.update_layout(height=250, margin=dict(t=20, b=20), title="Shrinking Δt -> Instant Speed")
                    st.plotly_chart(fig_vel, use_container_width=True)

            # --- 问题 2: 切线问题 (The Tangent Problem) ---
            with p_tab2:
                c1, c2 = st.columns([1.5, 1])
                with c1:
                    st.markdown("#### 🔭 The Optics Crisis")
                    st.info("**Challenge:** Find the angle of a curve at any single point.")
                    st.write("""
                    **Why it mattered:**
                    The 17th century was the age of the **Telescope** (Galileo, Kepler). 
                    To build powerful telescopes, you need to grind lenses into perfect curves.

                    **The Physics:**
                    Light refracts based on the angle it hits the glass. To calculate this angle, you need the **Normal Line** (perpendicular to the Tangent).
                    Euclid only knew tangents for circles, not complex lens shapes.
                    """)
                with c2:
                    # 简单示意图：透镜与光线
                    x_lens = np.linspace(-2, 2, 100)
                    y_lens = -0.2 * x_lens ** 2  # 简单的透镜形状

                    fig_tan = go.Figure()
                    fig_tan.add_trace(go.Scatter(x=x_lens, y=y_lens, name="Lens Surface", fill='tozeroy'))
                    # 光线
                    fig_tan.add_trace(
                        go.Scatter(x=[-1, 1], y=[2, 2], mode="lines", line=dict(dash='dash'), name="Incoming Light"))
                    fig_tan.add_trace(
                        go.Scatter(x=[-1, 0, 1], y=[2, -0.8, 2], mode="lines", name="Refraction Needs Angles"))

                    fig_tan.update_layout(height=250, margin=dict(t=30, b=20), showlegend=False,
                                          title="Refraction Geometry")
                    st.plotly_chart(fig_tan, use_container_width=True)

            # --- 问题 3: 极值问题 (The Maxima Problem) ---
            with p_tab3:
                c1, c2 = st.columns([1.5, 1])
                with c1:
                    st.markdown("#### 💣 The Warfare Crisis")
                    st.info("**Challenge:** When does a variable stop increasing and start decreasing?")
                    st.write("""
                    **Why it mattered:**
                    Cannons were the ultimate weapon. Generals asked: 
                    *At what angle should we fire to hit the **Maximum** distance?*

                    **The Math Insight:**
                    Fermat realized that at the peak of a trajectory, the object is momentarily **flat**.
                    This means the **Slope = 0**. This was the birth of Optimization.
                    """)

            # --- 问题 4: 面积问题 (The Area Problem) ---
            with p_tab4:
                c1, c2 = st.columns([1.5, 1])
                with c1:
                    st.markdown("#### 🪐 The Cosmology Crisis")
                    st.info("**Challenge:** Calculate the area inside a curve that isn't a circle.")
                    st.write("""
                    **Why it mattered:**
                    **Kepler's Second Law**: *Planets sweep out equal areas in equal times.*
                    But planetary orbits are **Ellipses** (irregular curves).

                    **The Failure:**
                    Ancient geometry had formulas for Squares ($l^2$) and Circles ($\pi r^2$). 
                    They had **NO** formula for an elliptical slice.
                    Kepler had to approximate it by summing infinite thin lines. This demanded **Integration**.
                    """)
                with c2:
                    # 克卜勒第二定律示意图
                    t = np.linspace(0, 2 * np.pi, 100)
                    x_el = 2 * np.cos(t)
                    y_el = 1.5 * np.sin(t)

                    fig_kep = go.Figure()
                    fig_kep.add_trace(go.Scatter(x=x_el, y=y_el, name="Orbit"))
                    # 扫过的面积 (简单的扇形示意)
                    fig_kep.add_trace(go.Scatter(x=[0, 2, 1.8, 0], y=[0, 0, 0.6, 0], fill="toself", name="Swept Area"))

                    fig_kep.update_layout(height=250, margin=dict(t=20, b=20), showlegend=False,
                                          title="Kepler's Area Law")
                    st.plotly_chart(fig_kep, use_container_width=True)
        # ==========================================
        # ERA III: 巨人的肩膀 (终极人物志版)
        # ==========================================
        with tabs[2]:
            st.subheader("🔦 Era III: The Shoulders of Giants (Pre-1660s)")
            st.write("""
            Before Newton and Leibniz, the "Calculus Puzzle" was 90% solved. 
            Meet the titans who built the foundation across Europe.
            """)

            # 按国家/学派分类
            giant_t1, giant_t2, giant_t3, giant_t4 = st.tabs([
                "🇮🇹 The Italian School",
                "🇫🇷 The French School",
                "🇩🇪 The German School",
                "🇬🇧 The British School"
            ])

            # --- 1. 意大利学派 (卡瓦列里) ---
            with giant_t1:
                st.markdown("#### Bonaventura Cavalieri (The Indivisibles)")
                c1, c2 = st.columns([1, 3])
                with c1:
                    st.image("cavalieri.jpg",
                             caption="Cavalieri (1598-1647)", use_container_width=True)
                with c2:
                    st.info("**Contribution: The Theory of Indivisibles**")
                    st.write(
                        "He viewed a volume as a stack of **infinite pages** (planes). This was the precursor to Integration.")
                    st.write(
                        "**Cavalieri's Principle:** If two solids have equal cross-sectional areas at every height, they must have equal volume.")
                    st.write(
                        "**Guldin's Theorem:** He proved that the volume of a solid of revolution = Area $\\times$ Distance traveled by the Centroid.")

                # 可视化：卡瓦列里原理
                st.caption("Visualization: Shearing a shape doesn't change its Area (Cavalieri's Principle)")
                fig_cav = go.Figure()
                # 原始正方形
                fig_cav.add_trace(go.Scatter(x=[0, 1, 1, 0, 0], y=[0, 0, 1, 1, 0], fill="toself", name="Static Square",
                                             line=dict(color="cyan")))
                # 剪切后的平行四边形
                fig_cav.add_trace(go.Scatter(x=[2, 3, 4, 3, 2], y=[0, 0, 1, 1, 0], fill="toself", name="Sheared Shape",
                                             line=dict(color="magenta")))
                fig_cav.update_layout(height=200, margin=dict(t=10, b=10), showlegend=False)
                st.plotly_chart(fig_cav, use_container_width=True)

            # --- 2. 法国学派 (分析三杰) ---
                # --- 2. 法国学派 (法兰西三杰：哲学家、业余大神与角斗士) ---
                with giant_t2:
                    st.markdown("#### 🇫🇷 The French Analytic Revolution")
                    st.caption("They merged Algebra and Geometry, creating the language of Calculus.")

                    # --- 笛卡尔 (睡懒觉的哲学家) ---
                    c_d1, c_d2 = st.columns([1, 3])
                    with c_d1:
                        st.image(
                            "https://upload.wikimedia.org/wikipedia/commons/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg",
                            caption="Descartes (1596-1650)", use_container_width=True)
                    with c_d2:
                        st.markdown("**René Descartes (The Dreamer)**")
                        st.write(
                            "He invented the **Coordinate System** ($x, y$). Before him, Geometry was shapes; after him, it was Algebra.")

                        # 趣闻：苍蝇与早起
                        with st.expander("The Fly & The Queen"):
                            st.write("""
                                * **The Fly on the Ceiling:** Legend has it he invented the coordinate system while lying in bed (his favorite hobby), watching a fly crawl on the ceiling and realizing he could describe its position with two numbers.
                                * **Death by Alarm Clock:** He loved sleeping until noon. Tragically, Queen Christina of Sweden hired him as a tutor but demanded lessons at **5:00 AM**. The cold early mornings caused him to catch pneumonia and die.
                                """)
                        st.info("*\"I think, therefore I am.\"* (He was a philosopher first, mathematician second!)")

                    st.divider()

                    # --- 费马 (喜欢恶作剧的律师) ---
                    c_f1, c_f2 = st.columns([1, 3])
                    with c_f1:
                        st.image("fermat.jpg",
                                 caption="Fermat (1601-1665)", use_container_width=True)
                    with c_f2:
                        st.markdown("**Pierre de Fermat (The Amateur Genius)**")
                        st.write(
                            "By day, a lawyer. By night, the 'Prince of Amateurs'. He found Maxima/Tangents using **Adequality**.")

                        # 趣闻
                        with st.expander("😈 The Troll of Mathematics"):
                            st.write("""
                                                * **The Margins:** He famously wrote a theorem in a book margin and added: *"I have a truly marvelous proof of this, which this margin is too narrow to contain."* It took humanity **358 years** to solve it (Fermat's Last Theorem).
                                                * **Feud with Descartes:** Fermat loved to challenge other mathematicians with impossible problems. He and Descartes hated each other. Descartes called Fermat's tangent method "rubbish" (it turned out to be correct).
                                                """)
                        # --- 硬核算式升级版 ---
                        with st.popover("📝 Deep Dive: Watch Fermat break the laws of logic"):
                            st.write("Let's find the slope (derivative) of $y = x^2$.")

                            st.markdown("**Step 1: The Shift (Adequality)**")
                            st.write("Compare $f(x)$ with a tiny shifted point $f(x+E)$.")
                            st.latex(r"(x+E)^2 \approx x^2")

                            st.markdown("**Step 2: Expand & Cancel**")
                            st.latex(r"x^2 + 2xE + E^2 \approx x^2")
                            st.write("Subtract $x^2$ from both sides:")
                            st.latex(r"2xE + E^2 \approx 0")

                            st.markdown("**Step 3: The 'Crime' (Divide by E)**")
                            st.warning("To divide by $E$, we must assume $E \\neq 0$.")
                            st.latex(r"\frac{2xE + E^2}{E} \implies 2x + E \approx 0")

                            st.markdown("**Step 4: The 'Magic' (Set E to 0)**")
                            st.warning("Now, we assume $E = 0$ to get rid of it.")
                            st.latex(r"2x + 0 = 2x")

                            st.success("Result: The slope is $2x$. (It's correct, but the logic contradicts itself!)")
                    st.divider()

                    # --- 罗伯瓦 (必须保密的角斗士) ---
                    c_r1, c_r2 = st.columns([1, 3])
                    with c_r1:
                        st.image("roberval.jpg",
                                 caption="Roberval (1602-1675)", use_container_width=True)
                    with c_r2:
                        st.markdown("**Gilles de Roberval (The Secretive Fighter)**")
                        st.write(
                            "He viewed curves as **Motion** (Kinematics) and found tangents using Velocity Vectors.")

                        # 趣闻：数学角斗士
                        with st.expander("⚔️ Why did he keep his math secret?"):
                            st.write("""
                                * **The Math Gladiator:** Roberval held the Chair of Math at the Collège Royal. The rule was: **Every 3 years, anyone could challenge him.** If he lost a math contest, he lost his job.
                                * **Secret Weapon:** Because of this, he **never published** his calculus methods! He kept them as "secret weapons" to defeat challengers during exams. This is why he is less famous than Newton today.
                                """)
            # --- 3. 德国学派 (开普勒) ---
            with giant_t3:
                st.markdown("#### Johannes Kepler (The Summation)")
                c_k1, c_k2 = st.columns([1, 3])
                with c_k1:
                    st.image("kepler.jpg",
                             caption="Kepler (1571-1630)", use_container_width=True)
                with c_k2:
                    st.info("**Contribution: Integration before Calculus**")
                    st.write(
                        "**The Wine Barrels:** To find the volume of barrels for his wedding, he treated them as sums of **infinite thin discs**.")
                    st.write(
                        "**Planetary Laws:** His 3 Laws of Motion provided the physics data that Newton later used to prove Calculus worked.")

                    # --- 3D 可视化升级：旋转体生成 ---
                    st.divider()
                    st.caption("🎨 Interactive Demo: Drag slider to create a Solid of Revolution (Guldin's Theorem)")

                    # 1. 交互滑块：控制旋转角度
                    sweep_angle = st.slider("Rotation Angle (Sweep)", 0, 360, 240, key="rev_slider")

                    # 2. 数学计算：生成环面 (Torus) 数据
                    # R = 旋转半径 (距离轴的距离), r = 圆本身的半径
                    R, r = 3, 1
                    theta = np.linspace(0, 2 * np.pi, 50)  # 圆的切片
                    phi = np.linspace(0, np.radians(sweep_angle), 60)  # 旋转的角度范围

                    # 生成网格
                    THETA, PHI = np.meshgrid(theta, phi)

                    # 环面参数方程
                    X = (R + r * np.cos(THETA)) * np.cos(PHI)
                    Y = (R + r * np.cos(THETA)) * np.sin(PHI)
                    Z = r * np.sin(THETA)

                    # 3. 绘图
                    fig_rev = go.Figure()

                    # A. 绘制生成的 3D 曲面
                    fig_rev.add_trace(go.Surface(
                        x=X, y=Y, z=Z,
                        colorscale='Viridis',  # 酷炫的渐变色
                        opacity=0.9,
                        showscale=False,
                        name="Solid Volume"
                    ))

                    # B. 绘制旋转轴 (Z轴)
                    fig_rev.add_trace(go.Scatter3d(
                        x=[0, 0], y=[0, 0], z=[-2, 2],
                        mode='lines',
                        line=dict(color='white', width=5, dash='dash'),
                        name="Axis of Rotation"
                    ))

                    # C. 绘制初始截面 (为了让人看清是由一个圆转出来的)
                    # 在 phi=0 处的圆
                    circle_x = (R + r * np.cos(theta))
                    circle_y = np.zeros_like(theta)
                    circle_z = r * np.sin(theta)
                    fig_rev.add_trace(go.Scatter3d(
                        x=circle_x, y=circle_y, z=circle_z,
                        mode='lines',
                        line=dict(color='red', width=4),
                        name="Generating Shape (2D)"
                    ))

                    # 4. 美化布局
                    fig_rev.update_layout(
                        height=400,  # 稍微高一点，展示细节
                        margin=dict(t=0, b=0, l=0, r=0),
                        scene=dict(
                            xaxis=dict(visible=False),
                            yaxis=dict(visible=False),
                            zaxis=dict(visible=False),  # 隐藏坐标轴，看起来像悬浮在太空
                            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))  # 默认视角
                        ),
                        template="plotly_dark",
                        showlegend=False
                    )

                    st.plotly_chart(fig_rev, use_container_width=True)
                    st.info(
                        "💡 **Guldin's Insight:** The volume is simply the **Area of the Red Circle** × **Distance traveled by its center**.")

                    # --- 4. 英国学派 (前驱：导师与密码专家) ---
                with giant_t4:
                    st.markdown("#### 🇬🇧 The British Predecessors")
                    st.caption("They set the stage for Newton's 'Annus Mirabilis' (Year of Wonders).")

                    # --- 伊萨克·巴罗 (Isaac Barrow) ---
                    c_b1, c_b2 = st.columns([1, 3])
                    with c_b1:
                        st.image("barrow.jpg",
                                 caption="Isaac Barrow (1630-1677)", use_container_width=True)
                    with c_b2:
                        st.markdown("**Isaac Barrow (The Master Geometer)**")
                        st.write("""
                           Newton's mentor and the first Lucasian Professor of Mathematics at Cambridge. 
                           He was perhaps the last great mathematician to believe that **Geometry was the only true language of math**.
                           """)

                        with st.expander("🔍 Deep Dive: The Differential Triangle"):
                            st.write("""
                               Barrow discovered the **Fundamental Theorem of Calculus** purely through geometry. 
                               He realized that if you draw a 'Differential Triangle' (a tiny triangle on the curve), 
                               the ratio of its sides is exactly the slope of the tangent.
                               """)
                            # 简单展示微分三角形逻辑
                            st.latex(r"\text{Slope} = \frac{\Delta y}{\Delta x} \approx \frac{dy}{dx}")
                            st.write(
                                "This insight linked the problem of **Tangents** directly to the problem of **Area**.")

                        with st.popover("⚔️ Fun Fact: The Strongest Professor"):
                            st.write("""
                               * **The Gladiator:** Barrow was famously strong. Legend has it he once fought off a massive guard dog with his bare hands while traveling in the East.
                               * **The Resignation:** He was so impressed by young Newton's genius that he **willingly resigned** his prestigious professor chair so Newton (only 26 then) could take over. Talk about the world's best teacher!
                               """)

                    st.divider()

                    # --- 约翰·沃利斯 (John Wallis) ---
                    c_w1, c_w2 = st.columns([1, 3])
                    with c_w1:
                        st.image("wallis.jpg",
                                 caption="John Wallis (1616-1703)", use_container_width=True)
                    with c_w2:
                        st.markdown("**John Wallis (The Algebraic Pioneer)**")
                        st.write("""
                           If Barrow was the last of the Greeks, Wallis was the first of the Moderns. 
                           He famously declared: **'Let's stop drawing pictures and start using equations!'**
                           """)

                        with st.expander("♾️ Contribution: Algebraizing the Infinite"):
                            st.write("""
                               * **Infinity Symbol:** He was the first to use the $\infty$ symbol in his book *Arithmetica Infinitorum*.
                               * **Defining the Inverse & Fractional Powers:** He was the first to formalize the definitions of negative and fractional exponents, such as $x^{-n} = 1/x^n$ and $x^{1/n} = \sqrt[n]{x}$.
                               * **The "Standardized" Bullet:** By treating all curves as simple powers ($x^n$), he unified the "ammunition" of Calculus, allowing Newton to apply the Binomial Theorem to any function.
                               * **The Product of Pi:** He created a famous infinite product to calculate $\pi$.
                               """)
                            st.latex(
                                r"\frac{\pi}{2} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \dots")

                        with st.popover("🕵️ Fun Fact: The Math Spy"):
                            st.write("""
                               * **Codebreaker:** During the English Civil War, Wallis was a master **cryptographer**. He could break complex coded messages for the government in his head while lying in bed at night.
                               * **Mental Calculator:** He once calculated the square root of a 53-digit number to 27 decimal places in his head just because he couldn't sleep!
                               """)
    # ==========================================
    # ERA IV: 诞生 (牛顿与莱布尼茨)
    # ==========================================
    with tabs[3]:  # Era IV: The Systematizers
        st.header("👑 Era IV: The Systematizers (1665 - 1684)")
        st.markdown("""
        Before them, Calculus was a bag of tricks. They turned it into a **System**.

        * **Newton** turned it into a physical engine using **Series**.
        * **Leibniz** turned it into a logical machine using **Symbols**.
        """)

        col_newton, col_leibniz = st.columns(2)

        # --- 🔴 Isaac Newton Column ---
        with col_newton:
            st.container(border=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg",
                     caption="Isaac Newton: The Pragmatist", width=250)

            # --- 1. The Engine: 广义二项式定理 ---
            st.subheader("🍎 1. The Engine: Infinite Series")
            st.markdown("Newton viewed functions as **Infinite Polynomials**.")
            st.write("He discovered that $(1+x)^n$ works even for fractions ($n=1/2$). This was his 'Nuclear Weapon'.")

            # 核心公式
            st.latex(r"(1-x^2)^{\frac{1}{2}} = 1 - \frac{1}{2}x^2 - \frac{1}{8}x^4 - \frac{1}{16}x^6 - \dots")
            st.write("This was a game-changer because polynomials are incredibly easy to manipulate. By turning complex curves into infinite polynomials, Newton could differentiate and integrate them term-by-term with simple power rules. It turned impossible calculus problems into basic algebra.")

            # === 🎮 交互演示：从直线变圆 ===
            st.markdown("---")
            st.caption("🎮 **Interactive Lab:** Watch Newton turns Algebra into Geometry")

            # 滑块：选择多项式的项数
            n_terms = st.slider("Approximation Terms", 1, 5, 2, key="newton_circle_slider")

            # 数据准备
            x = np.linspace(-1, 1, 400)
            y_true = np.sqrt(1 - x ** 2)  # 真实的圆

            # 计算级数逼近 (手动列出前几项以保证速度和清晰度)
            # y = 1 - 0.5x^2 - 0.125x^4 - 0.0625x^6 - 0.039x^8
            y_est = np.ones_like(x)  # Term 1: 1
            if n_terms >= 2: y_est -= 0.5 * x ** 2
            if n_terms >= 3: y_est -= 0.125 * x ** 4
            if n_terms >= 4: y_est -= 0.0625 * x ** 6
            if n_terms >= 5: y_est -= 0.0390625 * x ** 8

            # 绘图
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.plot(x, y_true, label="True Circle", color="black", linewidth=2)
            ax.plot(x, y_est, label=f"Newton's Series (n={n_terms})", color="red", linestyle="--", linewidth=2)

            # 图表美化
            ax.set_ylim(0, 1.1)
            ax.set_xlim(-1.1, 1.1)
            ax.legend()
            ax.grid(True, alpha=0.3)
            ax.set_title(f"Approximating a Circle with {n_terms} Terms")

            # 在 Streamlit 展示
            st.pyplot(fig)

            st.success(
                f"With just {n_terms} terms, the polynomial (Red) is already hugging the circle (Black). Newton used this to calculate $\pi$!")
            # ==========================================

            st.divider()

            # --- 1. The Masterpiece: 巨著问世 ---
            st.markdown("### 📜 1. The Masterpiece: *Principia* (1687)")

            col_bk1, col_bk2 = st.columns([1, 2])
            with col_bk1:
                # 建议加入书的封面图
                st.image(
                    "principia.jpg",
                    caption="Philosophiæ Naturalis Principia Mathematica(1687)")

            with col_bk2:
                st.write("""
                            Newton's *Philosophiae Naturalis Principia Mathematica* is arguably the most influential book in science. 

                            It wasn't just a physics textbook; it was his attempt to decode the **'Divine Order'** of the universe. Inside, he laid down the laws of motion and universal gravitation using his secret weapon: **Calculus** (which he called the 'Method of Fluxions').
                            """)
                st.info(
                    "💡 **Fun Fact:** Newton didn't actually use the word 'Calculus' in the book. He hid the math inside geometric proofs!")

            st.divider()

            # ... 后面接你原来的代码
            # --- 2. The Motion: 流数术 ---
            st.subheader("🌊 2. The Motion: Fluxions")
            st.markdown("He didn't care about static curves; he cared about **Moving Points**.")

            c_flux_1, c_flux_2 = st.columns([1, 2])
            with c_flux_1:
                st.latex(r"\text{Velocity} = \dot{x}")
                st.latex(r"\text{Accel} = \ddot{x}")
            with c_flux_2:
                st.caption(
                    "The **Dot** ($\dot{x}$) represents speed (derivative w.r.t Time). This notation created Modern Physics ($F=ma$).")

            # --- 3. 历史背景 (折叠区) ---
            st.divider()

            with st.expander("🤬 The Feud with Hooke (Drama)"):
                st.write("""
                **The Beef:** Hooke claimed *he* gave Newton the Inverse Square Law idea.
                **The Reaction:** Newton deleted every reference to Hooke from *Principia*.
                """)
                st.info("💬 'Standing on the shoulders of **Giants**' — Likely a sarcasm, as Hooke was short!")

            with st.expander("📐 Why Euclidean Geometry?"):
                st.write("""
                The "Smatterer" Shield: He deliberately made the Principia "abstruse" to deter "little Smatterers" (shallow critics) from pestering him with annoying arguments.

The Irrefutable Weapon: In the 1600s, Euclidean Geometry was the ultimate standard of truth. While Calculus was still controversial, a geometric proof was impossible to argue against.

Anti-Descartes: He despised René Descartes’ algebraic methods, viewing the reduction of physical reality to abstract symbols as "lazy" and less rigorous than geometric intuition.

Key Insight: Newton used Calculus to discover the truth, but used Geometry to build a fortress around it.
                """)
        # --- 🔵 G.W. Leibniz (符号 + 逻辑 + 二进制) ---
        with col_leibniz:
            st.container(border=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Gottfried_Wilhelm_von_Leibniz.jpg",
                     caption="G.W. Leibniz: The Systematizer", width=250)

            st.subheader("🦁 The Machine: The Rules")

            # --- 修改 1: 在规则上方加入肖像与宏观愿景，与 Newton 风格统一 ---
            st.write("""
                Leibniz wanted to make Calculus **automatic**. He dreamed of a *Mathesis Universalis*—a universal language where every logical error would be a simple calculation error.

                He invented the 'Cheat Codes' we memorize today:
                """)

            # --- 修改 2: 保持你原本的规则排版完全不动 ---
            st.markdown("**1. The Product Rule (1675)**")
            st.latex(r"d(uv) = u \, dv + v \, du")

            st.markdown("**2. The Quotient Rule (1677)**")
            st.latex(r"d\left(\frac{u}{v}\right) = \frac{v \, du - u \, dv}{v^2}")

            st.markdown("**3. The Chain Rule (1676)**")
            st.latex(r"\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}")

            st.caption(
                "While Newton had to expand series to solve these, Leibniz gave us **formulas** that work instantly.")

            # --- 修改 3: 加入一个低调的折叠区，介绍他除了符号以外的伟大发现 ---
            with st.expander("🧠 Leibniz's Legacy: Beyond the Symbols"):
                st.write("""
                * **The Integral Sign ($\int$):** He chose the elongated 'S' for *Summa* (Sum) because he realized integration is just the infinite sum of infinitesimal differences.
                * **Binary Logic:** He is the father of the **0 and 1** system, which he viewed as a mathematical representation of creation out of nothing.""")
                st.image(
                    "binary.jpg",
                    caption="Leibniz's Binary Manuscript (1703)")
                st.write(""""* **Optimization:** He believed God designed the world using the 'Calculus of Variations' to find the **Best of all possible worlds**—maximizing variety while minimizing waste.
                """)
                st.info("💬 'Let us calculate!' — His famous response to any intellectual dispute.")
            # --- 🤖 哲学区：二进制 ---
            with st.expander("🤖 The Code of God: Binary"):
                st.write("""
                Leibniz was obsessed with a 'Universal Language'.

                He invented the **Binary System (0 and 1)** used by computers today.
                * **1 (God)** represents existence.
                * **0 (Void)** represents nothingness.
                """)
                st.image(
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Leibniz_binary_system_1703.png/440px-Leibniz_binary_system_1703.png",
                    caption="Leibniz's Binary Manuscript (1703)")

        st.divider()

        # --- 🤝 The Grand Synthesis: FTC ---
        st.markdown("### 🏆 The Shared Discovery: Fundamental Theorem of Calculus")
        st.write("Despite their hate for each other, they both uncovered the same truth that connected Slope and Area.")

        c1, c2, c3 = st.columns([1, 3, 1])
        with c2:
            st.container(border=True)
            st.latex(r"\int_a^b f'(x) \, dx = f(b) - f(a)")

        # ==========================================
        # Era V: The Crisis of Logic (1734) - REFACTORED
        # ==========================================
        # 确保这里使用的是正确的 Tab 变量名 (如果你用的是列表则是 tabs[4]，如果是解包则是 tab5)
        with tabs[4]:
            st.subheader("👻 Era V: The Crisis of Logic (1734)")
            st.markdown(
                "Calculus worked perfectly for physics, but logically it was a disaster. Mathematicians were dividing by zero and getting away with it."
            )

            # 1. The Attack (Berkeley)
            with st.container():
                st.error("⚔️ The Attack: Bishop Berkeley (1734)")
                col_berk_1, col_berk_2 = st.columns([2, 1])

                with col_berk_1:
                    st.markdown("""
                    Bishop Berkeley published *The Analyst*, subtitled **"A Discourse Addressed to an Infidel Mathematician"**. 

                    **The Religious Motive:**
                    Berkeley wasn't just nitpicking math; he was fighting a **Holy War**. Scientists (the "Freethinkers") of his day mocked religious "mysteries" like the Trinity for being irrational. Berkeley struck back by proving that Calculus—the crown jewel of science—was built on even weirder "mysteries" that required pure faith to accept.

                    **His famous insult:**
                    > *"He divides by $dx$, so it is not zero. Then he throws it away, so it is zero. These are the **Ghosts of departed quantities**!"*
                    """)

                with col_berk_2:
                    # --- 保持原有肖像 ---
                    st.image(
                        "berkeley.jpg",
                        caption="George Berkeley")

                    st.caption("Berkeley's Point: logical fallacy.")
                    st.latex(r"\frac{(x+dx)^2 - x^2}{dx} = 2x + dx \xrightarrow{dx=0} 2x")
                    st.caption("If $dx$ is 0, you can't divide. If $dx$ isn't 0, you can't throw it away.")

            st.divider()

            # 2. The Defense (Bayes & d'Alembert)
            st.info("🛡️ The Defense: Trying to Fix the Foundation")

            col_def_1, col_def_2 = st.columns(2)

            with col_def_1:
                # --- 加入贝叶斯肖像 ---
                # 注意：历史上没有确切的贝叶斯画像，这是最常被引用的画像
                st.image("https://upload.wikimedia.org/wikipedia/commons/d/d4/Thomas_Bayes.gif", width=150,
                         caption="Thomas Bayes")

                st.markdown("#### 1. Thomas Bayes (1736)")
                st.caption("**The Logic of the Ratio**")
                st.write("""
                Long before he became famous for Probability, Bayes wrote an anonymous defense of Newton.

                **His Argument:**
                He argued that even if the quantities (distance and time) vanish to zero, **their ratio (speed) remains real**.

                *Analogy:* If a car takes a photo at 60mph, in that frozen instant ($t=0$), it moves distance ($d=0$). But the **Velocity** (the potential to move) is still real and calculable.
                """)

            with col_def_2:
                # --- 加入达朗贝尔肖像 ---
                st.image(
                    "alembert.jpg",
                    width=150, caption="Jean le Rond d'Alembert")

                st.markdown("#### 2. d'Alembert (1754)")
                st.caption("**The Concept of 'Limit'**")
                st.write("""
                d'Alembert finally hit the nail on the head in the *Encyclopédie*. He rejected "tiny numbers."

                **His Contribution:**
                He introduced the word **"Limit" (Limite)**.
                > *"The magnitude is not the ratio of two zeros, but the **Limit** that the ratio approaches."*

                **Note:** He created the *concept*, but the symbol $\lim$ was invented later by L'Huilier (1786).
                """)

            # 3. Conclusion
            st.markdown("---")
            st.success("""
            **The Resolution:** It took another 100 years for Cauchy and Weierstrass to turn d'Alembert's idea into the rigorous $\epsilon-\delta$ definition we use today. But the ghost was finally exorcised.
            """)

    # ==========================================
    # Era VI: The Reign of Rigor (19th Century)
    # ==========================================
    with tabs[5]:
        st.header("🏁 Era VI: The Reign of Rigor (The 19th Century)")
        st.markdown("""
        For 150 years, Calculus was built on "intuition" and "ghosts." 
        In the 19th century, three giants decided to rebuild the foundation with **cold, hard logic**.
        """)

        # --- 1. AUGUSTIN-LOUIS CAUCHY (The Limit Concept) ---
        st.subheader("1. Augustin-Louis Cauchy (1789-1857)")
        c_col1, c_col2 = st.columns([1, 3])
        with c_col1:
            # 这里替换为柯西的照片路径
            st.image(
                "cauchy.jpg",
                caption="Cauchy")
        with c_col2:
            st.markdown("""
            **The Problem:** Before Cauchy, mathematicians said derivatives were ratios of "tiny zeros" ($0/0$). This was illogical.

            **The Solution (The Limit):** Cauchy redefined $dy/dx$ not as a division, but as a **Limit**.
            * He said: "We don't need the value *at* zero. We only care about the **trend** as we get closer to zero."
            * He formalized the definition of **Continuity**: A function is continuous if small changes in $x$ produce small changes in $y$.
            """)
            st.info(
                "💡 **Impact:** He banished the 'Ghosts of departed quantities.' Calculus became the study of **Limits**, not infinitesimals.")

        st.divider()

        # --- 2. KARL WEIERSTRASS (The Static Logic / Epsilon-Delta) ---
        st.subheader("2. Karl Weierstrass (1815-1897)")
        st.markdown(
            "**The Father of Modern Rigor.** He hated 'motion' in math. He turned Calculus into static inequalities.")

        w_col1, w_col2 = st.columns([2, 1])

        with w_col2:
            # 这里替换为魏尔斯特拉斯的照片路径
            st.image("weierstrass.jpg",
                     caption="Weierstrass")
            st.caption("The man who formalized the $\epsilon-\delta$ definition.")

            # ... (之前的代码) ...

            with w_col1:
                st.markdown("#### 🏭 The Factory Challenge")
                st.write(
                    "Imagine you run a machine. The Limit exists only if you can satisfy the world's strictest boss.")

                # --- Interactive Visual (No Greek Letters) ---
                target_L = 4  # Perfect Output
                target_c = 2  # Perfect Knob Setting

                # 1. 客户的要求 (The Boss's Demand)
                st.markdown("**Step 1: The Boss sets the Quality Standard**")
                error_margin = st.slider("Allowed Error Margin (Green Zone)", 0.1, 2.0, 1.0, 0.1)

                # 2. 你的应对 (Your Solution)
                # 为了保证 x^2 在 4±error 范围内，x 必须在 sqrt(4-error) 和 sqrt(4+error) 之间
                # 我们计算出需要的 safe_range (delta)
                # 这是一个简化的演示计算
                safe_knob_range = error_margin / 4.5

                st.markdown(f"**Step 2: Your Response**")
                st.caption(
                    f"To satisfy an error of **{error_margin}**, you must keep the knob within **±{safe_knob_range:.3f}** (Orange Zone).")

                # Generate Graph
                x_vals = np.linspace(0, 4, 100)
                y_vals = x_vals ** 2

                fig_ed = go.Figure()

                # Green Zone (Quality Control)
                fig_ed.add_shape(type="rect",
                                 x0=0, y0=target_L - error_margin, x1=4, y1=target_L + error_margin,
                                 fillcolor="rgba(0, 255, 0, 0.2)", line=dict(width=0), layer="below"
                                 )
                fig_ed.add_annotation(x=0.5, y=target_L + error_margin, text="Acceptable Quality", showarrow=False,
                                      font=dict(color="green"))

                # Orange Zone (Knob Setting)
                fig_ed.add_shape(type="rect",
                                 x0=target_c - safe_knob_range, y0=0, x1=target_c + safe_knob_range, y1=16,
                                 fillcolor="rgba(255, 165, 0, 0.3)", line=dict(width=0), layer="below"
                                 )
                fig_ed.add_annotation(x=target_c, y=1, text="Your Knob Setting", showarrow=False,
                                      font=dict(color="orange"))

                # Function Curve
                fig_ed.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Machine Output',
                                            line=dict(color='white', width=3)))

                # Target Point
                fig_ed.add_trace(go.Scatter(x=[target_c], y=[target_L], mode='markers', name='Perfection',
                                            marker=dict(size=12, color='red')))

                fig_ed.update_layout(
                    title="Can you stay in the Green Zone?",
                    xaxis_title="Knob Setting (Input)", yaxis_title="Product Quality (Output)",
                    height=350, margin=dict(l=0, r=0, t=40, b=0),
                    showlegend=False
                )
                st.plotly_chart(fig_ed, use_container_width=True)

                if error_margin < 0.3:
                    st.success("🏆 Even with strict demands, you found a setting that works! The Limit exists.")
                else:
                    st.info("Try making the Allowed Error smaller to see if you can still handle it.")
        st.divider()

        # --- 3. BERNHARD RIEMANN (The Integral) ---
        st.subheader("3. Bernhard Riemann (1826-1866)")

        r_col1, r_col2 = st.columns([1, 2])

        with r_col1:
            # 这里替换为黎曼的照片路径
            st.image("riemann.jpg", caption="Riemann")

        with r_col2:
            st.markdown("""
            **The Problem:** Newton defined Integration as just "Anti-Differentiation." But what if the function is jagged, broken, or weird? You can't differentiate it, so Newton's method fails.

            **The Solution (Riemann Sums):** Riemann went back to the Greeks. He defined Area as the **Limit of Sums of Rectangles**.
            * It doesn't matter if the function is smooth.
            * As long as you can draw rectangles under it, you can integrate it.
            """)

        # --- Interactive Riemann Sum Visual ---
        st.markdown("#### 📊 Interactive: Riemann Sums")
        n_rects = st.slider("Number of Rectangles (n)", 4, 100, 10)

        # Data for Riemann
        x_r = np.linspace(0, np.pi, 200)
        y_r = np.sin(x_r)

        # Rectangles
        x_bar = np.linspace(0, np.pi, n_rects + 1)
        y_bar = np.sin(x_bar)  # Left Riemann sum
        width_bar = x_bar[1] - x_bar[0]

        fig_riemann = go.Figure()

        # Curve
        fig_riemann.add_trace(go.Scatter(x=x_r, y=y_r, mode='lines', name='f(x)=sin(x)', line=dict(color='#00ADB5')))

        # Rectangles
        fig_riemann.add_trace(go.Bar(
            x=x_bar[:-1], y=y_bar[:-1], width=[width_bar] * n_rects,
            offset=0, marker=dict(color='rgba(255, 255, 255, 0.3)', line=dict(color='pink', width=1)),
            name='Rectangles'
        ))

        fig_riemann.update_layout(
            title=f"Approximating Area with {n_rects} Rectangles",
            xaxis_title="x", yaxis_title="sin(x)",
            height=300, showlegend=False
        )
        st.plotly_chart(fig_riemann, use_container_width=True)

        st.caption(
            "**Legacy:** This method (Integration as Summation) is what allows computers to calculate areas today. They don't use formulas; they use millions of tiny Riemann rectangles.")


    # ==========================================
    # Era VII: The Modern Horizon (The Lebesgue Mastery)
    # ==========================================
    with tabs[6]:
        st.header("🌌 Era VII: The Modern Horizon")

        # --- 修改开始：使用列布局来放置文字和肖像 ---
        col_intro, col_img = st.columns([3, 1])  # 3:1 的比例让文字占主体

        with col_intro:
            st.markdown("### 🧩 Taming the Dirichlet 'Monster'")
            st.write("""
            In the 20th century, math encountered a crisis: functions so 'broken' that traditional area-calculating methods simply died. 
            Let's break down the logic of how **Henri Lebesgue** solved this.
            """)

        with col_img:
            # 勒贝格的经典肖像
            st.image("lebesgue.jpg",
                     caption="Henri Lebesgue")
        # --- 修改结束 ---

        # ---------------------------------------------------------
        # STEP 1: The Function Definition (以下代码保持完全不变)
        # ---------------------------------------------------------
        st.subheader("Step 1: Meet the Dirichlet Function $D(x)$")
        st.latex(
            r"D(x) = \begin{cases} 1, & x \in \mathbb{Q} \text{ (Rationals)} \\ 0, & x \in \mathbb{I} \text{ (Irrationals)} \end{cases}")
        st.info("Imagine a function that jumps between 0 and 1 infinitely fast, in every tiny interval.")

        # ---------------------------------------------------------
        # STEP 2: Why Riemann Fails (The Visual Proof)
        # ---------------------------------------------------------
        st.subheader("Step 2: Why Riemann Integration Fails")
        st.markdown("""
        Riemann tries to draw **vertical rectangles**. But because rationals and irrationals are both 'dense', 
        any rectangle—no matter how thin—contains points at both height 0 and height 1.
        """)

        col_r1, col_r2 = st.columns([2, 1])
        with col_r1:
            # 可视化：黎曼上下和的冲突
            n_r = 500
            x_r = np.linspace(0, 1, n_r)
            y_r = np.random.choice([0, 1], size=n_r, p=[0.7, 0.3])

            fig_r = go.Figure()
            # 绘制背景：灰色代表无法确定的“震荡区”
            fig_r.add_shape(type="rect", x0=0, y0=0, x1=1, y1=1, fillcolor="rgba(255,255,255,0.1)", line=dict(width=0))
            fig_r.add_trace(go.Scatter(x=x_r, y=y_r, mode='markers', marker=dict(size=2, color='black'), name="Chaos"))
            fig_r.update_layout(title="Riemann's Nightmare: No stable height.", height=300, showlegend=False,
                                template="plotly_dark")
            st.plotly_chart(fig_r, use_container_width=True)

        with col_r2:
            st.error("**The Logical Loop:**")
            st.markdown("""
            * **Upper Sum:** Always 1 (picks height 1).
            * **Lower Sum:** Always 0 (picks height 0).
            * Since $1 \\neq 0$, the area is **undefined**.
            """)

        st.divider()

        # ---------------------------------------------------------
        # STEP 3: The Secret of "Measure" (Weight of Infinity)
        # ---------------------------------------------------------
        st.subheader("Step 3: The Secret of 'Measure' (Weight of Infinity)")
        st.markdown("""
        Lebesgue realized that not all infinities are equal. We measure the **'Size' (Measure $\mu$)** of sets instead of just counting points.
        """)

        # 交互式对比：有理数 vs 无理数
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            st.write("**The Rationals ($\mathbb{Q}$)**")
            st.caption("Countable Infinity")
            st.write(
                "They are like tiny 'dust' particles. You can cover all of them with 'caps' of total length $\epsilon$.")
            st.success("📐 **Measure $\mu(\mathbb{Q}) = 0$**")

        with m_col2:
            st.write("**The Irrationals ($\mathbb{I}$)**")
            st.caption("Uncountable Infinity")
            st.write("They are the 'solid ocean' that fills the space between the dust.")
            st.success("📐 **Measure $\mu(\mathbb{I}) = 1$** (in the [0,1] range)")

        # ---------------------------------------------------------
        # STEP 4: The Lebesgue Solution (The Final Calculation)
        # ---------------------------------------------------------
        st.subheader("Step 4: The Lebesgue Solution")
        st.markdown(
            "Lebesgue groups the points by their **Height (Value)**, then multiplies by their **Measure (Weight)**.")

        # 优美的横向可视化
        fig_l = go.Figure()
        # 绘制无理数层 (y=0, Weight=1)
        fig_l.add_trace(
            go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='#1C83E1', width=8), name="Irrationals"))
        # 绘制有理数层 (y=1, Weight=0)
        fig_l.add_trace(go.Scatter(x=[0, 1], y=[1, 1], mode='lines', line=dict(color='#FF4B4B', width=2, dash='dash'),
                                   name="Rationals"))

        fig_l.update_layout(
            title="Horizontal Partitioning: Value × Weight",
            yaxis=dict(tickvals=[0, 1], ticktext=["Value: 0", "Value: 1"], range=[-0.5, 1.5]),
            height=350, template="plotly_dark"
        )
        st.plotly_chart(fig_l, use_container_width=True)

        # 最终计算
        st.latex(r"\text{Integral} = (1 \times \mu(\mathbb{Q})) + (0 \times \mu(\mathbb{I}))")
        st.latex(r"\text{Integral} = (1 \times 0) + (0 \times 1) = \mathbf{0}")

        st.success("""
        **Conclusion:** The integral is **0**. Even though there are infinitely many points at height 1, 
        they are 'weightless' in the eyes of Measure Theory. The 'solid' part of the function is all at height 0.
        """)
            # --- 终章 ---
    st.divider()
    st.markdown("### 🎬 Epilogue: The Torch is Passed")
    st.write(
        "You now possess the machinery built by Archimedes, Newton, and Lebesgue. It took 2000 years to forge these tools.")

    col_a, col_b = st.columns(2)
    with col_a:
        st.info("👉 **Chapter I: Limits**\n(The Logic of Cauchy)")
    with col_b:
        st.info("👉 **Chapter II: Differentiation**\n(The Fluxions of Newton)")
# ==========================================
# Chapter I: Limits (The Paradox) - 第一章：极限
# ==========================================

def render_topic_8_limits():
    st.header("🌉 Chapter I: Limits and Continuity")
    st.markdown("""
    To deeply understand Calculus, we must transition from the static equations of Algebra to the dynamic behavior of Limits. 
    This chapter establishes the rigorous foundation required to analyze instantaneous change.
    """)

    limit_tabs = st.tabs([
        "1. Numerical Approach",
        "2. The Epsilon-Delta Definition",
        "3. Algebraic Techniques",
        "4. L'Hôpital & Linearization",
        "5. The Squeeze Theorem: The Sandwich Strategy",
        "6. Asymptotes: The Unreachable Horizons",
        "7. Continuity of a Function",
        "8. The Fractal Frontier: Monsters of Continuity"
    ])

    # ==============================================================================
    # TAB 1: NUMERICAL APPROACH (数值与图像证据)
    # ==============================================================================
    with limit_tabs[0]:
        st.subheader("1. Numerical and Graphical Approach")

        col_i1, col_i2 = st.columns([1, 1.5])

        with col_i1:
            st.markdown("""
            A limit describes the exact value a function approaches as the input approaches a specific point, 
            even if the function itself is completely undefined at that point.
            """)
            st.latex(r"f(x) = \frac{x^2-1}{x-1}")
            st.write("At $x=1$, this yields the indeterminate form $0/0$. Let's observe the trend as $x \to 1$.")

            # 控制精度的交互滑块
            precision = st.slider("Decimal Precision ($x \\to 1$):", 1, 6, 3)
            delta = 10 ** (-precision)

            left_x, right_x = 1 - delta, 1 + delta

            # 使用安全的字典结构生成数据
            data = {
                "Approach": ["From Left ($x < 1$)", "From Right ($x > 1$)"],
                "Input x": [left_x, right_x],
                "Output f(x)": [(left_x ** 2 - 1) / (left_x - 1), (right_x ** 2 - 1) / (right_x - 1)]
            }
            df = pd.DataFrame(data)

            # 严格格式化数值，避免报错
            st.table(df.style.format({
                "Input x": f"{{:.{precision + 1}f}}",
                "Output f(x)": f"{{:.{precision + 1}f}}"
            }))

            st.success("The numerical data definitively converges to **2.0** from both sides.")

        with col_i2:
            x_vals = np.linspace(0.5, 1.5, 300)
            y_vals = x_vals + 1
            fig = go.Figure()

            fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name="f(x)", line=dict(color='#636EFA', width=3)))

            # 标记缺失的点 (Hole)
            fig.add_trace(go.Scatter(
                x=[1], y=[2], mode='markers', name="Undefined at x=1",
                marker=dict(symbol='circle-open', size=12, color='white', line=dict(width=2, color='red'))
            ))

            fig.update_layout(
                template="plotly_dark", height=400,
                title="Graphical Evidence of the Limit",
                xaxis_title="x", yaxis_title="f(x)"
            )
            st.plotly_chart(fig, use_container_width=True)

        # ==============================================================================
        # TAB 2: THE EPSILON-DELTA DEFINITION (严谨定义与病态反例)
        # ==============================================================================
        with limit_tabs[1]:
            st.subheader("2. The Rigorous Definition: Ending the 'Ghost' Era")

            st.markdown("""
            ### The Crisis of Calculus
            For 200 years after Newton and Leibniz, Calculus relied on **Infinitesimals**—mysterious numbers that were "infinitely small but not zero." Philosophers like Bishop Berkeley famously mocked them as the *"ghosts of departed quantities."*

            This reliance on visual intuition and vague concepts of "motion" caused a severe logical crisis when mathematicians discovered **Pathological Functions**—functions so chaotic that human intuition completely breaks down.

            To save the mathematical universe, Weierstrass introduced the $\epsilon-\delta$ definition in the 19th century. It eliminated the concept of "motion" (approaching) and replaced it with a **static, irrefutable logical contract**.


            """)

            st.latex(
                r"\lim_{x \to c} f(x) = L \iff \forall \epsilon > 0, \exists \delta > 0 \text{ s.t. } 0 < |x - c| < \delta \implies |f(x) - L| < \epsilon")

            st.markdown(
                "Let's see why this strict contract is necessary by comparing a **Healthy Function** with a **Pathological Function**.")

            # 使用内部 Tab 进行正反面对比
            case_tab1, case_tab2 = st.tabs(["Case A: The Healthy Function", "Case B: The Pathological Boss"])

            # ----------------------------------------------------------------------
            # CASE A: 正常函数，成功签订契约
            # ----------------------------------------------------------------------
            with case_tab1:
                st.markdown("#### Proving $\lim_{x \to 3} 2x = 6$")
                st.write(
                    "For a well-behaved function, we can always find a fine enough precision ($\delta$) to satisfy the tolerance ($\epsilon$).")

                col_def1, col_def2 = st.columns([1, 2])

                with col_def1:
                    epsilon = st.slider("Target Tolerance ($\epsilon$):", 0.1, 2.0, 1.0,
                                        help="Allowable deviation on the y-axis.")
                    delta_user = st.slider("Input Precision ($\delta$):", 0.05, 1.5, 0.5,
                                           help="Control range on the x-axis.")

                    max_output_error = 2 * delta_user
                    is_valid = max_output_error <= epsilon

                    st.divider()
                    if is_valid:
                        st.success("✅ Proof Condition Satisfied.")
                        st.write(
                            f"When $|x-3| < {delta_user}$, the maximum output error is **{max_output_error:.2f}**, perfectly within the tolerance $\epsilon = {epsilon}$.")
                    else:
                        st.error("❌ Proof Condition Failed.")
                        st.write(
                            f"Your input range ($\delta$) is too wide. The output error reaches **{max_output_error:.2f}**, exceeding the tolerance $\epsilon = {epsilon}$.")
                        st.write(f"**Required:** $\delta \le \epsilon/2 = {epsilon / 2:.2f}$")

                with col_def2:
                    x_e = np.linspace(1, 5, 100)
                    y_e = 2 * x_e
                    fig_def = go.Figure()

                    fig_def.add_trace(go.Scatter(x=x_e, y=y_e, name="f(x)=2x", line=dict(color='white')))
                    fig_def.add_hrect(y0=6 - epsilon, y1=6 + epsilon, fillcolor="red", opacity=0.15,
                                      annotation_text="Epsilon Tolerance Band")

                    box_color = "green" if is_valid else "orange"
                    fig_def.add_shape(type="rect",
                                      x0=3 - delta_user, x1=3 + delta_user,
                                      y0=6 - (2 * delta_user), y1=6 + (2 * delta_user),
                                      line=dict(color=box_color, width=2), fillcolor=box_color, opacity=0.3)

                    fig_def.update_layout(xaxis=dict(range=[1, 5]), yaxis=dict(range=[2, 10]), template="plotly_dark",
                                          height=400, title="Geometric Interpretation: Contract Signed")
                    st.plotly_chart(fig_def, use_container_width=True)

            # ----------------------------------------------------------------------
            # CASE B: 病态函数，契约崩溃
            # ----------------------------------------------------------------------
            with case_tab2:
                st.markdown("#### The Breakdown: Evaluating $f(x) = \sin(1/x)$ at $x=0$")
                st.markdown("""
                Why does $\lim_{x \\to 0} \sin(1/x)$ not exist? Our intuition says "it's connected." Let's test it with the formal law.

                **The Scenario:** Assume someone claims the limit is $0$. The skeptic sets a strict tolerance of **$\epsilon = 0.5$** (The Red Band). 
                Your job is to zoom in (shrink your $\delta$ window) and try to trap the function entirely inside the red band.


                """)

                zoom_level = st.select_slider("Zoom Level (Shrinking the $\delta$ window):",
                                              options=[1, 10, 100, 1000, 10000])

                # 动态调整 x 的范围 (模拟 delta 的缩小)
                delta_window = 1.0 / zoom_level
                x_patho = np.linspace(-delta_window, delta_window, 2000)
                x_patho = x_patho[x_patho != 0]  # 防止除以零
                y_patho = np.sin(1 / x_patho)

                fig_patho = go.Figure()
                fig_patho.add_trace(
                    go.Scatter(x=x_patho, y=y_patho, name="sin(1/x)", line=dict(color='#ff4b4b', width=1)))

                # 客户设定的死要求 Epsilon = 0.5
                fig_patho.add_hrect(
                    y0=-0.5, y1=0.5,
                    fillcolor="red",
                    opacity=0.15,
                    # 使用 Unicode 字符 ε 和 ± 替代 LaTeX 源码
                    annotation_text="Target Range (ε = ±0.5)",
                    annotation_position="top right",
                    annotation_font_size=14,
                    annotation_font_color="red"
                )

                fig_patho.update_layout(
                    # 直接用 f-string 和实体符号，绝不报错
                    title=f"Infinite Oscillation (Zoom: {zoom_level}x, δ = ±{delta_window:.4f})",
                    xaxis_title="Input x (Approaching 0)",
                    yaxis_title="Output f(x)",
                    template="plotly_dark",
                    yaxis=dict(range=[-1.2, 1.2]),
                    height=400
                )
                st.plotly_chart(fig_patho, use_container_width=True)

                st.error("""
                **The Verdict:** No matter how incredibly small you make your $\delta$ window (even at 10,000x zoom), the function continues to oscillate wildly between -1 and 1. 
                It is mathematically **impossible** to keep the output strictly inside the $\pm 0.5$ tolerance band. Thus, the contract fails. **The limit does not exist.**
                """)
    # ==============================================================================
    # TAB 3: ALGEBRAIC TECHNIQUES (代数技巧)
    # ==============================================================================
    with limit_tabs[2]:
        st.subheader("3. Algebraic Techniques for Indeterminate Forms")
        st.write(
            "Before using advanced tools, we rely on these 4 core algebraic manipulations to resolve $0/0$ and $\\infty/\\infty$ forms.")

        row1_col1, row1_col2 = st.columns(2)

        with row1_col1:
            st.markdown("#### 1. Factorization")
            st.latex(r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{x-2}")
            st.latex(r"= \lim_{x \to 2} (x+2) = 4")

        with row1_col2:
            st.markdown("#### 2. Conjugation")
            st.latex(r"\lim_{x \to 0} \frac{\sqrt{x+9}-3}{x} \cdot \frac{\sqrt{x+9}+3}{\sqrt{x+9}+3}")
            st.latex(r"= \lim_{x \to 0} \frac{x}{x(\sqrt{x+9}+3)} = \frac{1}{6}")

        st.divider()

        row2_col1, row2_col2 = st.columns(2)

        with row2_col1:
            st.markdown("#### 3. Complex Fractions")
            st.latex(r"\lim_{x \to 0} \frac{\frac{1}{x+2} - \frac{1}{2}}{x}")
            st.latex(r"= \lim_{x \to 0} \frac{\frac{2 - (x+2)}{2(x+2)}}{x} = \lim_{x \to 0} \frac{-x}{2x(x+2)}")
            st.latex(r"= \lim_{x \to 0} \frac{-1}{2(x+2)} = -\frac{1}{4}")

        with row2_col2:
            st.markdown("#### 4. Limits at Infinity")
            st.latex(r"\lim_{x \to \infty} \frac{3x^2 - x - 2}{5x^2 + 4x + 1}")
            st.latex(
                r"= \lim_{x \to \infty} \frac{3 - \frac{1}{x} - \frac{2}{x^2}}{5 + \frac{4}{x} + \frac{1}{x^2}} = \frac{3}{5}")

            x_inf = np.linspace(1, 50, 400)
            y_inf = (3 * x_inf ** 2 - x_inf - 2) / (5 * x_inf ** 2 + 4 * x_inf + 1)

            fig_inf = go.Figure()
            fig_inf.add_trace(go.Scatter(x=x_inf, y=y_inf, name="f(x)", line=dict(color='#00CC96', width=2)))
            fig_inf.add_hline(
                y=0.6,
                line_dash="dash",
                line_color="red",
                annotation_text="y = 3/5 (Asymptote)",
                annotation_position="bottom right"
            )

            fig_inf.update_layout(
                title="Visualizing the Horizontal Asymptote",
                template="plotly_dark",
                height=250,
                margin=dict(l=20, r=20, t=40, b=20),
                xaxis_title="x approaches infinity",
                yaxis_title="f(x)"
            )
            st.plotly_chart(fig_inf, use_container_width=True)

    # ==============================================================================
    # TAB 4: L'HOPITAL & LINEARIZATION (洛必达的几何本质)
    # ==============================================================================
        # 请根据你实际的 Tab 序号调整 limit_tabs 的索引
        with limit_tabs[3]:
            st.subheader("4. L'Hôpital's Rule: The Ultimate 0/0 Weapon")

            st.markdown("""
            ### 📖 The History: A Mathematical Heist?
            This famous rule is named after the Marquis de L'Hôpital, who published it in 1696. However, it was actually discovered by the brilliant mathematician **Johann Bernoulli**. L'Hôpital, a wealthy nobleman, essentially paid Bernoulli a salary in exchange for the rights to claim Bernoulli's mathematical discoveries as his own!

            ### 🎯 Why do we need it?
            Algebraic tricks (like factoring) only work on polynomials. When we face transcendental functions like $\lim_{x \\to 0} \\frac{\sin(x)}{x}$, algebra fails completely. **You cannot "factor" a sine wave.** We need a universal tool.

            ### 🧠 The Intuition: "A Race to Zero"
            Imagine the numerator $f(x)$ and denominator $g(x)$ as two runners. At $x=0$, they both hit the exact same position ($0/0$). 
            If they both start at $0$, the ratio of their positions near the origin is simply the ratio of **how fast they are running**. 

            Mathematically, if we zoom in infinitely close, curves become straight lines (**Local Linearization**). We stop dividing their *heights* and start dividing their *slopes* (derivatives):
            """)

            # 核心公式的推导展示
            st.latex(
                r"\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{\frac{f(x) - f(c)}{x - c}}{\frac{g(x) - g(c)}{x - c}} = \frac{f'(c)}{g'(c)}")

            st.divider()

            col_lh1, col_lh2 = st.columns([1, 1.5])

            with col_lh1:
                st.markdown("#### The Classic Proof: $\lim_{x \\to 0} \\frac{\sin(x)}{x}$")
                st.write(
                    "Both functions intersect at $(0,0)$. Let's compare their instantaneous speeds (derivatives) at this exact moment:")

                st.latex(r"f'(x) = \frac{d}{dx}\sin(x) = \cos(x) \implies f'(0) = 1")
                st.latex(r"g'(x) = \frac{d}{dx}x = 1 \implies g'(0) = 1")

                st.write("The true limit is simply the ratio of their tangent slopes:")
                st.latex(r"\lim_{x \to 0} \frac{\sin(x)}{x} = \frac{\cos(0)}{1} = \frac{1}{1} = 1")

                st.success(
                    "L'Hôpital's Rule elegantly converts an impossible division of static heights into a solvable division of dynamic speeds.")

            with col_lh2:
                x_z = np.linspace(-1, 1, 100)
                fig_lh = go.Figure()

                # 画出分子和分母的图像
                fig_lh.add_trace(go.Scatter(x=x_z, y=np.sin(x_z), name="Numerator: f(x) = sin(x)",
                                            line=dict(color='#00CC96', width=3)))
                fig_lh.add_trace(go.Scatter(x=x_z, y=x_z, name="Denominator: g(x) = x",
                                            line=dict(color='#FFD700', dash='dash', width=2)))

                # 添加清晰的标注
                fig_lh.add_annotation(
                    x=0.4, y=0.1,
                    text="Near x=0, the sine curve and<br>the straight line are virtually identical.<br>Their slope ratio is exactly 1:1.",
                    showarrow=True, arrowhead=2, ax=60, ay=40, font=dict(color="white")
                )

                fig_lh.update_layout(
                    title="Local Linearization: Curves Become Tangent Lines",
                    template="plotly_dark",
                    height=380,
                    xaxis_title="x (Zoomed in near 0)",
                    yaxis_title="y"
                )
                st.plotly_chart(fig_lh, use_container_width=True)
    # ==============================================================================
    # TAB 5: 夹逼定理
    # ==============================================================================
    with limit_tabs[4]:
        st.subheader("5. The Squeeze Theorem: The Sandwich Strategy")

        st.markdown("""
        ### 📖 The History: Archimedes' Trap
        The logic of "squeezing" dates back to **Archimedes** (250 BC), who calculated $\pi$ by trapping a circle between an inner and outer polygon. In modern calculus, we use this exact strategy to solve limits that defeat both algebraic tricks and L'Hôpital's Rule.

        ### 🎯 Why do we need it?
        Consider evaluating $\lim_{x \\to 0} x^2 \sin(1/x)$.
        You cannot plug in 0. You cannot factor it. And **L'Hôpital's Rule completely fails** because the derivative involves $\cos(1/x)$, which oscillates infinitely and has no limit. When the function acts like a maniac, we don't calculate its exact path—we trap it with "bodyguards."
        """)

        st.latex(
            r"\text{If } L(x) \le f(x) \le U(x) \text{ near } c, \text{ and } \lim_{x \to c} L(x) = \lim_{x \to c} U(x) = A, \text{ then } \lim_{x \to c} f(x) = A")

        st.divider()

        col_sq1, col_sq2 = st.columns([1, 1.5])

        with col_sq1:
            st.markdown("#### The Derivation: Taming the Chaos")
            st.write(
                "1. **Find the bounded core:** The sine function, no matter how chaotic its input, is always trapped between -1 and 1.")
            st.latex(r"-1 \le \sin\left(\frac{1}{x}\right) \le 1")

            st.write(
                "2. **Deploy the bodyguards:** Multiply the entire inequality by $x^2$. This constructs our Lower $L(x)$ and Upper $U(x)$ bounds.")
            st.latex(r"-x^2 \le x^2 \sin\left(\frac{1}{x}\right) \le x^2")

            st.write("3. **Spring the trap:** Evaluate the limit of the outer bodyguards as $x \to 0$.")
            st.latex(r"\lim_{x \to 0} (-x^2) = 0 \quad \text{and} \quad \lim_{x \to 0} (x^2) = 0")

            st.success(
                "Because both bodyguards converge to 0, the chaotic function trapped in the middle is forced to equal **0**.")

        with col_sq2:
            # 动态滑块：让用户观察视角的缩小
            zoom_sq = st.slider("Magnification (Zoom into x=0):", min_value=1.0, max_value=20.0, value=1.0, step=1.0)

            # 计算动态范围
            x_range = 1.0 / zoom_sq
            x_sq = np.linspace(-x_range, x_range, 2000)
            x_sq = x_sq[x_sq != 0]  # 避免除零错误

            # 定义三个函数：下界、中坚、上界
            y_lower = -x_sq ** 2
            y_upper = x_sq ** 2
            y_mid = (x_sq ** 2) * np.sin(10 / x_sq)  # 用 10/x 增加视觉上的震荡密集度，效果更好

            fig_sq = go.Figure()

            # 画出保镖 (Lower and Upper bounds)
            fig_sq.add_trace(
                go.Scatter(x=x_sq, y=y_upper, name="Upper Bound: x²", line=dict(color='#FFD700', width=2, dash='dot')))
            fig_sq.add_trace(
                go.Scatter(x=x_sq, y=y_lower, name="Lower Bound: -x²", line=dict(color='#00CC96', width=2, dash='dot')))

            # 画出被夹住的疯子函数
            fig_sq.add_trace(
                go.Scatter(x=x_sq, y=y_mid, name="f(x) = x²sin(1/x)", line=dict(color='#ff4b4b', width=1.5)))

            fig_sq.update_layout(
                title=f"The Squeeze in Action (Zoom: {zoom_sq}x)",
                template="plotly_dark",
                height=400,
                xaxis_title="x approaches 0",
                yaxis_title="y"
            )
            st.plotly_chart(fig_sq, use_container_width=True)

            st.info(
                "Observe how the red chaotic curve is strictly confined by the yellow and green parabolas. At x=0, the envelope crushes it to exactly 0.")
    # ==============================================================================
    # TAB 6 (或者新 Tab): ASYMPTOTES (渐近线的寻找与极限意义)
    # ==============================================================================
    with limit_tabs[5]:  # 请根据你实际的 tabs 数组长度修改索引
        st.subheader("6. Asymptotes: The Unreachable Horizons")
        st.markdown("""
        An asymptote is a line that a curve approaches as it heads towards infinity. 
        It is the ultimate geometric visualizer for **Limits**. Let's learn how to hunt them down.
        """)

        asym_type = st.radio("Select Asymptote Type to Explore:",
                             ["Vertical (VA)", "Horizontal (HA)", "Oblique / Slant (OA)"],
                             horizontal=True)

        st.divider()

        col_a1, col_a2 = st.columns([1, 1.2])

        if "Vertical" in asym_type:
            with col_a1:
                st.markdown("### Vertical Asymptote (VA)")
                st.write("**Geometric Meaning:** A solid wall the function cannot cross. It shoots to $\pm \infty$.")
                st.write("**Limit Definition:** $\lim_{x \\to c} f(x) = \pm \infty$")

                st.markdown("#### How to find it:")
                st.info(
                    "1. Fully simplify the rational function (cancel common factors to avoid 'holes').\n2. Set the **denominator = 0** and solve for x.")

                st.markdown("**Example:**")
                st.latex(r"f(x) = \frac{1}{x - 2}")
                st.write("Denominator $x - 2 = 0 \implies \mathbf{x = 2}$ is the VA.")

            with col_a2:
                x_va = np.linspace(0, 4, 400)
                y_va = 1 / (x_va - 2)
                # 核心技巧：在 x=2 附近强行插入 NaN，防止 Plotly 把正负无穷连成一条线
                y_va[np.abs(x_va - 2) < 0.05] = np.nan

                fig_va = go.Figure()
                fig_va.add_trace(go.Scatter(x=x_va, y=y_va, name="f(x)", line=dict(color='#00CC96', width=3)))
                fig_va.add_vline(x=2, line_dash="dash", line_color="red", annotation_text="VA: x = 2")

                fig_va.update_layout(template="plotly_dark", height=350, yaxis=dict(range=[-20, 20]),
                                     title="Approaching Infinity at a Point")
                st.plotly_chart(fig_va, use_container_width=True)

        elif "Horizontal" in asym_type:
            with col_a1:
                st.markdown("### Horizontal Asymptote (HA)")
                st.write(
                    "**Geometric Meaning:** The 'ceiling' or 'floor' the function settles on at the edges of the universe.")
                st.write("**Limit Definition:** $\lim_{x \\to \pm \infty} f(x) = L$")

                st.markdown("#### How to find it:")
                st.info("Compare the highest degree of the Numerator ($N$) and Denominator ($D$):")
                st.markdown("""
                * If $N < D$: The HA is always $\mathbf{y = 0}$ (x-axis).
                * If $N = D$: The HA is the **ratio of leading coefficients**.
                * If $N > D$: **No Horizontal Asymptote**.
                """)

                st.markdown("**Example ($N=D=2$):**")
                st.latex(r"f(x) = \frac{\mathbf{3}x^2 + 1}{\mathbf{1}x^2 - x}")
                st.write("Leading coefficients ratio $\implies \mathbf{y = 3}$ is the HA.")

            with col_a2:
                x_ha = np.linspace(-20, 20, 400)
                y_ha = (3 * x_ha ** 2 + 1) / (x_ha ** 2 - x_ha + 0.001)  # 略微偏移防除零
                y_ha[np.abs(x_ha - 1) < 0.5] = np.nan  # 屏蔽垂直渐近线的干扰
                y_ha[np.abs(x_ha) < 0.5] = np.nan

                fig_ha = go.Figure()
                fig_ha.add_trace(go.Scatter(x=x_ha, y=y_ha, name="f(x)", line=dict(color='#AB63FA', width=3)))
                fig_ha.add_hline(y=3, line_dash="dash", line_color="red", annotation_text="HA: y = 3")

                fig_ha.update_layout(template="plotly_dark", height=350, yaxis=dict(range=[-5, 10]),
                                     title="Settling Down at Infinity")
                st.plotly_chart(fig_ha, use_container_width=True)

        else:
            with col_a1:
                st.markdown("### Oblique / Slant Asymptote (OA)")
                st.write("**Geometric Meaning:** A diagonal 'ramp' the function rides towards infinity.")

                st.markdown("#### How to find it:")
                st.info(
                    "Occurs ONLY when the Numerator's degree is **exactly ONE more** than the Denominator's degree ($N = D + 1$).\n\nUse **Polynomial Long Division**. The quotient (ignoring the remainder) is the equation of the OA.")

                st.markdown("**Example ($N=2, D=1$):**")
                st.latex(r"f(x) = \frac{x^2 + 1}{x} \implies f(x) = x + \frac{1}{x}")
                st.write("As $x \\to \infty$, the remainder $1/x \\to 0$.")
                st.write("The quotient $\implies \mathbf{y = x}$ is the Oblique Asymptote.")

            with col_a2:
                x_oa = np.linspace(-10, 10, 400)
                y_oa = (x_oa ** 2 + 1) / x_oa
                y_oa[np.abs(x_oa) < 0.5] = np.nan  # 在 x=0 处断开 VA

                fig_oa = go.Figure()
                fig_oa.add_trace(go.Scatter(x=x_oa, y=y_oa, name="f(x)", line=dict(color='#FFA15A', width=3)))
                # 画出斜渐近线 y = x
                fig_oa.add_trace(go.Scatter(x=x_oa, y=x_oa, name="y = x", line=dict(color='red', dash='dash')))

                fig_oa.update_layout(template="plotly_dark", height=350, yaxis=dict(range=[-10, 10]),
                                     title="Riding the Slant to Infinity")
                st.plotly_chart(fig_oa, use_container_width=True)
    # ==============================================================================
    # TAB 7: CONTINUITY & DISCONTINUITIES (连续性与间断点)
    # ==============================================================================
    with limit_tabs[6]:  # 请根据你的 tabs 列表修改这里的索引号
        st.subheader("Continuity of a Function")
        st.write(
            "Before a function can be continuous, its limit must exist. Let's see how limits build the foundation of a 'smooth' curve.")

        col_c1, col_c2 = st.columns(2)

        with col_c1:
            st.markdown("### Step 1: When does a Limit Exist?")
            st.write(
                "For a limit to exist at $x=c$, the 'left path' and the 'right path' must meet at the exact same destination.")
            st.latex(r"\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L")
            st.info("If they don't meet, the limit **does not exist (DNE)**.")

        with col_c2:
            st.markdown("### Step 2: The 3 Pillars of Continuity")
            st.write("A function is continuous at $x=c$ if and only if it passes all three strict checks:")
            st.markdown("""
            1. $f(c)$ is **defined** (The point exists).
            2. $\lim_{x \to c} f(x)$ **exists** (The left and right paths meet).
            3. $\lim_{x \to c} f(x) = f(c)$ (The paths meet exactly at the point).
            """)

        st.divider()

        # ---------------- 间断点探测器 ----------------
        st.markdown("### The Discontinuity Explorer (When the Bridge Breaks)")
        st.write("Select a type of discontinuity to see which 'pillar' of continuity failed.")

        disc_type = st.radio(
            "Select Discontinuity Type:",
            ["1. Removable (Hole)", "2. Jump (Step)", "3. Infinite (Asymptote)"],
            horizontal=True
        )

        col_plot, col_text = st.columns([1.5, 1])

        with col_plot:
            fig_disc = go.Figure()

            if "Removable" in disc_type:
                # 制造一个可去间断点 (x=2 处有个洞，但被错误地填在了别处)
                x_val = np.linspace(0, 4, 100)
                y_val = -(x_val - 2) ** 2 + 4

                # 画正常的曲线
                fig_disc.add_trace(
                    go.Scatter(x=x_val, y=y_val, mode='lines', line=dict(color='#00CC96', width=3), name="Curve"))
                # 画出空心洞 (Limit exists)
                fig_disc.add_trace(go.Scatter(x=[2], y=[4], mode='markers',
                                              marker=dict(symbol='circle-open', size=12, color='white', line_width=2),
                                              name="Hole"))
                # 画出孤立的实心点 (f(c) is defined elsewhere)
                fig_disc.add_trace(
                    go.Scatter(x=[2], y=[2], mode='markers', marker=dict(size=10, color='#EF553B'), name="f(2) = 2"))

                fig_disc.update_layout(title="Removable Discontinuity (The Misplaced Brick)", yaxis=dict(range=[0, 5]))

            elif "Jump" in disc_type:
                # 制造一个跳跃间断点 (左极限 != 右极限)
                x_left = np.linspace(0, 2, 50)
                y_left = x_left + 1

                x_right = np.linspace(2, 4, 50)
                y_right = -x_right + 2

                fig_disc.add_trace(
                    go.Scatter(x=x_left, y=y_left, mode='lines', line=dict(color='#AB63FA', width=3), name="Left Path"))
                fig_disc.add_trace(
                    go.Scatter(x=[2], y=[3], mode='markers', marker=dict(symbol='circle', size=10, color='#AB63FA'),
                               name="f(2) = 3"))

                fig_disc.add_trace(go.Scatter(x=x_right, y=y_right, mode='lines', line=dict(color='#FFA15A', width=3),
                                              name="Right Path"))
                fig_disc.add_trace(go.Scatter(x=[2], y=[0], mode='markers',
                                              marker=dict(symbol='circle-open', size=12, color='white',
                                                          line=dict(color='#FFA15A', width=2)), name="Open Hole"))

                fig_disc.update_layout(title="Jump Discontinuity (The Broken Bridge)", yaxis=dict(range=[-3, 4]))

            elif "Infinite" in disc_type:
                # 制造无穷间断点 (极限奔向无穷)
                x_inf = np.linspace(0, 4, 200)
                y_inf = 1 / (x_inf - 2) ** 2
                y_inf[np.abs(x_inf - 2) < 0.05] = np.nan  # 在 x=2 处切断，防止连线

                fig_disc.add_trace(go.Scatter(x=x_inf, y=y_inf, mode='lines', line=dict(color='#EF553B', width=3),
                                              name="f(x) = 1/(x-2)²"))
                fig_disc.add_vline(x=2, line_dash="dash", line_color="white", annotation_text="x = 2")

                fig_disc.update_layout(title="Infinite Discontinuity (The Volcano)", yaxis=dict(range=[-1, 20]))

            fig_disc.update_layout(template="plotly_dark", height=400, xaxis_title="x", yaxis_title="f(x)")
            st.plotly_chart(fig_disc, use_container_width=True)

        with col_text:
            if "Removable" in disc_type:
                st.error("❌ Fails Condition 3")
                st.markdown("""
                **What happened?**
                The limit exists (both sides approach $y=4$). The function is defined ($f(2) = 2$). 
                But **they don't match**. 

                It's like building a bridge perfectly, but dropping the final brick in the river. 
                *You can 'remove' this discontinuity simply by redefining $f(2) = 4$.*
                """)
            elif "Jump" in disc_type:
                st.error("❌ Fails Condition 2")
                st.markdown("""
                **What happened?**
                The left limit approaches $y=3$, but the right limit approaches $y=0$. 
                Because Left $\\neq$ Right, **the overall limit DOES NOT EXIST**.

                This often happens in piecewise functions or absolute value fractions like $\\frac{|x|}{x}$.
                """)
            elif "Infinite" in disc_type:
                st.error("❌ Fails Conditions 1 & 2")
                st.markdown("""
                **What happened?**
                The function shoots to infinity. $f(2)$ is a division by zero (undefined), and the limit is infinity (which technically means it doesn't exist as a real number).

                This forms a **Vertical Asymptote**.
                """)
            # ==============================================================================
            # TAB 8: THE FRACTAL FRONTIER (The Ultimate Monsters)
            # ==============================================================================
            with limit_tabs[7]:  # Adjust the index based on your actual tabs array
                st.subheader("8. The Fractal Frontier: Monsters of Continuity")

                st.markdown("""
                ### 🕵️‍♂️ The Great Mathematical Illusion
                Up until the late 1800s, almost all mathematicians believed in a simple intuition: 
                **"If a curve is continuous (unbroken), it must eventually look smooth if you zoom in enough."** Think about a circle or a wave. If you zoom in on the edge, it looks like a flat, straight line. If it looks like a straight line, you can balance a tangent line on it, which means we can find its **Slope (Derivative)**. 

                Sure, a function like $y = |x|$ has *one* sharp corner where a tangent line fails. But surely, a continuous line can't be made of *only* corners, right?

                **Wrong. Prepare to meet the mathematical monsters that broke Calculus.**
                """)

                st.divider()

                # ------------------- The Monster Gallery -------------------
                st.markdown("### 👾 The Monster Gallery")
                st.write(
                    "Each of these four monsters passes our '3 Pillars of Continuity' test perfectly—they are completely unbroken. Yet, they cruelly reject any attempt to draw a smooth tangent line.")
                st.warning("""
                        **Mathematical Note:** While the **Weierstrass Function** is a strict function ($y=f(x)$), 
                        objects like the **Koch Snowflake** are geometric curves. Both, however, are created 
                        by the same mechanism: **The Limit of an Infinite Process.**
                        """)
                frac_tabs = st.tabs([
                    "1. Weierstrass (Algebra)",
                    "2. Koch Snowflake (Geometry)",
                    "3. Sierpiński (Nothingness)",
                    "4. Coastline Paradox (Reality)"
                ])

                with frac_tabs[0]:
                    col_w1, col_w2 = st.columns([1, 1.2])
                    with col_w1:
                        st.markdown("#### The Weierstrass Function (1872)")
                        st.write(
                            "Discovered by Karl Weierstrass, this was the first function to prove the illusion wrong using pure algebra.")
                        st.latex(r"f(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)")
                        st.write(
                            "**Why is it continuous?** It is built by adding infinitely many smooth cosine waves together. The bridge never breaks.")
                        st.write(
                            "**Why is it NOT differentiable?** As $n \\to \\infty$, the waves get shorter but vibrate *infinitely faster*. The curve becomes covered in infinitely dense, microscopic spikes. You cannot balance a flat tangent line on infinite vibration.")

                    with col_w2:
                        iterations = st.slider("Add layers of limits (n):", min_value=1, max_value=20, value=3, step=1)

                        x_weier = np.linspace(-2, 2, 2000)
                        y_weier = np.zeros_like(x_weier)
                        a, b = 0.5, 3.0

                        for n in range(iterations):
                            y_weier += (a ** n) * np.cos((b ** n) * np.pi * x_weier)

                        fig_weier = go.Figure()
                        fig_weier.add_trace(go.Scatter(x=x_weier, y=y_weier, line=dict(color='#00CC96', width=1.5)))

                        fig_weier.update_layout(
                            title=f"Weierstrass Function ({iterations} iterations)",
                            template="plotly_dark", height=350, margin=dict(l=20, r=20, t=40, b=20)
                        )
                        st.plotly_chart(fig_weier, use_container_width=True)

                with frac_tabs[1]:
                    col_k1, col_k2 = st.columns([1, 1])
                    with col_k1:
                        st.markdown("#### The Koch Snowflake (1904)")
                        st.write(
                            "Take an equilateral triangle. Break every straight line into 3 segments, erase the middle, and build a smaller 'tent' pointing outward. **Repeat infinitely.**")
                        st.write(
                            "Every iteration replaces smooth straight lines with sharp 'V' corners. In the limit, **zero straight lines remain**. Every single point is a sharp corner.")
                        st.error(
                            "🔥 **The Infinity Paradox:** The snowflake is entirely trapped inside a finite circle (**Finite Area**), but its boundary grows by 4/3 every step. In the limit, its **Perimeter is INFINITE**!")
                    with col_k2:
                        st.markdown("*(Visualizing the finite area with an infinite perimeter)*")
                        st.image(
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/KochFlake.svg/500px-KochFlake.svg.png",
                            caption="Koch Snowflake Iterations")

                with frac_tabs[2]:
                    col_s1, col_s2 = st.columns([1, 1])
                    with col_s1:
                        st.markdown("#### The Sierpiński Triangle (1915)")
                        st.write(
                            "Start with a solid triangle. Cut out the middle upside-down triangle. You now have 3 smaller solid triangles. Cut out their middles. **Repeat infinitely.**")
                        st.error(
                            "🌌 **The Paradox of Nothingness:** Unlike the Koch Snowflake that grows outward, this monster destroys itself from the inside. In the limit, you have removed so much that its **Area is strictly ZERO**. Yet, the total length of the web of lines left behind is **INFINITE**. It is a continuous net made of nothing.")
                    with col_s2:
                        st.markdown("*(Visualizing the area vanishing to zero while borders go to infinity)*")
                        st.image(
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Sierpinski_triangle_evolution.svg/600px-Sierpinski_triangle_evolution.svg.png",
                            caption="Sierpiński Triangle Evolution")

                with frac_tabs[3]:
                    col_c1, col_c2 = st.columns([1, 1])
                    with col_c1:
                        st.markdown("#### The Coastline Paradox (1967)")
                        st.write(
                            "You might think these monsters only exist on a mathematician's scratchpad. But in 1967, Benoit Mandelbrot looked at a map and asked: **How long is the coast of Britain?**")
                        st.write("""
                        * Measure it with a **100km** ruler: You miss the bays, getting a short length.
                        * Measure it with a **1km** ruler: You trace more jagged edges, the length increases.
                        * Measure it with an **atomic** ruler: The length approaches **infinity**.
                        """)
                        st.write(
                            "Nature doesn't build in straight lines. Coastlines, clouds, and blood vessels are all real-world fractals—continuous, but infinitely jagged.")

                        st.info(
                            "📄 **Want to blow your mind?** Read Benoit Mandelbrot's original, highly readable 1967 paper published in *Science*: [How Long Is the Coast of Britain? Statistical Self-Similarity and Fractional Dimension](https://en.wikipedia.org/wiki/How_Long_Is_the_Coast_of_Britain%3F_Statistical_Self-Similarity_and_Fractional_Dimension)")

                    with col_c2:
                        st.image(
                            "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Britain-fractal-coastline-combined.jpg/600px-Britain-fractal-coastline-combined.jpg",
                            caption="The Coastline Paradox in action")

                st.divider()

                # ------------------- 深层拓展与结语 -------------------
                st.markdown("### 🍿 Escaping to the Fractional Dimension")
                st.write(
                    "Because these monsters are infinitely jagged, they occupy *more* space than a 1D line, but *less* space than a 2D solid shape. They live in the **decimals between dimensions** (1.x D).")

                # =====================================================================
                # 新增模块：用 st.expander 隐藏硬核推导，不破坏原有界面的清爽
                # =====================================================================
                with st.expander("🧮 Deep Dive: How do Limits calculate a Dimension? (The Math)", expanded=False):
                    st.markdown("""
                    You might be wondering: How can a dimension be a decimal? And more importantly, **where does the Limit come in?**

                    To understand this, we must redefine how we calculate dimensions using the concept of **Scaling**. Let's see what happens when we scale an object up by a factor of $S$ (let's say, scale by 3):

                    * **1D (Line):** Scale its length by 3, and you get exactly **3** copies of the original line. ($3 = 3^1$)
                    * **2D (Square):** Scale its sides by 3, and you get exactly **9** copies of the original square. ($9 = 3^2$)
                    * **3D (Cube):** Scale its edges by 3, and you get exactly **27** copies of the original cube. ($27 = 3^3$)

                    Notice the pattern? $\\text{Number of Copies} = \\text{Scale}^{\\text{Dimension}}$. 
                    Using logarithms, we can flip this to solve for the Dimension ($D$):
                    $$D = \\frac{\\log(\\text{Copies})}{\\log(\\text{Scale})}$$

                    #### The Koch Snowflake Dimension
                    Now apply this to the Koch Snowflake. Every time you zoom in (scale) by a factor of **3**, the fractal doesn't give you 3 copies—it produces exactly **4** segments. Plug this into our formula:
                    $$D = \\frac{\\log(4)}{\\log(3)} \\approx 1.2618$$
                    It is strictly greater than 1, but less than 2!

                    #### The Ultimate Limit: Box-Counting Dimension
                    For wild, real-world fractals like coastlines, we can't just count perfectly symmetrical copies. Instead, mathematicians place a grid of tiny boxes (with side length $\\epsilon$) over the shape and count how many boxes ($N$) contain a piece of the curve.

                    To find the *exact*, true dimension, we cannot use finite boxes. We must shrink the boxes until they are infinitely small. This requires our ultimate mathematical tool—**The Limit**:

                    $$D = \\lim_{\\epsilon \\to 0} \\frac{\\log(N(\\epsilon))}{\\log(1/\\epsilon)}$$

                    **Conclusion:** Limits are not just for finding points on a graph. They are the only mathematical tool powerful enough to define the fundamental geometry of nature itself.
                    """)
                # =====================================================================

                # 原有的视频与总结代码（完全未改动）
                col_vid, col_text = st.columns([1.5, 1])
                with col_vid:
                    # 3B1B 神级视频嵌入
                    st.video("https://www.youtube.com/watch?v=gB9n2gHsHN4")
                with col_text:
                    st.write(
                        "👉 **Highly Recommended:** Watch this masterpiece by *3Blue1Brown* to visualize how limits create fractional dimensions. It is the absolute perfect visual conclusion to our study of limits.")

                    st.success("""
                    🌉 **The Final Bridge to Chapter II**

                    We have successfully used **Limits** to define **Continuity**. Continuity guarantees that a function has a connected **Position** without any gaps. 

                    But Fractals reveal a critical limitation: **Position $\\neq$ Direction.** A curve can be perfectly continuous, yet have no defined slope at any point.

                    In physics and engineering, knowing *where* a particle is located is useless if we cannot calculate *how fast* it is changing. To study motion, we must filter out these jagged functions and study curves that are strictly **'Smooth'**.

                    How do we mathematically measure 'Smoothness'? We don't need new math—we just need to apply our ultimate tool, the **Limit**, to a completely new object: **The Rate of Change**.
                    **Welcome to Chapter II: Differentiation.**
                    """)

# ==========================================
# Chapter II: Differentiation (The Motion) - 第二章：微分
# ==========================================

# 假设这是你的第二章渲染函数
def render_topic_differentiation():
    st.header("📈 Chapter II: Differentiation (The Science of Change)")

    # 定义第二章的 Tabs
    diff_tabs = st.tabs([
        "1. Introduction",
        "2. Geometric Insights ",  # <--- 你的新 Tab
        "3. The Rules of Calculus",
        "4. Calculus: Binomial Theorem to Taylor series",
        "5. 🌱 The Shapes of Nature: Exponentials, Logs, and Waves",
        "6. ⚔️ The Training Ground: Applying Your Knowledge",
        "7. 🎭 The Two Faces of Curves: Implicit vs. Parametric"
    ])

    # ==============================================================================
    # TAB 1: FIRST PRINCIPLES & THE CONTINUITY RECAP
    # ==============================================================================
    with diff_tabs[0]:
        # --- Part 1: The Recap - Why Chapter I isn't enough ---
        st.subheader("🧐 Recap: The " + r"$|x|$" + " Warning")

        col_recap_text, col_recap_viz = st.columns([1.2, 1])
        with col_recap_text:
            st.write("""
            In Chapter I, we learned about **Continuity** (being connected). It's a necessary condition for smoothness, but it's not enough.

            Look at the absolute value function $f(x) = |x|$.
            * **Is it continuous at x=0?** Yes. You can draw it without lifting your pen.
            * **Is it "smooth" at x=0?** No. It has a sharp corner.

            If you approach $x=0$ from the left, the slope is **-1**. From the right, the slope is **+1**. They don't agree. Therefore, the derivative (slope) does not exist at the corner.
            """)
            st.warning(
                "👉 **Golden Rule:** Differentiability implies Continuity, but Continuity DOES NOT imply Differentiability.")

        with col_recap_viz:
            # 绘制 y=|x| 的示意图
            x_abs = np.linspace(-2, 2, 200)
            fig_abs = go.Figure()
            fig_abs.add_trace(
                go.Scatter(x=x_abs, y=np.abs(x_abs), mode='lines', name='y=|x|', line=dict(color='#FF4B4B', width=3)))
            # 标记尖角
            fig_abs.add_trace(go.Scatter(x=[0], y=[0], mode='markers',
                                         marker=dict(color='yellow', size=12, line=dict(width=2, color='red')),
                                         name='Sharp Corner (Not Differentiable)'))
            fig_abs.update_layout(template="plotly_dark", height=300, margin=dict(t=30, b=20),
                                  title="Continuous but NOT Differentiable at x=0")
            st.plotly_chart(fig_abs, use_container_width=True)

        st.divider()

        # --- Part 2: First Principles - The Solution ---
        st.subheader("🔬 The " + r"$0/0$" + " Hack: Newton's First Principles")
        st.write("""
        If a curve is smooth, how do we find its slope at a single point?
        Standard slope formula: $m = \\frac{y_2 - y_1}{x_2 - x_1}$.
        At a single instant, $x_2 = x_1$ and $y_2 = y_1$, so we get $\\frac{0}{0}$. A disaster.

        **Newton's Solution:** Don't calculate at *one* point. Calculate the average slope between *two* points, and use a **Limit** to crush the distance between them to zero.
        """)

        # 核心公式
        st.latex(r"\text{Derivative } f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")

        # --- Part 3: The Interactive Visualization (Secant to Tangent) ---
        st.info(
            "🎛️ **Interactive Lab:** We want to find the slope of $y=x^2$ at the point $P(1,1)$. Drag the slider $h$ towards 0 from either side. Watch the red **Secant Line** transform into the green **Tangent Line**.")

        # 滑块：h 是两个点之间的水平距离。允许负值！
        # 初始值设为 1.0，让用户有操作空间
        h = st.slider("Distance h (from P to Q):", min_value=-1.5, max_value=1.5, value=1.0, step=0.01)

        # 为了防止数学除零错误，如果 h 恰好是 0，我们用一个极小值代替用于计算显示
        h_calc = h if abs(h) > 1e-5 else 1e-5

        # 定义函数和点
        def f_main(x): return x ** 2

        x_p, y_p = 1.0, f_main(1.0)  # 固定点 P (1, 1)
        x_q, y_q = x_p + h_calc, f_main(x_p + h_calc)  # 移动点 Q

        # 计算割线斜率
        slope_secant = (y_q - y_p) / (x_q - x_p)
        # 我们知道 x^2 在 x=1 处的真实导数是 2
        true_derivative = 2.0

        # 绘图准备
        x_plot = np.linspace(-0.5, 2.5, 200)
        fig_first = go.Figure()

        # 1. 绘制主曲线 y=x^2
        fig_first.add_trace(go.Scatter(x=x_plot, y=f_main(x_plot), mode='lines', name='f(x) = x²',
                                       line=dict(color='royalblue', width=3)))

        # 2. 绘制割线/切线
        # 根据 h 的大小决定线的颜色和名字，提供视觉反馈
        is_close = abs(h) < 0.1
        line_color = '#00CC96' if is_close else '#FF4B4B'  # 绿色代表接近切线，红色代表割线
        line_name = 'Tangent Line (Approx)' if is_close else 'Secant Line'
        line_width = 3 if is_close else 2
        line_dash = 'solid' if is_close else 'dashdot'

        # 割线方程: y - y_p = m * (x - x_p)
        y_secant_line = slope_secant * (x_plot - x_p) + y_p
        fig_first.add_trace(go.Scatter(x=x_plot, y=y_secant_line, mode='lines', name=line_name,
                                       line=dict(color=line_color, width=line_width, dash=line_dash)))

        # 3. 绘制点 P (固定) 和 Q (移动)
        fig_first.add_trace(
            go.Scatter(x=[x_p], y=[y_p], mode='markers+text', text=['P (Fixed)'], textposition="bottom right",
                       marker=dict(size=12, color='white', line=dict(width=2, color='blue')), name='Point P'))
        fig_first.add_trace(
            go.Scatter(x=[x_q], y=[y_q], mode='markers+text', text=['Q (Moving)'], textposition="top left",
                       marker=dict(size=10, color=line_color), name='Point Q'))

        # 锁定坐标轴，防止画面抖动
        fig_first.update_layout(
            title=dict(text=f"Secant Slope: {slope_secant:.4f}  →  Target Derivative: {true_derivative}",
                       font=dict(size=18)),
            template="plotly_dark", height=500,
            xaxis=dict(range=[-0.5, 2.5], title="x"),
            yaxis=dict(range=[-1, 6], title="y"),
            hovermode="x unified"
        )
        st.plotly_chart(fig_first, use_container_width=True)

        # 成功提示
        if is_close:
            st.success(
                f"🎯 **Bulls-eye!** As $h$ becomes tiny, the secant line balances perfectly on point P. The slope settles at exactly **{true_derivative}**. You have just visualized a derivative!")

        st.divider()

        # ==============================================================================
        # PART 4: THE PHYSICS CONNECTION (s -> v -> a) - NEWLY ADDED
        # ==============================================================================
        st.subheader("🏎️ From Math to Physics: Form 4 Linear Motion")

        col_phys_text, col_phys_img = st.columns([1.5, 1])
        with col_phys_text:
            st.write("""
            Let's connect this mathematical slope to something you already know from **Form 4 Physics**.
            * **Displacement ($s$):** Your position over time.
            * **Velocity ($v$):** The rate of change of displacement. (The **Derivative** of $s$)
            * **Acceleration ($a$):** The rate of change of velocity. (The **Derivative** of $v$)

            When you found the slope of the tangent line above, you were actually calculating the **Instantaneous Velocity**.
            """)

        with col_phys_img:
            # 🖼️ 【图片占位符】你可以放一张物理学里位移、速度、加速度关系的课本图
            # 如果你有本地图片，可以改成 st.image("images/your_physics_image.png")
            st.image(
                "linearmotiongraph.png",
                caption="Physics Motion Concepts: s, v, a", use_container_width=True)

        st.info(
            "🧪 **Interactive Physics Lab:** Drag the time slider below. Watch how the **slope (steepness)** of the top graph perfectly dictates the **height (value)** of the graph directly below it.")

        # 1. 交互滑块：时间 t (为了不和上面的 h 冲突，这里用 t_current)
        t_current = st.slider("Time (t) in seconds:", min_value=0.0, max_value=4.0, value=2.0, step=0.1)

        # 2. 定义物理量: s(t) = t^2, v(t) = 2t, a(t) = 2
        t_range = np.linspace(0, 4, 200)
        s_data = t_range ** 2
        v_data = 2 * t_range
        a_data = np.full_like(t_range, 2)

        s_now = t_current ** 2
        v_now = 2 * t_current
        a_now = 2.0

        # 3. 创建 1行3列 的并排子图 (形似三个正方形)
        from plotly.subplots import make_subplots
        fig_motion = make_subplots(
            rows=1, cols=3,
            subplot_titles=(f"1️⃣ s(t)=t² | Pos: {s_now:.1f} m",
                            f"2️⃣ v(t)=2t | Vel: {v_now:.1f} m/s",
                            f"3️⃣ a(t)=2 | Acc: {a_now:.1f} m/s²")
        )

        # Plot 1: Displacement (s-t graph) - 第一列
        fig_motion.add_trace(go.Scatter(x=t_range, y=s_data, name='s(t)', line=dict(color='#636EFA', width=3)), row=1,
                             col=1)
        fig_motion.add_trace(go.Scatter(x=[t_current], y=[s_now], mode='markers',
                                        marker=dict(color='white', size=10, line=dict(color='#636EFA', width=2)),
                                        showlegend=False), row=1, col=1)

        # 画切线 (直观展示速度)
        tangent_x = np.linspace(max(0, t_current - 0.8), min(4, t_current + 0.8), 10)
        tangent_y = v_now * (tangent_x - t_current) + s_now
        fig_motion.add_trace(
            go.Scatter(x=tangent_x, y=tangent_y, mode='lines', line=dict(color='#00CC96', width=3, dash='dot'),
                       name='Tangent (Velocity)'), row=1, col=1)

        # Plot 2: Velocity (v-t graph) - 第二列
        fig_motion.add_trace(go.Scatter(x=t_range, y=v_data, name='v(t)', line=dict(color='#EF553B', width=3)), row=1,
                             col=2)
        fig_motion.add_trace(
            go.Scatter(x=[t_current], y=[v_now], mode='markers+text', text=[f"{v_now:.1f}"], textposition="top center",
                       marker=dict(color='#00CC96', size=12), showlegend=False), row=1, col=2)

        # Plot 3: Acceleration (a-t graph) - 第三列
        fig_motion.add_trace(go.Scatter(x=t_range, y=a_data, name='a(t)', line=dict(color='#AB63FA', width=3)), row=1,
                             col=3)
        fig_motion.add_trace(go.Scatter(x=[t_current], y=[a_now], mode='markers',
                                        marker=dict(color='white', size=10, line=dict(color='#AB63FA', width=2)),
                                        showlegend=False), row=1, col=3)

        # 布局美化与防抖动锁定
        fig_motion.update_layout(
            height=400,  # 高度从 700 调成 400，配合并排布局形成正方形视觉
            template="plotly_dark",
            hovermode="x unified",
            showlegend=False,
            margin=dict(t=60, b=20)
        )

        # 分别锁定三个图表的 X 轴和 Y 轴
        fig_motion.update_yaxes(title_text="s (m)", range=[-1, 17], row=1, col=1)
        fig_motion.update_xaxes(title_text="Time (s)", range=[0, 4], row=1, col=1)

        fig_motion.update_yaxes(title_text="v (m/s)", range=[-1, 9], row=1, col=2)
        fig_motion.update_xaxes(title_text="Time (s)", range=[0, 4], row=1, col=2)

        fig_motion.update_yaxes(title_text="a (m/s²)", range=[0, 4], row=1, col=3)
        fig_motion.update_xaxes(title_text="Time (s)", range=[0, 4], row=1, col=3)

        st.plotly_chart(fig_motion, use_container_width=True)

        # ==============================================================================
        # TAB 2: GEOMETRIC INSIGHTS (Visualizing the Proofs)
        # ==============================================================================
        with diff_tabs[1]:
            st.subheader("📐 Algebra is a Tool. Geometry is the Truth.")
            st.write("""
            We know how to calculate limits algebraically. But do we really *see* what's happening? 
            Let's forget the formulas for a moment and rediscover differentiation using pure geometric intuition.
            """)

            # --- ACT 1: THE SQUARE (x^2) ---
            st.divider()
            st.markdown("### 🟩 Act I: The Growing Square ($x^2$)")

            col_sq_text, col_sq_viz = st.columns([1, 1.5])

            with col_sq_text:
                st.write("""
                Let's stop thinking of $y=x^2$ as a parabola curve.
                Instead, think of it literally: **The Area of a Square with side length $x$.**

                What happens if we nudge the side length $x$ by a tiny amount, **$dx$**? How much does the area ($y$) change? Let's call the change **$dy$**.

                Look at the diagram. The added area has three parts:
                1.  A rectangle on the right ($x \cdot dx$)
                2.  A rectangle on the top ($x \cdot dx$)
                3.  A tiny corner piece ($dx \cdot dx$)

                In Calculus, $dx$ is infinitely small. The corner piece $(dx)^2$ is *infinitely* smaller than the strips. So we throw it away.
                """)
                st.latex(r"dy \approx x \cdot dx + x \cdot dx = 2x \cdot dx")
                st.write("""
                This means the "Exchange Rate" of area for side length is:
                """)
                st.latex(r"\frac{dy}{dx} = 2x")
                st.success(
                    "👉 **Insight:** The derivative of $x^2$ is $2x$ because a square has **2** sides that grow.")

            with col_sq_viz:
                # 交互式正方形面积演示
                x_val = st.slider("Side length (x):", 1.0, 5.0, 3.0, key="sq_x")
                dx_val = st.slider("Nudge amount (dx):", 0.1, 1.0, 0.5, key="sq_dx")  # dx 故意设大一点以便可视化

                fig_sq = go.Figure()

                # 1. 原始正方形 (蓝色)
                fig_sq.add_shape(type="rect", x0=0, y0=0, x1=x_val, y1=x_val,
                                 line=dict(color="royalblue", width=2), fillcolor="rgba(65, 105, 225, 0.3)",
                                 layer="below")
                fig_sq.add_trace(
                    go.Scatter(x=[x_val / 2], y=[x_val / 2], text=[f"Original Area: x² = {x_val ** 2:.2f}"],
                               mode="text", showlegend=False))

                # 2. 增加的矩形条 (绿色) - dy 的主要部分
                # 右侧条
                fig_sq.add_shape(type="rect", x0=x_val, y0=0, x1=x_val + dx_val, y1=x_val,
                                 line=dict(color="green", width=0), fillcolor="rgba(0, 204, 150, 0.6)", layer="below")
                # 顶部条
                fig_sq.add_shape(type="rect", x0=0, y0=x_val, x1=x_val, y1=x_val + dx_val,
                                 line=dict(color="green", width=0), fillcolor="rgba(0, 204, 150, 0.6)", layer="below")

                # 3. 微小的角块 (红色) - 被忽略的 dx^2
                fig_sq.add_shape(type="rect", x0=x_val, y0=x_val, x1=x_val + dx_val, y1=x_val + dx_val,
                                 line=dict(color="red", width=1), fillcolor="rgba(255, 75, 75, 0.8)", layer="below")

                # 4. 标注
                fig_sq.add_trace(go.Scatter(
                    x=[x_val / 2, x_val + dx_val / 2, x_val + dx_val / 2],
                    y=[x_val + dx_val / 2, x_val / 2, x_val + dx_val / 2],
                    text=["x·dx (Top Strip)", "x·dx (Side Strip)", "(dx)² (Tiny Corner!)"],
                    mode="text", showlegend=False
                ))

                fig_sq.update_layout(
                    template="plotly_dark", height=400, width=400,
                    xaxis=dict(range=[-0.5, 6.5], title="x", showgrid=False, zeroline=False),
                    yaxis=dict(range=[-0.5, 6.5], title="y", showgrid=False, zeroline=False),
                    margin=dict(t=20, b=20, l=20, r=20),
                    shapes=[]
                )
                # 强制设置坐标轴比例一致，保证正方形看起来是正方形
                fig_sq.update_yaxes(scaleanchor="x", scaleratio=1)

                st.plotly_chart(fig_sq, use_container_width=True)

            # --- ACT 2: THE CUBE & HIGHER POWERS ---
            st.divider()
            st.markdown("### 🧊 Act II: Cubes and Beyond ($x^3 \\to x^n$)")

            col_cube, col_nth = st.columns(2)

            with col_cube:
                st.write("#### The Volume of a Cube ($x^3$)")
                st.write("""
                Now imagine a cube with side $x$. Volume $V = x^3$.
                Imagine painting a thin layer of thickness **$dx$** onto the cube. 
                Where does the main volume increase come from?

                It comes from the **3 main faces** coating the outside.
                * Area of one face = $x^2$.
                * Volume added to one face $\\approx x^2 \\cdot dx$.

                Since there are 3 such faces growing outward:
                $$dy \\approx 3 \\cdot (x^2 \\cdot dx)$$
                $$\\frac{dy}{dx} = 3x^2$$
                *(The paint on the edges ($dx^2$) and corners ($dx^3$) is too thin to count.)*
                """)

                # --- 新增的 3D 立方体可视化 ---
                def get_box_pts(x0, y0, z0, dx_len, dy_len, dz_len):
                    # 辅助函数：生成方块的 8 个顶点用于 Mesh3d
                    return (
                        [x0, x0 + dx_len, x0 + dx_len, x0, x0, x0 + dx_len, x0 + dx_len, x0],
                        [y0, y0, y0 + dy_len, y0 + dy_len, y0, y0, y0 + dy_len, y0 + dy_len],
                        [z0, z0, z0, z0, z0 + dz_len, z0 + dz_len, z0 + dz_len, z0 + dz_len]
                    )

                fig_cube = go.Figure()

                x_c = 3.0
                dx_c = 0.4  # dx 设大一点方便看

                # 1. 核心立方体 (Original x^3) - 蓝色
                xb, yb, zb = get_box_pts(0, 0, 0, x_c, x_c, x_c)
                fig_cube.add_trace(
                    go.Mesh3d(x=xb, y=yb, z=zb, alphahull=0, color='royalblue', opacity=0.15, hoverinfo='skip'))

                # 2. 三个主要增长面 (3 * x^2 * dx) - 绿色
                # 顶部面
                xt, yt, zt = get_box_pts(0, 0, x_c, x_c, x_c, dx_c)
                fig_cube.add_trace(
                    go.Mesh3d(x=xt, y=yt, z=zt, alphahull=0, color='#00CC96', opacity=0.7, name='Top Face'))
                # 右侧面
                xr, yr, zr = get_box_pts(x_c, 0, 0, dx_c, x_c, x_c)
                fig_cube.add_trace(
                    go.Mesh3d(x=xr, y=yr, z=zr, alphahull=0, color='#00CC96', opacity=0.7, name='Right Face'))
                # 前侧面
                xf, yf, zf = get_box_pts(0, x_c, 0, x_c, dx_c, x_c)
                fig_cube.add_trace(
                    go.Mesh3d(x=xf, y=yf, z=zf, alphahull=0, color='#00CC96', opacity=0.7, name='Front Face'))

                # 3. 边缘和角落 (可忽略的高阶微小量 dx^2, dx^3) - 红色
                # 边缘 1 (上右)
                xe1, ye1, ze1 = get_box_pts(x_c, 0, x_c, dx_c, x_c, dx_c)
                fig_cube.add_trace(go.Mesh3d(x=xe1, y=ye1, z=ze1, alphahull=0, color='#FF4B4B', opacity=0.9))
                # 边缘 2 (上前)
                xe2, ye2, ze2 = get_box_pts(0, x_c, x_c, x_c, dx_c, dx_c)
                fig_cube.add_trace(go.Mesh3d(x=xe2, y=ye2, z=ze2, alphahull=0, color='#FF4B4B', opacity=0.9))
                # 边缘 3 (前右)
                xe3, ye3, ze3 = get_box_pts(x_c, x_c, 0, dx_c, dx_c, x_c)
                fig_cube.add_trace(go.Mesh3d(x=xe3, y=ye3, z=ze3, alphahull=0, color='#FF4B4B', opacity=0.9))
                # 角落 (上前右)
                xc, yc, zc = get_box_pts(x_c, x_c, x_c, dx_c, dx_c, dx_c)
                fig_cube.add_trace(go.Mesh3d(x=xc, y=yc, z=zc, alphahull=0, color='#FF4B4B', opacity=1.0))

                fig_cube.update_layout(
                    scene=dict(
                        xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
                        camera=dict(eye=dict(x=1.7, y=1.7, z=1.7))  # 调整初始视角
                    ),
                    margin=dict(l=0, r=0, b=0, t=0),
                    height=350, showlegend=False
                )
                st.plotly_chart(fig_cube, use_container_width=True)

            with col_nth:
                st.write("#### The General Power Rule ($x^n$)")
                st.write("""
                We saw $x^2 \\to 2x$ and $x^3 \\to 3x^2$. Don't just guess the pattern. **Prove it.**

                We use Algebra's "atomic weapon": The **Binomial Expansion** of $(x+dx)^n$.

                $$(x+dx)^n = x^n + n \\cdot x^{n-1}(dx) + \\frac{n(n-1)}{2}x^{n-2}(dx)^2 + \\dots$$

                The change $dy = (x+dx)^n - x^n$. When we subtract $x^n$, the first term is gone.
                $$dy = n x^{n-1}(dx) + \\text{[stuff with } (dx)^2 \\text{]}$$

                When $dx \\to 0$, all the higher powers vanish instantly. Only the survivor remains:
                """)
                st.latex(r"\frac{dy}{dx} = n x^{n-1}")
                st.success("🎉 **Q.E.D.** The Power Rule is proven for all whole numbers.")

            # --- ACT 3: SINE & COSINE (The Jewel of Geometry) ---
            st.divider()
            st.markdown("### ➰ Act III: The Trigonometry Miracle ($\\sin x \\to \\cos x$)")
            st.write("This is one of the most beautiful arguments in all of mathematics.")

            # Step 1: The Guess
            st.write("#### Step 1: The Suspicious Graph")
            st.write("Let's look at the graph of $f(x) = \\sin(x)$ and plot its slope at every point.")

            # Sin/Cos 对比图
            # 1. 扩大范围，从 -2π 到 4π，展示更多波浪起伏
            x_trig = np.linspace(-2 * np.pi, 4 * np.pi, 400)
            y_sin = np.sin(x_trig)
            y_cos = np.cos(x_trig)

            fig_trig_guess = go.Figure()
            fig_trig_guess.add_trace(
                go.Scatter(x=x_trig, y=y_sin, name='f(x) = sin(x)', line=dict(color='#636EFA', width=3)))
            fig_trig_guess.add_trace(
                go.Scatter(x=x_trig, y=y_cos, name="Slope f'(x)", line=dict(color='#EF553B', width=3, dash='dot')))

            # 2. 定制 X 轴刻度，让它显示 π 的倍数
            tick_values = [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi]
            tick_labels = ['-2π', '-π', '0', 'π', '2π', '3π', '4π']

            fig_trig_guess.update_layout(
                template="plotly_dark", height=300,
                title="The slope of sine looks strangely familiar...",
                xaxis=dict(
                    title="x (radians)",
                    tickmode='array',  # 告诉 Plotly 我们要自定义刻度
                    tickvals=tick_values,  # 真实的数值位置
                    ticktext=tick_labels,  # 屏幕上显示的文本
                    showgrid=True,
                    gridcolor='rgba(255, 255, 255, 0.1)'
                ),
                yaxis=dict(
                    showgrid=True,
                    gridcolor='rgba(255, 255, 255, 0.1)'
                ),
                hovermode="x unified"  # 加一个统一悬浮窗，体验更好
            )
            st.plotly_chart(fig_trig_guess, use_container_width=True)

            st.info(
                "🤔 It *looks* exactly like $\\cos(x)$. But is it? Or is it just an impostor function that looks similar? We need proof.")

            # Step 2: The Proof (Unit Circle)
            st.write("#### Step 2: The Unit Circle Truth")
            st.write("""
            Let's go back to the definition in the Unit Circle (Radius $R=1$).
            * $x$ is the angle (and arc length).
            * **$\\sin(x)$ is the vertical height.**

            Let's nudge the angle $x$ by a tiny amount **$dx$**.
            Look at the diagram below. We zoom in infinitely close to the point $P$ on the circle.
            """)

            col_uc_text, col_uc_viz = st.columns([1, 1.8])

            with col_uc_text:
                st.markdown("""
                **The Magic of the Tiny Triangle:**

                1.  The tiny arc length is **$dx$**. Because it's infinitely small, it's basically a straight line (the hypotenuse of the tiny triangle).
                2.  The change in height is **$d(\\sin x)$** (the vertical side of the tiny triangle).
                3.  **Crucial Geometry:** The tiny triangle is a perfect mini-replica of the big triangle, but **rotated by 90°**.

                In the tiny triangle:
                $$\\sin(\\text{tiny angle}) = \\frac{\\text{Opposite}}{\\text{Hypotenuse}} = \\frac{d(\\sin x)}{dx}$$

                Because of the 90° rotation, the "Opposite" side of the tiny triangle corresponds to the "Adjacent" side of the big triangle!

                In the big triangle, the Adjacent side is **$\\cos(x)$**.

                Therefore:
                $$\\frac{d(\\sin x)}{dx} = \\cos(x)$$
                """)
                st.success(
                    "🤯 **Mind Blown:** We found the derivative without a single limit calculation, just by looking at similar triangles!")

            with col_uc_viz:
                # 单位圆几何证明可视化
                angle_base = np.pi / 3  # 基础角度 60度
                d_angle = 0.15  # dx，用于可视化演示

                # 大三角形坐标
                p_x, p_y = np.cos(angle_base), np.sin(angle_base)

                # 小三角形坐标 (近似)
                q_x, q_y = np.cos(angle_base + d_angle), np.sin(angle_base + d_angle)
                # 小三角形的第三个顶点 (用于构成直角)
                corner_x, corner_y = q_x, p_y

                fig_uc = go.Figure()

                # 1. 画单位圆弧
                theta = np.linspace(0, np.pi / 2 + 0.2, 100)
                fig_uc.add_trace(
                    go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='gray', dash='dash'),
                               name='Unit Circle'))

                # 2. 画大三角形 (基准)
                fig_uc.add_trace(
                    go.Scatter(x=[0, p_x, p_x, 0], y=[0, 0, p_y, 0], fill='toself', fillcolor='rgba(99, 110, 250, 0.2)',
                               line=dict(color='#636EFA', width=2), name='Big Triangle'))
                # 标注 cos(x) 和 sin(x)
                fig_uc.add_annotation(x=p_x / 2, y=0, text="cos(x)", yshift=-15, showarrow=False,
                                      font=dict(color='#636EFA'))
                fig_uc.add_annotation(x=p_x, y=p_y / 2, text="sin(x)", xshift=15, showarrow=False,
                                      font=dict(color='#636EFA'))

                # 3. 画微小三角形 (关键！)
                # Hypotenuse (dx)
                fig_uc.add_trace(
                    go.Scatter(x=[p_x, q_x], y=[p_y, q_y], mode='lines', line=dict(color='#00CC96', width=4),
                               name='dx (Arc)'))
                # Vertical side (d(sin x))
                fig_uc.add_trace(
                    go.Scatter(x=[q_x, corner_x], y=[q_y, corner_y], mode='lines', line=dict(color='#EF553B', width=4),
                               name='d(sin x)'))
                # Horizontal side (修好了丢失的一边：从 white 改为 gray)
                fig_uc.add_trace(
                    go.Scatter(x=[p_x, corner_x], y=[p_y, corner_y], mode='lines', line=dict(color='gray', width=2)))

                # 4. 标注微小量
                fig_uc.add_annotation(x=(p_x + q_x) / 2, y=(p_y + q_y) / 2, text="dx", xshift=15, yshift=15,
                                      showarrow=False, font=dict(color='#00CC96', size=14, weight="bold"))
                fig_uc.add_annotation(x=q_x, y=(p_y + q_y) / 2, text="d(sin x)", xshift=25, showarrow=False,
                                      font=dict(color='#EF553B', size=14))

                # 5. 画半径线指向 P (从 white 改为 gray)
                fig_uc.add_trace(go.Scatter(x=[0, p_x], y=[0, p_y], mode='lines', line=dict(color='gray', width=2)))

                # 布局设置，聚焦在第一象限并保持比例
                fig_uc.update_layout(
                    template="plotly_dark", height=450,
                    xaxis=dict(range=[-0.1, 1.2], showgrid=False, zeroline=False, visible=False),
                    yaxis=dict(range=[-0.1, 1.2], showgrid=False, zeroline=False, visible=False),
                    margin=dict(t=20, b=20, l=20, r=20),
                    showlegend=False
                )
                fig_uc.update_yaxes(scaleanchor="x", scaleratio=1)

                st.plotly_chart(fig_uc, use_container_width=True)
                st.caption(
                    "Diagram: Zooming in on the unit circle. The tiny triangle (green/red/gray) is similar to the big triangle (blue), but rotated 90°.")

    # ==============================================================================
    # TAB 3: THE RULES OF CALCULUS (Product, Quotient, Chain)
    # ==============================================================================
    with diff_tabs[2]:
        st.subheader("🛠️ The Toolkit: How to Combine Functions")
        st.write("""
        We know the basic derivatives ($x^2, \sin x, e^x$). But the real world is messy. 
        What happens when functions multiply, divide, or nest inside each other? 
        Let's build our ultimate toolkit.
        """)

        # ---------------------------------------------------------
        # 1. THE PRODUCT RULE
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 1️⃣ The Product Rule ($u \cdot v$)")

        col_prod_text, col_prod_viz = st.columns([1, 1.2])

        with col_prod_text:
            st.write("""
            What is the derivative of $y = u(x) \cdot v(x)$?

            Remember the square from Act I? Let's use the exact same logic, but for a **Rectangle**.
            * The width is $u$ and the height is $v$. Area = $u \cdot v$.

            If we nudge $x$ by $dx$, the width grows by $du$, and the height grows by $dv$.
            The total new area has 3 extra pieces:
            1. The top strip: $u \cdot dv$
            2. The side strip: $v \cdot du$
            3. The tiny corner: $du \cdot dv$ (which vanishes to $0$)

            So the change in area is just the two main strips!
            """)
            st.latex(r"d(uv) = u \cdot dv + v \cdot du")
            st.latex(r"\frac{d}{dx}[u \cdot v] = u \frac{dv}{dx} + v \frac{du}{dx}")
            st.success("**Rule:** First times derivative of Second, PLUS Second times derivative of First.")

        with col_prod_viz:
            # 交互式矩形乘积法则可视化
            u_val = st.slider("Width (u):", 1.0, 5.0, 4.0, key="prod_u")
            v_val = st.slider("Height (v):", 1.0, 5.0, 2.5, key="prod_v")
            du_val = 0.8  # 固定增量用于可视化
            dv_val = 0.6

            fig_prod = go.Figure()
            # 1. Base Rectangle (u * v)
            fig_prod.add_shape(type="rect", x0=0, y0=0, x1=u_val, y1=v_val, line=dict(color="royalblue", width=2),
                               fillcolor="rgba(65, 105, 225, 0.3)")
            fig_prod.add_annotation(x=u_val / 2, y=v_val / 2, text="Area = u · v", showarrow=False,
                                    font=dict(color="royalblue", size=16))

            # 2. Side Strip (v * du)
            fig_prod.add_shape(type="rect", x0=u_val, y0=0, x1=u_val + du_val, y1=v_val,
                               line=dict(color="#00CC96", width=0), fillcolor="rgba(0, 204, 150, 0.5)")
            fig_prod.add_annotation(x=u_val + du_val / 2, y=v_val / 2, text="v · du", showarrow=False, textangle=-90,
                                    font=dict(color="#00CC96"))

            # 3. Top Strip (u * dv)
            fig_prod.add_shape(type="rect", x0=0, y0=v_val, x1=u_val, y1=v_val + dv_val,
                               line=dict(color="#FF9900", width=0), fillcolor="rgba(255, 153, 0, 0.5)")
            fig_prod.add_annotation(x=u_val / 2, y=v_val + dv_val / 2, text="u · dv", showarrow=False,
                                    font=dict(color="#FF9900"))

            # 4. Tiny Corner (du * dv)
            fig_prod.add_shape(type="rect", x0=u_val, y0=v_val, x1=u_val + du_val, y1=v_val + dv_val,
                               line=dict(color="#FF4B4B", width=1), fillcolor="rgba(255, 75, 75, 0.8)")
            fig_prod.add_annotation(x=u_val + du_val / 2, y=v_val + dv_val / 2, text="Ignore", showarrow=False,
                                    font=dict(size=10, color="white"))

            fig_prod.update_layout(
                template="plotly_dark", height=350,
                xaxis=dict(range=[-0.5, 6.5], title="Width (u)", showgrid=False, zeroline=False),
                yaxis=dict(range=[-0.5, 6.5], title="Height (v)", showgrid=False, zeroline=False),
                margin=dict(t=20, b=20, l=20, r=20),
            )
            fig_prod.update_yaxes(scaleanchor="x", scaleratio=1)
            st.plotly_chart(fig_prod, use_container_width=True)

        # ---------------------------------------------------------
        # 2. THE QUOTIENT RULE
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 2️⃣ The Quotient Rule ($u / v$)")
        st.write("How do we find the derivative of division? There are two paths to the truth.")

        tab_q1, tab_q2 = st.tabs(
            ["Path A: The Elegant Hack (Using Product Rule)", "Path B: The Classical Method (Limits)"])

        with tab_q1:
            st.write(
                "**The Hack:** We hate division. So let's turn it into multiplication and use the rule we just proved!")
            st.latex(r"\text{Let } y = \frac{u}{v}")
            st.write("Multiply both sides by $v$ to get rid of the fraction:")
            st.latex(r"u = y \cdot v")
            st.write(
                "Now, take the derivative of both sides. Since the right side is a multiplication, use the **Product Rule**!")
            st.latex(r"u' = (y' \cdot v) + (y \cdot v')")
            st.write("Our goal is to find $y'$ (the derivative of the quotient). Let's isolate $y'$:")
            st.latex(r"y' \cdot v = u' - y \cdot v'")
            st.write("But remember, $y$ is originally $u/v$. Plug that back in:")
            st.latex(r"y' \cdot v = u' - \left(\frac{u}{v}\right) v'")
            st.write("Multiply the whole equation by $v$ to clear the mini-fraction, then divide by $v^2$:")
            st.latex(r"y' = \frac{u'v - uv'}{v^2}")
            st.info(
                "💡 **Notice:** We derived the Quotient Rule without touching a single complicated limit, just by being clever with the Product Rule!")

        with tab_q2:
            st.write(
                "**The Classical Limit:** This is the traditional textbook proof. We add a 'clever zero' to make factoring possible.")
            st.latex(
                r"\frac{d}{dx} \left[\frac{u(x)}{v(x)}\right] = \lim_{h \to 0} \frac{\frac{u(x+h)}{v(x+h)} - \frac{u(x)}{v(x)}}{h}")
            st.write("Find a common denominator for the top fraction:")
            st.latex(r"= \lim_{h \to 0} \frac{u(x+h)v(x) - u(x)v(x+h)}{h \cdot v(x+h)v(x)}")
            st.write("Subtract and add $u(x)v(x)$ in the numerator (the clever trick):")
            st.latex(r"= \lim_{h \to 0} \frac{[u(x+h)v(x) - u(x)v(x)] - [u(x)v(x+h) - u(x)v(x)]}{h \cdot v(x+h)v(x)}")
            st.write("Factor out $v(x)$ and $u(x)$, apply the limit, and you get the exact same result:")
            st.latex(r"= \frac{u'v - uv'}{v^2}")

        # ---------------------------------------------------------
        # 3. THE CHAIN RULE
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 3️⃣ The Chain Rule ($f(g(x))$)")
        st.write("""
                What if functions are nested, like Matryoshka dolls? E.g., $y = \sin(x^2)$.
                A derivative is just a **Scaling Factor **. If the inner function stretches your step by $2\\times$, and the outer function compresses it by $0.5\\times$, the total effect is $2 \\times 0.5 = 1\\times$.

                Let's visualize this using number line for exactly this function:
                * **Inner Function:** $u = g(x) = x^2$ 
                * **Outer Function:** $y = f(u) = \sin(u)$
                """)

        col_chain_text, col_chain_viz = st.columns([1, 1.5])

        with col_chain_text:
            # 交互式滑动 dx，范围调小一点以保证近似计算的准确度
            dx_chain = st.slider("Step size (dx):", 0.01, 0.30, 0.10, step=0.01, key="chain_dx")

            # 我们选择 x0 = 0.8 作为起始点，因为这里的伸缩比例都是正的，便于可视化
            x0 = 0.80
            x1 = x0 + dx_chain

            # 第一层映射：u = x^2
            u0 = x0 ** 2
            u1 = x1 ** 2
            du_chain = u1 - u0
            u_prime = 2 * x0  # 导数：2x

            # 第二层映射：y = sin(u)
            y0 = np.sin(u0)
            y1 = np.sin(u1)
            dy_chain = y1 - y0
            y_prime = np.cos(u0)  # 导数：cos(u)

            st.write(f"Let's start at **$x = {x0}$** and take a small step $dx$:")

            st.markdown(f"**1. The Inner Function ($u=x^2$):**")
            st.markdown(f"The derivative is $2x$. At $x={x0}$, the stretch factor is **${u_prime:.1f}$**.")
            st.markdown(
                f"👉 $du$ ({du_chain:.3f}) is approx **${u_prime:.1f}\\times$** larger than $dx$ ({dx_chain:.3f}).")

            st.markdown(f"**2. The Outer Function ($y=\\sin(u)$):**")
            st.markdown(
                f"The derivative is $\\cos(u)$. At $u={u0:.2f}$, the stretch factor is $\\cos({u0:.2f}) \\approx$ **{y_prime:.2f}**.")
            st.markdown(
                f"👉 $dy$ ({dy_chain:.3f}) is scaled by approx **${y_prime:.2f}\\times$** from $du$ ({du_chain:.3f}).")

            st.write(f"**Total Chain Reaction:**")
            st.latex(
                f"\\frac{{dy}}{{dx}} \\approx \\frac{{{dy_chain:.3f}}}{{{dx_chain:.3f}}} \\approx {dy_chain / dx_chain:.2f}")
            st.write("Multiply the two theoretical stretch factors together:")
            st.latex(
                f"\\frac{{dy}}{{du}} \\cdot \\frac{{du}}{{dx}} = {y_prime:.2f} \\cdot {u_prime:.1f} = {y_prime * u_prime:.2f}")

        with col_chain_viz:
            # Plotly 三数轴联动图
            fig_chain = go.Figure()

            y_line_x, y_line_u, y_line_y = 3, 2, 1

            # 画基础数轴 (浅灰色)，为了适应真实数值，将 X 轴范围设为 0.4 到 1.8
            axis_range = [0.4, 1.8]
            for y_pos in [y_line_x, y_line_u, y_line_y]:
                fig_chain.add_trace(
                    go.Scatter(x=axis_range, y=[y_pos, y_pos], mode='lines', line=dict(color='gray', width=1)))

            # 1. x 轴上的区间 (dx)
            fig_chain.add_trace(go.Scatter(x=[x0, x1], y=[y_line_x, y_line_x], mode='lines+markers',
                                           line=dict(color='#636EFA', width=8), marker=dict(size=12), name='dx'))
            fig_chain.add_annotation(x=(x0 + x1) / 2, y=y_line_x + 0.15, text=f"dx = {dx_chain:.2f}", showarrow=False,
                                     font=dict(color='#636EFA', size=14))

            # 2. u 轴上的区间 (du)
            fig_chain.add_trace(go.Scatter(x=[u0, u1], y=[y_line_u, y_line_u], mode='lines+markers',
                                           line=dict(color='#00CC96', width=8), marker=dict(size=12), name='du'))
            fig_chain.add_annotation(x=(u0 + u1) / 2, y=y_line_u + 0.15,
                                     text=f"du = {du_chain:.2f} (≈ {u_prime:.1f}x stretch)",
                                     showarrow=False, font=dict(color='#00CC96', size=14))

            # 3. y 轴上的区间 (dy)
            fig_chain.add_trace(go.Scatter(x=[y0, y1], y=[y_line_y, y_line_y], mode='lines+markers',
                                           line=dict(color='#FF4B4B', width=8), marker=dict(size=12), name='dy'))
            fig_chain.add_annotation(x=(y0 + y1) / 2, y=y_line_y + 0.15,
                                     text=f"dy = {dy_chain:.2f} (≈ {y_prime:.2f}x stretch)",
                                     showarrow=False, font=dict(color='#FF4B4B', size=14))

            # 绘制映射虚线：连接起点与起点，终点与终点
            fig_chain.add_trace(go.Scatter(x=[x0, u0], y=[y_line_x, y_line_u], mode='lines',
                                           line=dict(color='white', width=1, dash='dot')))
            fig_chain.add_trace(go.Scatter(x=[x1, u1], y=[y_line_x, y_line_u], mode='lines',
                                           line=dict(color='white', width=1, dash='dot')))
            fig_chain.add_trace(go.Scatter(x=[u0, y0], y=[y_line_u, y_line_y], mode='lines',
                                           line=dict(color='white', width=1, dash='dot')))
            fig_chain.add_trace(go.Scatter(x=[u1, y1], y=[y_line_u, y_line_y], mode='lines',
                                           line=dict(color='white', width=1, dash='dot')))

            # 轴侧边标签
            fig_chain.add_annotation(x=0.45, y=y_line_x, text="x", showarrow=False, font=dict(size=18, color="white"))
            fig_chain.add_annotation(x=0.45, y=y_line_u, text="u = x²", showarrow=False,
                                     font=dict(size=18, color="white"))
            fig_chain.add_annotation(x=0.45, y=y_line_y, text="y = sin(u)", showarrow=False,
                                     font=dict(size=18, color="white"))

            fig_chain.update_layout(
                template="plotly_dark", height=400,
                xaxis=dict(visible=False, range=axis_range),  # 锁定坐标轴以防止抖动
                yaxis=dict(visible=False, range=[0.5, 3.5]),
                margin=dict(t=20, b=20, l=20, r=20),
                showlegend=False
            )
            st.plotly_chart(fig_chain, use_container_width=True)

            st.caption(
                "Look closely at the lengths of the colored bars. The blue bar ($dx$) gets stretched by a factor of 1.6 to become the green bar ($du$). But then, the green bar gets slightly compressed by a factor of 0.8 to become the red bar ($dy$).")

            # ==============================================================================
            # TAB 5: THE CALCULUS TIME MACHINE (Newton meets Taylor)
            # ==============================================================================
            with diff_tabs[3]:  # 确保这里的索引与你的Tabs数量匹配
                st.subheader("Calculus: Binomial Theorem to Taylor Series")
                st.write("""
                    This page contains one of the most beautiful connections in the history of mathematics. 
                    We will travel from a quarantine room in 1665 to a formal mathematical proof 50 years later, witnessing how algebra, geometry, and calculus are ultimately the exact same truth.
                    """)

                st.divider()


                # ------------------------------------------------------------------------------
                # ACT I: NEWTON (1665)
                # ------------------------------------------------------------------------------
                st.markdown("### 🍎 Act I: 1665 - The Quarantine Genius & The Pi Hack")
                st.write("""
                    During the Great Plague, a 23-year-old Isaac Newton discovered the **General Binomial Theorem**, allowing him to expand fractional powers into infinite series. He immediately used this to perform the greatest mathematical 'hack' of his era: calculating $\pi$.
                    """)

                col_n_alg, col_n_geo = st.columns([1, 1])
                with col_n_alg:
                    st.markdown("#### 🏹 The Algebraic Setup")
                    st.write(
                        "Newton started with a circle of radius $1/2$ centered at $(1/2, 0)$. The equation is $(x - 1/2)^2 + y^2 = (1/2)^2$. Solving for $y$ gives:")
                    st.latex(r"y = \sqrt{x - x^2}")

                    st.write("To use his new Binomial Theorem, he factored out an $x$ inside the root:")
                    st.latex(r"y = \sqrt{x(1 - x)} = x^{1/2} \cdot (1 - x)^{1/2}")

                    st.write("He then expanded the $(1 - x)^{1/2}$ part using his newly discovered algebraic patterns:")
                    st.latex(r"(1-x)^{1/2} = 1 - \frac{1}{2}x - \frac{1}{8}x^2 - \frac{1}{16}x^3 - \dots")

                    st.write(
                        "Multiplying the $x^{1/2}$ back in, he transformed the circle into a series of simple polynomials:")
                    st.latex(r"y = x^{1/2} - \frac{1}{2}x^{3/2} - \frac{1}{8}x^{5/2} - \frac{1}{16}x^{7/2} - \dots")

                with col_n_geo:
                    st.markdown("#### 📐 The Geometric Magic (Why integrate to $x=1/4$?)")
                    st.write("""
                        Newton decided to integrate this series from $x=0$ to $x=1/4$. 
                        Why $1/4$? Because of the perfect geometry it creates:
                        """)

                    st.write("**1. The Triangle:**")
                    st.write("""
                        Let the center be $C(1/2, 0)$. The point on the curve at $x=1/4$ is $P$. 
                        The height at $P$ is $y = \sqrt{1/4 - (1/4)^2} = \\frac{\sqrt{3}}{4}$. 
                        Dropping a line to $D(1/4, 0)$ forms a right triangle $\Delta CDP$.
                        * Base ($CD$) = $1/2 - 1/4 = \mathbf{1/4}$
                        * Height ($DP$) = $\mathbf{\\frac{\sqrt{3}}{4}}$
                        * **Triangle Area** = $\\frac{1}{2} \cdot \\frac{1}{4} \cdot \\frac{\sqrt{3}}{4} = \mathbf{\\frac{\sqrt{3}}{32}}$
                        """)

                    st.write("**2. The Sector:**")
                    st.write("""
                        Look at the angle $\\theta$ at the center $C$. 
                        $\cos(\\theta) = \\frac{\\text{Adjacent}}{\\text{Hypotenuse}} = \\frac{1/4}{\\text{Radius}(1/2)} = \\frac{1}{2}$. 
                        Therefore, $\\theta = \mathbf{60^\circ}$ (or $\pi/3$).
                        * The area of a $60^\circ$ sector is exactly $\\frac{1}{6}$ of the whole circle.
                        * **Sector Area** = $\\frac{1}{6} \cdot \pi R^2 = \\frac{1}{6} \pi (1/2)^2 = \mathbf{\\frac{\pi}{24}}$
                        """)

                    st.write("The algebraic integral from $0$ to $1/4$ equals the Sector Area minus the Triangle Area:")
                    st.latex(r"\text{Integral Sum} = \frac{\pi}{24} - \frac{\sqrt{3}}{32}")

                    # --- 新增：几何可视化模块 ---
                    x_circ = np.linspace(0, 0.6, 200)
                    y_circ = np.sqrt(x_circ - x_circ ** 2)
                    fig_geo = go.Figure()

                    # 画圆弧 (灰色虚线)
                    fig_geo.add_trace(go.Scatter(x=x_circ, y=y_circ, mode='lines', line=dict(color='gray', dash='dash'),
                                                 name='Circle'))

                    # 画积分面积 (绿色填充)
                    x_int = np.linspace(0, 0.25, 100)
                    y_int = np.sqrt(x_int - x_int ** 2)
                    fig_geo.add_trace(
                        go.Scatter(x=np.concatenate([x_int, [0.25, 0]]), y=np.concatenate([y_int, [0, 0]]),
                                   fill='toself', fillcolor='rgba(0, 204, 150, 0.4)', line=dict(width=0),
                                   name='Integral Area'))

                    # 画三角形 CDP (红色填充)
                    fig_geo.add_trace(go.Scatter(x=[0.5, 0.25, 0.25, 0.5], y=[0, np.sqrt(3) / 4, 0, 0],
                                                 mode='lines', fill='toself', fillcolor='rgba(239, 85, 59, 0.3)',
                                                 line=dict(color='#EF553B', width=2), name='Triangle CDP'))

                    # 标注点 C, D, P
                    fig_geo.add_trace(go.Scatter(x=[0.5, 0.25, 0.25], y=[0, 0, np.sqrt(3) / 4], mode='markers+text',
                                                 marker=dict(color='white', size=8),
                                                 text=['C(1/2, 0)', 'D(1/4, 0)', 'P(1/4, √3/4)'],
                                                 textposition=['bottom right', 'bottom left', 'top right'],
                                                 showlegend=False))

                    fig_geo.update_layout(template="plotly_dark", height=350, margin=dict(t=20, b=20, l=10, r=10),
                                          xaxis=dict(range=[-0.1, 0.7], scaleanchor="y", scaleratio=1),
                                          yaxis=dict(range=[-0.1, 0.6]), showlegend=False)
                    st.plotly_chart(fig_geo, use_container_width=True)

                # --- THE SIMULATOR ---
                st.markdown("#### 🧮 Newton's $\pi$ Simulator")
                st.write(
                    "By integrating his infinite series and setting it equal to the geometric area, Newton solved for $\pi$. Slide to see how fast it converges due to the $(1/4)^n$ shrinking factor!")

                n_terms_newton = st.slider("Number of Series Terms used:", 1, 12, 3, key="newton_terms_merged")

                def binom_coeff_final(n):
                    if n == 0: return 1.0
                    res = 1.0
                    for i in range(n):
                        res *= (0.5 - i) / (i + 1)
                    return res

                x_limit_final = 0.25
                area_calc_final = 0.0

                # --- 新增：动态公式文本生成 ---
                latex_terms = []

                for i in range(n_terms_newton):
                    coeff = binom_coeff_final(i) * ((-1) ** i)
                    power = i + 1.5
                    term = (coeff * (x_limit_final ** power)) / power
                    area_calc_final += term

                    # 将系数转化为完美分数以供显示 (例如 2/3, -1/5, -1/28...)
                    frac = Fraction(coeff / power).limit_denominator(1000)
                    num, den = abs(frac.numerator), frac.denominator
                    sign_str = "+" if frac > 0 else "-"
                    if i == 0: sign_str = ""  # 第一项前面不加符号

                    # 构造单项的 LaTeX 字符串: (例如: - \frac{1}{5}(\frac{1}{4})^{5/2} )
                    term_str = f"{sign_str} \\frac{{{num}}}{{{den}}}\\left(\\frac{{1}}{{4}}\\right)^{{{2 * i + 3}/2}}"
                    latex_terms.append(term_str)

                pi_guess_final = 24 * (area_calc_final + (np.sqrt(3) / 32))
                error_final = abs(pi_guess_final - np.pi)

                # --- 新增：展示动态算式 ---
                series_latex_str = " ".join(latex_terms)
                if n_terms_newton < 12:
                    series_latex_str += " + \dots"

                st.latex(r"\text{Area} \approx " + series_latex_str)
                st.latex(r"\pi \approx 24 \times \left( \text{Area} + \frac{\sqrt{3}}{32} \right)")

                col_sim1, col_sim2 = st.columns(2)
                with col_sim1:
                    st.metric("Newton's π Estimate", f"{pi_guess_final:.12f}")
                with col_sim2:
                    st.metric("Actual π", f"{np.pi:.12f}", delta=f"-{error_final:.12e}", delta_color="inverse")

                st.divider()
                # ------------------------------------------------------------------------------
                # ACT II: TAYLOR (1715)
                # ------------------------------------------------------------------------------
                st.markdown("### 🧬 Act II: 1715 - Brook Taylor & The Master Formula")

                col_taylor_intro, col_taylor_img = st.columns([2, 1])
                with col_taylor_intro:
                    st.write("""
                        Fifty years after Newton used algebraic patterns to expand $(1-x)^{1/2}$, English mathematician **Brook Taylor** published a generalized method. 
                        He realized you don't need to guess algebraic patterns. You can perfectly clone *any* function by extracting its "DNA"—its derivatives at a single point!
                        """)
                with col_taylor_img:
                    # 预留给泰勒肖像的位置
                    st.image("https://zh.wikipedia.org/zh-cn/%E5%B8%83%E9%B2%81%E5%85%8B%C2%B7%E6%B3%B0%E5%8B%92",
                             caption="Brook Taylor (1685 - 1731)")

                # 调整了这里的列宽比例：从 [1, 1] 改为 [1.3, 1]，给左边的长公式留出足够的显示空间
                col_taylor_proof, col_taylor_sin = st.columns([1.3, 1])

                # 调整列宽比例，给左边足够的空间
                col_taylor_proof, col_taylor_sin = st.columns([1.3, 1])

                with col_taylor_proof:
                    st.markdown("#### 🛠️ The Proof: Finding the Coefficients")
                    st.write("Suppose we want to build an infinite polynomial $P(x)$ to match a function $f(x)$:")
                    st.latex(r"P(x) = c_0 + c_1x + c_2x^2 + c_3x^3 + \dots")
                    st.write("We find the coefficients by matching their derivatives at $x=0$.")

                    st.write("**1. Match Position ($x=0$):**")
                    st.latex(r"P(0) = c_0 \implies \mathbf{c_0 = f(0)}")

                    st.write("**2. Match 1st Derivative (Slope):**")
                    # 使用 aligned 将过长的公式折叠成两行，并在等号处对齐
                    st.latex(r"""
                        \begin{aligned}
                        P'(x) &= c_1 + 2c_2x + \dots \\
                        &\implies P'(0) = c_1 \implies \mathbf{c_1 = f'(0)}
                        \end{aligned}
                    """)

                    st.write("**3. Match 2nd Derivative (Curvature):**")
                    # 修复溢出的关键：将二阶导数折叠换行显示
                    st.latex(r"""
                        \begin{aligned}
                        P''(x) &= 2c_2 + (3 \cdot 2)c_3x + \dots \\
                        &\implies P''(0) = 2c_2 \implies \mathbf{c_2 = \frac{f''(0)}{2}}
                        \end{aligned}
                    """)

                    st.write("**4. Match 3rd Derivative:**")
                    # 保持排版一致，三阶导数也折叠
                    st.latex(r"""
                        \begin{aligned}
                        P'''(x) &= (3 \cdot 2 \cdot 1)c_3 \\
                        &\implies \mathbf{c_3 = \frac{f'''(0)}{3!}}
                        \end{aligned}
                    """)

                    st.success(
                        "✨ **The Master Formula:** Taking derivatives creates a factorial ($n!$). To isolate the coefficient, we divide by $n!$.")
                    st.latex(r"\mathbf{c_n = \frac{f^{(n)}(0)}{n!}}")

                with col_taylor_sin:
                    st.markdown("#### 🌊 Applying it to $f(x) = \sin(x)$")
                    st.write("Using Taylor's formula, let's clone $\sin(x)$ by finding its derivatives at $x=0$:")

                    st.markdown("""
                        * $f(0) = \sin(0) = \mathbf{0} \implies c_0 = 0$
                        * $f'(0) = \cos(0) = \mathbf{1} \implies c_1 = 1/1! = 1$
                        * $f''(0) = -\sin(0) = \mathbf{0} \implies c_2 = 0$
                        * $f'''(0) = -\cos(0) = \mathbf{-1} \implies c_3 = -1/3!$
                        """)
                    st.latex(r"\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots")

                    terms_val_sin = st.slider("Number of non-zero terms (n):", 1, 6, 2, key="taylor_sin_n_merged")

                    x_plot_sin = np.linspace(-3 * np.pi, 3 * np.pi, 400)
                    y_target_sin = np.sin(x_plot_sin)
                    y_taylor_sin = np.zeros_like(x_plot_sin)
                    latex_str_sin = "P(x) = "

                    for n in range(terms_val_sin):
                        power = 2 * n + 1
                        coef = ((-1) ** n) / math.factorial(power)
                        y_taylor_sin += coef * (x_plot_sin ** power)

                        if n == 0:
                            latex_str_sin += "x"
                        else:
                            sign = "-" if n % 2 != 0 else "+"
                            # 修复：直接用原生字符串 (r"...") 加上变量拼接，彻底告别 f-string 大括号报错！
                            latex_str_sin += r" " + sign + r" \frac{x^{" + str(power) + r"}}{" + str(power) + r"!}"

                    fig_taylor_sin = go.Figure()
                    fig_taylor_sin.add_trace(go.Scatter(x=x_plot_sin, y=y_target_sin, mode='lines',
                                                        line=dict(color='gray', width=3, dash='dash'),
                                                        name='Target: sin(x)'))
                    fig_taylor_sin.add_trace(
                        go.Scatter(x=x_plot_sin, y=y_taylor_sin, mode='lines', line=dict(color='#00CC96', width=4),
                                   name='Taylor Clone'))

                    # 修复 2：加入 yaxis=dict(range=[-3, 3]) 锁死 Y 轴范围，防止波浪被拉平
                    fig_taylor_sin.update_layout(template="plotly_dark", height=250,
                                                 yaxis=dict(range=[-3, 3]),
                                                 margin=dict(t=10, b=10, l=10, r=10), showlegend=False)
                    st.plotly_chart(fig_taylor_sin, use_container_width=True)
                    st.latex(latex_str_sin)

                st.divider()

                # ------------------------------------------------------------------------------
                # ACT III: THE GRAND CONNECTION
                # ------------------------------------------------------------------------------
                st.markdown("### 🔗 Act III: The Grand Connection (Taylor Proves Newton)")
                st.write("""
                    In Act I, you saw Newton guess the coefficients for $(1-x)^{1/2}$ using algebraic patterns: **$1, -1/2, -1/8, -1/16$**. 

                    Now, watch what happens if we apply **Taylor's Calculus Formula** ($c_n = f^{(n)}(0) / n!$) to that exact same function $f(x) = (1-x)^{1/2}$ at $x=0$:
                    """)

                col_conn1, col_conn2 = st.columns(2)
                with col_conn1:
                    st.markdown("""
                        **1. Take Derivatives at $x=0$:**
                        * $f(0) = (1-0)^{1/2} = \mathbf{1}$
                        * $f'(0) = -\\frac{1}{2}(1-0)^{-1/2} = \mathbf{-1/2}$
                        * $f''(0) = -\\frac{1}{4}(1-0)^{-3/2} = \mathbf{-1/4}$
                        * $f'''(0) = -\\frac{3}{8}(1-0)^{-5/2} = \mathbf{-3/8}$
                        """)

                with col_conn2:
                    st.markdown("""
                        **2. Divide by $n!$ (Taylor's Rule):**
                        * $c_0 = 1 / 0! = \mathbf{1}$
                        * $c_1 = (-1/2) / 1! = \mathbf{-1/2}$
                        * $c_2 = (-1/4) / 2! = \mathbf{-1/8}$
                        * $c_3 = (-3/8) / 3! = \mathbf{-1/16}$
                        """)

                st.success(
                    "🤯 **History Connects!** The numbers are identical! Newton's 'Binomial Theorem' was actually the Taylor Series all along. Newton discovered the *what* through algebra, and 50 years later, Taylor proved the *why* through calculus.")

    # ==============================================================================
    # TAB 4: THE NATURAL CONSTANTS (Exp, Log, Trig)
    # ==============================================================================
    # 假设这段代码放在 with diff_tabs[3]: 之下
    with diff_tabs[4]:
        st.subheader("🌱 The Shapes of Nature: Exponentials, Logs, and Waves")
        st.write("""
        We've mastered polynomials ($x^2, x^3$). But nature doesn't grow in polynomials. 
        Populations multiply, temperatures decay, and pendulums swing. 
        Let's uncover the derivatives of nature's favorite functions.
        """)

        # ---------------------------------------------------------
        # ACT I: EXPONENTIALS (The 3Blue1Brown Approach)
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 🦠 Act I: Exponential Growth ($2^t$ and $e^t$)")

        col_exp_text, col_exp_viz = st.columns([1.2, 1])
        with col_exp_text:
            st.write("""
            Imagine a population of bacteria that doubles every day: $P(t) = 2^t$.
            Using First Principles, its derivative is:
            """)
            st.latex(
                r"P'(t) = \lim_{h \to 0} \frac{2^{t+h} - 2^t}{h} = 2^t \cdot \left[ \lim_{h \to 0} \frac{2^h - 1}{h} \right]")
            st.write("""
            The derivative is just $2^t$ multiplied by a **mystery constant** (which calculates to $\\approx 0.693$).
            If we used $8^t$, the mystery constant would be $\\approx 2.079$.

            Mathematicians asked: **Is there a base where this constant is exactly 1.000?** Yes, it's Euler's number: $e \\approx 2.71828$. But *why* does its derivative equal itself?

            **The Secret: The Infinite Polynomial**
            To build a function that is its own derivative, we construct an infinite series where taking the derivative just shifts every term one step to the left:
            """)
            st.latex(r"e^t = 1 + t + \frac{t^2}{2!} + \frac{t^3}{3!} + \frac{t^4}{4!} + \dots")
            st.write("Take the derivative of this entire infinite series:")
            st.latex(
                r"\frac{d}{dt}e^t = 0 + 1 + \frac{2t}{2!} + \frac{3t^2}{3!} + \dots = 1 + t + \frac{t^2}{2!} + \dots")
            st.success(
                "🤯 **Mind Blown:** The derivative recreates the EXACT same infinite series! Therefore, $\\frac{d}{dt} e^t = e^t$.")

            st.write("""
            **The Grand Finale: Unlocking 0.693 with the Chain Rule**
            Now we have our "perfect tool" ($e^t$), we can solve the $2^t$ mystery. 
            Since $2 = e^{\ln(2)}$, we can rewrite our bacteria population:
            $$2^t = (e^{\ln 2})^t = e^{(\ln 2) t}$$

            Now, apply the **Chain Rule**. The derivative of the outer function ($e^{\\text{stuff}}$) is itself, multiplied by the derivative of the inner function ($(\\ln 2) t$):
            $$\\frac{d}{dt} e^{(\ln 2) t} = e^{(\ln 2) t} \cdot \ln(2) = 2^t \cdot \ln(2)$$

            *The circle is complete:* That mystery constant $0.693...$ we calculated at the very beginning? It was exactly **$\ln(2)$** all along!
            """)

        with col_exp_viz:
            # 交互式指数函数斜率演示
            base_val = st.slider("Choose a Base (a):", min_value=1.5, max_value=4.0, value=2.0, step=0.1,
                                 key="exp_base")

            t_plot = np.linspace(-1, 2, 100)
            y_plot = base_val ** t_plot

            # 在 t=0 处的切线 (y - 1 = m * (t - 0)) -> y = m*t + 1
            # 真实的 m 就是 ln(base)
            slope_m = np.log(base_val)
            tangent_y = slope_m * t_plot + 1

            fig_exp = go.Figure()
            # 曲线
            fig_exp.add_trace(go.Scatter(x=t_plot, y=y_plot, mode='lines', line=dict(color='#636EFA', width=3),
                                         name=f'y = {base_val}^t'))
            # 切线
            fig_exp.add_trace(
                go.Scatter(x=t_plot, y=tangent_y, mode='lines', line=dict(color='#00CC96', width=2, dash='dot'),
                           name=f'Tangent at t=0'))
            # t=0 的点
            fig_exp.add_trace(go.Scatter(x=[0], y=[1], mode='markers',
                                         marker=dict(color='white', size=10, line=dict(color='#00CC96', width=2)),
                                         showlegend=False))

            # 动态标题反馈
            if abs(base_val - np.e) < 0.15:
                title_text = f"🎯 Base {base_val:.2f} ≈ e! Slope is exactly 1.00"
                title_color = "#00CC96"
            else:
                title_text = f"Base {base_val:.1f}^t → Slope constant is {slope_m:.3f}"
                title_color = "white"

            fig_exp.update_layout(
                template="plotly_dark", height=400,
                title=dict(text=title_text, font=dict(color=title_color)),
                xaxis=dict(title="Time (t)", range=[-1, 2]),
                yaxis=dict(title="Population", range=[0, 5]),
                margin=dict(t=40, b=20, l=20, r=20),
                hovermode="x unified"
            )
            st.plotly_chart(fig_exp, use_container_width=True)

        # ---------------------------------------------------------
        # ACT II: LOGARITHMS (The Mirror Reflection)
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 🪞 Act II: The Natural Logarithm ($\ln x$)")

        col_log_text, col_log_viz = st.columns([1, 1.2])
        with col_log_text:
            st.write("""
            What about the inverse of $e^x$? The natural logarithm $y = \ln(x)$.

            We don't need complex limits here. We just need **Geometry**.
            Geometrically, an inverse function is just a reflection across the diagonal line $y = x$. This reflection simply **swaps the X and Y axes**.

            **Think about it like climbing stairs:**
            1. Imagine you are on the $e^x$ curve at point $(a, e^a)$. 
            2. Suppose the slope here is **2**. This means for every **1 step Right (X)**, you go **2 steps Up (Y)**.
            3. Now, reflect this across $y=x$. The X and Y directions swap!
            4. Your new instructions are: for every **1 step Up (New Y)**, you go **2 steps Right (New X)**.
            5. What is the slope of this new line? Rise over Run = **$1/2$**.

            **Conclusion:** When you reflect a curve, its slope perfectly flips to its reciprocal (倒数).
            * If the slope of $e^x$ at point $(a, b)$ is **$b$**.
            * The slope of $\ln(x)$ at the reflected point $(b, a)$ must be **$1/b$**.

            Let's call our current x-coordinate $x$. The slope is simply $\\frac{1}{x}$.
            """)
            st.latex(r"\frac{d}{dx} \ln(x) = \frac{1}{x}")
            st.info(
                "💡 Notice the beauty: The slope of the logarithm gets less and less steep exactly as $1/x$ gets smaller and smaller.")

        with col_log_viz:
            # 交互式对数反射演示
            a_val = st.slider("Slide point on e^x (a):", -1.0, 1.5, 0.5, step=0.1, key="log_a")

            x_val_exp = np.linspace(-2, 3, 100)
            y_val_exp = np.exp(x_val_exp)

            x_val_log = np.linspace(0.01, 5, 100)
            y_val_log = np.log(x_val_log)

            fig_log = go.Figure()

            # y=x 对称线
            fig_log.add_trace(
                go.Scatter(x=[-2, 5], y=[-2, 5], mode='lines', line=dict(color='gray', width=1, dash='dash'),
                           name='y = x'))

            # e^x 及其切线
            e_a = np.exp(a_val)
            slope_exp = e_a
            tangent_exp_y = slope_exp * (x_val_exp - a_val) + e_a
            fig_log.add_trace(
                go.Scatter(x=x_val_exp, y=y_val_exp, mode='lines', line=dict(color='#636EFA', width=3), name='y = e^x'))
            fig_log.add_trace(
                go.Scatter(x=x_val_exp, y=tangent_exp_y, mode='lines', line=dict(color='#636EFA', width=1),
                           showlegend=False))
            fig_log.add_trace(go.Scatter(x=[a_val], y=[e_a], mode='markers+text', text=[f"Slope = {slope_exp:.2f}"],
                                         textposition="top left", marker=dict(size=8, color='#636EFA'),
                                         showlegend=False))

            # ln(x) 及其切线
            slope_log = 1 / e_a
            tangent_log_y = slope_log * (x_val_log - e_a) + a_val
            fig_log.add_trace(go.Scatter(x=x_val_log, y=y_val_log, mode='lines', line=dict(color='#EF553B', width=3),
                                         name='y = ln(x)'))
            fig_log.add_trace(
                go.Scatter(x=x_val_log, y=tangent_log_y, mode='lines', line=dict(color='#EF553B', width=1),
                           showlegend=False))
            fig_log.add_trace(go.Scatter(x=[e_a], y=[a_val], mode='markers+text', text=[f"Slope = 1/{slope_exp:.2f}"],
                                         textposition="bottom right", marker=dict(size=8, color='#EF553B'),
                                         showlegend=False))

            # 连接两个对称点的虚线
            fig_log.add_trace(
                go.Scatter(x=[a_val, e_a], y=[e_a, a_val], mode='lines', line=dict(color='white', width=1, dash='dot'),
                           showlegend=False))

            fig_log.update_layout(
                template="plotly_dark", height=450,
                xaxis=dict(range=[-2, 4], scaleanchor="y", scaleratio=1, title="x"),
                yaxis=dict(range=[-2, 4], title="y"),
                margin=dict(t=20, b=20, l=20, r=20),
            )
            st.plotly_chart(fig_log, use_container_width=True)

        # ---------------------------------------------------------
        # ACT III: TRIGONOMETRY (Circular Motion)
        # ---------------------------------------------------------
        st.divider()
        st.markdown("### 🎡 Act III: Trigonometry as Circular Motion")

        col_trig_text, col_trig_viz = st.columns([1, 1.2])
        with col_trig_text:
            st.write("""
            Let's drop the abstract triangles and look at this like a video game. 

            Imagine you are driving a car counter-clockwise on a circular track (Radius = 1) at a constant speed of 1 radian per second.
            At any time $t$:
            * **Your Horizontal Position (X)** is $\\cos(t)$
            * **Your Vertical Position (Y)** is $\\sin(t)$

            Because the car's speed is 1, its **Velocity (Derivative)** is literally just the direction the headlights are pointing!

            **Let's test two specific moments:**
            1. **At $t=0$ (The far right edge):** You are at coordinate $(1, 0)$. Your car is pointing **straight UP**.
               This means your vertical speed (Y-derivative) is **1**, and your horizontal speed (X-derivative) is **0**.
               Check the math: $\\frac{d}{dt}\\sin(0) = \\cos(0) = 1$. It matches!

            2. **At $t=\\frac{\\pi}{2}$ (The very top):** You are at coordinate $(0, 1)$. Your car is pointing **straight LEFT**.
               This means your horizontal speed (X-derivative) is **-1** (because left is negative), and your vertical speed is **0**.
               Check the math: $\\frac{d}{dt}\\cos(\\frac{\\pi}{2}) = -\\sin(\\frac{\\pi}{2}) = -1$. It matches perfectly!

            Since the velocity arrow (headlights) is always perfectly tangent to the circle, it is always rotated exactly 90° from your position. 
            This 90° rotation is geometrically identical to swapping X and Y, and making X negative.
            """)
            st.latex(r"\frac{d}{dt} \sin t = \cos t")
            st.latex(r"\frac{d}{dt} \cos t = -\sin t")

        with col_trig_viz:
            # 圆周运动速度矢量演示
            t_angle = st.slider("Time (t) in radians:", 0.0, float(2 * np.pi), 1.0, step=0.1, key="trig_t")

            fig_circ = go.Figure()

            # 画圆
            theta_circ = np.linspace(0, 2 * np.pi, 100)
            fig_circ.add_trace(go.Scatter(x=np.cos(theta_circ), y=np.sin(theta_circ), mode='lines',
                                          line=dict(color='gray', dash='dash'), name='Unit Circle'))

            # Position Vector
            px, py = np.cos(t_angle), np.sin(t_angle)
            fig_circ.add_trace(
                go.Scatter(x=[0, px], y=[0, py], mode='lines+markers', line=dict(color='#636EFA', width=3),
                           marker=dict(size=8), name='Position (cos t, sin t)'))

            # Velocity Vector (放在原点展示旋转)
            vx, vy = -np.sin(t_angle), np.cos(t_angle)
            fig_circ.add_trace(
                go.Scatter(x=[0, vx], y=[0, vy], mode='lines+markers', line=dict(color='#EF553B', width=3),
                           marker=dict(size=8), name='Velocity (-sin t, cos t)'))

            # 标注直角符号 (简单示意)
            fig_circ.add_trace(
                go.Scatter(x=[px / 5, (px + vx) / 5, vx / 5], y=[py / 5, (py + vy) / 5, vy / 5], mode='lines',
                           line=dict(color='white', width=1), showlegend=False))

            fig_circ.update_layout(
                template="plotly_dark", height=400,
                xaxis=dict(range=[-1.5, 1.5], scaleanchor="y", scaleratio=1, zerolinecolor='gray',
                           title="X-axis (cos)"),
                yaxis=dict(range=[-1.5, 1.5], zerolinecolor='gray', title="Y-axis (sin)"),
                margin=dict(t=20, b=20, l=20, r=20),
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            st.plotly_chart(fig_circ, use_container_width=True)
            st.caption(
                "The red Velocity vector is always the blue Position vector rotated 90° counter-clockwise. This simple rotation explains why sines and cosines swap places (and flip signs) when you take derivatives.")

        # ==============================================================================
        # NEW SECTION: DERIVING TAN, SEC, CSC, COT
        # ==============================================================================
        st.divider()
        st.markdown("### 🔓 Unlocking the Rest: $\\tan, \\sec, \\csc, \\cot$")
        st.write("""
            Now that we have geometrically proven the derivatives of $\\sin(x)$ and $\\cos(x)$, we have the keys to unlock all the other trigonometric functions. We don't need any new circles or graphs—just pure algebra and the **Quotient Rule**:
            """)
        st.latex(r"\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}")

        # 使用 Tabs 来分类展示四个推导，保持页面整洁
        tab_tan, tab_sec, tab_csc, tab_cot = st.tabs([
            "Derivative of tan(x)",
            "Derivative of sec(x)",
            "Derivative of csc(x)",
            "Derivative of cot(x)"
        ])

        with tab_tan:
            st.markdown("#### The Proof for $\\tan(x)$")
            st.write("Since $\\tan(x) = \\frac{\\sin(x)}{\\cos(x)}$, we apply the Quotient Rule:")
            # tan(x) 的推导
            st.latex(r"""
                    \begin{aligned}
                    \frac{d}{dx} \tan(x) &= \frac{d}{dx} \left( \frac{\sin x}{\cos x} \right) \\
                    &= \frac{(\cos x)(\cos x) - (\sin x)(-\sin x)}{\cos^2 x} \\
                    &= \frac{\cos^2 x + \sin^2 x}{\cos^2 x} \\
                    &= \frac{1}{\cos^2 x} \quad \text{(Since } \sin^2 x + \cos^2 x = 1 \text{)} \\
                    &= \sec^2(x)
                    \end{aligned}
                """)
            st.success("✨ Result: $\\frac{d}{dx} \\tan(x) = \\sec^2(x)$")

        with tab_sec:
            st.markdown("#### The Proof for $\\sec(x)$")
            st.write(
                "Since $\\sec(x) = \\frac{1}{\\cos(x)}$, we apply the Quotient Rule (where $u=1$ and $v=\\cos x$):")
            # sec(x) 的推导
            st.latex(r"""
                    \begin{aligned}
                    \frac{d}{dx} \sec(x) &= \frac{d}{dx} \left( \frac{1}{\cos x} \right) \\
                    &= \frac{(0)(\cos x) - (1)(-\sin x)}{\cos^2 x} \\
                    &= \frac{\sin x}{\cos^2 x} \\
                    &= \frac{1}{\cos x} \cdot \frac{\sin x}{\cos x} \\
                    &= \sec(x)\tan(x)
                    \end{aligned}
                """)
            st.success("✨ Result: $\\frac{d}{dx} \\sec(x) = \\sec(x)\\tan(x)$")

        with tab_csc:
            st.markdown("#### The Proof for $\\csc(x)$")
            st.write("Since $\\csc(x) = \\frac{1}{\\sin(x)}$, we apply the Quotient Rule:")
            # csc(x) 的推导
            st.latex(r"""
                    \begin{aligned}
                    \frac{d}{dx} \csc(x) &= \frac{d}{dx} \left( \frac{1}{\sin x} \right) \\
                    &= \frac{(0)(\sin x) - (1)(\cos x)}{\sin^2 x} \\
                    &= \frac{-\cos x}{\sin^2 x} \\
                    &= -\frac{1}{\sin x} \cdot \frac{\cos x}{\sin x} \\
                    &= -\csc(x)\cot(x)
                    \end{aligned}
                """)
            st.success("✨ Result: $\\frac{d}{dx} \\csc(x) = -\\csc(x)\\cot(x)$")

        with tab_cot:
            st.markdown("#### The Proof for $\\cot(x)$")
            st.write("Since $\\cot(x) = \\frac{\\cos(x)}{\\sin(x)}$, we apply the Quotient Rule:")
            # cot(x) 的推导
            st.latex(r"""
                    \begin{aligned}
                    \frac{d}{dx} \cot(x) &= \frac{d}{dx} \left( \frac{\cos x}{\sin x} \right) \\
                    &= \frac{(-\sin x)(\sin x) - (\cos x)(\cos x)}{\sin^2 x} \\
                    &= \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x} \\
                    &= -\frac{1}{\sin^2 x} \quad \text{(Factoring out the negative)} \\
                    &= -\csc^2(x)
                    \end{aligned}
                """)
            st.success("✨ Result: $\\frac{d}{dx} \\cot(x) = -\\csc^2(x)$")

        st.info(
            "💡 **Pattern Alert:** Did you notice that the derivatives of all the 'co-' functions ($\\cos$, $\\csc$, $\\cot$) always have a **negative sign**? This is a great trick to double-check your memory during exams!")

        # ==============================================================================
        # TAB 7: THE TRAINING GROUND (Practical Application)
        # ==============================================================================
        with diff_tabs[5]:  # 请确保这里的索引对应你新增的 Tab
            st.subheader("⚔️ The Training Ground: Applying Your Knowledge")
            st.write("""
            Now that you understand the *why* behind the rules, it's time to test your mathematical instincts. 
            In calculus, solving complex derivatives isn't about memorizing 100 different templates. It is about identifying the **structure** of the equation and applying the basic rules (Chain, Product, Quotient) step-by-step.

            Try solving these on paper first, then click to reveal the step-by-step breakdown!
            """)

            st.divider()

            # ---------------------------------------------------------
            # Q1: Chain Rule (Basic Onion)
            # ---------------------------------------------------------
            with st.expander("🔥 Question 1: The 'Onion' Method 👉 $y = \sin(\ln x)$"):
                st.markdown("#### The Chain Rule Strategy")
                st.write(
                    "Think of this function as an onion. You must peel the **Outer function** before you can reach the **Inner function**.")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    * **Outer Function:** $\sin(\\text{stuff})$
                    * **Inner Function:** $\ln x$
                    """)
                with col2:
                    st.markdown("""
                    * Derivative of Outer: $\cos(\\text{stuff})$
                    * Derivative of Inner: $\\frac{1}{x}$
                    """)

                st.markdown("#### The Execution:")
                st.latex(r"""
                \begin{aligned}
                y' &= \underbrace{\cos(\ln x)}_{\text{Deriv of Outer (keep inside intact)}} \cdot \underbrace{\left(\frac{1}{x}\right)}_{\text{Deriv of Inner}} \\
                y' &= \frac{\cos(\ln x)}{x}
                \end{aligned}
                """)

            # ---------------------------------------------------------
            # Q2: Product Rule
            # ---------------------------------------------------------
            with st.expander("🔥 Question 2: The Tag Team 👉 $y = e^x \sec x$"):
                st.markdown("#### The Product Rule Strategy")
                st.write(
                    "Two entirely different functions are multiplying each other. We must use the Product Rule: $(uv)' = u'v + uv'$.")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("""
                    * **First function ($u$):** $e^x$
                    * **Second function ($v$):** $\sec x$
                    """)
                with col2:
                    st.markdown("""
                    * $u' = e^x$ (The immortal function!)
                    * $v' = \sec x \\tan x$ (From our previous proof)
                    """)

                st.markdown("#### The Execution:")
                st.latex(r"""
                \begin{aligned}
                y' &= (u')(v) + (u)(v') \\
                y' &= (e^x)(\sec x) + (e^x)(\sec x \tan x) \\
                y' &= e^x \sec x (1 + \tan x) \quad \text{(Factored for elegance)}
                \end{aligned}
                """)

            # ---------------------------------------------------------
            # Q3: The Trap (Simplification)
            # ---------------------------------------------------------
            with st.expander("🚨 Question 3: The Ninja Trap 👉 $y = e^{\ln(\csc 2x)}$"):
                st.markdown("#### The Strategy: Look before you leap!")
                st.warning(
                    "If you try to use the Chain Rule immediately, you will create a massive, ugly mess. A true mathematician always checks if the expression can be simplified first!")

                st.write(
                    "Remember the fundamental property of logarithms and exponentials: They are perfect opposites. $e^{\ln(\\text{stuff})} = \\text{stuff}$.")

                st.markdown("#### Step 1: Disarm the trap")
                st.latex(r"y = e^{\ln(\csc 2x)} \implies y = \csc(2x)")

                st.markdown("#### Step 2: Simple Chain Rule")
                st.write("Now we just have an outer function $\csc(\\text{stuff})$ and an inner function $2x$.")
                st.latex(r"""
                \begin{aligned}
                y' &= \underbrace{-\csc(2x)\cot(2x)}_{\text{Deriv of Outer}} \cdot \underbrace{(2)}_{\text{Deriv of Inner}} \\
                y' &= -2\csc(2x)\cot(2x)
                \end{aligned}
                """)
                st.success("Lesson learned: Always simplify algebraically before doing calculus!")

            # ---------------------------------------------------------
            # Q4: Product + Chain Rule Combo
            # ---------------------------------------------------------
            with st.expander("☠️ Question 4: The Combo Breaker 👉 $y = \sin^2(x) \cos^3(x)$"):
                st.markdown("#### The Strategy: Rewrite to see clearly")
                st.write(
                    "First, rewrite the notation so you don't get confused by the powers: $y = (\sin x)^2 \cdot (\cos x)^3$")
                st.write("We have a Product Rule, but **both** pieces require the Chain Rule!")

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**(u) Left piece:** $(\sin x)^2$")
                    st.latex(r"u' = 2(\sin x)^1 \cdot (\cos x)")
                with col2:
                    st.markdown("**(v) Right piece:** $(\cos x)^3$")
                    st.latex(r"v' = 3(\cos x)^2 \cdot (-\sin x)")

                st.markdown("#### The Execution ($(uv)' = u'v + uv'$):")
                st.latex(r"""
                \begin{aligned}
                y' &= \big[2\sin x \cos x\big] \cdot (\cos^3 x) + (\sin^2 x) \cdot \big[-3\cos^2 x \sin x\big] \\
                y' &= 2\sin x \cos^4 x - 3\sin^3 x \cos^2 x
                \end{aligned}
                """)
                st.write(
                    "*(You can factor out $\sin x \cos^2 x$ if you want to be extra neat, but this is the core calculus step completed!)*")

            # ---------------------------------------------------------
            # Q5: The Final Boss (Triple Chain Rule)
            # ---------------------------------------------------------
            with st.expander("🐉 Question 5: The Final Boss 👉 $y = \sqrt{x^2 + \sec(2x+3)}$"):
                st.markdown("#### The Strategy: The 3-Layer Inception")
                st.write(
                    "Rewrite the square root as a power of $1/2$. This function has an outer shell, a middle layer, and a deep core.")
                st.latex(r"y = \Big( x^2 + \sec(2x+3) \Big)^{1/2}")

                st.markdown("""
                1. **Outer Shell:** $(\\text{huge stuff})^{1/2}$ $\implies$ Bring down $1/2$, subtract 1 from power.
                2. **Middle Layer:** $x^2 + \sec(\\text{core})$ $\implies$ Normal derivative, but secant triggers another chain.
                3. **Deep Core:** $2x+3$ $\implies$ Derivative is simply 2.
                """)

                st.markdown("#### The Execution (Peeling it all at once):")
                st.latex(r"""
                \begin{aligned}
                y' &= \underbrace{\frac{1}{2}\Big( x^2 + \sec(2x+3) \Big)^{-1/2}}_{\text{Peeling Layer 1}} \cdot \underbrace{\left[ 2x + \sec(2x+3)\tan(2x+3) \cdot (2) \right]}_{\text{Peeling Layer 2 \& 3}}
                \end{aligned}
                """)

                st.write("Let's clean it up by putting the negative exponent back into the denominator:")
                st.latex(r"""
                y' = \frac{2x + 2\sec(2x+3)\tan(2x+3)}{2\sqrt{x^2 + \sec(2x+3)}}
                """)
                st.write("Divide everything by 2 for the final perfect answer:")
                st.latex(r"""
                y' = \frac{x + \sec(2x+3)\tan(2x+3)}{\sqrt{x^2 + \sec(2x+3)}}
                """)
                # ==============================================================================
                # TAB 8: THE TWO FACES OF CURVES (Implicit vs. Parametric)
                # ==============================================================================
                with diff_tabs[6]:  # 请根据你的 Tab 数量调整索引
                    st.subheader("🎭 The Two Faces of Curves: Implicit vs. Parametric")
                    st.write("""
                    How do we describe a curve? 
                    One way is to set a **Static Rule** that coordinates must follow (Implicit). 
                    Another way is to record a **Dynamic Journey** over time (Parametric). 
                    Let's explore their distinct purposes and the profound truth they reveal when we take their derivatives.
                    """)

                    st.divider()

                    # --- 第一部分：它们的真正用途 (The Real Use Cases) ---
                    st.markdown("### 🛠️ What are their actual purposes?")

                    col_use_im, col_use_pa = st.columns(2)
                    with col_use_im:
                        st.info("🏛️ **Implicit: The Unbreakable Constraints**")
                        st.write(
                            "**What it is:** Equations where $x$ and $y$ are hopelessly tangled together (e.g., $y + \sin(xy) = x$).")
                        st.markdown("""
                        **When to use it:**
                        * **Shapes, not motions:** Perfect for analyzing static geometric boundaries like circles, ellipses, or complex blobs.
                        * **The Algebraically Impossible:** When you physically cannot isolate $y$ on one side of the equals sign, Implicit Differentiation is your only mathematical lifeline to find the slope.
                        """)
                    with col_use_pa:
                        st.success("🛰️ **Parametric: The Physics Engine**")
                        st.write(
                            "**What it is:** Introducing a third variable, $t$ (time), to dictate exactly where $x$ and $y$ are (e.g., $x=\cos t, y=\sin t$).")
                        st.markdown("""
                        **When to use it:**
                        * **Computer Graphics & Physics:** To animate a bullet, you need to know not just *where* its path is, but exactly *when* it hits a coordinate.
                        * **Self-Intersecting Paths:** A normal function cannot loop back on itself (like a figure-8). Parametric equations can easily describe paths that cross the same point at different times.
                        """)

                    st.divider()

                    # --- 第二部分：推导对比 ---
                    st.markdown("### ⚔️ The Calculus Duel: Finding $dy/dx$")
                    st.write("Let's test both methods on the exact same unit circle.")

                    tab_im_proof, tab_pa_proof = st.tabs(
                        ["Method 1: Implicit Differentiation", "Method 2: Parametric Differentiation"])

                    with tab_im_proof:
                        st.write("Differentiate both sides of the **Static Rule**: $x^2 + y^2 = 1$")
                        st.latex(r"""
                        \begin{aligned}
                        \frac{d}{dx}(x^2) + \frac{d}{dx}(y^2) &= \frac{d}{dx}(1) \\
                        2x + 2y \cdot \frac{dy}{dx} &= 0 \\
                        \mathbf{\frac{dy}{dx}} &= \mathbf{-\frac{x}{y}}
                        \end{aligned}
                        """)

                    with tab_pa_proof:
                        st.write(
                            "Divide the vertical speed by the horizontal speed from the **Dynamic Journey**: $x = \cos t, y = \sin t$")
                        st.latex(r"""
                        \begin{aligned}
                        \frac{dx}{dt} &= -\sin t \\
                        \frac{dy}{dt} &= \cos t \\
                        \frac{dy}{dx} &= \frac{dy/dt}{dx/dt} = \frac{\cos t}{-\sin t} \\
                        \mathbf{\frac{dy}{dx}} &= \mathbf{-\frac{x}{y}} \quad \text{(Since } y=\sin t, x=\cos t\text{)}
                        \end{aligned}
                        """)

                    # --- 第三部分：深刻含义揭晓 (The Deep Meaning) ---
                    st.error("🤯 **Why do both methods give the exact same answer?**")
                    st.write("""
                        Because they are just **two different languages describing the same shape.**

                        The 'steepness' (slope) of the circle at a specific point is a geometric fact. 
                        * The **Implicit** equation ($x^2 + y^2 = 1$) looks at the circle as a static rule.
                        * The **Parametric** equations ($x = \cos t, y = \sin t$) look at the circle as a moving path.

                        The fact that $dy/dx$ is identical in both cases proves that our mathematical tools—whether they focus on static rules or dynamic motion—are perfectly consistent with the underlying geometry.
                        """)
                    st.divider()
# Application


import streamlit as st
import numpy as np
import plotly.graph_objects as go


def render_applications():
    st.header("⚙️ Part 2: Applications of Differentiation")
    st.write(
        "Welcome to the Hardcore Engineering & Physics module. Here, we use calculus to solve real-world optimization and dynamic tracking problems.")

    app_tabs = st.tabs(["1. Curve Analysis", "2. Related Rates", "3. Optimisation"])

    # =========================================================
    # TAB 1: CURVE ANALYSIS
    # =========================================================
    with app_tabs[0]:
        st.subheader("Curve Analysis: Identifying Key Points")
        st.write(
            "Derivatives allow us to determine the exact coordinates where a function changes its increasing/decreasing behavior or its concavity.")

        col_def, col_plot = st.columns([1.3, 1])

        with col_def:
            st.markdown("### 1. The Core Definitions")
            st.markdown("""
            * **Critical Point:** A point where $f'(x) = 0$ **OR** where $f'(x)$ is undefined.
            * **Stationary Point:** A specific type of critical point where $f'(x) = 0$. The tangent line is perfectly horizontal.
            * **Relative Extremum:** The local maximum or minimum point. It occurs at a critical point where $f'(x)$ changes sign.
            * **Point of Inflection:** A point where the curve changes concavity. Here, $f''(x) = 0$ (or is undefined) AND $f''(x)$ changes sign.
            """)

            with st.expander("🧐 Deep Dive: Critical vs. Stationary Points"):
                st.write(
                    "All stationary points are critical points, but **not all critical points are stationary points!**")
                st.markdown("""
                * **Case A: The Smooth Valley ($y = x^2$)** At $x=0$, $y' = 0$. The curve is flat. This is BOTH a critical point and a stationary point.
                * **Case B: The Sharp Corner ($y = |x|$)**
                  At $x=0$, there is a sharp corner, so the derivative $y'$ is **undefined**. This is a **Critical Point**, but it is NOT a stationary point.
                """)

            st.divider()

            st.markdown("### 2. Rigorous Analysis with Sign Tables")
            st.info("Example Function: $f(x) = x^3 - 3x^2 + 2$")

            st.write("#### Step 1: First Derivative Test (Extrema)")
            st.latex(r"f'(x) = 3x^2 - 6x = 3x(x - 2)")
            st.write(
                "Setting $f'(x) = 0$, our stationary points are at $x = 0$ and $x = 2$. Let's check the signs around them:")

            st.markdown("""
            | Interval | Test Value ($x$) | Sign of $f'(x)$ | Behavior of $f(x)$ |
            | :--- | :---: | :---: | :--- |
            | $x < 0$ | -1 | $(-)(-)$ = **$+$** | ↗ Increasing |
            | **$x = 0$** | **0** | **$0$** | $\\rightarrow$ **Local Max** |
            | $0 < x < 2$ | 1 | $(+)(-)$ = **$-$** | ↘ Decreasing |
            | **$x = 2$** | **2** | **$0$** | $\\rightarrow$ **Local Min** |
            | $x > 2$ | 3 | $(+)(+)$ = **$+$** | ↗ Increasing |
            """)

            st.write("#### Step 2: Second Derivative Test (Concavity)")
            st.latex(r"f''(x) = 6x - 6 = 6(x - 1)")
            st.write("Setting $f''(x) = 0$, our potential inflection point is at $x = 1$. Let's verify:")

            st.markdown("""
            | Interval | Test Value ($x$) | Sign of $f''(x)$ | Concavity of $f(x)$ |
            | :--- | :---: | :---: | :--- |
            | $x < 1$ | 0 | **$-$** | ∩ Concave Down |
            | **$x = 1$** | **1** | **$0$** | **Point of Inflection** |
            | $x > 1$ | 2 | **$+$** | ∪ Concave Up |
            """)

        with col_plot:
            st.markdown("<br><br>", unsafe_allow_html=True)
            x_vals = np.linspace(-1.5, 3.5, 100)
            y_vals = x_vals ** 3 - 3 * x_vals ** 2 + 2

            fig_curve = go.Figure()
            fig_curve.add_trace(
                go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)', line=dict(color='#636EFA', width=3)))
            fig_curve.add_trace(
                go.Scatter(x=[0], y=[2], mode='markers+text', text=["Local Max (0,2)"], textposition="top center",
                           marker=dict(size=12, color='#EF553B'), name='Max'))
            fig_curve.add_trace(
                go.Scatter(x=[2], y=[-2], mode='markers+text', text=["Local Min (2,-2)"], textposition="bottom center",
                           marker=dict(size=12, color='#00CC96'), name='Min'))
            fig_curve.add_trace(
                go.Scatter(x=[1], y=[0], mode='markers+text', text=["Inflection (1,0)"], textposition="top right",
                           marker=dict(size=10, color='#FFA15A', symbol='diamond'), name='Inflection'))

            fig_curve.update_layout(template="plotly_dark", height=550, margin=dict(t=20, b=20, l=20, r=20),
                                    showlegend=False)
            st.plotly_chart(fig_curve, use_container_width=True)

        st.divider()

        # [REVERSE ENGINEERING Q10]
        st.markdown("### 🕵️ Advanced Challenge: Reverse Engineering")
        with st.expander("Challenge: Find the Extremum from Derivative Graphs"):
            st.markdown(
                "**Problem:** Given the graphs of $dy/dx$ and $d^2y/dx^2$ for function $y=f(x)$. The curve $y=f(x)$ passes through $(-1, 6)$ and $(1, 2)$. Determine the coordinates of the maximum and minimum points.")

            col_q10_1, col_q10_2 = st.columns(2)
            x_q10 = np.linspace(-2, 2, 100)
            dy_dx = 3 * x_q10 ** 2 - 3
            d2y_dx2 = 6 * x_q10

            with col_q10_1:
                fig_dy = go.Figure()
                fig_dy.add_trace(go.Scatter(x=x_q10, y=dy_dx, mode='lines', line=dict(color='#00CC96', width=3)))
                fig_dy.add_trace(go.Scatter(x=[-1, 1], y=[0, 0], mode='markers+text', text=["x=-1", "x=1"],
                                            textposition="top center", marker=dict(size=10, color='red')))
                fig_dy.update_layout(title="Graph of dy/dx", template="plotly_dark", height=250,
                                     margin=dict(t=40, b=10, l=10, r=10), showlegend=False)
                st.plotly_chart(fig_dy, use_container_width=True)

            with col_q10_2:
                fig_d2y = go.Figure()
                fig_d2y.add_trace(go.Scatter(x=x_q10, y=d2y_dx2, mode='lines', line=dict(color='#FFA15A', width=3)))
                fig_d2y.add_trace(go.Scatter(x=[-1, 1], y=[-6, 6], mode='markers+text', text=["y=-6", "y=6"],
                                             textposition=["bottom right", "top left"],
                                             marker=dict(size=10, color='red')))
                fig_d2y.update_layout(title="Graph of d²y/dx²", template="plotly_dark", height=250,
                                      margin=dict(t=40, b=10, l=10, r=10), showlegend=False)
                st.plotly_chart(fig_d2y, use_container_width=True)

            st.write("**Visual Solution:**")
            st.write(
                "1. **From $dy/dx$:** The line crosses the x-axis at $x = -1$ and $x = 1$. These are our stationary points.")
            st.write("2. **From $d^2y/dx^2$:**")
            st.markdown("- At $x = -1$, the value is $-6$ (Concave Down $\\implies$ **Local Maximum**).")
            st.markdown("- At $x = 1$, the value is $+6$ (Concave Up $\\implies$ **Local Minimum**).")
            st.success(
                "Result: The Maximum point is $(-1, 6)$ and the Minimum point is $(1, 2)$. No integration needed!")

        # =========================================================
        # TAB 2: RELATED RATES
        # =========================================================
        with app_tabs[1]:
            st.subheader("Rate of Change: Related Rates & Dynamics")
            st.write(
                "When variables are related by an equation, their rates of change with respect to time ($t$) are linked via the Chain Rule.")

            # [NEW HARDCORE 1] 航天测控：火箭追踪
            with st.expander("🚀 Hardcore Challenge 1: Radar Tracking a Rocket (Angular Velocity)", expanded=True):
                st.markdown(
                    "**Problem:** A rocket blasts off vertically from a launchpad. A radar station is located 5,000 meters away. The rocket's upward velocity is $v = 500t$ m/s. The radar's camera must rotate at an angle $\\theta$ to keep the rocket in the center of the frame. Find the **angular velocity** (how fast the camera is rotating, $d\\theta/dt$) exactly 10 seconds after launch.")

                col_r1, col_r2 = st.columns([1.2, 1])
                with col_r1:
                    st.write("**1. The Physics Model:**")
                    st.write("First, find the height $h$ at $t=10$. Since $v = 500t$, height is the integral:")
                    st.latex(r"h(t) = \int 500t \, dt = 250t^2")
                    st.write("At $t=10$, $h = 25,000$ m, and velocity $dh/dt = 5,000$ m/s.")

                    st.write("**2. The Geometry (Trigonometry):**")
                    st.latex(r"\tan \theta = \frac{h}{5000}")

                    st.write("**3. Differentiate w.r.t time $t$ (Chain Rule):**")
                    st.latex(r"\sec^2 \theta \cdot \frac{d\theta}{dt} = \frac{1}{5000} \cdot \frac{dh}{dt}")

                    st.write("**4. Solve for Angular Velocity:**")
                    st.write("When $h = 25,000$, $\\tan\\theta = 5$. Thus, $\\sec^2\\theta = 1 + 5^2 = 26$.")
                    st.latex(
                        r"26 \cdot \frac{d\theta}{dt} = \frac{1}{5000} \cdot 5000 \implies \frac{d\theta}{dt} = \frac{1}{26} \text{ rad/s}")
                    st.success(
                        "Result: The camera rotates at approx 0.038 rad/s (2.2°/sec). Try the slider to see how it slows down as the rocket gets higher!")

                with col_r2:
                    t_slider = st.slider("Time after launch $t$ (seconds):", 1, 20, 10, key="rocket_time")
                    h_current = 250 * (t_slider ** 2)
                    v_current = 500 * t_slider
                    theta_rad = np.arctan(h_current / 5000)
                    dtheta_dt = (v_current / 5000) / (1 + (h_current / 5000) ** 2)

                    st.metric("Camera Rotation Speed (dθ/dt)", f"{dtheta_dt * (180 / np.pi):.2f} °/sec")

                    fig_rocket = go.Figure()
                    fig_rocket.add_trace(go.Scatter(x=[0, 5000, 5000], y=[0, 0, h_current], mode='lines',
                                                    line=dict(color='gray', dash='dash')))
                    fig_rocket.add_trace(
                        go.Scatter(x=[0], y=[0], mode='markers+text', text=["📡 Radar"], textposition="bottom right",
                                   marker=dict(size=15, color='#00CC96')))
                    fig_rocket.add_trace(go.Scatter(x=[5000], y=[h_current], mode='markers+text', text=["🚀 Rocket"],
                                                    textposition="top center", marker=dict(size=15, color='#EF553B')))

                    arc_x = [0] + [1000 * np.cos(a) for a in np.linspace(0, theta_rad, 20)] + [0]
                    arc_y = [0] + [1000 * np.sin(a) for a in np.linspace(0, theta_rad, 20)] + [0]
                    fig_rocket.add_trace(go.Scatter(x=arc_x, y=arc_y, fill='toself', fillcolor='rgba(255,161,90,0.5)',
                                                    line=dict(color='rgba(255,255,255,0)'), showlegend=False))
                    fig_rocket.add_annotation(x=1500, y=500, text=f"θ = {theta_rad * (180 / np.pi):.1f}°",
                                              showarrow=False, font=dict(color="#FFA15A", size=14))

                    fig_rocket.update_layout(template="plotly_dark", height=300, margin=dict(t=20, b=20, l=20, r=20),
                                             xaxis_range=[-500, 6000], yaxis_range=[-500, 105000], showlegend=False)
                    st.plotly_chart(fig_rocket, use_container_width=True)

            # -------------------------------------------------------------
            # THE CORE 5 RELATED RATES PROBLEMS (FULLY DETAILED)
            # -------------------------------------------------------------

            # 1. The Sliding Ladder
            with st.expander("Example 1: The Sliding Ladder Problem"):
                st.markdown(
                    "**Problem:** A 10m ladder leans against a vertical wall. The base of the ladder slides away from the wall at a constant rate of 1 m/s. How fast is the top of the ladder sliding down the wall when the base is 6m away from the wall?")
                st.markdown("")

                st.write("**Detailed Solution:**")
                st.write(
                    "1. **Set up the Geometry:** Let $x$ be the horizontal distance from the wall, and $y$ be the vertical height on the wall. According to the Pythagorean theorem:")
                st.latex(r"x^2 + y^2 = 10^2")

                st.write("2. **Differentiate implicitly with respect to time $t$:**")
                st.latex(r"2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0")

                st.write(
                    "3. **Substitute the known instant values:** We are given $x = 6$ and the sliding speed $\\frac{dx}{dt} = 1$.")
                st.write("First, we must find the current height $y$ when $x = 6$:")
                st.latex(r"6^2 + y^2 = 100 \implies y = 8")

                st.write("Now, plug everything into our differentiated equation:")
                st.latex(r"""
                \begin{aligned}
                2(6)(1) + 2(8)\frac{dy}{dt} &= 0 \\
                12 + 16\frac{dy}{dt} &= 0 \\
                \frac{dy}{dt} &= -\frac{12}{16} = -0.75 \text{ m/s}
                \end{aligned}
                """)
                st.success("Conclusion: The top of the ladder is sliding downwards at a rate of 0.75 m/s.")

            # 2. The Conical Tank (Deep Dive)
            with st.expander("Example 2: The Conical Tank Problem (Deep Dive)"):
                st.markdown(
                    "**Problem:** Water is poured into a conical tank (vertex down) at a rate of 2 m³/min. The tank has a base radius of 4m and a height of 10m. How fast is the water level rising when the depth is 5m?")
                st.markdown("")

                st.write("**Why do students get stuck here?**")
                st.write(
                    "The volume of a cone is $V = \\frac{1}{3}\pi r^2 h$. If we differentiate this directly, we get a messy product rule involving $dr/dt$, which we **don't know**. We must eliminate $r$ first to create a function purely in terms of $h$.")

                st.write("**Step 1: Eliminate a variable using Similar Triangles**")
                st.write(
                    "Look at the cross-section. The water forms a small triangle inside the large tank triangle. Their proportions are permanently locked:")
                st.latex(
                    r"\frac{\text{Water Radius } r}{\text{Water Height } h} = \frac{\text{Tank Radius } 4}{\text{Tank Height } 10} \implies r = 0.4h")

                st.write("**Step 2: Rewrite the Volume Formula**")
                st.latex(r"V = \frac{1}{3}\pi (0.4h)^2 h = \frac{1}{3}\pi (0.16h^2)h = \frac{4}{75}\pi h^3")

                st.write("**Step 3: Differentiate with respect to time $t$**")
                st.write("Now, applying the Chain Rule is easy since we only have $V$ and $h$:")
                st.latex(
                    r"\frac{dV}{dt} = 3 \cdot \frac{4}{75}\pi h^2 \frac{dh}{dt} = \frac{4}{25}\pi h^2 \frac{dh}{dt}")

                st.write("**Step 4: Plug in the instant values**")
                st.write(
                    "We are given the fill rate $\\frac{dV}{dt} = 2$ and we want to find $\\frac{dh}{dt}$ exactly when $h = 5$:")
                st.latex(
                    r"2 = \frac{4}{25}\pi (5)^2 \frac{dh}{dt} \implies 2 = 4\pi \frac{dh}{dt} \implies \frac{dh}{dt} = \frac{1}{2\pi} \approx 0.159 \text{ m/min}")
                st.success("Conclusion: The water level is rising at approximately 0.159 m/min.")

            # 3. Intersecting Cars
            with st.expander("Example 3: Two Cars at an Intersection"):
                st.markdown(
                    "**Problem:** Car A drives North from an intersection at 60 km/h. Car B drives East from the same intersection at 80 km/h. What is the rate of change of the straight-line distance between them 2 hours after they leave the intersection?")
                st.markdown("")

                st.write("**Detailed Solution:**")
                st.write(
                    "1. **Set up the Geometry:** Let $y$ be Car A's distance North, $x$ be Car B's distance East, and $z$ be the straight-line distance between them. They form a right triangle:")
                st.latex(r"x^2 + y^2 = z^2")

                st.write("2. **Differentiate implicitly with respect to time $t$:**")
                st.latex(
                    r"2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 2z\frac{dz}{dt} \implies x\frac{dx}{dt} + y\frac{dy}{dt} = z\frac{dz}{dt}")

                st.write("3. **Find their exact positions after $t = 2$ hours:**")
                st.write("We know $\\frac{dy}{dt} = 60$ and $\\frac{dx}{dt} = 80$.")
                st.write("- $y = 60 \\times 2 = 120$ km")
                st.write("- $x = 80 \\times 2 = 160$ km")
                st.write("- $z = \sqrt{160^2 + 120^2} = \sqrt{25600 + 14400} = \sqrt{40000} = 200$ km")

                st.write("4. **Substitute values and solve for $\\frac{dz}{dt}$:**")
                st.latex(r"""
                \begin{aligned}
                (160)(80) + (120)(60) &= (200)\frac{dz}{dt} \\
                12800 + 7200 &= 200\frac{dz}{dt} \\
                20000 &= 200\frac{dz}{dt} \\
                \frac{dz}{dt} &= 100 \text{ km/h}
                \end{aligned}
                """)
                st.success("Conclusion: The distance between the cars is increasing at exactly 100 km/h.")

            # 4. The Shadow Problem
            with st.expander("Example 4: The Moving Shadow Problem"):
                st.markdown(
                    "**Problem:** A 1.8m tall person walks *away* from a 5.4m tall street light at a speed of 1.5 m/s.")
                st.markdown(
                    "**Find:**<br>(A) At what rate is the **length of their shadow** increasing?<br>(B) At what rate is the **tip of their shadow** moving?",
                    unsafe_allow_html=True)
                st.markdown("")

                st.write("**Detailed Solution:**")
                st.write(
                    "1. **Set up the variables:** Let $x$ be the person's distance from the lamppost, and $s$ be the length of the shadow. The person's walking speed is $\\frac{dx}{dt} = 1.5$ m/s.")

                st.write(
                    "2. **Use Similar Triangles:** The large triangle (lamppost to shadow tip) and the small triangle (person to shadow tip) are similar triangles. We set up the ratio (Height / Base):")
                st.latex(r"\frac{5.4}{x + s} = \frac{1.8}{s}")

                st.write(
                    "3. **Simplify the equation:** Cross-multiply to establish a clean relationship between $x$ and $s$ before doing any calculus:")
                st.latex(r"""
                \begin{aligned}
                5.4s &= 1.8(x + s) \\
                5.4s &= 1.8x + 1.8s \\
                3.6s &= 1.8x \\
                2s &= x \implies s = 0.5x
                \end{aligned}
                """)

                st.write("---")
                st.markdown("**(A) Rate of change of the shadow's length:**")
                st.write(
                    "We need to find $\\frac{ds}{dt}$. Differentiate our simplified equation $s = 0.5x$ with respect to time $t$:")
                st.latex(r"\frac{ds}{dt} = 0.5 \frac{dx}{dt}")
                st.write("Substitute the known walking speed $\\frac{dx}{dt} = 1.5$:")
                st.latex(r"\frac{ds}{dt} = 0.5(1.5) = 0.75 \text{ m/s}")
                st.success("Result A: The length of the shadow itself is growing at 0.75 m/s.")

                st.write("---")
                st.markdown("**(B) Rate of change of the shadow's tip:**")
                st.write(
                    "The tip of the shadow's distance from the lamppost is the total distance $(x + s)$. We need to find how fast this total distance is growing: $\\frac{d}{dt}(x + s)$.")
                st.latex(r"\frac{d}{dt}(x + s) = \frac{dx}{dt} + \frac{ds}{dt}")
                st.write("Substitute the values we just calculated:")
                st.latex(r"\frac{d}{dt}(x + s) = 1.5 + 0.75 = 2.25 \text{ m/s}")
                st.success("Result B: The tip of the shadow is moving across the ground at 2.25 m/s.")

            # 5. Dynamic Area (SPM) with Visualization
            with st.expander("Example 5: Dynamic Area Under a Curve"):
                st.markdown(
                    "**Problem:** A curve is $y = 6x - x^2$. Point $P(x,y)$ lies on the curve. Point $Q$ is $(x, 0)$ on the x-axis. The Area of triangle $POQ$ is given by $A = \\frac{1}{2}(6x^2 - x^3)$. Given that $x$ is increasing at a constant rate of 2 units/sec, find the rate of change for the Area $A$ when (i) $x=2$, (ii) $x=5$.")

                st.write("**Visualizing the Geometry:**")
                st.write(
                    "Let's look at how the triangle changes shape as the point $P$ moves along the parabola. Notice how the triangle grows, but then gets 'squished' as it moves further right.")

                col_q15_v1, col_q15_v2 = st.columns(2)
                x_p = np.linspace(0, 6, 100)
                y_p = 6 * x_p - x_p ** 2

                def plot_q15_triangle(x_val, title):
                    y_val = 6 * x_val - x_val ** 2
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=x_p, y=y_p, mode='lines', name='y=6x-x²', line=dict(color='gray')))
                    fig.add_trace(go.Scatter(x=[0, x_val, x_val, 0], y=[0, 0, y_val, 0], fill='toself',
                                             fillcolor='rgba(0,204,150,0.4)', line=dict(color='#00CC96'),
                                             name=f'Triangle'))
                    fig.add_trace(
                        go.Scatter(x=[x_val], y=[y_val], mode='markers+text', text=["P(x,y)"], textposition="top right",
                                   marker=dict(size=8, color='white'), showlegend=False))
                    fig.update_layout(title=title, template="plotly_dark", height=250,
                                      margin=dict(t=30, b=10, l=10, r=10), showlegend=False)
                    return fig

                with col_q15_v1:
                    st.plotly_chart(plot_q15_triangle(2, "Situation (i): x = 2"), use_container_width=True)
                with col_q15_v2:
                    st.plotly_chart(plot_q15_triangle(5, "Situation (ii): x = 5"), use_container_width=True)

                st.write("**Detailed Solution:**")
                st.write(
                    "1. We are given the area formula $A(x) = 3x^2 - \\frac{1}{2}x^3$ and the speed $\\frac{dx}{dt} = 2$.")
                st.write(
                    "2. **Apply the Chain Rule:** To find how fast Area grows over time, we link it: $\\frac{dA}{dt} = \\frac{dA}{dx} \cdot \\frac{dx}{dt}$")
                st.latex(r"\frac{dA}{dx} = 6x - \frac{3}{2}x^2")

                st.write("---")
                st.write("**(i) When $x = 2$ (Triangle is getting taller and wider):**")
                st.latex(r"\frac{dA}{dx} = 6(2) - \frac{3}{2}(2)^2 = 12 - 6 = 6")
                st.latex(r"\frac{dA}{dt} = 6 \cdot 2 = 12 \text{ units}^2\text{/sec (Area is Increasing)}")

                st.write("**(ii) When $x = 5$ (Triangle gets wider but much shorter):**")
                st.latex(r"\frac{dA}{dx} = 6(5) - \frac{3}{2}(5)^2 = 30 - 37.5 = -7.5")
                st.latex(r"\frac{dA}{dt} = -7.5 \cdot 2 = -15 \text{ units}^2\text{/sec (Area is Decreasing)}")
    # =========================================================
        # =========================================================
        # TAB 3: OPTIMISATION
        # =========================================================
        with app_tabs[2]:
            st.subheader("🏗️ Industrial Engineering: Advanced Optimisation")
            st.write(
                "Optimisation uses derivatives to find the absolute maximum or minimum values of a physical quantity under given constraints. We will start from basic geometry and scale up to hardcore engineering.")

            # --- Level 1 & 2: Basic Optimisation ---
            with st.expander("🟢 Level 1: The Classic Fencing Problem"):
                st.markdown(
                    "**Problem:** A farmer has 100m of fencing to build a rectangular enclosure against a wall. What dimensions maximize area?")
                st.markdown("")
                st.write("1. **Constraint:** Perimeter is $2x + y = 100 \implies y = 100 - 2x$")
                st.write("2. **Objective Function (Area):** $A(x) = x \cdot y = 100x - 2x^2$")
                st.write("3. **Find Maximum:** $A'(x) = 100 - 4x = 0 \implies x = 25$. If $x=25$, $y=50$.")
                st.success("Max Area = $1250$ m².")

            with st.expander("🟡 Level 2: The Rotated Cone"):
                st.markdown(
                    "**Problem:** $\Delta ADB$ is a right-angled triangle with a fixed hypotenuse of $6\sqrt{3}$ cm. It is rotated about its vertical axis $AD$ to form a cone. Find the height ($h$) that generates the maximum volume.")
                st.markdown("")
                st.write("1. **Constraint (Pythagoras):** The hypotenuse is the slant height. Let radius be $r$.")
                st.latex(r"r^2 + h^2 = (6\sqrt{3})^2 = 108 \implies r^2 = 108 - h^2")
                st.write("2. **Objective Function (Volume):** Substitute $r^2$ to eliminate a variable:")
                st.latex(r"V(h) = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi (108 - h^2)h = 36\pi h - \frac{1}{3}\pi h^3")
                st.write("3. **Differentiate & Solve:**")
                st.latex(r"V'(h) = 36\pi - \pi h^2 = 0 \implies h^2 = 36 \implies h = 6 \text{ cm}")
                st.success("The maximum volume is achieved when the height is exactly 6 cm.")

            # --- Level 3: Structural Engineering ---
            with st.expander("🟠 Level 3: The Strongest Beam (Structural Engineering)", expanded=False):
                st.markdown(
                    "**Problem:** You must cut a rectangular beam from a cylindrical log of diameter $D=10$ cm. The physical **Strength ($S$)** of a beam is proportional to its width $b$ and the square of its height $h$ ($S = b \cdot h^2$). What dimensions ($b$ and $h$) maximize the beam's strength?")
                st.markdown("")

                col_b1, col_b2 = st.columns([1, 1])
                with col_b1:
                    st.write("**1. The Constraint (Pythagoras):**")
                    st.write("The corners of the rectangle touch the circle, so the diagonal is the diameter $D$.")
                    st.latex(r"b^2 + h^2 = D^2 \implies h^2 = 100 - b^2")

                    st.write("**2. The Objective Function:**")
                    st.latex(r"S(b) = b(100 - b^2) = 100b - b^3")

                    st.write("**3. Differentiate & Solve:**")
                    st.latex(r"S'(b) = 100 - 3b^2 = 0 \implies b = \frac{10}{\sqrt{3}} \approx 5.77 \text{ cm}")
                    st.latex(r"h = \sqrt{100 - (\frac{100}{3})} = 10\sqrt{\frac{2}{3}} \approx 8.16 \text{ cm}")
                    st.success(
                        r"**Golden Rule of Beams:** The strongest beam always has a height-to-width ratio of exactly $\sqrt{2}:1$. It is never a perfect square!")

                with col_b2:
                    b_slider = st.slider("Adjust Beam Width $b$:", 1.0, 9.9, 5.77, key="beam_width")
                    h_val = np.sqrt(100 - b_slider ** 2)
                    strength = b_slider * (h_val ** 2)

                    st.metric("Beam Strength (S = bh²)", f"{strength:.1f}", delta=f"{strength - 384.9:.1f} from Max")

                    fig_beam = go.Figure()
                    theta_circle = np.linspace(0, 2 * np.pi, 100)
                    fig_beam.add_trace(go.Scatter(x=5 * np.cos(theta_circle), y=5 * np.sin(theta_circle), mode='lines',
                                                  line=dict(color='saddlebrown', width=4), fill='toself',
                                                  fillcolor='rgba(139,69,19,0.2)'))
                    rect_x = [-b_slider / 2, b_slider / 2, b_slider / 2, -b_slider / 2, -b_slider / 2]
                    rect_y = [-h_val / 2, -h_val / 2, h_val / 2, h_val / 2, -h_val / 2]
                    fig_beam.add_trace(
                        go.Scatter(x=rect_x, y=rect_y, mode='lines', fill='toself', fillcolor='rgba(0,204,150,0.6)',
                                   line=dict(color='#00CC96', width=3)))

                    fig_beam.update_layout(template="plotly_dark", height=280, margin=dict(t=10, b=10, l=10, r=10),
                                           xaxis=dict(scaleanchor="y", scaleratio=1), showlegend=False)
                    st.plotly_chart(fig_beam, use_container_width=True)

            # --- Level 4: Cost Optimization ---
            with st.expander("🔴 Level 4: Manufacturing Cost Optimization"):
                st.markdown(
                    "**Problem:** You must design a cylindrical can holding $V = 1000\pi$ cm³. The material for the top and bottom caps is **3 times more expensive** than the side material. Find the radius $r$ and height $h$ that minimize total material cost.")
                st.markdown("")

                st.write("**1. The Cost Function:**")
                st.write("Let the cost of the side material be $k$ per cm². The top and bottom will cost $3k$ per cm².")
                st.latex(r"\text{Cost} = \text{Cost of Caps} + \text{Cost of Sides}")
                st.latex(r"C(r, h) = 2(\pi r^2)(3k) + (2\pi rh)(k) = 6\pi k r^2 + 2\pi k r h")

                st.write("**2. Eliminate $h$ using the Volume Constraint:**")
                st.latex(r"V = \pi r^2 h \implies 1000\pi = \pi r^2 h \implies h = \frac{1000}{r^2}")
                st.write("Substitute $h$ back into the Cost function:")
                st.latex(
                    r"C(r) = 6\pi k r^2 + 2\pi k r \left(\frac{1000}{r^2}\right) = 6\pi k r^2 + \frac{2000\pi k}{r}")

                st.write("**3. Differentiate & Find Minimum:**")
                st.write("Set $C'(r) = 0$ to find the minimum cost:")
                st.latex(r"C'(r) = 12\pi k r - \frac{2000\pi k}{r^2} = 0")
                st.latex(
                    r"12\pi k r = \frac{2000\pi k}{r^2} \implies 12r^3 = 2000 \implies r^3 = \frac{2000}{12} \approx 166.6")
                st.latex(r"r \approx 5.50 \text{ cm}")

                st.write("**4. Find the corresponding Height:**")
                st.latex(r"h = \frac{1000}{(5.50)^2} \approx 33.0 \text{ cm}")
                st.success(
                    "Result: The optimal ratio is $h:r = 6:1$. Because the caps are so expensive, calculus proves the cheapest can design must be very tall and skinny to minimize the use of the expensive cap material!")

            # --- Level 5: Fluid Dynamics ---
            with st.expander("🔥 Level 5: Optimal Fluid Dynamics (Trapezoidal Gutter)"):
                st.markdown(
                    "**Problem:** A metal sheet of width $W=30$ cm is folded into a gutter. The base and two sides each have a length of 10 cm. The sides are folded up at an angle $\\theta$. What angle maximizes the cross-sectional area (and thus water flow)?")
                st.markdown("")

                st.write("**1. Geometry of the Area:**")
                st.write(
                    "We need the area of a trapezoid: $A = \\frac{1}{2}(\\text{Top Width} + \\text{Base}) \\times \\text{Height}$.")
                st.write("- Base = 10")
                st.write("- Height $h = 10\sin\\theta$")
                st.write("- Top width = Base + 2(Horizontal Shift) = $10 + 2(10\cos\\theta) = 10 + 20\cos\\theta$")
                st.latex(
                    r"A(\theta) = \frac{10 + (10 + 20\cos\theta)}{2} \times 10\sin\theta = (10 + 10\cos\theta) \times 10\sin\theta = 100(1 + \cos\theta)\sin\theta")

                st.write("**2. Differentiate using Product Rule ($u = 1+\cos\\theta, v = \sin\\theta$):**")
                st.latex(r"A'(\theta) = 100 [ (-\sin\theta)(\sin\theta) + (1 + \cos\theta)(\cos\theta) ]")
                st.latex(r"A'(\theta) = 100 [ -\sin^2\theta + \cos\theta + \cos^2\theta ]")

                st.write("**3. Use Trig Identities to solve $A'(\\theta) = 0$:**")
                st.write("Convert everything to cosine using $\\sin^2\\theta = 1 - \\cos^2\\theta$:")
                st.latex(r"-(1 - \cos^2\theta) + \cos\theta + \cos^2\theta = 0")
                st.latex(r"2\cos^2\theta + \cos\theta - 1 = 0")

                st.write("Factor the quadratic equation:")
                st.latex(r"(2\cos\theta - 1)(\cos\theta + 1) = 0")
                st.latex(r"\cos\theta = \frac{1}{2} \implies \theta = 60^\circ")
                st.success(
                    "Result: The maximum flow occurs at exactly 60°. This proves that the most efficient open channel shape is exactly half of a perfect regular hexagon!")

                st.write("**Interactive Visualization:**")
                theta_deg = st.slider("Test Fold Angle θ (degrees):", 0, 90, 60, key="gutter_angle")
                theta_r = np.radians(theta_deg)
                area_val = 100 * (1 + np.cos(theta_r)) * np.sin(theta_r)

                st.metric("Cross-Sectional Area", f"{area_val:.1f} cm²", delta=f"{area_val - 129.9:.1f} from Max")

                fig_gut = go.Figure()
                gut_x = [-5, 5, 5 + 10 * np.cos(theta_r), -5 - 10 * np.cos(theta_r), -5]
                gut_y = [0, 0, 10 * np.sin(theta_r), 10 * np.sin(theta_r), 0]
                fig_gut.add_trace(go.Scatter(x=gut_x, y=gut_y, fill='toself', fillcolor='rgba(66, 135, 245, 0.5)',
                                             line=dict(color='#4287f5', width=3)))

                fig_gut.update_layout(template="plotly_dark", height=250, margin=dict(t=10, b=10, l=10, r=10),
                                      xaxis=dict(scaleanchor="y", scaleratio=1), xaxis_range=[-20, 20],
                                      yaxis_range=[-2, 15], showlegend=False)
                st.plotly_chart(fig_gut, use_container_width=True)

            # =========================================================
            # 终极挑战阶段 1：纯数学解法解答过河问题
            # =========================================================
            st.divider()
            st.markdown("### 🏆 The Ultimate Challenge: Optimization across Two Mediums")

            with st.expander("The Lifeguard / Canoe Problem (Solving with Calculus)"):
                st.markdown(
                    "**Problem:** Mukhriz rows his canoe from point A in the river to point C on the shore, then cycles from C to D. The perpendicular distance from A to shore B is $30$m. Total shore distance $BD = 400$m. His rowing speed is 40 m/min, and cycling speed is 50 m/min. Let $x$ be the distance from B to his landing point C. Find $x$ to minimize total travel time.")
                st.markdown("")

                st.write("**1. The Mathematical Model (Time = Distance / Speed):**")
                st.write("Total Time $T(x) = \\text{Time}_{\\text{row}} + \\text{Time}_{\\text{cycle}}$")
                st.write("- Rowing Distance (Pythagoras): $\sqrt{x^2 + 30^2}$")
                st.write("- Cycling Distance: $400 - x$")
                st.latex(r"T(x) = \frac{\sqrt{x^2 + 30^2}}{40} + \frac{400 - x}{50}")

                st.write("**2. The Derivative (Chain Rule):**")
                st.write("Set $T'(x) = 0$ to find the minimum time:")
                st.latex(r"T'(x) = \frac{1}{40} \cdot \frac{1}{2}(x^2+900)^{-1/2} \cdot (2x) - \frac{1}{50} = 0")
                st.latex(r"\frac{x}{40\sqrt{x^2 + 900}} - \frac{1}{50} = 0")

                st.write("**3. Solving the Algebra:**")
                st.latex(r"""
                \begin{aligned}
                \frac{x}{40\sqrt{x^2+900}} &= \frac{1}{50} \\
                50x &= 40\sqrt{x^2+900} \\
                5x &= 4\sqrt{x^2+900} \\
                \end{aligned}
                """)
                st.write("Square both sides:")
                st.latex(r"""
                \begin{aligned}
                25x^2 &= 16(x^2 + 900) \\
                25x^2 &= 16x^2 + 14400 \\
                9x^2 &= 14400 \\
                x^2 &= 1600 \implies x = 40 \text{ m}
                \end{aligned}
                """)
                st.success(
                    "Calculus proves that Mukhriz should land exactly 40m from point B to minimize his travel time.")

            # =========================================================
            # 终极挑战阶段 2：斯涅尔定律的视角转换
            # =========================================================
            with st.expander("🌌 The Grand Finale: Fermat's Principle & Snell's Law", expanded=True):
                st.markdown(
                    "Did you know **Light Rays** automatically solve the exact same calculus problem instantly? **Fermat's Principle** states that light takes the path of least time. Because light travels slower in water than in air, it bends when it hits the surface. This bending is governed by **Snell's Law**:")
                st.latex(r"\frac{\sin \theta_{water}}{v_{water}} = \frac{\sin \theta_{land}}{v_{land}}")
                st.markdown(
                    "[Image illustrating Fermat's Principle with a path crossing two different mediums, highlighting refraction similar to a lifeguard running on sand and swimming in water]")

                st.write("**How does the Canoe map to the Light Ray?**")
                st.write("Look at your calculus equation before we squared it:")
                st.latex(r"\frac{1}{40} \left( \frac{x}{\sqrt{x^2 + 900}} \right) = \frac{1}{50} (1)")

                st.write(
                    "Look at the interactive diagram below. $\\theta_{water}$ is the angle between the rowing path and the vertical Normal line. By basic trigonometry, $\\sin \\theta_{water} = \\frac{\\text{Opposite}}{\\text{Hypotenuse}} = \\frac{x}{\\sqrt{x^2+900}}$.")
                st.write(
                    "Because Mukhriz cycles completely flat along the shore, his angle to the Normal line is $90^\circ$. And $\\sin(90^\circ) = 1$.")

                x_snell = st.slider("Landing Point x (m):", 0, 150, 40, key="snell_slider")

                sin_theta_w = x_snell / np.sqrt(x_snell ** 2 + 30 ** 2) if x_snell != 0 else 0
                ratio_w = sin_theta_w / 40
                ratio_l = 1.0 / 50

                fig_snell = go.Figure()
                fig_snell.add_shape(type="rect", x0=0, y0=0, x1=150, y1=40, fillcolor="rgba(0, 191, 255, 0.1)",
                                    line_width=0)
                fig_snell.add_shape(type="rect", x0=0, y0=-20, x1=150, y1=0, fillcolor="rgba(34, 139, 34, 0.1)",
                                    line_width=0)

                fig_snell.add_trace(
                    go.Scatter(x=[0, x_snell], y=[30, 0], mode='lines+markers', name='Rowing in Water (v=40)',
                               line=dict(color='#00BFFF', width=3)))
                fig_snell.add_trace(
                    go.Scatter(x=[x_snell, 150], y=[0, 0], mode='lines+markers', name='Cycling on Land (v=50)',
                               line=dict(color='#32CD32', width=4)))

                # Normal Line
                fig_snell.add_trace(go.Scatter(x=[x_snell, x_snell], y=[-15, 40], mode='lines', name='Normal Line',
                                               line=dict(color='white', dash='dash')))

                # Arrows & Angles
                fig_snell.add_annotation(x=x_snell - 5, y=10, text="θ_water", showarrow=True, arrowhead=2, ax=15,
                                         ay=-15, font=dict(color="#00BFFF", size=13))
                fig_snell.add_annotation(x=x_snell + 20, y=-5, text="θ_land = 90°", showarrow=True, arrowhead=2, ax=-20,
                                         ay=10, font=dict(color="#32CD32", size=13))
                fig_snell.add_annotation(x=x_snell, y=43, text="Normal Line", showarrow=False,
                                         font=dict(color="white", size=12))

                fig_snell.update_layout(template="plotly_dark", height=300, margin=dict(t=10, b=10, l=10, r=10),
                                        showlegend=True, yaxis=dict(scaleanchor="x", scaleratio=1))
                st.plotly_chart(fig_snell, use_container_width=True)

                col_s1, col_s2 = st.columns(2)
                with col_s1:
                    st.info(
                        f"**Water Side Calculation:** \n\n $\\frac{{\\sin \\theta_{{water}}}}{{40}} = {ratio_w:.5f}$")
                with col_s2:
                    st.success(f"**Land Side Calculation:** \n\n $\\frac{{\\sin 90^\\circ}}{{50}} = {ratio_l:.5f}$")

                if abs(ratio_w - ratio_l) < 0.0001:
                    st.error(
                        "🤯 **PERFECT MATCH!** At $x=40$, the ratios are equal. The derivative equation $T'(x)=0$ you solved earlier is literally Snell's Law in disguise! Calculus is the source code of reality.")

            # =========================================================
            # 重构后的超详细彩虹题 (隐函数求导)
            # =========================================================
            with st.expander("🌈 Bonus Challenge: The Rainbow Angle (Implicit Differentiation)"):
                st.markdown(
                    "**The Mystery:** Why do rainbows always appear as a 42-degree circle in the sky? It's a pure calculus optimization problem happening inside millions of raindrops.")
                st.markdown("")

                st.write("**The Physics Setup:**")
                st.write(
                    "When sunlight enters a spherical raindrop, it refracts (bends), reflects off the back wall, and refracts again as it exits. The total deflection angle $D$ of the light ray depends on the angle it enters (the incidence angle $\\theta_i$) and the refracted angle inside the drop ($\\theta_r$).")
                st.write("The deflection is modeled by the equation:")
                st.latex(r"D = \pi + 2\theta_i - 4\theta_r")

                st.write(
                    "These two angles are permanently linked by **Snell's Law** for water (where refractive index $k \\approx 1.33$):")
                st.latex(r"\sin\theta_i = k \sin\theta_r")

                st.write(
                    "To find where the rainbow is brightest, we must find the minimum deflection angle. We need to set $\\frac{dD}{d\\theta_i} = 0$.")

                st.divider()

                st.write("**Step 1: Implicit Differentiation on Snell's Law**")
                st.write(
                    "We differentiate both sides of $\\sin\\theta_i = k \\sin\\theta_r$ with respect to $\\theta_i$. Remember to use the Chain Rule for $\\theta_r$!")
                st.latex(r"\cos\theta_i = k \cos\theta_r \cdot \frac{d\theta_r}{d\theta_i}")
                st.write("Isolate the derivative of the inner angle:")
                st.latex(r"\frac{d\theta_r}{d\theta_i} = \frac{\cos\theta_i}{k\cos\theta_r}")

                st.write("**Step 2: Differentiate the Deflection Function**")
                st.write("Now differentiate $D = \pi + 2\\theta_i - 4\\theta_r$ with respect to $\\theta_i$:")
                st.latex(r"\frac{dD}{d\theta_i} = 0 + 2 - 4\frac{d\theta_r}{d\theta_i}")

                st.write("**Step 3: Set to Zero and Substitute**")
                st.latex(r"2 - 4\left(\frac{\cos\theta_i}{k\cos\theta_r}\right) = 0")
                st.latex(
                    r"2 = \frac{4\cos\theta_i}{k\cos\theta_r} \implies 2k\cos\theta_r = 4\cos\theta_i \implies k\cos\theta_r = 2\cos\theta_i")

                st.write("**Step 4: The Algebraic Masterstroke (Solving for $\\theta_i$)**")
                st.write(
                    "We have an equation with both $\\cos\\theta_r$ and $\\cos\\theta_i$. How do we get rid of $\\theta_r$? We square both sides and use trig identities!")
                st.latex(r"k^2 \cos^2\theta_r = 4 \cos^2\theta_i")
                st.write("Use the identity $\\cos^2 x = 1 - \sin^2 x$:")
                st.latex(r"k^2 (1 - \sin^2\theta_r) = 4 \cos^2\theta_i")

                st.write(
                    "Look back at our original Snell's Law: $\\sin\\theta_i = k \\sin\\theta_r$. Square it: $\\sin^2\\theta_i = k^2 \\sin^2\\theta_r$. Substitute this back in!")
                st.latex(r"k^2 - k^2\sin^2\theta_r = 4 \cos^2\theta_i")
                st.latex(r"k^2 - \sin^2\theta_i = 4 \cos^2\theta_i")

                st.write("Convert $\\sin^2\\theta_i$ to $(1 - \cos^2\\theta_i)$ so everything is in terms of cosine:")
                st.latex(r"k^2 - (1 - \cos^2\theta_i) = 4 \cos^2\theta_i")
                st.latex(r"k^2 - 1 + \cos^2\theta_i = 4 \cos^2\theta_i")
                st.latex(r"k^2 - 1 = 3 \cos^2\theta_i")
                st.latex(r"\cos\theta_i = \sqrt{\frac{k^2 - 1}{3}}")

                st.success(
                    "By plugging in the refractive index of water ($k = 1.333$), we find $\\cos\\theta_i \\approx 0.507$, which means $\\theta_i \\approx 59.4^\circ$. If you plug this incidence angle back into the deflection equation, you get exactly **42.5 degrees**. Calculus proves why every rainbow you will ever see sits at exactly that angle in the sky!")

#牛顿法


def render_numerical_methods():
    st.header("🧮 Part 3: Numerical Methods & Algorithms")
    st.write(
        "When traditional algebra hits a dead end, computer science and calculus step in. Welcome to the art of approximation.")

    num_tabs = st.tabs(["📘 1. The Philosophy", "⚙️ 2. The Engine (Simulator)", "⚠️ 3. Chaos & Failures"])

    # ==========================================
    # TAB 1: 理论哲学 (Transcendental, IVT, Linearization)
    # ==========================================
    with num_tabs[0]:
        st.markdown("### 1. The Foundation: Transcendental Equations")
        st.write("Why do we need complex algorithms? Consider this equation:")
        st.latex(r"\ln(x) + x - 2 = 0")
        st.write("""
        * **Algebraic Equations:** Contain only standard operations (e.g., $x^2 + 3x + 2 = 0$). Solvable by exact formulas.
        * **Transcendental Equations:** Contain logarithms, exponentials, or trig functions. They "transcend" standard algebra.
        """)
        st.info(
            "**Deep Insight:** 99% of equations in real-world physics or engineering cannot be solved analytically (by hand). **Numerical Methods** are the only way to find a solution.")

        st.divider()

        col_ivt1, col_ivt2 = st.columns([1.2, 1])
        with col_ivt1:
            st.markdown("### 2. Root Detection: Intermediate Value Theorem (IVT)")
            st.write("Before running a search algorithm, we must prove a root actually exists.")
            st.markdown(
                "**Theorem:** If $f(x)$ is continuous on the interval $[a, b]$, and $f(a) \cdot f(b) < 0$ (meaning they have opposite signs), a root MUST exist between them.")
            st.write("Testing our equation $f(x) = \ln(x) + x - 2$:")
            st.write("- At $x=1$: $f(1) = -1$ (Negative)")
            st.write("- At $x=2$: $f(2) \approx 0.693$ (Positive)")
            st.success(
                "Conclusion: A root definitely exists between $x=1$ and $x=2$. This narrows down our search area and provides an excellent initial guess $x_0$.")

        with col_ivt2:
            x_range = np.linspace(0.5, 3, 100)
            y_range = np.log(x_range) + x_range - 2
            fig_ivt = go.Figure()
            fig_ivt.add_trace(
                go.Scatter(x=x_range, y=y_range, mode='lines', name='f(x)', line=dict(color='#636EFA', width=3)))
            fig_ivt.add_hline(y=0, line_dash="dash", line_color="white")
            fig_ivt.add_trace(
                go.Scatter(x=[1, 2], y=[-1, 0.693], mode='markers+text', text=["f(1) is Negative", "f(2) is Positive"],
                           textposition=["bottom center", "top center"], marker=dict(size=12, color='#EF553B'),
                           name='Test Points'))
            fig_ivt.update_layout(template="plotly_dark", height=300, margin=dict(t=10, b=10, l=10, r=10),
                                  showlegend=False)
            st.plotly_chart(fig_ivt, use_container_width=True)

        st.divider()

        st.markdown("### 3. The Core Tool: The 'Slope Triangle' Geometry")
        st.write(
            "Finding the root of a curve is hard, but finding the root of a straight line is elementary math. Instead of complex calculus, let's build the formula using a simple **Right Triangle**.")

        # 1. 回忆初中斜率公式
        st.write("**Step 1: The Basic Slope Formula**")
        st.write(
            "Remember from middle school that the slope $m$ of a line is 'rise over run' (vertical change divided by horizontal change). In calculus, the slope of the tangent line is the derivative $f'(x_n)$.")
        st.latex(r"m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}")

        # 2. 构造三角形 (对应你截图里的绝佳逻辑)
        st.write("**Step 2: Finding the 'Triangle' on the Graph**")
        st.write(
            "Imagine drawing a tangent line at point $A(x_n, f(x_n))$ on the curve. This line slides down the slope and hits the x-axis at our next guess, point $B(x_{n+1}, 0)$.")
        st.write("These two points create a right triangle:")
        st.markdown("""
                * **Vertical side (Height):** The y-coordinate of point A, which has a length of $f(x_n)$.
                * **Horizontal side (Width):** The distance between our two guess points, which is $x_n - x_{n+1}$.
                """)

        # 3. 代入斜率公式
        st.write("**Step 3: Plugging into the Slope Formula**")
        st.write("Substitute these specific lengths into our slope formula from Step 1:")
        st.latex(r"f'(x_n) = \frac{f(x_n) - 0}{x_n - x_{n+1}}")

        # 4. 简单的代数移项
        st.write("**Step 4: Isolating the Next Guess**")
        st.write(
            "Now, we use basic algebra to solve for our next guess, $x_{n+1}$. First, swap the denominator with the slope:")
        st.latex(r"x_n - x_{n+1} = \frac{f(x_n)}{f'(x_n)}")

        st.write(
            "Finally, move $x_n$ over and flip the signs to completely isolate $x_{n+1}$. This gives us the famous Newton-Raphson iteration formula:")

        # 5. 最终公式
        st.latex(r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}")

        # 删掉那句 st.markdown，替换成真正的 Streamlit 图片代码：
        st.image("newtonRaphsonMethod.png", caption="Geometric Derivation of Newton's Method", use_container_width=True)

    # ==========================================
    # TAB 2: 算法引擎 (Convergence & Simulator)
    # ==========================================
    with num_tabs[1]:
        st.markdown("### 4 & 5. Linear vs. Quadratic Convergence")
        st.write(
            "The algorithm feeds the output of the previous step back into the formula as the new input. But what makes Newton's method the absolute king of algorithms is its **convergence speed**.")

        # 新增：对比平方收敛和线性收敛的深度解释
        col_conv1, col_conv2 = st.columns(2)
        with col_conv1:
            st.success("**Quadratic Convergence (The Superpower)**")
            st.write(
                "Normally, Newton's method is quadratic ($e_{n+1} \approx C \cdot e_n^2$). This means the number of accurate decimal places **DOUBLES** with every step!")
            st.markdown("""
            * **Step 1:** Error $0.1$ (1 accurate digit)
            * **Step 2:** Error $0.01$ (2 accurate digits)
            * **Step 3:** Error $0.0001$ (4 accurate digits)
            * **Step 4:** Error $0.00000001$ (8 accurate digits)
            """)
            st.write("🏃‍♂️ **Analogy:** It's like **teleporting** closer to your destination.")

        with col_conv2:
            st.error("**Linear Convergence (The Trap)**")
            st.write(
                "If the root is a **Multiple Root** (the curve 'kisses' the x-axis instead of piercing it), both $f(x)$ and slope $f'(x)$ approach zero simultaneously. The formula loses its power ($e_{n+1} \approx 0.5 \cdot e_n$).")
            st.markdown("""
            * **Step 1:** Error $0.1$
            * **Step 2:** Error $0.05$
            * **Step 3:** Error $0.025$
            * **Step 4:** Error $0.0125$
            """)
            st.write(
                "🚶‍♂️ **Analogy:** It's like **walking** slowly to your destination, gaining only a fraction of a digit per step.")
            st.markdown("")

        st.divider()

        st.markdown("### 🕹️ Live Newton-Raphson Simulator")

        # 完美呼应 Tab 1 的超越方程
        mode = st.radio("Choose a scenario to test:",
                        ["A. Transcendental Equation (Watch the explosive Quadratic Convergence!)",
                         "B. The 'Double Root' Trap (Watch it degrade to slow Linear Convergence)"])

        if 'nr_step_main' not in st.session_state:
            st.session_state.nr_step_main = 0

        # 根据用户的选择设定目标方程
        if "Transcendental" in mode:
            # 使用 Tab 1 的方程，保持教学连贯性
            f_str = r"f(x) = \ln(x) + x - 2 = 0"
            df_str = r"f'(x) = \frac{1}{x} + 1"
            start_val = 0.5  # 刻意设得远一点，展示恐怖的收敛速度
            x_min, x_max = 0.1, 4.0
            y_min, y_max = -3, 3

            def get_f(x):
                return np.log(x) + x - 2 if x > 0 else float('nan')

            def get_df(x):
                return (1 / x) + 1 if x > 0 else float('nan')
        else:
            # 保留重根陷阱，展示线性收敛的龟速
            f_str = r"f(x) = x^3 - 3x + 2 = 0 \text{ (Double root at x=1)}"
            df_str = r"f'(x) = 3x^2 - 3"
            start_val = 2.5
            x_min, x_max = 0.0, 3.0
            y_min, y_max = -2, 10

            def get_f(x):
                return x ** 3 - 3 * x + 2

            def get_df(x):
                return 3 * x ** 2 - 3

        st.latex(f"\\text{{Solving: }} {f_str} \quad \quad \\text{{Derivative: }} {df_str}")

        col_sim1, col_sim2 = st.columns([1, 1.5])

        with col_sim1:
            x0 = st.slider("Select Initial Guess $x_0$:", x_min + 0.1, x_max, start_val, step=0.1, key="sim_slider")

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("Iterate +1 Step", use_container_width=True):
                    st.session_state.nr_step_main += 1
            with col_btn2:
                if st.button("Reset", use_container_width=True):
                    st.session_state.nr_step_main = 0

            # 计算过程
            history = [x0]
            # 防御处理：避免初始值为负数时的报错
            safe_f0 = get_f(x0)
            errors = [abs(safe_f0) if not np.isnan(safe_f0) else 999]
            curr_x = x0

            for _ in range(st.session_state.nr_step_main):
                if curr_x <= 0 and "Transcendental" in mode:
                    break  # 绝对防御：防止ln(负数)崩溃

                f_val = get_f(curr_x)
                df_val = get_df(curr_x)
                if abs(df_val) < 1e-9: break  # 防止分母为0

                curr_x = curr_x - (f_val / df_val)
                history.append(curr_x)
                errors.append(abs(get_f(curr_x)))

            st.metric(f"Current Guess (Step {st.session_state.nr_step_main})", f"{history[-1]:.8f}")
            st.metric("Current Error |f(x)|", f"{errors[-1]:.2e}")

            if st.session_state.nr_step_main > 0:
                if "Transcendental" in mode:
                    st.success(
                        "Quadratic Convergence! The exponent of the error roughly doubles every step. We conquered the Transcendental Equation instantly.")
                else:
                    st.error(
                        "Linear Convergence detected! Because the curve is flat at the root ($f'(x) \\approx 0$), the algorithm loses its superpower. It crawls slowly toward the answer.")

        with col_sim2:
            x_plot = np.linspace(x_min, x_max, 200)
            # 处理超越方程的绘图数据
            if "Transcendental" in mode:
                y_plot = np.where(x_plot > 0, np.log(x_plot) + x_plot - 2, np.nan)
            else:
                y_plot = get_f(x_plot)

            fig_nr = go.Figure()

            # 绘制主函数曲线
            fig_nr.add_trace(
                go.Scatter(x=x_plot, y=y_plot, mode='lines', line=dict(color='gray', width=3), name='f(x)'))
            fig_nr.add_hline(y=0, line_color="white")

            # 动态绘制切线跳跃过程
            for i in range(len(history) - 1):
                xn = history[i]
                xn_next = history[i + 1]
                fn = get_f(xn)
                dfn = get_df(xn)

                # 如果是历史步骤，用半透明的线画出痕迹
                if i < len(history) - 2:
                    fig_nr.add_trace(go.Scatter(x=[xn, xn_next], y=[fn, 0], mode='lines',
                                                line=dict(color='rgba(0, 204, 150, 0.3)', width=1), showlegend=False))
                    fn_next_hist = get_f(xn_next)
                    if not np.isnan(fn_next_hist):
                        fig_nr.add_trace(go.Scatter(x=[xn_next, xn_next], y=[0, fn_next_hist], mode='lines',
                                                    line=dict(color='rgba(255, 255, 255, 0.2)', dash='dot', width=1),
                                                    showlegend=False))

                # 如果是最新的一步，重点高亮
                else:
                    fig_nr.add_trace(go.Scatter(x=[xn], y=[fn], mode='markers', marker=dict(size=10, color='red'),
                                                name='Point of Tangency'))

                    # 绘制真实切线
                    tangent_x = np.array([x_min, x_max])
                    tangent_y = dfn * (tangent_x - xn) + fn
                    fig_nr.add_trace(go.Scatter(x=tangent_x, y=tangent_y, mode='lines',
                                                line=dict(color='rgba(255, 161, 90, 0.5)', dash='dash', width=2),
                                                name='True Tangent Line'))

                    # 绘制跳跃线
                    fig_nr.add_trace(go.Scatter(x=[xn, xn_next], y=[fn, 0], mode='lines+markers',
                                                line=dict(color='#00CC96', width=4), marker=dict(size=8),
                                                name=f'Jump (Step {i + 1})'))

                    # 重置高度的虚线
                    fn_next = get_f(xn_next)
                    if not np.isnan(fn_next):
                        fig_nr.add_trace(go.Scatter(x=[xn_next, xn_next], y=[0, fn_next], mode='lines',
                                                    line=dict(color='white', dash='dot', width=2), name='Reset Height'))

            fig_nr.update_layout(template="plotly_dark", height=400, margin=dict(t=10, b=10, l=10, r=10),
                                 xaxis_range=[x_min, x_max], yaxis_range=[y_min, y_max])
            st.plotly_chart(fig_nr, use_container_width=True)

        # ==========================================
        # TAB 3: 算法灾难实验室 (Failure Modes & Chaos)
        # ==========================================
        with num_tabs[2]:
            st.markdown("### 6. The Dark Side: Divergence & Failure Modes")
            st.write(
                "An advanced algorithm engineer must know exactly when their tools will break. Let's physically simulate the three fatal flaws of Newton's method:")

            # 使用单选按钮让用户切换不同的“翻车”场景
            fail_mode = st.radio("🚨 Select a Failure Mode to Simulate:",
                                 ["A. The Flat Spot (Zero Derivative)",
                                  "B. Overshooting (Flung into the void)",
                                  "C. Endless Oscillation (The Ping-Pong trap)"],
                                 horizontal=True)

            st.divider()

            col_f_text, col_f_plot = st.columns([1, 1.5])

            with col_f_text:
                # 动态生成每个模式的解释和初始参数
                if "Flat Spot" in fail_mode:
                    st.error("**A. The Flat Spot (Zero Derivative)**")
                    st.write(
                        "If you accidentally start your guess at a local minimum or maximum, the tangent line is perfectly horizontal ($f'(x)=0$).")
                    st.latex(r"x_{n+1} = x_n - \frac{f(x_n)}{0} \rightarrow \text{Crash!}")
                    st.write("**Target:** $f(x) = x^3 - 3x + 1$")
                    st.write("**Start Point:** $x_0 = 1.0$ (At the valley bottom)")
                    x0 = 1.0

                    def f(x):
                        return x ** 3 - 3 * x + 1

                    def df(x):
                        return 3 * x ** 2 - 3

                elif "Overshooting" in fail_mode:
                    st.warning("**B. Overshooting**")
                    st.write(
                        "If the slope is very flat, the tangent line shoots millions of miles away. It throws your next guess completely out of bounds.")
                    st.write("**Target:** $f(x) = \\arctan(x)$")
                    st.write("**Start Point:** $x_0 = 1.5$")
                    x0 = 1.5

                    def f(x):
                        return np.arctan(x)

                    def df(x):
                        return 1 / (1 + x ** 2)

                else:
                    st.info("**C. Endless Oscillation**")
                    st.write(
                        "For certain equations, the tangent lines will ping-pong back and forth across the y-axis symmetrically forever. It enters an infinite loop.")
                    st.write("**Target:** $f(x) = \sqrt[3]{x}$")
                    st.write("**Start Point:** $x_0 = 1.0$")
                    x0 = 1.0

                    # Python 对负数开三次方有复数问题，这里用 sign(x)*abs(x)^(1/3) 解决
                    def f(x):
                        return np.sign(x) * np.abs(x) ** (1 / 3)

                    def df(x):
                        return (1 / 3) * np.abs(x) ** (-2 / 3) if x != 0 else 0

                # 为每个模式创建独立的步数记录，防止切换时报错
                step_key = f"fail_step_{fail_mode}"
                if step_key not in st.session_state:
                    st.session_state[step_key] = 0

                col_fb1, col_fb2 = st.columns(2)
                if col_fb1.button("Iterate +1 Step", key=f"btn_step_{fail_mode}", use_container_width=True):
                    st.session_state[step_key] += 1
                if col_fb2.button("Reset", key=f"btn_reset_{fail_mode}", use_container_width=True):
                    st.session_state[step_key] = 0

                # 翻车模拟计算核心
                history = [x0]
                curr_x = x0
                crashed = False

                for i in range(st.session_state[step_key]):
                    val_df = df(curr_x)
                    # 触发 A 模式崩溃
                    if abs(val_df) < 1e-9:
                        crashed = True
                        break
                    curr_x = curr_x - f(curr_x) / val_df
                    history.append(curr_x)

                if crashed:
                    st.error("💥 CRASH! Division by zero detected. Algorithm terminated.")
                else:
                    st.metric(f"Current Guess (Step {len(history) - 1})", f"{history[-1]:.4f}")

                # 补充震荡和起飞的提示
                if "Overshooting" in fail_mode and len(history) > 2:
                    st.warning("Look at the x-axis! The number is getting exponentially huge!")
                if "Oscillation" in fail_mode and len(history) > 2:
                    st.info(
                        "Notice the signs? Positive, negative, positive... It's doubling its distance away from the root every time!")

            with col_f_plot:
                fig_fail = go.Figure()

                # 动态计算绘图范围，让图表能“跟随”那些飞走的点
                min_x = min(history) if history else x0
                max_x = max(history) if history else x0
                pad = max(2, abs(max_x - min_x) * 0.5)
                pad = min(pad, 15)  # 限制最大 padding，防止直接缩放到看不清

                xp = np.linspace(min_x - pad, max_x + pad, 400)
                yp = f(xp)

                # 绘制主函数曲线
                fig_fail.add_trace(go.Scatter(x=xp, y=yp, mode='lines', line=dict(color='gray', width=3), name='f(x)'))
                fig_fail.add_hline(y=0, line_color="white")

                # 绘制翻车轨迹
                for i in range(len(history) - 1):
                    xn = history[i]
                    xn_next = history[i + 1]
                    fn = f(xn)
                    dfn = df(xn)

                    # 历史痕迹
                    if i < len(history) - 2:
                        fig_fail.add_trace(go.Scatter(x=[xn, xn_next], y=[fn, 0], mode='lines',
                                                      line=dict(color='rgba(239, 85, 59, 0.3)', width=1),
                                                      showlegend=False))
                        fn_next_val = f(xn_next)
                        fig_fail.add_trace(go.Scatter(x=[xn_next, xn_next], y=[0, fn_next_val], mode='lines',
                                                      line=dict(color='rgba(255, 255, 255, 0.2)', dash='dot', width=1),
                                                      showlegend=False))
                    else:
                        # 最新一步的高亮
                        fig_fail.add_trace(go.Scatter(x=[xn], y=[fn], mode='markers', marker=dict(size=10, color='red'),
                                                      name='Point of Tangency'))
                        fig_fail.add_trace(go.Scatter(x=[xn, xn_next], y=[fn, 0], mode='lines+markers',
                                                      line=dict(color='#EF553B', width=4), marker=dict(size=8),
                                                      name=f'Disaster Jump'))
                        if not crashed:
                            fn_next_val = f(xn_next)
                            fig_fail.add_trace(go.Scatter(x=[xn_next, xn_next], y=[0, fn_next_val], mode='lines',
                                                          line=dict(color='white', dash='dot', width=2),
                                                          name='Reset Height'))

                # 特殊处理：如果是分母为零崩溃，画一条平行的红色虚线
                if crashed and len(history) > 0:
                    xn = history[-1]
                    fn = f(xn)
                    fig_fail.add_trace(go.Scatter(x=[xn], y=[fn], mode='markers', marker=dict(size=10, color='red'),
                                                  name='Point of Tangency'))
                    fig_fail.add_trace(go.Scatter(x=[xn - pad, xn + pad], y=[fn, fn], mode='lines',
                                                  line=dict(color='#EF553B', width=4, dash='dash'),
                                                  name='Horizontal Tangent (Crash)'))

                fig_fail.update_layout(template="plotly_dark", height=400, margin=dict(t=10, b=10, l=10, r=10))
                st.plotly_chart(fig_fail, use_container_width=True)

            st.divider()


#integration

# 这是一个包含整个第三章所有逻辑和绘图的“超级函数”

def render_topic_integration():
    st.title("Chapter III: Integration")
    st.markdown(
        "Welcome to the **Integration** chapter! Here, math comes to life. Play with the interactive tools below to truly understand what integrals do.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "1. Basic Rules",
        "2. Trigo",
        "3. Techniques",
        "4. Interactive Area & Volume",
        "5. Trapezoidal Rule"
    ])

    # --- Tab 1 ~ 3 保持简洁清晰的静态展示 ---
    with tab1:
        st.header("Basic Integration")
        st.latex(r"\int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)")
        st.latex(r"\int \frac{1}{x} \, dx = \ln|x| + C")

    with tab2:
        st.header("Trigonometric Integration")
        st.latex(r"\int \sin x \, dx = -\cos x + C \quad \quad \int \cos x \, dx = \sin x + C")

    with tab3:
        st.header("Techniques of Integration")
        st.write("1. **Substitution:** " + r"$\int f(g(x))g'(x) \, dx = \int f(u) \, du$")
        st.write("2. **By Parts:** " + r"$\int u \, dv = uv - \int v \, du$")



        # --- Tab 4: 终极动态面积与旋转体积 (空白宽容 + 智能解析版) ---
        # ==========================================
        with tab4:
            st.header("Interactive Area & Volume Visualizer")
            st.write(
                "Calculate the area between two curves, choose the axis of revolution, and interact with the models! You can enter `pi`, `2pi`, `sqrt(2)`, or `e` for boundaries.")

            # 1. 用户交互区 UI
            col_axis, col_input1, col_input2 = st.columns([1, 1.5, 1.5])
            with col_axis:
                rotation_axis = st.radio("Axis of Revolution", ["X-axis", "Y-axis"])
            with col_input1:
                user_f = st.text_input("Top/Right Function $f(x)$", value="sin(x)")
                a_str = st.text_input("Lower Bound ($a = x_1$)", value="0")
            with col_input2:
                # 默认把 g(x) 设为空白，模拟学生的真实操作
                user_g = st.text_input("Bottom/Left Function $g(x)$", value="")
                b_str = st.text_input("Upper Bound ($b = x_2$)", value="2pi")

                # 2. 安全解析与数学引擎计算
                x_sym = sp.Symbol('x')
                try:
                    import re
                    def preprocess_formula(formula):
                        f = formula.replace('^', '**')
                        # 自动为常见函数补全括号
                        f = re.sub(r'(sqrt|sin|cos|tan|exp|log|ln)\s*([a-zA-Z])', r'\1(\2)', f)
                        # 自动把 "数字+字母" 中间补上乘号
                        f = re.sub(r'(\d)\s*([a-zA-Z\(])', r'\1*\2', f)
                        return f

                    safe_f_str = user_f.strip() if user_f.strip() else "0"
                    safe_g_str = user_g.strip() if user_g.strip() else "0"
                    safe_a_str = a_str.strip() if a_str.strip() else "0"
                    safe_b_str = b_str.strip() if b_str.strip() else "1"

                    safe_f = preprocess_formula(safe_f_str)
                    safe_g = preprocess_formula(safe_g_str)
                    safe_a = preprocess_formula(safe_a_str)
                    safe_b = preprocess_formula(safe_b_str)

                    # 【核心修复】：建立字典，强制把输入的字母 'e' 翻译成数学常数 E
                    local_dict = {'e': sp.E}

                    # 解析函数时带上字典
                    expr_f = sp.sympify(safe_f, locals=local_dict)
                    expr_g = sp.sympify(safe_g, locals=local_dict)

                    # 解析上下限时也带上字典 (这样学生在 Bound 里输 e 也没问题)
                    a = float(sp.sympify(safe_a, locals=local_dict).evalf())
                    b = float(sp.sympify(safe_b, locals=local_dict).evalf())

                    f_num = sp.lambdify(x_sym, expr_f, 'numpy')
                    g_num = sp.lambdify(x_sym, expr_g, 'numpy')

                    def f_val(val):
                        res = f_num(val)
                        return np.full_like(val, res) if np.isscalar(res) else res

                    def g_val(val):
                        res = g_num(val)
                        return np.full_like(val, res) if np.isscalar(res) else res

                    st.session_state['f_val_func'] = f_val
                    st.session_state['g_val_func'] = g_val

                except Exception as e:
                    st.error(
                        f"Syntax Error: Invalid math expression. You can use 'pi', '2pi', 'e', 'sqrt(2)', etc.\n\nDetail: {e}")
                    st.stop()

            # ===============================
            # 开始计算逻辑
            # ===============================
            if a >= b:
                st.error("Lower bound must be less than upper bound!")
            else:
                st.markdown("### Step-by-Step Solution")

                # 计算面积
                area_integral = expr_f - expr_g
                area_res, _ = integrate.quad(lambda val: f_val(val) - g_val(val), a, b)

                st.info("**1. Area Between Curves:**")
                st.latex(
                    rf"A = \int_{{{a}}}^{{{b}}} \left( ({sp.latex(expr_f)}) - ({sp.latex(expr_g)}) \right) dx = {area_res:.4f} \text{{ units}}^2")

                # 计算体积
                st.info(f"**2. Volume of Revolution (around {rotation_axis}):**")

                if rotation_axis == "X-axis":
                    st.write("Using the **Washer Method**: " + r"$V = \pi \int_a^b [f(x)^2 - g(x)^2] dx$")
                    vol_res = np.pi * integrate.quad(lambda val: (f_val(val)) ** 2 - (g_val(val)) ** 2, a, b)[0]
                    st.latex(
                        rf"V_x = \pi \int_{{{a}}}^{{{b}}} \left( ({sp.latex(expr_f)})^2 - ({sp.latex(expr_g)})^2 \right) dx")
                else:
                    st.write("Using the **Cylindrical Shell Method**: " + r"$V = 2\pi \int_a^b x[f(x) - g(x)] dx$")
                    vol_res = 2 * np.pi * integrate.quad(lambda val: val * (f_val(val) - g_val(val)), a, b)[0]
                    st.latex(
                        rf"V_y = 2\pi \int_{{{a}}}^{{{b}}} x \left( ({sp.latex(expr_f)}) - ({sp.latex(expr_g)}) \right) dx")

                st.success(f"**Final Volume:** {vol_res:.4f} units³")

                # ===============================
                # 3. 动态绘图 (全 Plotly 双雄)
                # ===============================
                st.markdown("### Visualizations")

                col_plot1, col_plot2 = st.columns(2)

                # --- 左图：Plotly 2D 交互式全景图 ---
                with col_plot1:
                    fig_2d = go.Figure()

                    span = b - a
                    if span < 1e-3: span = 1.0
                    x_wide = np.linspace(a - span * 1.5, b + span * 1.5, 500)

                    fig_2d.add_trace(go.Scatter(x=x_wide, y=f_val(x_wide), mode='lines', name='$f(x)$',
                                                line=dict(color='blue', width=2)))
                    fig_2d.add_trace(go.Scatter(x=x_wide, y=g_val(x_wide), mode='lines', name='$g(x)$',
                                                line=dict(color='red', width=2)))

                    x_fill = np.linspace(a, b, 200)
                    fig_2d.add_trace(
                        go.Scatter(x=x_fill, y=g_val(x_fill), mode='lines', line=dict(width=0), showlegend=False,
                                   hoverinfo='skip'))
                    fig_2d.add_trace(go.Scatter(x=x_fill, y=f_val(x_fill), mode='lines', fill='tonexty',
                                                fillcolor='rgba(135, 206, 235, 0.5)', line=dict(width=0),
                                                name='Integral Area', hoverinfo='skip'))

                    fig_2d.add_hline(y=0, line_color="black", line_width=1)
                    fig_2d.add_vline(x=0, line_color="black", line_width=1)

                    fig_2d.update_layout(
                        title="2D Area (Scroll to Zoom, Drag to Pan)",
                        margin=dict(l=0, r=0, b=0, t=40),
                        hovermode="x unified",
                        xaxis=dict(zeroline=False),
                        yaxis=dict(zeroline=False),
                        height=400
                    )
                    st.plotly_chart(fig_2d, use_container_width=True)

                # --- 右图：Plotly 交互式 3D 旋转模型 ---
                with col_plot2:
                    theta = np.linspace(0, 2 * np.pi, 60)
                    u = np.linspace(a, b, 100)
                    U, Theta = np.meshgrid(u, theta)
                    fig_3d = go.Figure()

                    if rotation_axis == "X-axis":
                        X_out, Y_out, Z_out = U, f_val(U) * np.cos(Theta), f_val(U) * np.sin(Theta)
                        X_in, Y_in, Z_in = U, g_val(U) * np.cos(Theta), g_val(U) * np.sin(Theta)
                    else:
                        X_out, Y_out, Z_out = U * np.cos(Theta), f_val(U), U * np.sin(Theta)
                        X_in, Y_in, Z_in = U * np.cos(Theta), g_val(U), U * np.sin(Theta)

                    fig_3d.add_trace(
                        go.Surface(x=X_out, y=Y_out, z=Z_out, colorscale='Blues', opacity=0.9, name='Outer',
                                   showscale=False))
                    fig_3d.add_trace(go.Surface(x=X_in, y=Y_in, z=Z_in, colorscale='Reds', opacity=0.5, name='Inner',
                                                showscale=False))

                    fig_3d.update_layout(
                        title="3D Volume (Drag to Rotate)",
                        margin=dict(l=0, r=0, b=0, t=40),
                        scene=dict(xaxis_title='X Axis', yaxis_title='Y Axis', zaxis_title='Z Axis'),
                        height=400
                    )
                    st.plotly_chart(fig_3d, use_container_width=True)

            # ==========================================
            # --- Tab 5: 动态交互版梯形法则 (支持双曲线 & 防崩溃) ---
            # ==========================================
            with tab5:
                st.header("Interactive Numerical Integration: Trapezoidal Rule")
                st.write(
                    "See how the number of trapezoids ($n$) affects the accuracy of the area between the two curves.")

                # 【拦截保护】：如果 a >= b，或者 Tab 4 的函数解析失败，直接不跑后续代码
                if a >= b:
                    st.warning(
                        "⚠️ Please ensure Lower Bound ($a$) is less than Upper Bound ($b$) in Tab 4 to view this section.")
                elif 'f_val_func' not in st.session_state or 'g_val_func' not in st.session_state:
                    st.warning("⚠️ Please enter valid functions in Tab 4 first.")
                else:
                    n_slider = st.slider("Number of Trapezoids ($n$)", min_value=1, max_value=50, value=6)

                    # 从全局状态提取函数
                    current_f = st.session_state['f_val_func']
                    current_g = st.session_state['g_val_func']

                    # 为 Tab 5 独立计算精确面积，防止跨 Tab 变量丢失
                    exact_area, _ = integrate.quad(lambda val: current_f(val) - current_g(val), a, b)

                    # 计算梯形法则
                    x_trap = np.linspace(a, b, n_slider + 1)
                    y_trap_f = current_f(x_trap)
                    y_trap_g = current_g(x_trap)

                    # 梯形的高度是两曲线之差
                    y_trap_diff = y_trap_f - y_trap_g
                    trap_res = np.trapz(y_trap_diff, x_trap)

                    st.success(f"**Trapezoidal Estimate:** {trap_res:.4f}")
                    st.write(f"Compare this with the exact integral: {exact_area:.4f}")

                    # 绘制双曲线之间的梯形
                    fig_trap, ax_t = plt.subplots(figsize=(8, 4), dpi=100)

                    span = b - a
                    x_smooth = np.linspace(a - span * 0.2, b + span * 0.2, 300)

                    ax_t.plot(x_smooth, current_f(x_smooth), 'b-', linewidth=2, label="$f(x)$")
                    ax_t.plot(x_smooth, current_g(x_smooth), 'r-', linewidth=2, label="$g(x)$")

                    # 画梯形：连接 f(x) 和 g(x) 之间的空间
                    for i in range(n_slider):
                        verts = [
                            (x_trap[i], y_trap_g[i]),
                            (x_trap[i], y_trap_f[i]),
                            (x_trap[i + 1], y_trap_f[i + 1]),
                            (x_trap[i + 1], y_trap_g[i + 1])
                        ]
                        poly = Polygon(verts, facecolor='lightgreen', edgecolor='green', alpha=0.4, linewidth=1.5)
                        ax_t.add_patch(poly)

                        # 画出梯形的上下边，视觉更清晰
                        ax_t.plot([x_trap[i], x_trap[i + 1]], [y_trap_f[i], y_trap_f[i + 1]], 'g--', alpha=0.8)
                        ax_t.plot([x_trap[i], x_trap[i + 1]], [y_trap_g[i], y_trap_g[i + 1]], 'g--', alpha=0.8)

                    ax_t.set_title(f"Approximation with {n_slider} Trapezoids")
                    ax_t.grid(True, linestyle='--', alpha=0.5)
                    ax_t.legend()
                    st.pyplot(fig_trap)

# 4. 占位符模块
# ==========================================
def render_coming_soon(topic_name):
    """
    渲染一个“敬请期待”的页面，供未完成的章节调用。
    """
    st.title(topic_name)
    st.markdown("---")

    # 显示黄色的警告框
    st.warning(f"🚧 **{topic_name}** is currently under construction!")

    # 英文介绍文本
    st.write(
        "Welcome to the uncharted territories of this section. Our team is currently working hard to forge interactive visualizations and high-quality content for you.")

    # 放一个进度条装饰一下
    st.progress(0)



# ==========================================
# 你的其他章节渲染函数放在这个下面
# ==========================================
# def render_integration_chapter():
# ...

# ==========================================
# ==========================================
# 5. 主程序入口 (极简叙事版)
# ==========================================
def main():
    st.sidebar.title("🧮 Mathovator")
    st.sidebar.caption("Matrikulasi Innovation Project")

    # 定义菜单：前面保持原样，微积分部分开启 Saga 叙事
    menu_options = [
        "Topic 1: Number Systems",
        "Topic 2: Equations & Inequalities",
        "Topic 3: Sequences & Series",
        "Topic 4: Matrices",
        "Topic 5: Linear Equations",
        "Topic 6: Polynomials",
        "Topic 7: Trigonometry",

        # === 唯一的高亮区域：微积分史诗 ===
        "--- 📜 THE CALCULUS SAGA ---",
        "0. The Grand Tale (Overview)",  # 总览故事
        "Chapter I: Limits (The Paradox)",  # 极限
        "Chapter II: Differentiation (The Motion)", # 微分
        "Chapter III: Integration (The Area)"  # 积分
    ]

    # 侧边栏选择
    topic_selection = st.sidebar.selectbox("Navigate:", menu_options)

    # 动态显示氛围感
    if "Topic" in topic_selection:
        st.sidebar.markdown("---")
        st.sidebar.caption("Classical Mathematical Structures")
    elif "Chapter" in topic_selection or "Grand Tale" in topic_selection:
        st.sidebar.markdown("---")
        st.sidebar.success("🔥 Exploring the Science of Change.")

    st.sidebar.markdown("---")

    # === 路由逻辑 (Routing) ===

    # 1. 微积分总览
    # 1. 如果用户选到了那个带横线的“主题标题”，自动帮他跳转到 Grand Tale
    if topic_selection == "--- 📜 THE CALCULUS SAGA ---":
        render_calculus_grand_story()
    if topic_selection == "0. The Grand Tale (Overview)":
        render_calculus_grand_story()

        # 2. 前置章节 (直接根据原名跳转)
    elif topic_selection == "Topic 1: Number Systems":
        render_topic_1_number_system()

    elif topic_selection == "Topic 3: Sequences & Series":
        render_topic_3_sequence()

    # 其他还没做的代数 Topic 占位
    elif "Topic" in topic_selection:
        render_coming_soon(topic_selection)

    # 3. 微积分章节 (Saga 系列)
    elif topic_selection == "Chapter I: Limits (The Paradox)":
        render_topic_8_limits()



    elif topic_selection == "Chapter II: Differentiation (The Motion)":

        # 1. 更新二级子菜单，加入 Part 3

        sub_chapter = st.radio(

            "📖 Select Section:",

            ["Part 1: Core Concepts & Intuition", "Part 2: Real-World Applications",
             "Part 3: Numerical Methods (The Algorithm)"],

            horizontal=True

        )

        st.divider()

        # 2. 逻辑分流

        if sub_chapter == "Part 1: Core Concepts & Intuition":

            render_topic_differentiation()


        elif sub_chapter == "Part 2: Real-World Applications":

            render_applications()


        elif sub_chapter == "Part 3: Numerical Methods (The Algorithm)":

            render_numerical_methods()  # 调用我们要写的新函数

    elif topic_selection == "Chapter III: Integration (The Area)":
        render_topic_integration()

if __name__ == "__main__":
    main()