import streamlit as st
import numpy as np
import plotly.graph_objects as go
import scipy.stats as stats  # <--- 新增：用于二项分布计算
import math

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

import math
import streamlit as st
import numpy as np
import plotly.graph_objects as go


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

    with tab4:
        st.subheader("The Architecture of Chance")

        col_ctrl, col_vis = st.columns([1.2, 2.5])

        with col_ctrl:
            st.markdown("### 1. Build the Triangle")
            n_rows = st.slider("Number of Rows (n)", 0, 15, 5)
            p_val = st.slider("Probability of Right Turn (p)", 0.0, 1.0, 0.5, 0.1)

            st.markdown("---")
            st.markdown("### 2. Live Calculation")

            # 动态计算演示
            k_demo = n_rows // 2
            coeff_demo = math.comb(n_rows, k_demo)
            prob_demo = stats.binom.pmf(k_demo, n_rows, p_val)

            st.info(f"**Focus on Term k={k_demo}**")
            st.write("1️⃣ **Path Count:**")
            st.latex(rf"\binom{{{n_rows}}}{{{k_demo}}} = {coeff_demo}")
            st.write("2️⃣ **Probability:**")
            st.latex(rf"P = {prob_demo:.4f}")

        with col_vis:
            st.markdown("#### The Expanding Pyramid")

            fig_tri = go.Figure()

            # 🔥 这里的循环逻辑确保了每一行都被画出来
            for r in range(n_rows + 1):
                row_coeffs = [math.comb(r, k) for k in range(r + 1)]
                ys = [-r] * (r + 1)
                xs = np.linspace(-r, r, r + 1) if r > 0 else [0]

                is_current = (r == n_rows)

                # 颜色逻辑：适配浅色背景
                if is_current:
                    color = '#00ADB5'
                    text_color = 'white'
                    opacity = 1.0
                else:
                    color = 'rgba(100, 100, 100, 0.3)'  # 更深的灰色，确保白底能看见
                    text_color = 'rgba(0, 0, 0, 0.5)'  # 黑色字
                    opacity = 0.8

                fig_tri.add_trace(go.Scatter(
                    x=xs, y=ys,
                    mode='markers+text',
                    text=[str(c) for c in row_coeffs],
                    textfont=dict(color=text_color, size=12),
                    marker=dict(size=30, color=color, symbol='circle', opacity=opacity),
                    hoverinfo='text',
                    hovertext=[f"Row {r}, k={k}: {c} paths" for k, c in enumerate(row_coeffs)],
                    showlegend=False
                ))

            fig_tri.update_layout(
                height=400,
                xaxis=dict(visible=False, range=[-(n_rows + 1), (n_rows + 1)]),
                yaxis=dict(visible=False, range=[-(n_rows + 0.5), 0.5]),
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=0, t=20, b=0),
                title=f"Pascal's Triangle (Rows 0-{n_rows})"
            )
            st.plotly_chart(fig_tri, use_container_width=True)

            # 柱状图 + Normal Curve 修复
            st.markdown(f"#### Probability Distribution")
            x_k = np.arange(0, n_rows + 1)
            probs = stats.binom.pmf(x_k, n_rows, p_val)

            fig_bar = go.Figure()
            # 1. Bar Chart
            fig_bar.add_trace(go.Bar(x=x_k, y=probs, name='Binomial', marker_color='#FDB827'))

            # 2. Normal Curve Overlay
            mu = n_rows * p_val
            sigma = math.sqrt(n_rows * p_val * (1 - p_val))
            if sigma > 0:
                x_norm = np.linspace(0, n_rows, 200)
                y_norm = stats.norm.pdf(x_norm, mu, sigma)
                fig_bar.add_trace(go.Scatter(x=x_norm, y=y_norm, mode='lines', name='Normal Curve',
                                             line=dict(color='#00ADB5', width=3)))

            fig_bar.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0))
            st.plotly_chart(fig_bar, use_container_width=True)

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
            **Why was Calculus invented? Not for homework, but for Faith.**

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
            st.image("https://upload.wikimedia.org/wikipedia/commons/d/d4/Johannes_Kepler_1610.jpg",
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
                    $$ v = \frac{\Delta d}{\Delta t} = \frac{0}{0} $$
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
                    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d4/Johannes_Kepler_1610.jpg",
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

            # --- 4. 英国学派 (前驱) ---
            with giant_t4:
                st.markdown("#### The Direct Predecessors")

                # --- 巴罗 ---
                c_b1, c_b2 = st.columns([1, 3])
                with c_b1:
                    st.image("https://upload.wikimedia.org/wikipedia/commons/2/23/Isaac_Barrow.jpg",
                             caption="Barrow (1630-1677)", use_container_width=True)
                with c_b2:
                    st.markdown("**Isaac Barrow (The Mentor)**")
                    st.write("Newton's teacher at Cambridge.")
                    st.write(
                        "He discovered the **Fundamental Theorem of Calculus** geometrically using the **'Differential Triangle'**.")
                    st.write("He famously resigned his professorship so the young Newton could take his place.")

                st.divider()

                # --- 沃利斯 ---
                c_w1, c_w2 = st.columns([1, 3])
                with c_w1:
                    st.image("https://upload.wikimedia.org/wikipedia/commons/6/69/John_Wallis.jpg",
                             caption="Wallis (1616-1703)", use_container_width=True)
                with c_w2:
                    st.markdown("**John Wallis (The Arithmetician)**")
                    st.write("He shifted Calculus from Geometry (shapes) to **Algebra** (formulas).")
                    st.write("He introduced the symbol for infinity: $\infty$.")
                    st.write(
                        "He calculated integrals of powers like $x^{-1}$ and $x^{1/2}$ purely by arithmetic patterns.")
    # ==========================================
    # ERA IV: 诞生 (牛顿与莱布尼茨)
    # ==========================================
    with tabs[3]:
        st.subheader("🍎 Era IV: The Birth (1660s)")
        st.write("The separate problems (Tangents vs Areas) were unified into one system.")

        col_n, col_l = st.columns(2)

        with col_n:
            st.image("https://upload.wikimedia.org/wikipedia/commons/3/39/GodfreyKneller-IsaacNewton-1689.jpg",
                     width=150)
            st.markdown("**Isaac Newton (The Physicist)**")
            st.write("**Year:** 1665-1666 (The Plague Years).")
            st.write("**Concept:** **Fluxions** ($\dot{x}$).")
            st.write("**View:** Variables are flowing quantities (Motion).")
            st.write("**Publication:** Delayed until 1736 (he hated criticism).")
            st.info("He used this to prove Gravity and explain Kepler's Laws.")

        with col_l:
            st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Gottfried_Wilhelm_von_Leibniz.jpg", width=150)
            st.markdown("**G.W. Leibniz (The Logician)**")
            st.write("**Year:** 1684 (Published First).")
            st.write("**Concept:** **Differentials** ($dx$).")
            st.write("**View:** Curves are infinite tiny polygons (Geometry).")
            st.write("**Legacy:** He gave us the symbols $\int$ and $d$.")
            st.success("He discovered the Product Rule and Chain Rule.")

        st.divider()
        st.success(
            "🏆 **The Fundamental Theorem of Calculus:** They both proved that Differentiation (Slope) and Integration (Area) are **INVERSE** operations.")

    # ==========================================
    # ERA V: 危机 (贝克莱与贝叶斯)
    # ==========================================
    with tabs[4]:
        st.subheader("👻 Era V: The Crisis of Logic (1734)")
        st.write("Calculus worked, but its foundation was rotten. How can you divide by zero?")

        st.error("**The Attack: Bishop Berkeley**")
        st.write("Bishop Berkeley published *The Analyst* to attack the 'Infidel Mathematicians'.")
        st.markdown(
            "> *\"He divides by $dx$, so it is not zero. Then he throws it away, so it is zero. These are the **Ghosts of departed quantities**!\"*")
        st.write("He argued: If math rests on a 'Double Error', it is no better than religious mysticism.")

        st.info("**The Defense: d'Alembert & Bayes**")
        st.write("**d'Alembert (1754):** Suggested we need a theory of **Limits**, not tiny numbers.")
        st.write("**Thomas Bayes:** Argued that the logic of the *Ratio* holds true, even if the tiny numbers vanish.")
        st.write(
            "**Lagrange:** Tried to use Algebra (Taylor Series) to avoid Limits, but failed to handle convergence.")

    # ==========================================
    # ERA VI: 严谨化 (柯西、魏尔斯特拉斯、黎曼)
    # ==========================================
    with tabs[5]:
        st.subheader("🏁 Era VI: The Reign of Rigor (19th Century)")
        st.write("It took 150 years to banish the ghosts.")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**1. Cauchy (The Limit)**")
            st.write("1821. He defined the Limit strictly. We don't reach zero, we analyze the **Trend**.")
            st.latex(r"\lim_{x \to c} f(x) = L")
        with c2:
            st.markdown("**2. Weierstrass (The Logic)**")
            st.write("1874. He removed all 'motion' intuition. He created the **Epsilon-Delta** definition.")
            st.latex(r"\forall \epsilon > 0, \exists \delta > 0...")
        with c3:
            st.markdown("**3. Riemann (The Integral)**")
            st.write("1854. He formalized Integration as the limit of sums of rectangles (**Riemann Sums**).")

        st.write("This ended the Second Math Crisis. Calculus was now solid rock.")

    # ==========================================
    # ERA VII: 现代视界 (实变与勒贝格)
    # ==========================================
    with tabs[6]:
        st.subheader("🚀 Era VII: Modern Horizons (20th Century)")
        st.write("Just when we thought we were done, **Pathological Functions** appeared.")

        st.markdown("**The Problem:**")
        st.write(
            "Functions like the Dirichlet Function (1 if rational, 0 if irrational) are impossible to integrate with Riemann's method (too many jumps).")

        st.markdown("**The Solution: Henri Lebesgue (1902)**")
        st.write("Lebesgue reinvented Integration. Instead of slicing the Domain ($x$), he sliced the Range ($y$).")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Riemann Integration**")
            st.caption("Vertical Slicing")
            st.write("Summing vertical bars.")
            st.progress(80)
        with col2:
            st.markdown("**Lebesgue Integration**")
            st.caption("Horizontal Layering (Measure)")
            st.write("Summing horizontal layers (Measure Theory).")
            st.progress(100)

        # 勒贝格可视化
        fig_leb = go.Figure()
        x_vals = np.linspace(0, 10, 50)
        y_vals = np.sin(x_vals) + 2
        # 黎曼 (竖条)
        fig_leb.add_trace(go.Bar(x=x_vals, y=y_vals, name="Riemann (Vertical)", marker_color='rgba(0, 173, 181, 0.5)'))
        # 勒贝格 (横线示意)
        fig_leb.add_trace(go.Scatter(x=[0, 10], y=[2.5, 2.5], mode='lines', name="Lebesgue (Horizontal Layer)",
                                     line=dict(color='red', dash='dash')))
        fig_leb.update_layout(height=300, margin=dict(t=30, b=10), title="Riemann vs Lebesgue Concept")
        st.plotly_chart(fig_leb, use_container_width=True)

        st.success(
            "This led to **Real Analysis** and **Functional Analysis**, the math that powers Quantum Mechanics today.")

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
    st.header("🌉 Chapter I: Limits & Continuity")

    # 剧情回顾：连接 Grand Tale
    with st.expander("🔙 Recap: Banish the Ghosts", expanded=False):
        st.write(
            "In the Grand Tale, we saw Berkeley's attack on $0/0$. **Limits** are the surgical tools that fix this logical contradiction.")

    t1, t2, t3 = st.tabs(["The Toolkit (Calculation)", "The Handshake (Existence)", "Repair Game (Continuity)"])

    # --- Tab 1: 计算工具箱 ---
    with t1:
        st.subheader("🧰 The Surgical Tools for 0/0")
        choice = st.radio("Choose your tool:", ["Factorization", "Conjugate"], horizontal=True)
        if "Factorization" in choice:
            st.latex(r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2} \frac{(x-2)(x+2)}{(x-2)} = 4")
            st.caption("We surgically remove the 'problem term' $(x-2)$ that causes the error.")
        else:
            st.latex(r"\lim_{x \to 0} \frac{\sqrt{x+9}-3}{x} = \frac{1}{6}")
            st.caption("Using the 'Conjugate Mirror' to clear the square root.")

    # --- Tab 2: 存在性 (左右极限) ---
    with t2:
        st.subheader("🤝 The Handshake Rule")
        st.write(
            "A limit exists only if the traveler from the Left and the traveler from the Right meet at the same point.")

        # 交互：断桥实验
        broken = st.toggle("Break the Bridge")
        x = np.linspace(0, 4, 100)
        # 如果 broken 为真，右半部分向上平移
        y = np.where(x < 2, x ** 2, (x + 2 if broken else x ** 2))

        fig = go.Figure(go.Scatter(x=x, y=y, line=dict(color='#00ADB5', width=3)))
        st.plotly_chart(fig, use_container_width=True)
        st.write("Result: " + ("❌ Limit DNE (L ≠ R)" if broken else "✅ Limit Exists (L = R)"))

    # --- Tab 3: 连续性修复游戏 ---
    with t3:
        st.subheader("🔧 The Continuity Repair")
        st.info("Remember the 'Removable Discontinuity'? You can fix the function by moving this point.")

        # 滑块：移动点的高度
        target_y = st.slider("Adjust f(2) height", 0.0, 8.0, 1.0)

        x_line = np.linspace(0, 4, 100)
        y_line = x_line + 2
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_line, y=y_line, name='Function Path', line=dict(color='gray')))
        fig.add_trace(
            go.Scatter(x=[2], y=[target_y], mode='markers', marker=dict(size=15, color='#FDB827'), name='Your Point'))
        st.plotly_chart(fig, use_container_width=True)

        # 判定是否修复成功
        if abs(target_y - 4.0) < 0.1:
            st.success("🎉 Repair Successful! The function is now continuous.")


# ==========================================
# Chapter II: Differentiation (The Motion) - 第二章：微分
# ==========================================
def render_topic_differentiation():
    st.header("📈 Chapter II: Differentiation (The Knife)")

    # 剧情回顾
    with st.expander("🔙 Recap: The Snapshot of the Moment", expanded=False):
        st.write(
            "Newton invented differentiation to calculate planetary speed. It is essentially finding the ultimate direction of a slope as the gap vanishes.")

    t1, t2, t3 = st.tabs(["First Principles", "Visual Gallery", "Parametric (God's Eye)"])

    # --- Tab 1: 第一性原理 (割线变切线) ---
    with t1:
        st.subheader("🔍 The Microscopic Definition")
        st.latex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")

        # 滑块：h 趋近于 0
        h = st.slider("Let distance h approach 0", 0.01, 2.0, 1.0)

        x = np.linspace(0, 3, 100)
        # 计算割线数据
        x1, x2 = 1.0, 1.0 + h
        m = (x2 ** 2 - x1 ** 2) / (x2 - x1)  # 斜率
        y_secant = x1 ** 2 + m * (x - x1)  # 割线方程

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=x ** 2, name='Curve'))
        fig.add_trace(go.Scatter(x=[x1, x2], y=[x1 ** 2, x2 ** 2], mode='markers', marker=dict(color='red')))
        fig.add_trace(go.Scatter(x=x, y=y_secant, line=dict(dash='dash'), name='Secant to Tangent'))
        st.plotly_chart(fig, use_container_width=True)

        if h < 0.1:
            st.success("🌟 Miracle Moment: The Secant line has become the Tangent! The slope is now the derivative.")

    # --- Tab 2: 导数画廊 ---
    with t2:
        st.subheader("🎨 Derivative Gallery")
        f_type = st.selectbox("Choose a function:", ["Polynomial (x³)", "Trigonometric (sin x)", "Exponential (eˣ)"])
        x = np.linspace(-3, 3, 100)

        # 根据选择生成不同的函数数据
        if "x³" in f_type:
            y, yp = x ** 3, 3 * x ** 2
        elif "sin" in f_type:
            y, yp = np.sin(x), np.cos(x)
        else:
            y, yp = np.exp(x), np.exp(x)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, name='Original f(x)'))
        fig.add_trace(go.Scatter(x=x, y=yp, name="Derivative f'(x) (Slope)", line=dict(dash='dot')))
        st.plotly_chart(fig, use_container_width=True)

    # --- Tab 3: 参数方程 (上帝视角) ---
    with t3:
        st.subheader("🌀 Parametric: Beyond x and y")
        st.write("In physics, $x$ and $y$ are often controlled by Time ($t$).")

        # 滑块：控制时间 t
        t_val = st.slider("Time (t)", 0.0, 6.28, 0.0)
        st.latex(r"x = \cos(t), \quad y = \sin(t)")

        t_range = np.linspace(0, 6.28, 100)
        fig = go.Figure(go.Scatter(x=np.cos(t_range), y=np.sin(t_range), name='Motion Path'))

        # 红色标记点代表粒子位置
        fig.add_trace(
            go.Scatter(x=[np.cos(t_val)], y=[np.sin(t_val)], mode='markers', marker=dict(size=15, color='red')))
        fig.update_layout(width=400, height=400)
        st.plotly_chart(fig, use_container_width=True)


# ==========================================
# 4. 占位符模块
# ==========================================
def render_coming_soon(topic_name):
    st.title(f"🚧 {topic_name}")
    st.markdown("---")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.info("⚠️ Lab Under Construction...")
        st.write("We are coding deep visualizations for this topic.")
        st.progress(10)
    with col2:
        st.warning("Developer Mode: Module Not Linked")

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
        "Chapter II: Differentiation (The Motion)",  # 微分
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
        render_topic_differentiation()

    elif topic_selection == "Chapter III: Integration (The Area)":
        render_coming_soon("Integration (The Area)")

if __name__ == "__main__":
    main()