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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "1. The Evolution (History)",
    "2. Complex Logic (Rotation)",
    "3. Polar Coordinates",
    "4. Euler's Formula",
    "5. The Power of i (Real-World Impact)"
])

# ---------------------------------------------------------
# TAB 1: 维度的史诗 (Equations & The Evolution of Numbers)
# ---------------------------------------------------------
with tab1:
    st.subheader("🌌 Topic 1: The Equation Driven Evolution")
    st.write(
        "Textbooks often teach numbers as a boring list of categories: $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$. But history tells a different story. New dimensions of numbers were not 'invented'—they were **forced into existence** when mathematicians hit the wall of impossible equations.")
    st.markdown("---")

    # 创建 7 个子标签页来仔细讲述每一段历史
    sub_tabs = st.tabs([
        "1. The Absurd Debt",
        "2. Pythagoras' Blood",
        "3. The Math Mafia",
        "4. The Grand Duel",
        "5. The Ghost Dimension",
        "6. The Quintic Wall",
        "7. Algorithms"
    ])

    # ==========================================
    # 1. 线性方程与整数
    # ==========================================
    with sub_tabs[0]:
        st.header("🐑 Act 1: The Absurd Debt")
        col_txt, col_fig = st.columns([1.2, 1])
        with col_txt:
            st.info("**The Equation:** $x + 5 = 3$")
            st.write("""
            **The Context:** Early humans only needed **Natural Numbers ($\mathbb{N}$)**. If you have 3 sheep and someone asks for 5, the transaction is simply impossible. 

            **The Crisis:** For centuries, European mathematicians called negative answers *numeri absurdi* (absurd numbers). They refused to write them down, treating equations like $x + 5 = 3$ as "unsolvable."

            **The Breakthrough:** In 628 AD, Indian mathematician **Brahmagupta** changed the world. He realized that numbers didn't just represent physical objects; they could represent **concepts**. He defined positive numbers as "Fortunes" and negative numbers as **"Debts."** By accepting debt, the number line was stretched backwards into the void, giving birth to **Integers ($\mathbb{Z}$)**.
            """)
            st.latex(r"ax + b = 0 \implies x = -\frac{b}{a}")

        with col_fig:
            fig1 = go.Figure()
            fig1.add_shape(type="line", x0=-5, y0=0, x1=5, y1=0, line=dict(color="gray", width=2))
            fig1.add_trace(
                go.Scatter(x=[1, 2, 3], y=[0] * 3, mode='markers+text', text=["1", "2", "3"], textposition="top center",
                           marker=dict(size=12, color='#00ADB5'), name='N (Objects)'))
            fig1.add_trace(go.Scatter(x=[-2], y=[0], mode='markers+text', text=["-2 (Debt)"], textposition="top center",
                                      marker=dict(size=18, color='#FF2E63', symbol="star"), name='Z (Debt)'))
            fig1.add_annotation(x=0, y=0.5, text="Expanding Left", showarrow=True, arrowhead=2, ax=50, ay=0,
                                font=dict(color="#FF2E63", size=14))
            fig1.update_layout(title="Expanding the 1D Line", xaxis=dict(range=[-5, 5]),
                               yaxis=dict(range=[-2, 2], visible=False), template="plotly_dark", height=350)
            st.plotly_chart(fig1, use_container_width=True)

    # ==========================================
    # 2. 二次方程与无理数
    # ==========================================
    with sub_tabs[1]:
        st.header("📐 Act 2: Pythagoras' Blood")
        col_txt, col_fig = st.columns([1.2, 1])
        with col_txt:
            st.warning("**The Equation:** $x^2 = 2$")
            st.write("""
            **The Context:** The Ancient Greeks worshipped proportions. They believed the universe was built entirely on **Rational Numbers ($\mathbb{Q}$)** (fractions like $\\frac{1}{2}$ or $\\frac{3}{4}$). 

            **The Crisis:** A Pythagorean named **Hippasus** tried to calculate the diagonal of a square with sides of length 1. Using the Pythagorean theorem, the diagonal must be a number $x$ where $x^2 = 2$. Hippasus proved that this number could **never** be written as a fraction.

            **The Tragedy:** This revelation destroyed the Pythagorean worldview. Legend says they took Hippasus out on a boat and **drowned him at sea** to keep the secret. 

            Eventually, humanity had to accept these "flawed" numbers. They were named **Irrational Numbers**, filling the microscopic black holes in the **Real Number Line ($\mathbb{R}$)**.
            """)
            st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

        with col_fig:
            fig2 = go.Figure()
            fig2.add_shape(type="line", x0=0, y0=0, x1=3, y1=0, line=dict(color="gray", width=2))
            fig2.add_trace(
                go.Scatter(x=[0, 1, 1, 0, 0], y=[0, 0, 1, 1, 0], mode='lines', line=dict(color='gray', dash='dot'),
                           name='Square'))
            fig2.add_trace(
                go.Scatter(x=[0, 1], y=[1, 0], mode='lines', line=dict(color='#FDB827', width=3), name='Diagonal'))
            fig2.add_trace(go.Scatter(x=[np.sqrt(2)], y=[0], mode='markers+text', text=["√2 (Irrational)"],
                                      textposition="top right", marker=dict(size=15, color='#FF2E63', symbol='diamond'),
                                      name='Root'))
            fig2.update_layout(title="The Geometry Crisis", xaxis=dict(range=[-0.5, 2.5]),
                               yaxis=dict(range=[-0.5, 1.5], visible=False), template="plotly_dark", height=350)
            st.plotly_chart(fig2, use_container_width=True)

        # ==========================================
        # 3. 三次方程与意大利黑帮 (完整公式版)
        # ==========================================
            # ==========================================
            # 3. 三次方程与意大利黑帮 (30:0 决斗细节版)
            # ==========================================
            with sub_tabs[2]:
                st.header("🗡️ Act 3: The Math Mafia")
                col_txt, col_fig = st.columns([1.2, 1])
                with col_txt:
                    st.error("**The Equation:** $x^3 + px = q$")
                    st.write("""
                    **The Context:** Welcome to 16th-century Italy, where math was a bloodsport. University jobs were won through public "Math Duels." If you discovered a new formula, you kept it as a deadly secret weapon to destroy your rivals.

                    **The Arrogant Apprentice:** A mathematician named Scipione del Ferro secretly solved the cubic equation. On his deathbed, he whispered the formula to his student, **Fior**. Fior was a mediocre mathematician, but armed with this "secret weapon," he thought he was invincible. He arrogantly challenged **Tartaglia** (a brilliant scholar left with a stutter after a childhood sword wound) to a public duel.

                    **The 30-0 Slaughter:** The rules were simple: they exchanged 30 math problems. Fior confidently submitted 30 cubic equations, expecting to humiliate Tartaglia. Panic set in for Tartaglia, but in the middle of the night just before the deadline, his sheer genius took over. He not only deduced Fior's secret trick, but mastered the entire cubic system. Tartaglia solved all 30 of Fior's problems in two hours. Fior, who only knew one memorized trick, couldn't solve a single problem from Tartaglia. **Tartaglia won 30 to 0, destroying Fior's career.**

                    **The Betrayal:** A famous Milanese doctor and gambler, **Gerolamo Cardano**, begged Tartaglia for this invincible formula. Tartaglia shared it only after Cardano swore a holy religious oath never to publish it. 

                    Years later, Cardano found del Ferro's old notes. Feeling his oath to Tartaglia was void, Cardano published the formula in his masterpiece, *Ars Magna* (1545). Tartaglia was humiliated, and the formula went down in history under Cardano's name.
                    """)

                    # 完整的卡尔达诺公式：展示出它恐怖的对称性和嵌套结构
                    st.latex(
                        r"x = \sqrt[3]{\frac{q}{2} + \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}} + \sqrt[3]{\frac{q}{2} - \sqrt{\frac{q^2}{4} + \frac{p^3}{27}}}")

                with col_fig:
                    fig3 = go.Figure()
                    x_plot = np.linspace(-3, 3, 100)
                    y_plot = x_plot ** 3 - 3 * x_plot
                    fig3.add_shape(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="white", width=2))
                    fig3.add_trace(
                        go.Scatter(x=x_plot, y=y_plot, mode='lines', line=dict(color='#FF2E63', width=4),
                                   name='Cubic Weapon'))
                    fig3.add_annotation(x=0, y=5, text="The Ultimate Weapon", showarrow=False,
                                        font=dict(size=18, color="#FF2E63"))
                    fig3.update_layout(title="The Battlefield of Cubics", xaxis=dict(range=[-4, 4]),
                                       yaxis=dict(range=[-10, 10]), template="plotly_dark", height=400)  # 稍微加高了一点点适应新文本
                    st.plotly_chart(fig3, use_container_width=True)

    # ==========================================
    # 4. 四次方程与世纪决斗
    # ==========================================
    with sub_tabs[3]:
        st.header("🛡️ Act 4: The Grand Duel")
        col_txt, col_fig = st.columns([1.2, 1])
        with col_txt:
            st.error("**The Equation:** $x^4 + px^2 + qx + r = 0$")
            st.write("""
            **The Context:** Furious at the betrayal, Tartaglia challenged Cardano. But Cardano hid behind his secret weapon: his former servant-turned-prodigy, **Ludovico Ferrari**.

            **The 4D Master:** Ferrari was a monster of intellect. Not only had he mastered the Cubic, but at age 20, he successfully mapped out the 4th degree: **The Quartic Equation**. 

            His solution was horrifyingly long. To solve a Quartic, you first had to build a "Resolvent Cubic" equation:
            """)
            st.latex(r"y^3 - p y^2 - 4r y + (4pr - q^2) = 0")
            st.write("""
            **The Showdown:** In 1548, a grand public duel was held in Milan. Tartaglia walked in confident, only to face Ferrari's monstrous 4th-degree math. Ferrari's formulas were so advanced and his eloquence so dominating that Tartaglia realized he was outmatched. 

            Fearing the angry Milanese crowd, Tartaglia **fled the city in the middle of the night**, leaving the Cardano-Ferrari duo as the undisputed kings of Algebra.
            """)

        with col_fig:
            fig4 = go.Figure()
            x_plot = np.linspace(-3, 3, 100)
            y_plot2 = x_plot ** 4 - 4 * x_plot ** 2
            fig4.add_shape(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="white", width=2))
            fig4.add_trace(go.Scatter(x=x_plot, y=y_plot2, mode='lines', line=dict(color='#00ADB5', width=4),
                                      name='Quartic Superiority'))
            fig4.add_annotation(x=0, y=5, text="Ferrari's 4D Counter-Attack", showarrow=False,
                                font=dict(size=18, color="#00ADB5"))
            fig4.update_layout(title="1548 Milan Duel: The Quartic", xaxis=dict(range=[-3, 3]),
                               yaxis=dict(range=[-5, 15]), template="plotly_dark", height=350)
            st.plotly_chart(fig4, use_container_width=True)

            # ==========================================
            # 5. 虚数维度的诞生 (完美契合图片与三次方程悖论)
            # ==========================================
            with sub_tabs[4]:
                st.header("👻 Act 5: The Ghost Dimension")
                col_txt, col_fig = st.columns([1.2, 1])

                with col_txt:
                    st.write("""
                    **The First Encounter:** Imaginary numbers first appeared as a bizarre puzzle. In his book *Ars Magna* (as seen in the image), Cardano posed a seemingly simple problem: **"Divide 10 into two parts whose product is 40."**
                    """)
                    st.latex(r"x(10 - x) = 40 \implies x^2 - 10x + 40 = 0")
                    st.write("""
                    Using the quadratic formula, he got $5 + \sqrt{-15}$ and $5 - \sqrt{-15}$. They perfectly add up to 10 and multiply to 40. But since a rectangle can't have a negative area, Cardano dismissed it. He called this process **"mental torture"** and famously concluded that it was **"as refined as it is useless."**
                    """)

                    st.success("**The Unignorable Paradox:** $x^3 = 15x + 4$")
                    st.write("""
                    Cardano thought he could ignore negative roots—until he hit the cubic equation above. Graph it, and the real answer physically exists: **$x = 4$**. 

                    But when he plugged the numbers into his "perfect" cubic formula, it spit out this monstrosity:
                    """)
                    st.latex(r"x = \sqrt[3]{2 + \sqrt{-121}} + \sqrt[3]{2 - \sqrt{-121}}")
                    st.write("""
                    **The Crisis:** He could no longer dismiss this as "useless"! The final answer ($4$) was real. How could the *only* mathematical path to a real answer force you to travel through impossible ghost numbers? 

                    **Bombelli's Bridge:** Decades later, **Rafael Bombelli** treated $\sqrt{-1}$ (which we now call $i$) as a real working gear. He found that $(2 + 11i) + (2 - 11i) = 4$. To solve 1D problems, numbers were forced to leap into the **2D Complex Plane ($\mathbb{C}$)** and perfectly cancel each other out to return safely. Imaginary numbers were suddenly very real.
                    """)

                with col_fig:
                    # 插入卡尔达诺的原著插图，完美对应左侧第一段文本
                    try:
                        st.image("cardano.jpg", caption="Ars Magna: '...as refined as it is useless.'",
                                 use_container_width=True)
                    except:
                        st.info("🖼️ [Placeholder: Insert your Cardano Ars Magna image here]")

                    st.markdown("<br>", unsafe_allow_html=True)  # 增加一点垂直间距让排版更好看

                    # 保留原本非常棒的跨维度桥梁图，对应左侧最后一段文本
                    fig5 = go.Figure()
                    fig5.add_shape(type="line", x0=-2, y0=0, x1=6, y1=0, line=dict(color="white", width=2))  # Real
                    fig5.add_shape(type="line", x0=0, y0=-15, x1=0, y1=15, line=dict(color="cyan", dash="dot"))  # Imag
                    fig5.add_trace(
                        go.Scatter(x=[0, 2], y=[0, 11], mode='lines+markers', line=dict(color='#E056FD', width=3),
                                   name='Jump to 2+11i'))
                    fig5.add_trace(
                        go.Scatter(x=[2, 4], y=[11, 0], mode='lines+markers', line=dict(color='#E056FD', width=3),
                                   name='Return via 2-11i'))
                    fig5.add_trace(go.Scatter(x=[4], y=[0], mode='markers+text', text=["Lands on Real 4"],
                                              textposition="bottom right", marker=dict(size=15, color='#00ADB5')))
                    fig5.update_layout(title="Bombelli's Dimensional Bridge", xaxis=dict(range=[-1, 6]),
                                       yaxis=dict(range=[-5, 15]), template="plotly_dark", height=300,
                                       margin=dict(l=0, r=0, t=30, b=0))
                    st.plotly_chart(fig5, use_container_width=True)

            # ==========================================
            # 6. 五次方程与绝笔信 (融入学术界的打压史与舍瓦利耶的托付)
            # ==========================================
            with sub_tabs[5]:
                st.header("🧱 Act 6: The Unsolvable Wall")
                col_txt, col_fig = st.columns([1.2, 1])

                with col_txt:
                    st.info("**The Equation:** $ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0$")
                    st.write("""
                    **The 300-Year Obsession:** After mastering degrees 1 through 4, humanity spent three centuries searching for the "Quintic Formula." Instead of a formula, they found tragedy. The two geniuses who finally solved the mystery were destroyed by the arrogance of the mathematical establishment.
                    """)

                    with st.expander("📖 Niels Henrik Abel: Ignored by the 'God' of Math", expanded=True):
                        st.write("""
                        In 1824, a starving 22-year-old Norwegian named **Niels Henrik Abel** proved the impossible: **The Quintic formula does not exist.** Too poor to publish his full proof, he condensed it into a dense 6-page pamphlet and mailed it to Carl Friedrich Gauss—the "Prince of Mathematics." Gauss, assuming it was the rambling of a crank, **threw the unread pamphlet into the trash.** Abel spent years wandering Europe in poverty, unrecognized. He contracted tuberculosis and died at age 26. Tragically, a letter offering him a prestigious professorship in Berlin arrived just two days after his death.
                        """)

                    with st.expander("🩸 Évariste Galois: Three Strikes and a Duel", expanded=True):
                        st.write("""
                        While Abel proved it was impossible, a fiery French teenager named **Évariste Galois** invented the math to explain *why*. But the French Academy repeatedly crushed him:

                        1. **Lost by Cauchy:** He sent his first paper to Cauchy, who simply lost it.
                        2. **Buried with Fourier:** He submitted it for a grand prize to Fourier, who died shortly after, taking the manuscript to his grave.
                        3. **Rejected by Poisson:** He sent it to Poisson, who returned it, labeling Galois's genius as *"incomprehensible."*

                        On May 29, 1832, Galois was challenged to a duel. Certain he would die the next morning, the 20-year-old stayed up all night frantically writing his mathematical testament in a letter to his friend, **Auguste Chevalier**. In the margins, he famously scribbled: **"Je n'ai pas le temps" (I have no time).**

                        He died from a gunshot wound to the stomach the next day. It took 14 years for another mathematician, Liouville, to decipher that letter and announce that this dead teenager had invented **Group Theory**—proving that the internal symmetry of a 5th-degree equation is permanently broken.
                        """)

                with col_fig:
                    fig6 = go.Figure()
                    x_plot = np.linspace(-1.5, 1.5, 100)
                    y_plot = x_plot ** 5 - x_plot + 1
                    fig6.add_shape(type="line", x0=-2, y0=0, x1=2, y1=0, line=dict(color="gray", width=2))
                    fig6.add_trace(go.Scatter(x=x_plot, y=y_plot, mode='lines', line=dict(color='#FF2E63', width=4),
                                              name='Quintic Curve'))
                    fig6.add_trace(go.Scatter(x=[-1.167], y=[0], mode='markers+text',
                                              text=["Root physically exists!<br>But formula is impossible."],
                                              textposition="top right", marker=dict(size=12, color='red')))
                    fig6.update_layout(title="The Death of Algebra: The Quintic Wall", xaxis=dict(range=[-2, 2]),
                                       yaxis=dict(range=[-2, 3]), template="plotly_dark", height=350,
                                       margin=dict(l=0, r=0, t=30, b=0))
                    st.plotly_chart(fig6, use_container_width=True)

                    # 在图表下方加一个视觉强烈的结语，为下一章（数值法）做完美铺垫
                    st.error("""
                    **The End of an Era:** The 300-year quest for the 'Perfect Formula' died with Galois. 
                    So, how do modern computers solve equations today? **We abandoned formulas, and embraced algorithms.**
                    """)

                    # 如果你有伽罗瓦手稿的图片，解除这行的注释并放上你的图片路径
                    # st.image("galois_manuscript.jpg", caption="Galois' final letter to Auguste Chevalier.", use_container_width=True)

    # ==========================================
    # 7. 算法时代的降临
    # ==========================================
    with sub_tabs[6]:
        st.header("🚀 Act 7: Dawn of Algorithms")
        col_txt, col_fig = st.columns([1.2, 1])
        with col_txt:
            st.warning("**The Shift:** From 'Symbolic' to 'Numerical'")
            st.write("""
            **The Aftermath:** If Galois proved we cannot *write* the answer with symbols and square roots, how do modern engineers design bridges, simulate fluid dynamics, or send rockets to Mars?

            **The Paradigm Shift:** We stopped looking for perfect formulas. If algebra fails, we use **Calculus**.

            Instead of searching for a static equation, we built **Algorithms**. By using derivatives (tangent lines), we can "hunt" the root. We make a guess, follow the slope down, make a better guess, and infinitely approximate the exact truth in milliseconds. 

            **We have left the era of pure Algebra and entered the era of Numerical Methods.**

            *(👉 Head over to the **Numerical Methods** Tab to see this algorithm in live action!)*
            """)

        with col_fig:
            fig7 = go.Figure()
            x_plot = np.linspace(-1.5, 0, 100)
            y_plot = x_plot ** 5 - x_plot + 1
            fig7.add_shape(type="line", x0=-2, y0=0, x1=1, y1=0, line=dict(color="gray", width=2))
            fig7.add_trace(
                go.Scatter(x=x_plot, y=y_plot, mode='lines', line=dict(color='#FF2E63', width=4), opacity=0.5,
                           name='Quintic'))

            # 模拟一次牛顿迭代的切线
            x0 = -0.5
            y0 = x0 ** 5 - x0 + 1
            slope = 5 * x0 ** 4 - 1
            x_tan = np.linspace(-1.5, 0.5, 50)
            y_tan = slope * (x_tan - x0) + y0
            fig7.add_trace(go.Scatter(x=x_tan, y=y_tan, mode='lines', line=dict(color='#FDB827', dash='dash', width=2),
                                      name='Tangent (Hunt)'))
            fig7.add_trace(
                go.Scatter(x=[x0], y=[y0], mode='markers', marker=dict(size=10, color='white'), showlegend=False))
            fig7.add_annotation(x=-1.167, y=0, text="Hunting the Root...", showarrow=True, arrowhead=2, ax=40, ay=-30,
                                font=dict(color="#FDB827"))
            fig7.update_layout(title="The Computer's Approach: Newton's Method", xaxis=dict(range=[-2, 1]),
                               yaxis=dict(range=[-1, 2]), template="plotly_dark", height=350)
            st.plotly_chart(fig7, use_container_width=True)

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
import streamlit as st
import numpy as np
import plotly.graph_objects as go

# ---------------------------------------------------------
# 必须先初始化 Session State（为了让你的按钮和滑块联动）
# ---------------------------------------------------------
if 'euler_t_3d' not in st.session_state:
    st.session_state.euler_t_3d = 0.0


def set_t(val):
    st.session_state.euler_t_3d = val


# ---------------------------------------------------------
# TAB 4: 欧拉公式与 3D 螺旋
# ---------------------------------------------------------
with tab4:
    st.subheader("🌌 Decoding God's Formula: From Growth to Perfect Rotation")
    st.caption("How compound interest, imaginary numbers, and time merge into the most beautiful equation in math.")

    physics_step = st.radio(
        "🔬 Select Experiment:",
        ["1. The Engine: Real vs Imaginary Growth",
         "2. The Tool: Wrapping the Radius (Radians)",
         "3. The Dimension Leap: The 3D Helix"],
        horizontal=True
    )

    st.markdown("---")
    col1, col2 = st.columns([1.2, 2])

    # ==========================================
    # 实验 1：e 的诞生与 i 的转向
    # ==========================================
    if physics_step == "1. The Engine: Real vs Imaginary Growth":
        with col1:
            st.markdown("### Where do $e$ and $i$ meet?")
            growth_type = st.radio("Choose the laws of physics:",
                                   ["Real Growth (Stretch)", "Imaginary Growth (Rotate)"])

            n_val = st.slider("Split Steps (n)", 1, 100, 5)

            if growth_type == "Real Growth (Stretch)":
                st.info(r"""
                **The Banker's Limit ($e$)**
                In 1683, Jacob Bernoulli asked: If a bank gives 100% interest, and I compound it $n$ times a year, will I get infinite money?
                $$ \lim_{n \to \infty} (1 + \frac{1}{n})^n = e \approx 2.718... $$
                **Conclusion:** Real growth pushes you endlessly forward, but hits a speed limit: $e$.
                """)
                current_val = (1 + 1 / n_val) ** n_val
                st.metric("Current Value", f"{current_val:.5f}", delta=f"Distance to e: {np.e - current_val:.5f}",
                          delta_color="inverse")

            else:
                st.success(r"""
                **The Orthogonal Push ($i$)**
                What if we apply growth from the **side**? By multiplying the interest by $i$, the growth direction becomes perpendicular to your current path.
                $$ \lim_{n \to \infty} (1 + \frac{i\pi}{n})^n = -1 $$
                **Conclusion:** Imaginary growth doesn't stretch you; it **turns** you. As steps $\to \infty$, it draws a perfect half-circle.
                """)
                st.caption("👉 Increase $n$ to see the jagged polygon smooth out into a perfect orbit!")

        with col2:
            fig4 = go.Figure()
            if growth_type == "Real Growth (Stretch)":
                # 画逼近 e 的极限曲线
                x_vals = np.arange(1, 101)
                y_vals = (1 + 1 / x_vals) ** x_vals
                fig4.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='(1 + 1/n)ⁿ',
                                          line=dict(color='#00ADB5', width=3)))
                # 当前 n 的点
                fig4.add_trace(
                    go.Scatter(x=[n_val], y=[(1 + 1 / n_val) ** n_val], mode='markers+text', text=[f"n={n_val}"],
                               textposition="bottom right", marker=dict(size=12, color='#FF2E63'), name='Current Step'))
                # e 的渐近线
                fig4.add_shape(type="line", x0=0, y0=np.e, x1=100, y1=np.e,
                               line=dict(color="#FDB827", dash="dash", width=2))
                fig4.add_annotation(x=50, y=np.e + 0.05, text="The Speed Limit: e ≈ 2.718", showarrow=False,
                                    font=dict(color="#FDB827"))
                fig4.update_layout(title="Approaching continuous growth", xaxis_title="Steps (n)",
                                   yaxis_title="Final Value", xaxis=dict(range=[0, 100]), yaxis=dict(range=[1.5, 3.0]),
                                   template="plotly_dark", height=450)

            else:
                # 画多边形逼近圆
                step = 1 + (1j * np.pi / n_val)
                z = 1 + 0j
                path_x, path_y = [1], [0]
                for _ in range(n_val):
                    z = z * step
                    path_x.append(z.real)
                    path_y.append(z.imag)

                # 完美的半圆作为参考
                theta = np.linspace(0, np.pi, 100)
                fig4.add_trace(
                    go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='gray', dash='dot'),
                               name='Perfect Path (Infinity)'))
                # 实际的计算路径
                fig4.add_trace(go.Scatter(x=path_x, y=path_y, mode='lines+markers', name='Actual Path',
                                          line=dict(color='#FF2E63', width=3), marker=dict(size=6)))
                # 连接原点到终点
                fig4.add_trace(
                    go.Scatter(x=[0, path_x[-1]], y=[0, path_y[-1]], mode='lines', line=dict(color='#00ADB5', width=2),
                               name='Final Position'))

                fig4.update_layout(title="Imaginary Compound Interest = Rotation",
                                   xaxis=dict(range=[-1.5, 1.5], title="Real"),
                                   yaxis=dict(range=[0, 1.5], title="Imaginary"), height=450, template="plotly_dark")

            st.plotly_chart(fig4, use_container_width=True)

    # ==========================================
    # 实验 2：弧度制的本质
    # ==========================================
    elif physics_step == "2. The Tool: Wrapping the Radius (Radians)":
        with col1:
            st.markdown("### Why measure in Radians?")
            st.write(
                "To combine geometry with algebra, we must stop using arbitrary 'Degrees' (based on ancient Babylonians) and use nature's ruler: **The Radius**.")
            wrap_val = st.slider("Wrap the Red Radius onto the circle:", 0.0, 3.14, 0.0, step=0.05)

            if wrap_val == 0.0:
                st.info("Pick up the red radius ($r=1$) lying on the ground...")
            elif wrap_val < 3.14:
                st.warning(f"Wrapping... Arc length is now **{wrap_val:.2f}** radius lengths.")
            else:
                st.success(
                    f"**Exactly $\pi$ radians!** Half a circle is mathematically equal to $\pi$ times the radius.")

        with col2:
            fig4 = go.Figure()
            theta = np.linspace(0, 2 * np.pi, 100)
            # 背景圆
            fig4.add_trace(
                go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines', line=dict(color='rgba(255,255,255,0.2)'),
                           showlegend=False))
            # 半径基准线
            fig4.add_trace(
                go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line=dict(color='gray', dash='dash'), name='Radius r=1'))

            # 弯曲的弧线
            if wrap_val > 0:
                arc_t = np.linspace(0, wrap_val, 50)
                fig4.add_trace(
                    go.Scatter(x=np.cos(arc_t), y=np.sin(arc_t), mode='lines', line=dict(color='#FF2E63', width=6),
                               name='Wrapped Radius'))
                # 连接圆心到终点
                fig4.add_trace(go.Scatter(x=[0, np.cos(wrap_val)], y=[0, np.sin(wrap_val)], mode='lines',
                                          line=dict(color='#00ADB5', width=2), name='Angle'))

            # 留在地上未弯曲的直线部分
            remaining_length = max(0, 3.14 - wrap_val)
            if remaining_length > 0:
                fig4.add_trace(go.Scatter(x=np.linspace(1, 1, 10), y=np.linspace(wrap_val, 3.14, 10), mode='lines',
                                          line=dict(color='#FF2E63', width=6, dash='dot'), name='Remaining Radius'))

            fig4.update_layout(xaxis=dict(range=[-1.5, 1.5], visible=False),
                               yaxis=dict(range=[-0.5, 3.5], visible=False), height=450,
                               title="1 Radian = 1 Radius wrapped around the edge", template="plotly_dark")
            st.plotly_chart(fig4, use_container_width=True)

    # ==========================================
    # 实验 3：欧拉公式与 3D 螺旋
    # ==========================================
    elif physics_step == "3. The Dimension Leap: The 3D Helix":
        with col1:
            st.markdown(r"### Euler's Formula: $$ e^{i\theta} = \cos(\theta) + i\sin(\theta) $$")
            st.write("""
            **The Ultimate Revelation:** What happens when continuous growth ($e$), imaginary rotation ($i$), and time ($\\theta$) combine? 

            A circle pulled through time becomes a **3D Helix**.
            * 🟡 **Real Shadow (Wall):** Looks like $\cos(\\theta)$
            * 🔴 **Imaginary Shadow (Floor):** Looks like $\sin(\\theta)$
            """)
            st.divider()

            st.write("**Jump to a specific moment:**")
            cols = st.columns(4)
            cols[0].button("Start (0)", on_click=set_t, args=(0.0,))
            cols[1].button("90° (π/2)", on_click=set_t, args=(np.pi / 2,))
            cols[2].button("180° (π)", on_click=set_t, args=(np.pi,))
            cols[3].button("360° (2π)", on_click=set_t, args=(2 * np.pi,))

            # 这里绑定了 session_state
            t_3d = st.slider("Flow of Time (θ)", 0.0, 4 * np.pi, key='euler_t_3d')

            if abs(t_3d - np.pi) < 0.1:
                st.error("""
                💥 **Euler's Identity:** Look where the red dot is! 
                At exactly $\\theta = \pi$, the helix rotates half a circle and lands perfectly on the Real $-1$.
                $$ e^{i\pi} + 1 = 0 $$
                """)

        with col2:
            t_range = np.linspace(0, 4 * np.pi, 300)
            x_helix = t_range
            y_helix = np.cos(t_range)
            z_helix = np.sin(t_range)

            fig4 = go.Figure()
            # 3D 螺旋主线
            fig4.add_trace(
                go.Scatter3d(x=x_helix, y=y_helix, z=z_helix, mode='lines', line=dict(color='#00ADB5', width=6),
                             name='e^(iθ) Helix'))

            # Imaginary 投影 (Sin) - 投射在 y=2 的墙上
            fig4.add_trace(go.Scatter3d(x=x_helix, y=np.ones_like(t_range) * 2, z=z_helix, mode='lines',
                                        line=dict(color='#FF2E63', width=3), opacity=0.3,
                                        name='Imaginary Proj: Sin(θ)'))

            # Real 投影 (Cos) - 投射在 z=-2 的地板上
            fig4.add_trace(go.Scatter3d(x=x_helix, y=y_helix, z=np.ones_like(t_range) * -2, mode='lines',
                                        line=dict(color='#FDB827', width=3), opacity=0.3, name='Real Proj: Cos(θ)'))

            # 当前时间的动态点
            cur_x, cur_y, cur_z = t_3d, np.cos(t_3d), np.sin(t_3d)
            fig4.add_trace(
                go.Scatter3d(x=[cur_x], y=[cur_y], z=[cur_z], mode='markers', marker=dict(size=12, color='#FF2E63'),
                             name="Current Position"))

            # 连接点到墙面和地面的虚线指示线
            fig4.add_trace(go.Scatter3d(x=[cur_x, cur_x], y=[cur_y, 2], z=[cur_z, cur_z], mode='lines',
                                        line=dict(color='#FF2E63', dash='dot', width=2), showlegend=False))
            fig4.add_trace(go.Scatter3d(x=[cur_x, cur_x], y=[cur_y, cur_y], z=[cur_z, -2], mode='lines',
                                        line=dict(color='#FDB827', dash='dot', width=2), showlegend=False))

            fig4.update_layout(
                scene=dict(
                    xaxis_title='Time (θ)', yaxis_title='Real Axis', zaxis_title='Imaginary Axis',
                    aspectmode='manual', aspectratio=dict(x=2.5, y=1, z=1),
                    xaxis=dict(range=[0, 13], showgrid=False), yaxis=dict(range=[-2, 2]), zaxis=dict(range=[-2, 2])
                ),
                height=500, margin=dict(l=0, r=0, b=0, t=0), template="plotly_dark",
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            st.plotly_chart(fig4, use_container_width=True)

import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import streamlit as st

import plotly.graph_objects as go
import numpy as np
import streamlit as st

# ---------------------------------------------------------
# TAB 5: The Power of i (Real-World Impact)
# ---------------------------------------------------------
with tab5:
    st.subheader("⚡ Topic 5: The Power of i (Real-World Impact)")
    st.write(
        "Now that we've seen how imaginary numbers perfectly govern 'rotation', what happens when this power is unleashed upon the real world? If $i$ were merely a 'mathematical ghost', we could have left it in the 16th century. But the chilling truth is: **the entire infrastructure of modern society, and the source code of our universe, are written in complex numbers.**")
    st.markdown("---")

    # 砍掉了 Mandelbrot，现在只剩下 2 个极致硬核的 Tabs
    app_tabs = st.tabs(["1. Taming the Waves", "2. Quantum Source Code"])

    # ==========================================
    # Application 1: AC Power & Signal Processing (深度扩写版)
    # ==========================================
    with app_tabs[0]:
        st.header("🌊 1. Taming the Waves (AC Power & Signal Processing)")
        c1, c2 = st.columns([1.2, 1])

        with c1:
            st.write("""
            **The Engineer's Nightmare:**
            The Alternating Current (AC) in your wall outlet and the 5G WiFi signal in your phone are all undulating waves. Imagine you are an electrical engineer who needs to add two waves with different timings (phases). In the real-number world, you must use brutal trigonometry:
            """)
            st.latex(r"A \cos(\omega t + \phi_1) + B \cos(\omega t + \phi_2) = \text{???}")
            st.write("""
            If you have to calculate the superposition of thousands of waves for a city's power grid, these trigonometric identities will make the math literally impossible to compute in real-time.

            **The Complex Dream (Phasors):**
            Using Euler's formula ($e^{i\\theta}$), engineers "upgrade" these 1D waves into **3D rotating complex vectors** (called *Phasors*). 

            Instead of tracking a wave moving up and down over time, they freeze the wave and look at it straight down the time axis. The wave becomes a simple arrow pointing in a specific direction on the Complex Plane. 
            """)
            st.latex(r"\mathbf{V}_{total} = A e^{i\phi_1} + B e^{i\phi_2}")
            st.write("""
            **The Miracle:** Horrifying trigonometric calculations are instantly reduced to **elementary school vector addition**. 

            This is the foundation of the **Fourier Transform**, a mathematical prism that splits chaotic real-world signals into perfect rotating complex circles. Every time your **Noise-Canceling Headphones** instantly calculate and invert a sound wave to create silence, or your router packs high-definition video into a radio wave, it is heavily relying on imaginary numbers to do the heavy lifting.
            """)

        with c2:
            # 强化版的 3D 螺旋波浪图
            t = np.linspace(0, 4 * np.pi, 200)
            real_part = np.cos(t)
            imag_part = np.sin(t)

            fig_wave = go.Figure()
            # 3D 螺旋线 (复数空间中的真实形态)
            fig_wave.add_trace(
                go.Scatter3d(x=t, y=real_part, z=imag_part, mode='lines', line=dict(color='#00ADB5', width=6),
                             name="Complex Wave e^(it)"))
            # 实数平面上的投影 (我们现实中看到的波)
            fig_wave.add_trace(go.Scatter3d(x=t, y=real_part, z=np.full_like(t, -1.5), mode='lines',
                                            line=dict(color='#FF2E63', width=3, dash='dash'),
                                            name="Real Projection (AC Voltage)"))

            # 增加一个时间截面的“相量(Phasor)”箭头，强化刚才文本里提到的概念
            current_t = 2 * np.pi
            fig_wave.add_trace(
                go.Scatter3d(x=[current_t, current_t], y=[0, np.cos(current_t)], z=[0, np.sin(current_t)],
                             mode='lines+markers', line=dict(color='#FDB827', width=5), marker=dict(size=8),
                             name="Phasor (Vector at a specific time)"))

            fig_wave.update_layout(
                title="Dimensional Strike: 3D Helix vs 2D Wave",
                scene=dict(
                    xaxis_title="Time (t)", yaxis_title="Real Part", zaxis_title="Imaginary Part",
                    yaxis=dict(range=[-1.5, 1.5]), zaxis=dict(range=[-1.5, 1.5])
                ),
                margin=dict(l=0, r=0, b=0, t=40), height=500, template="plotly_dark",
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            st.plotly_chart(fig_wave, use_container_width=True)

    # ==========================================
    # Application 2: Quantum Mechanics (Veritasium 彩蛋版)
    # ==========================================
    with app_tabs[1]:
        st.header("⚛️ 2. The Source Code of Reality (Quantum Mechanics)")
        st.write(
            "For centuries, mathematicians believed complex numbers were just a 'convenient shortcut' invented by engineers to make calculations easier. Until the 1920s, when the birth of Quantum Mechanics shattered our worldview.")

        st.error("**The Schrödinger Equation:**")
        st.latex(r"i \hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi")

        st.write("""
        Stare closely at the very first letter of the most fundamental equation in physics—**it is the imaginary number $i$.**

        Here, describing the wave function $\Psi$ of fundamental particles (like electrons) *must* involve complex numbers. Microscopic particles don't exist at a single definite point; they evolve as complex probability waves spinning through spacetime.
        """)

        with st.expander("😠 Schrödinger's Struggle: Even Geniuses Found it Unintuitive", expanded=True):
            st.write("""
            In fact, **Erwin Schrödinger himself originally hated this $i$!**

            When he first wrote the equation in 1926, he complained in a letter to physicist Hendrik Lorentz:
            > *"What is unpleasant here, and indeed directly to be objected to, is the use of complex numbers. $\Psi$ is surely fundamentally a real function."*

            Schrödinger desperately tried to remove $i$ and write a 'purely real' version of his equation. He failed. Without the imaginary number $i$ representing rotation and phase, the equation simply could not describe the true behavior of electrons. **Schrödinger didn't want to use imaginary numbers; the Creator forced him to.**
            """)

        with st.expander("⚖️ The 2021 Ultimate Verdict: Imaginary Numbers are Real", expanded=True):
            st.write("""
            For a long time, stubborn physicists held onto the hope that 'maybe imaginary numbers are just mathematical equivalence, and the physical world is inherently real'.

            But in **2021**, two teams of top physicists conducted rigorous quantum entanglement experiments and published their findings in *Nature*, finally proving: **If we only use real numbers, the predictions of quantum mechanics will fail.** Our universe, at a fundamental physical level, strictly and absolutely requires imaginary numbers.
            """)

        st.info("""
        As the renowned physicist Freeman Dyson marveled:
        > *"Schrödinger put the square root of minus one into the equation, and suddenly it made sense... Before this, imaginary numbers were a playground for mathematicians; but after quantum mechanics, **imaginary numbers became the true foundation upon which our universe operates.***"
        """)