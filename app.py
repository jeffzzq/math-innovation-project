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

        # Sub-Tab 3: 3D 螺旋 (保留)
        elif physics_step == "3. Dimension Up: The 3D Helix":
            with col1:
                st.markdown("### Euler's Formula: The Ultimate Form")
                cols = st.columns(4)
                if 'euler_t_3d' not in st.session_state: st.session_state['euler_t_3d'] = 2.0
                if cols[0].button("0"): st.session_state['euler_t_3d'] = 0.0
                if cols[1].button("π/2"): st.session_state['euler_t_3d'] = np.pi / 2
                if cols[2].button("π"): st.session_state['euler_t_3d'] = np.pi
                if cols[3].button("2π"): st.session_state['euler_t_3d'] = 2 * np.pi
                t_3d = st.slider("Time Flow (t)", 0.0, 4 * np.pi, float(st.session_state['euler_t_3d']), key='slider_3d_helix')
                st.session_state['euler_t_3d'] = t_3d
                if abs(t_3d - np.pi) < 0.1: st.error("🌟 **Moment of Truth**: When t = π, the helix rotates exactly half a circle and lands on Real -1!")
            with col2:
                t_range = np.linspace(0, 4 * np.pi, 300)
                x_helix = t_range
                y_helix = np.cos(t_range)
                z_helix = np.sin(t_range)
                fig = go.Figure()
                fig.add_trace(go.Scatter3d(x=x_helix, y=y_helix, z=z_helix, mode='lines', line=dict(color='#00ADB5', width=5), name='e^it (Helix)'))
                fig.add_trace(go.Scatter3d(x=x_helix, y=np.ones_like(t_range) * 2, z=z_helix, mode='lines', line=dict(color='#FF2E63', width=3), opacity=0.5, name='Sin(t) Proj'))
                fig.add_trace(go.Scatter3d(x=x_helix, y=y_helix, z=np.ones_like(t_range) * -2, mode='lines', line=dict(color='#FDB827', width=3), opacity=0.5, name='Cos(t) Proj'))
                cur_x, cur_y, cur_z = t_3d, np.cos(t_3d), np.sin(t_3d)
                fig.add_trace(go.Scatter3d(x=[cur_x], y=[cur_y], z=[cur_z], mode='markers', marker=dict(size=10, color='#FF2E63')))
                fig.add_trace(go.Scatter3d(x=[cur_x, cur_x, cur_x], y=[2, cur_y, cur_y], z=[cur_z, cur_z, -2], mode='lines', line=dict(color='#FF2E63', dash='dash')))
                fig.update_layout(scene=dict(xaxis_title='Time (t)', yaxis_title='Real', zaxis_title='Imag', aspectmode='manual', aspectratio=dict(x=2, y=1, z=1), xaxis=dict(range=[0, 13]), yaxis=dict(range=[-2, 2]), zaxis=dict(range=[-2, 2])), height=500, margin=dict(l=0, r=0, b=0, t=0))
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
# 5. 主程序入口
# ==========================================
def main():
    st.sidebar.title("📚 Matri-X Navigation")
    topic_selection = st.sidebar.radio(
        "Select Chapter:",
        [
            "Topic 1: Number Systems",
            "Topic 2: Equations & Inequalities",
            "Topic 3: Sequences & Series",
            "Topic 4: Matrices",
            "Topic 5: Linear Equations",
            "Topic 6: Polynomials",
            "Topic 7: Trigonometry",
        ]
    )
    st.sidebar.markdown("---")
    st.sidebar.caption("Designed for Matrikulasi Innovation")

    if topic_selection == "Topic 1: Number Systems":
        render_topic_1_number_system()
    elif topic_selection == "Topic 2: Equations & Inequalities":
        render_coming_soon("Topic 2: Equations & Inequalities")
    elif topic_selection == "Topic 3: Sequences & Series":
        render_topic_3_sequence()  # <--- 这里调用了新函数！
    else:
        render_coming_soon(topic_selection)

if __name__ == "__main__":
    main()