import streamlit as st
import numpy as np
import plotly.graph_objects as go

# 页面配置
st.set_page_config(page_title="Linear Algebra", layout="wide")


# ==========================================
# 1. 共享的辅助绘图函数 (所有的画图工具都放在这)
# ==========================================
def draw_vector(fig, x, y, name, color, dash=False, origin=(0, 0), show_arrow=True, opacity=1.0):
    line_style = dict(color=color, width=3 if not dash else 2, dash='dash' if dash else 'solid')
    fig.add_trace(go.Scatter(
        x=[origin[0], origin[0] + x], y=[origin[1], origin[1] + y],
        mode='lines', line=line_style, name=name, opacity=opacity,
        showlegend=False if dash else True, hoverinfo='none' if dash else 'all'
    ))
    if show_arrow:
        fig.add_annotation(x=origin[0] + x, y=origin[1] + y, ax=origin[0], ay=origin[1],
                           xref="x", yref="y", axref="x", ayref="y",
                           showarrow=True, arrowhead=2, arrowsize=1.2, arrowcolor=color)


def create_base_figure(max_range=6):
    fig = go.Figure()
    fig.update_layout(
        xaxis=dict(range=[-max_range, max_range], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True,
                   gridcolor='lightgrey'),
        yaxis=dict(range=[-max_range, max_range], zeroline=True, zerolinewidth=2, zerolinecolor='black', showgrid=True,
                   gridcolor='lightgrey', scaleanchor="x", scaleratio=1),
        width=700, height=700, plot_bgcolor='#f8f9fa'
    )
    return fig
def draw_warped_grid(fig, M, color='rgba(150, 200, 255, 0.4)'):
    grid_range = 5
    for i in range(-grid_range, grid_range + 1):
        pt1, pt2 = M @ np.array([-grid_range, i]), M @ np.array([grid_range, i])
        fig.add_trace(go.Scatter(x=[pt1[0], pt2[0]], y=[pt1[1], pt2[1]], mode='lines', line=dict(color=color, width=1.5), hoverinfo='skip'))
        pt3, pt4 = M @ np.array([i, -grid_range]), M @ np.array([i, grid_range])
        fig.add_trace(go.Scatter(x=[pt3[0], pt4[0]], y=[pt3[1], pt4[1]], mode='lines', line=dict(color=color, width=1.5), hoverinfo='skip'))

# --- 3D 绘图函数 (Omni-Solver 需要) ---
def create_geogebra_base():
    fig = go.Figure()
    axis_len = 15
    fig.add_trace(go.Scatter3d(x=[-axis_len, axis_len], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='#ff4757', width=3), name='X轴'))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[-axis_len, axis_len], z=[0, 0], mode='lines', line=dict(color='#2ed573', width=3), name='Y轴'))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-axis_len, axis_len], mode='lines', line=dict(color='#1e90ff', width=3), name='Z轴'))
    return fig

def add_vector_arrow(fig, start, end, color, name):
    vec = end - start
    fig.add_trace(go.Scatter3d(x=[start[0], end[0]], y=[start[1], end[1]], z=[start[2], end[2]], mode='lines', line=dict(color=color, width=5), name=name))
    fig.add_trace(go.Cone(x=[end[0]], y=[end[1]], z=[end[2]], u=[vec[0]], v=[vec[1]], w=[vec[2]], sizemode="absolute", sizeref=1.5, anchor="tip", colorscale=[[0, color], [1, color]], showscale=False))

# ... (其他的 draw_warped_grid, create_geogebra_base 等函数也请放在这里) ...

# ==========================================
# 2. 侧边栏子菜单：切换向量或矩阵
# ==========================================
st.sidebar.title("📚 Course Modules")
module = st.sidebar.radio("Go to:", ["Vector", "Matrice"])

# ==========================================
# 3. 逻辑分发：根据选择显示内容
# ==========================================
if module == "Vector":
    st.title("🚀 Chapter I: The Foundations of Vectors")

    st.markdown(
        "Vectors are not merely arrows on a graph; they are the architectural framework of mathematical space. Let us explore their fundamental properties.")

    # Using Tabs for a cleaner, academic UI
    tab_mag, tab_dot, tab_cross, tab_app = st.tabs([
        "1. Magnitude & Direction",
        "2. The Dot Product",
        "3. The Cross Product",
        "4. Applications"
    ])

    # --- TAB 1: Magnitude & Direction Cosines ---
    with tab_mag:
        st.header("Magnitude & Direction Cosines")
        st.markdown(
            "Every vector in 3D space has an intrinsic length and a specific orientation relative to the coordinate axes.")

        col1, col2, col3 = st.columns(3)
        with col1:
            x = st.number_input("x-component", value=3.0, step=1.0)
        with col2:
            y = st.number_input("y-component", value=4.0, step=1.0)
        with col3:
            z = st.number_input("z-component", value=5.0, step=1.0)

        v = np.array([x, y, z])
        mag = np.linalg.norm(v)

        st.latex(r"|\vec{v}| = \sqrt{x^2 + y^2 + z^2}")

        if mag == 0:
            st.error("Magnitude is 0. A zero vector has no direction!")
        else:
            st.info(f"Calculated Magnitude: **{mag:.4f}**")

            st.markdown("### 1. The Direction Angles (α, β, γ)")

            # Calculate the angles in degrees
            alpha = np.degrees(np.arccos(x / mag))
            beta = np.degrees(np.arccos(y / mag))
            gamma = np.degrees(np.arccos(z / mag))

            c1, c2, c3 = st.columns(3)
            c1.metric("Angle with X-axis (α)", f"{alpha:.1f}°")
            c2.metric("Angle with Y-axis (β)", f"{beta:.1f}°")
            c3.metric("Angle with Z-axis (γ)", f"{gamma:.1f}°")

            # --- 修复符号显示的 3D 可视化部分 ---
            st.markdown(
                "Here is a 3D visualization showing exactly where **α, β, and γ** are located relative to the vector.")

            fig = go.Figure()
            axis_len = max(mag, 2) * 1.2
            offset = mag * 0.4

            # 1. 画出向量 Vector v (红色粗线)
            fig.add_trace(go.Scatter3d(
                x=[0, x], y=[0, y], z=[0, z],
                mode='lines+markers', name='Vector v',
                line=dict(color='red', width=7),
                marker=dict(size=4)
            ))

            # 2. 画出坐标轴 Axes (灰色细线)
            fig.add_trace(
                go.Scatter3d(x=[0, axis_len], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='grey', width=2),
                             showlegend=False))
            fig.add_trace(
                go.Scatter3d(x=[0, 0], y=[0, axis_len], z=[0, 0], mode='lines', line=dict(color='grey', width=2),
                             showlegend=False))
            fig.add_trace(
                go.Scatter3d(x=[0, 0], y=[0, 0], z=[0, axis_len], mode='lines', line=dict(color='grey', width=2),
                             showlegend=False))

            # 3. 坐标轴标签 (X, Y, Z) - 直接用纯文本
            fig.add_trace(go.Scatter3d(
                x=[axis_len, 0, 0], y=[0, axis_len, 0], z=[0, 0, axis_len],
                mode='text', text=['X', 'Y', 'Z'], textposition='middle right',
                textfont=dict(color='black', size=16), showlegend=False
            ))

            # 4. 角度标签 (α, β, γ) - 【修复重点】直接用纯文本的希腊字母，不要用 LaTeX 代码
            fig.add_trace(go.Scatter3d(
                x=[offset, 0, 0], y=[0, offset, 0], z=[0, 0, offset],
                mode='markers+text',
                marker=dict(size=5, color='purple'),
                text=['  α', '  β', '  γ'],  # 直接打出 α β γ
                textposition='middle right',
                textfont=dict(color='purple', size=18),
                showlegend=False
            ))

            # 5. 投影虚线
            fig.add_trace(go.Scatter3d(
                x=[x, x], y=[y, 0], z=[z, 0],
                mode='lines', line=dict(color='orange', width=2.5, dash='dash'),
                name='Projection to X'
            ))
            fig.add_trace(go.Scatter3d(
                x=[x, 0], y=[y, y], z=[z, 0],
                mode='lines', line=dict(color='green', width=2.5, dash='dash'),
                name='Projection to Y'
            ))
            fig.add_trace(go.Scatter3d(
                x=[x, 0], y=[y, 0], z=[z, z],
                mode='lines', line=dict(color='blue', width=2.5, dash='dash'),
                name='Projection to Z'
            ))

            fig.update_layout(
                scene=dict(aspectmode='cube'),
                margin=dict(l=0, r=0, b=0, t=0),
                scene_dragmode='orbit',
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
            )
            st.plotly_chart(fig, use_container_width=True)

            st.caption(
                "✨ **Tip:** Look at the dashed lines! They form perfect right-angled triangles with the vector. This is why $\cos\\alpha = x / |\\vec{v}|$ (Adjacent / Hypotenuse).")
            # --- 结束 3D 可视化部分 ---

            st.markdown("### 2. The Direction Cosines")
            st.markdown(
                "If we drop a perpendicular line from the tip of the vector to the X-axis, we form a right-angled triangle. Using basic trigonometry (SOH-CAH-TOA), the cosine of the angle is the adjacent side (the coordinate) divided by the hypotenuse (the magnitude).")

            st.latex(
                r"\cos\alpha = \frac{x}{|\vec{v}|}, \quad \cos\beta = \frac{y}{|\vec{v}|}, \quad \cos\gamma = \frac{z}{|\vec{v}|}")

            # --- 替换原来的第 3 和第 4 节 ---

            st.markdown(r"""
                            ### 3. The Unit Vector: The Bridge Between Algebra and Geometry

                            Why is the Unit Vector written as a matrix of cosines? Let's break it down step-by-step.

                            **Step A: The Algebraic Definition**
                            To create a Unit Vector ($\hat{v}$) — a vector with a length of exactly $1$ — we must take the original vector $\vec{v}$ and divide it by its own total length ($|\vec{v}|$).

                            If $\vec{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$, then shrinking the whole vector means dividing *each individual piece*:
                            """)

            # 展示代数除法
            st.latex(
                r"\hat{v} = \frac{1}{|\vec{v}|} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} \frac{x}{|\vec{v}|} \\ \frac{y}{|\vec{v}|} \\ \frac{z}{|\vec{v}|} \end{bmatrix}")

            st.markdown(r"""
                            **Step B: The Geometric Substitution**
                            Now, look at those three fractions inside the matrix: $\frac{x}{|\vec{v}|}$, $\frac{y}{|\vec{v}|}$, and $\frac{z}{|\vec{v}|}$. 

                            Do they look familiar? From our right-angled triangles in the 3D plot above, we already proved that $\cos\alpha = \frac{x}{|\vec{v}|}$ (Adjacent / Hypotenuse).

                            When we substitute the cosines into the fractions, the matrix transforms into pure geometry:
                            """)

            # 展示代入替换
            st.latex(r"\hat{v} = \begin{bmatrix} \cos\alpha \\ \cos\beta \\ \cos\gamma \end{bmatrix}")

            st.info(
                r"💡 The Direction Cosines are not just random angles. They are literally the new $x, y, z$ coordinates of the vector after you shrink its length to exactly 1.")

            st.markdown(r"""
                            ---
                            ### 4. The Famous Identity: Why does it equal 1?

                            You will constantly see this rule in exams: $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$. 

                            Why does adding their squares magically equal 1? It is not magic; it is just the **3D Pythagorean Theorem** applied to the Unit Vector. Let's prove it:

                            **1. The Coordinates:** We just proved that the coordinates of the Unit Vector $\hat{v}$ are $(\cos\alpha, \cos\beta, \cos\gamma)$.

                            **2. The Definition:** By definition, the total length (magnitude) of *any* Unit Vector is exactly **$1$**.

                            **3. The Calculation:** How do we calculate the length of a vector? We square its components, add them together, and take the square root. Let's do that for $\hat{v}$:
                            """)

            # 展示长度计算
            st.latex(r"|\hat{v}| = \sqrt{(\cos\alpha)^2 + (\cos\beta)^2 + (\cos\gamma)^2} = 1")

            st.markdown(r"""
                            To remove the square root, we simply square both sides of the equation ($1^2$ is still $1$). And there we have it—the famous identity:
                            """)

            # 最终公式
            st.latex(r"\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1")
            # --- TAB 2: The Dot Product ---
            # --- TAB 2: The Dot Product ---
            # --- TAB 2: The Dot Product ---
            with tab_dot:
                st.header("The Dot Product: From Work to Axioms")

                # ==========================================
                # 1. 物理直觉与投影
                # ==========================================
                st.markdown("### 1. The Physical Intuition: Work and Projection")
                st.markdown(r"""
                        Let's start with a physical concept: **Work**. If a Force ($\vec{F}$) drags an object along a displacement ($\vec{s}$), the work done is the magnitude of the force multiplied by the displacement, but *only the portion of the force in the direction of the movement*.
                        """)

                st.latex(r"W = |\vec{F}| \cdot |\vec{s}| \cdot \cos\theta")

                # [Visual 1]
                fig1 = go.Figure()
                fig1.add_trace(
                    go.Scatter(x=[0, 6], y=[0, 0], mode='lines+markers+text', name='Displacement (s)', text=['', 's'],
                               textposition='bottom right', line=dict(color='blue', width=5)))
                fig1.add_trace(
                    go.Scatter(x=[0, 3], y=[0, 4], mode='lines+markers+text', name='Force (F)', text=['', 'F'],
                               textposition='top left', line=dict(color='red', width=5)))
                fig1.add_trace(
                    go.Scatter(x=[3, 3], y=[4, 0], mode='lines', line=dict(color='orange', width=2, dash='dash')))
                fig1.add_trace(
                    go.Scatter(x=[0, 3], y=[0, 0], mode='lines', name='Shadow', line=dict(color='orange', width=8)))
                fig1.update_layout(title="Visual 1: The Shadow of Force", xaxis=dict(range=[-1, 7], zeroline=False),
                                   yaxis=dict(range=[-1, 5], zeroline=False), height=350,
                                   margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig1, use_container_width=True)

                st.info(r"""
                        **A Note on Mathematical Rigor:** Physics gives us the *intuition* (Work), but mathematics requires rigorous *definitions*. In pure math, we don't 'prove' the dot product from physics; instead, we **define** a mathematical operation to intentionally mirror these physical properties (Linearity and Symmetry). Let's formalize these as axioms.
                        """)

                # ==========================================
                # 2. 点积的两大公理
                # ==========================================
                st.markdown("### 2. The Two Axioms of the Dot Product")

                st.markdown("#### Axiom 1: Linearity and The Distributive Property")
                st.markdown(r"""
                        **Case A:** Imagine two forces, $F_1$ and $F_2$, dragging an object over distance $s_1$. The work done by the combined force is exactly equal to the work done by $F_1$ plus the work done by $F_2$.
                        $$(F_1 + F_2) \cdot s_1 = (F_1 \cdot s_1) + (F_2 \cdot s_1)$$

                        **Case B:** If one force $F$ drags an object for distance $s_1$, and then continues for $s_2$:
                        $$F \cdot (s_1 + s_2) = (F \cdot s_1) + (F \cdot s_2)$$

                        **The Insight:** This establishes the **Distributive Property**. Because of this linearity, we can infinitely break down any vector into a sum of smaller basis vectors, and the dot product will distribute perfectly across all of them.
                        """)

                # [Visual 2]
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=[0, 8], y=[0, 0], mode='lines', name='Displacement (s)',
                                          line=dict(color='blue', width=3)))
                fig2.add_trace(go.Scatter(x=[0, 2], y=[0, 3], mode='lines+text', name='F1', text=['', 'F1'],
                                          textposition='top left', line=dict(color='red', width=4)))
                fig2.add_trace(go.Scatter(x=[2, 5.5], y=[3, 4.5], mode='lines+text', name='F2', text=['', 'F2'],
                                          textposition='top right', line=dict(color='green', width=4)))
                fig2.add_trace(
                    go.Scatter(x=[0, 5.5], y=[0, 4.5], mode='lines+text', name='F_total (F1+F2)', text=['', 'F1+F2'],
                               textposition='bottom right', line=dict(color='purple', width=5)))
                fig2.add_trace(go.Scatter(x=[2, 2], y=[3, 0], mode='lines', showlegend=False,
                                          line=dict(color='red', width=2, dash='dash')))
                fig2.add_trace(go.Scatter(x=[5.5, 5.5], y=[4.5, 0], mode='lines', showlegend=False,
                                          line=dict(color='purple', width=2, dash='dash')))
                fig2.update_layout(
                    title="Visual 2: The Distributive Property (Red Shadow + Green Shadow = Purple Shadow)",
                    xaxis=dict(range=[-1, 7]), yaxis=dict(range=[-1, 5]), height=350, margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig2, use_container_width=True)

                st.markdown("#### Axiom 2: Relative Position and The Commutative Property")
                st.markdown(r"""
                        If vectors $F$ and $s$ form a triangle, rotating that entire triangle in space does not change their geometric relationship. 
                        Furthermore, projecting $F$ onto $s$, or projecting $s$ onto $F$, yields the exact same geometric area. This defines the **Commutative Property**:
                        $$F \cdot s = s \cdot F$$
                        """)

                # [Visual 3]
                fig3 = go.Figure()
                fig3.add_trace(
                    go.Scatter(x=[0, 5], y=[0, 0], mode='lines+markers+text', name='Vector A', text=['', 'A'],
                               textposition='bottom right', line=dict(color='blue', width=4)))
                fig3.add_trace(
                    go.Scatter(x=[0, 3], y=[0, 4], mode='lines+markers+text', name='Vector B', text=['', 'B'],
                               textposition='top left', line=dict(color='red', width=4)))
                fig3.add_trace(go.Scatter(x=[3, 3], y=[4, 0], mode='lines', name='Proj B onto A',
                                          line=dict(color='red', width=2, dash='dash')))
                fig3.add_trace(go.Scatter(x=[0, 3], y=[0, 0], mode='lines', name='Shadow of B (Length=3)',
                                          line=dict(color='red', width=6, dash='dot')))
                fig3.add_trace(go.Scatter(x=[5, 1.8], y=[0, 2.4], mode='lines', name='Proj A onto B',
                                          line=dict(color='blue', width=2, dash='dash')))
                fig3.add_trace(go.Scatter(x=[0, 1.8], y=[0, 2.4], mode='lines', name='Shadow of A (Length=3)',
                                          line=dict(color='blue', width=6, dash='dot')))
                fig3.update_layout(title="Visual 3: Commutativity (Shadow B × |A| == Shadow A × |B| == 15)",
                                   xaxis=dict(range=[-1, 6], scaleanchor="y", scaleratio=1), yaxis=dict(range=[-1, 5]),
                                   height=400, margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig3, use_container_width=True)

                # ==========================================
                # 3. 代数展开与 p=-p 证明 (严谨化：引入标准正交基底)
                # ==========================================
                st.markdown("---")
                st.markdown("### 3. The Algebraic Breakdown: Defining the Orthonormal Basis")
                st.markdown(r"""
                        To compute this algebraically, we must place our vectors in a Cartesian coordinate system defined by a **Standard Orthonormal Basis** ($\hat{i}$ and $\hat{j}$). 
                        "Orthonormal" means two strictly defined rules:
                        1. **Normal (Unit Length):** The basis vectors have a length of exactly $1$. Therefore, $\hat{i} \cdot \hat{i} = 1$ and $\hat{j} \cdot \hat{j} = 1$.
                        2. **Orthogonal:** They are perfectly perpendicular to each other.
                        """)

                st.markdown(r"""
                        Now, expand the product of $\vec{a} = x_1\hat{i} + y_1\hat{j}$ and $\vec{b} = x_2\hat{i} + y_2\hat{j}$ using our proven Distributive Property:
                        $$\vec{a} \cdot \vec{b} = x_1x_2(\hat{i} \cdot \hat{i}) + x_1y_2(\hat{i} \cdot \hat{j}) + y_1x_2(\hat{j} \cdot \hat{i}) + y_1y_2(\hat{j} \cdot \hat{j})$$
                        """)

                st.info(r"""
                        **The Symmetry of Orthogonality:** Why does the mixed term ($\hat{i} \cdot \hat{j}$) always equal $0$?

                        Assume their product is $p$. If we move one vector to point in the exact opposite direction (making it negative $-\hat{i}$), the algebraic product mathematically becomes $-p$. 

                        However, assuming Euclidean space is **isotropic** (behaves the same in all directions), flipping an orthogonal axis does not change the physical 90-degree intersection. By Axiom 2, the geometric interaction remains identical.
                        $$-p = p \implies p = 0$$

                        Substituting $\hat{i} \cdot \hat{i} = 1$ and $\hat{i} \cdot \hat{j} = 0$, the cross-terms vanish cleanly:
                        $$\vec{a} \cdot \vec{b} = x_1x_2 + y_1y_2$$
                        """)

                # [Visual 4]
                fig4 = go.Figure()
                fig4.add_trace(go.Scatter(x=[0, 0], y=[0, 3], mode='lines+markers+text', name='j (Up)', text=['', 'j'],
                                          textposition='top right', line=dict(color='red', width=5)))
                fig4.add_trace(
                    go.Scatter(x=[0, 3], y=[0, 0], mode='lines+markers+text', name='i (Right)', text=['', 'i'],
                               textposition='bottom right', line=dict(color='blue', width=5)))
                fig4.add_trace(
                    go.Scatter(x=[0, -3], y=[0, 0], mode='lines+markers+text', name='-i (Left)', text=['', '-i'],
                               textposition='bottom left', line=dict(color='green', width=5, dash='dash')))
                fig4.update_layout(title="Visual 4: Symmetry of Orthogonality (-p must equal p)",
                                   xaxis=dict(range=[-4, 4]), yaxis=dict(range=[-1, 4]), height=350,
                                   margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig4, use_container_width=True)

                # ==========================================
                # 4a. 左上与向右向量的直观证明
                # ==========================================
                st.markdown("#### A Visual Proof: The Surviving Projection")
                st.markdown(r"""
                        Take a vector $OA = (-3, 4)$ and $OB = (5, 0)$. 
                        Because orthogonal basis vectors multiply to $0$, the vertical component ($4\hat{j}$) contributes absolutely nothing.

                        * **Algebraically:** $(-3 \times 5) + (4 \times 0) = -15$
                        * **Geometrically:** The horizontal shadow of $OA$ is $-3$. Multiplying it by the length of $OB$ ($5$) gives $-15$. 
                        """)

                # [Visual 5a]
                fig5a = go.Figure()
                fig5a.add_trace(
                    go.Scatter(x=[0, -3], y=[0, 4], mode='lines+markers+text', name='Vector OA', text=['O', 'A(-3, 4)'],
                               textposition='top left', line=dict(color='red', width=4)))
                fig5a.add_trace(
                    go.Scatter(x=[0, 5], y=[0, 0], mode='lines+markers+text', name='Vector OB', text=['', 'B(5, 0)'],
                               textposition='bottom right', line=dict(color='blue', width=4)))
                fig5a.add_trace(go.Scatter(x=[-3, -3], y=[4, 0], mode='lines', name='Drop Perpendicular',
                                           line=dict(color='orange', width=2, dash='dash')))
                fig5a.add_trace(go.Scatter(x=[0, -3], y=[0, 0], mode='lines', name='Surviving Projection',
                                           line=dict(color='orange', width=6)))
                fig5a.update_layout(title="Visual 5a: Only the horizontal projection survives",
                                    xaxis=dict(range=[-4, 6], zeroline=False),
                                    yaxis=dict(range=[-1, 5], zeroline=False), height=350,
                                    margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig5a, use_container_width=True)

                # ==========================================
                # 4b. 余弦定理暴力展开证明 (严谨化：几何与代数的逻辑桥梁)
                # ==========================================
                st.markdown("#### The General Proof: Bridging Geometry and Algebra")
                st.markdown(r"""
                        Is it a coincidence that the algebraic definition ($x_1x_2 + y_1y_2$) perfectly matches the geometric reality ($|A||B|\cos\theta$) for *all* vectors? 
                        No. We can verify this consistency using an independent geometric theorem: the **Law of Cosines**.
                        """)

                # [Visual 5b]
                fig5b = go.Figure()
                fig5b.add_trace(
                    go.Scatter(x=[0, 2], y=[0, 4], mode='lines+markers+text', name='Vector OA', text=['O', 'A(x1, y1)'],
                               textposition='top left', line=dict(color='red', width=4)))
                fig5b.add_trace(
                    go.Scatter(x=[0, 5], y=[0, 2], mode='lines+markers+text', name='Vector OB', text=['', 'B(x2, y2)'],
                               textposition='bottom right', line=dict(color='blue', width=4)))
                fig5b.add_trace(go.Scatter(x=[2, 5], y=[4, 2], mode='lines+text', name='Vector AB', text=['', ''],
                                           line=dict(color='green', width=2, dash='dash')))
                fig5b.update_layout(title="Visual 5b: Forming a general triangle",
                                    xaxis=dict(range=[-1, 6], zeroline=False),
                                    yaxis=dict(range=[-1, 5], zeroline=False), height=350,
                                    margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig5b, use_container_width=True)

                st.markdown(r"""
                        From the Law of Cosines:
                        $$|AB|^2 = |OA|^2 + |OB|^2 - 2|OA||OB|\cos\angle AOB$$

                        Substitute the coordinate distances using the Pythagorean theorem:
                        $$x_2^2 - 2x_1x_2 + x_1^2 + y_2^2 - 2y_1y_2 + y_1^2 = (x_1^2 + y_1^2) + (x_2^2 + y_2^2) - 2|OA||OB|\cos\angle AOB$$

                        Cancel the squared terms and divide by $-2$:
                        $$x_1x_2 + y_1y_2 = |OA||OB|\cos\angle AOB$$
                        """)
                st.success(
                    "This proves that in a flat Euclidean space, our algebraic axiom logically enforces the physical projection geometry.")

                # ==========================================
                # 5. 余弦合角公式 (带滑块)
                # ==========================================
                st.markdown("---")
                st.markdown("### 4. Application: Rotational Invariance & The Cosine Difference Formula")
                st.markdown(r"""
                    Because the dot product depends solely on the relative angle and magnitudes, it is **invariant under coordinate rotations**. We can exploit this to easily prove $\cos(\alpha - \beta)$.
                    """)

                # [Visual 6]
                rot_angle = st.slider("Rotate the System (Match Vector B to X-axis)", 0, 45, 0,
                                      help="Drag this to rotate the vectors clockwise!")

                # 动态计算当前角度
                curr_alpha_deg = 75 - rot_angle
                curr_beta_deg = 45 - rot_angle

                alpha_rad = np.radians(curr_alpha_deg)
                beta_rad = np.radians(curr_beta_deg)

                ax, ay = np.cos(alpha_rad), np.sin(alpha_rad)
                bx, by = np.cos(beta_rad), np.sin(beta_rad)


                # ---------------------------------------------------------
                # 核心修复：手写画 2D 圆弧的辅助函数
                # ---------------------------------------------------------
                def get_arc_2d(radius, start_angle_rad, end_angle_rad, num_points=50):
                    t = np.linspace(start_angle_rad, end_angle_rad, num_points)
                    return radius * np.cos(t), radius * np.sin(t)


                fig6 = go.Figure()

                # 1. 画单位圆和坐标轴
                theta = np.linspace(0, 2 * np.pi, 100)
                fig6.add_trace(go.Scatter(x=np.cos(theta), y=np.sin(theta), mode='lines',
                                          line=dict(color='lightgrey', dash='dash'), showlegend=False))
                fig6.add_trace(go.Scatter(x=[-1.2, 1.2], y=[0, 0], mode='lines', line=dict(color='black', width=1),
                                          showlegend=False))
                fig6.add_trace(go.Scatter(x=[0, 0], y=[-1.2, 1.2], mode='lines', line=dict(color='black', width=1),
                                          showlegend=False))

                # 2. 画向量 A 和 B
                fig6.add_trace(go.Scatter(x=[0, ax], y=[0, ay], mode='lines+markers', name='Vector A',
                                          line=dict(color='red', width=4)))
                fig6.add_trace(go.Scatter(x=[0, bx], y=[0, by], mode='lines+markers', name='Vector B',
                                          line=dict(color='blue', width=4)))

                # 3. 画角度圆弧与标注 (仅当角度大于 0 时绘制，避免重叠)
                if curr_alpha_deg > 0:
                    arc_a_x, arc_a_y = get_arc_2d(0.2, 0, alpha_rad)
                    fig6.add_trace(go.Scatter(x=arc_a_x, y=arc_a_y, mode='lines', line=dict(color='red', width=2),
                                              showlegend=False))
                    # 动态角度标签：旋转前显示 α，旋转中显示具体度数
                    label_alpha_arc = "α" if rot_angle == 0 else f"{curr_alpha_deg}°"
                    fig6.add_trace(
                        go.Scatter(x=[np.cos(alpha_rad / 2) * 0.28], y=[np.sin(alpha_rad / 2) * 0.28], mode='text',
                                   text=[label_alpha_arc], textfont=dict(color='red', size=14), showlegend=False))

                if curr_beta_deg > 0:
                    arc_b_x, arc_b_y = get_arc_2d(0.35, 0, beta_rad)
                    fig6.add_trace(go.Scatter(x=arc_b_x, y=arc_b_y, mode='lines', line=dict(color='blue', width=2),
                                              showlegend=False))
                    # 动态角度标签
                    label_beta_arc = "β" if rot_angle == 0 else f"{curr_beta_deg}°"
                    fig6.add_trace(
                        go.Scatter(x=[np.cos(beta_rad / 2) * 0.45], y=[np.sin(beta_rad / 2) * 0.45], mode='text',
                                   text=[label_beta_arc], textfont=dict(color='blue', size=14), showlegend=False))

                # 4. 动态坐标端点标注 (教学展示的核心)
                if rot_angle == 0:
                    label_a = "A(cos α, sin α)"
                    label_b = "B(cos β, sin β)"
                elif rot_angle == 45:  # Vector B 完全贴在 X 轴上
                    label_a = "A'(cos(α-β), sin(α-β))"
                    label_b = "B'(1, 0)"
                else:  # 旋转过渡过程
                    label_a = f"A'({ax:.2f}, {ay:.2f})"
                    label_b = f"B'({bx:.2f}, {by:.2f})"

                fig6.add_trace(
                    go.Scatter(x=[ax * 1.25], y=[ay * 1.15], mode='text', text=[label_a], textposition='middle center',
                               textfont=dict(color='red', size=13), showlegend=False))
                fig6.add_trace(
                    go.Scatter(x=[bx * 1.25], y=[by * 1.15], mode='text', text=[label_b], textposition='middle center',
                               textfont=dict(color='blue', size=13), showlegend=False))

                fig6.update_layout(title="Visual 6: Rotational Invariance of the Dot Product",
                                   xaxis=dict(range=[-1.5, 1.5], scaleanchor="y", scaleratio=1, zeroline=False,
                                              showgrid=False),
                                   yaxis=dict(range=[-1.5, 1.5], zeroline=False, showgrid=False),
                                   height=500, margin=dict(l=0, r=0, b=0, t=30))
                st.plotly_chart(fig6, use_container_width=True)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Method 1: Original Coordinates**")
                    st.latex(r"\vec{A} \cdot \vec{B} = \cos\alpha\cos\beta + \sin\alpha\sin\beta")

                with col2:
                    st.markdown("**Method 2: Rotated Coordinates**")
                    st.latex(
                        r"\vec{A}' \cdot \vec{B}' = \cos(\alpha-\beta)(1) + \sin(\alpha-\beta)(0) = \cos(\alpha-\beta)")

                st.success(
                    r"**The Geometric Equivalence:** $ \cos(\alpha - \beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta $")

        # --- TAB 3: Cross Product & Normal Vectors ---
        # --- TAB 3: The Cross Product ---
        with tab_cross:
            st.header("The Cross Product: Generating the Normal Vector")

            # ==========================================
            # 1. 动机与几何定义
            # ==========================================
            st.markdown("### 1. Motivation: Torque and Area")
            st.markdown(r"""
                If the Dot Product measures how "parallel" two vectors are, the Cross Product measures how **"perpendicular"** they are. 

                **The Physical Origin:** Think of pushing a door (Torque $\vec{\tau}$). If the door handle is at position $\vec{r}$ and you push with force $\vec{F}$, pushing *parallel* to the door does nothing. Pushing strictly *perpendicular* creates maximum rotation.
                Magnitude of Torque: $|\vec{\tau}| = |\vec{r}| |\vec{F}| \sin\theta$

                **The Geometric Meaning:** This magnitude exactly equals the area of the parallelogram formed by the two vectors. 
                But area is just a number. In 3D space, a surface has an **orientation**. We describe this orientation using a strictly perpendicular vector: the **Normal Vector**.
                """)

            # [Visual 1: 面积与法向量的三维动态交互]
            st.markdown("#### Visual: The Parallelogram and its Normal")
            angle_cross = st.slider("Angle between A and B (degrees)", 0, 180, 90, key='cross_angle')
            rad_cross = np.radians(angle_cross)

            v_A = np.array([2, 0, 0])
            v_B = np.array([2 * np.cos(rad_cross), 2 * np.sin(rad_cross), 0])
            # 叉积计算法向量
            v_N = np.cross(v_A, v_B)

            fig_cross1 = go.Figure()
            # 画底部的平行四边形
            fig_cross1.add_trace(
                go.Mesh3d(x=[0, v_A[0], v_A[0] + v_B[0], v_B[0]], y=[0, v_A[1], v_A[1] + v_B[1], v_B[1]],
                          z=[0, 0, 0, 0], i=[0, 0], j=[1, 2], k=[2, 3], color='lightblue', opacity=0.5, name='Area'))
            # 画 Vector A 和 B
            fig_cross1.add_trace(
                go.Scatter3d(x=[0, v_A[0]], y=[0, v_A[1]], z=[0, 0], mode='lines+text', name='Vector A', text=['', 'A'],
                             line=dict(color='red', width=5)))
            fig_cross1.add_trace(
                go.Scatter3d(x=[0, v_B[0]], y=[0, v_B[1]], z=[0, 0], mode='lines+text', name='Vector B', text=['', 'B'],
                             line=dict(color='blue', width=5)))
            # 画 Normal Vector (AxB)
            fig_cross1.add_trace(
                go.Scatter3d(x=[0, v_N[0]], y=[0, v_N[1]], z=[0, v_N[2]], mode='lines+text', name='A x B (Normal)',
                             text=['', 'A x B'], line=dict(color='green', width=6)))

            fig_cross1.update_layout(
                scene=dict(xaxis=dict(range=[-3, 5]), yaxis=dict(range=[-3, 5]), zaxis=dict(range=[-1, 5]),
                           aspectmode='cube'), margin=dict(l=0, r=0, b=0, t=0), height=400)
            st.plotly_chart(fig_cross1, use_container_width=True)

            # ==========================================
            # 2. 公理：右手定则与反交换律
            # ==========================================
            st.markdown("### 2. Axiom: The Right-Hand Rule and Anti-Commutativity")
            st.markdown(r"""
                Since there are two directions perpendicular to a plane (up or down), mathematics strictly defines the direction using the **Right-Hand Rule**: sweep your right fingers from $\vec{a}$ to $\vec{b}$, and your thumb points to $\vec{a} \times \vec{b}$.
                """)

            col1, col2 = st.columns(2)
            with col1:
                st.info(r"""
                    **Anti-Commutativity:**
                    If you sweep from $\vec{b}$ to $\vec{a}$, your hand flips upside down. Thus:
                    $$\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})$$

                    As a direct consequence, a vector crossed with itself has $0$ area:
                    $$\vec{a} \times \vec{a} = \vec{0}$$
                    """)
            with col2:
                st.info(r"""
                    **The Right-Handed Coordinate System:**
                    By definition, the standard basis vectors strictly follow this rule:
                    * $\hat{i} \times \hat{j} = \hat{k}$  (and $\hat{j} \times \hat{i} = -\hat{k}$)
                    * $\hat{j} \times \hat{k} = \hat{i}$  (and $\hat{k} \times \hat{j} = -\hat{i}$)
                    * $\hat{k} \times \hat{i} = \hat{j}$  (and $\hat{i} \times \hat{k} = -\hat{j}$)
                    """)

            # ==========================================
            # 3. 严格推导：从代数展开到行列式
            # ==========================================
            st.markdown("---")
            st.markdown("### 3. Rigorous Derivation: Expanding the Vectors")
            st.markdown(r"""
                We do not just memorize the matrix determinant. We must derive it using the distributive property. 
                Let $\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}$ and $\vec{b} = b_x\hat{i} + b_y\hat{j} + b_z\hat{k}$.

                Expand $\vec{a} \times \vec{b}$ into 9 terms:
                """)

            st.latex(r"""
                \begin{aligned}
                \vec{a} \times \vec{b} &= (a_x\hat{i} + a_y\hat{j} + a_z\hat{k}) \times (b_x\hat{i} + b_y\hat{j} + b_z\hat{k}) \\
                &= a_xb_x(\hat{i}\times\hat{i}) + a_xb_y(\hat{i}\times\hat{j}) + a_xb_z(\hat{i}\times\hat{k}) \\
                &\quad + a_yb_x(\hat{j}\times\hat{i}) + a_yb_y(\hat{j}\times\hat{j}) + a_yb_z(\hat{j}\times\hat{k}) \\
                &\quad + a_zb_x(\hat{k}\times\hat{i}) + a_zb_y(\hat{k}\times\hat{j}) + a_zb_z(\hat{k}\times\hat{k})
                \end{aligned}
                """)

            st.markdown(r"""
                Apply our axioms: self-crosses become $\vec{0}$, and mixed crosses become the third basis vector (respecting the negative signs for reverse order). The 9 terms collapse into 6 terms:
                """)

            st.latex(r"""
                \begin{aligned}
                \vec{a} \times \vec{b} &= 0 + a_xb_y(\hat{k}) + a_xb_z(-\hat{j}) \\
                &\quad + a_yb_x(-\hat{k}) + 0 + a_yb_z(\hat{i}) \\
                &\quad + a_zb_x(\hat{j}) + a_zb_y(-\hat{i}) + 0
                \end{aligned}
                """)

            st.markdown("Group the $\hat{i}$, $\hat{j}$, and $\hat{k}$ components together:")
            st.latex(
                r"\vec{a} \times \vec{b} = (a_yb_z - a_zb_y)\hat{i} - (a_xb_z - a_zb_x)\hat{j} + (a_xb_y - a_yb_x)\hat{k}")

            st.success(r"""
                **The Elegance of the Determinant:** Mathematicians noticed that this messy algebraic result perfectly matches the expansion of a $3 \times 3$ determinant. This is why we write it as a matrix—it is purely a mnemonic tool for the brute-force expansion above!
                """)
            st.latex(
                r"\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}")


            # --- TAB 4: Applications ---

            # --- 封装的 GeoGebra 风格画图函数 ---
            def create_geogebra_base():
                fig = go.Figure()
                # 绘制贯穿原点的红绿蓝 X, Y, Z 轴，模拟专业数学软件
                axis_len = 15
                fig.add_trace(go.Scatter3d(x=[-axis_len, axis_len], y=[0, 0], z=[0, 0], mode='lines',
                                           line=dict(color='#ff4757', width=3), name='X-axis', hoverinfo='skip'))
                fig.add_trace(go.Scatter3d(x=[0, 0], y=[-axis_len, axis_len], z=[0, 0], mode='lines',
                                           line=dict(color='#2ed573', width=3), name='Y-axis', hoverinfo='skip'))
                fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-axis_len, axis_len], mode='lines',
                                           line=dict(color='#1e90ff', width=3), name='Z-axis', hoverinfo='skip'))
                fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='markers+text', text=['Origin(0,0,0)'],
                                           marker=dict(color='black', size=4), name='Origin'))
                return fig


            def add_vector_arrow(fig, start, end, color, name):
                # 用 Cone 模拟矢量箭头，这是提升专业感的关键
                vec = end - start
                fig.add_trace(
                    go.Scatter3d(x=[start[0], end[0]], y=[start[1], end[1]], z=[start[2], end[2]], mode='lines',
                                 line=dict(color=color, width=5), name=name))
                fig.add_trace(
                    go.Cone(x=[end[0]], y=[end[1]], z=[end[2]], u=[vec[0]], v=[vec[1]], w=[vec[2]], sizemode="absolute",
                            sizeref=1.5, anchor="tip", colorscale=[[0, color], [1, color]], showscale=False,
                            hoverinfo='skip'))


            # --- TAB 4: Applications (The Omni-Solver) ---
            with tab_app:
                st.header("🎯 The Omni-Solver: 3D Geometry Master")
                st.markdown(
                    "A complete ecosystem for 3D Geometry: Understand how equations are built, and then use them to solve complex spatial interactions.")

                # ==========================================
                # 顶层导航：区分“学基础”和“解大题”
                # ==========================================
                app_section = st.radio("Select Section:", [
                    "📖 Part A: Equation Builder",
                    "🚀 Part B: Interaction Solver"
                ], horizontal=True)
                st.markdown("---")

                if app_section == "📖 Part A: Equation Builder":
                    st.markdown("### The Anatomy of 3D Equations")
                    st.markdown(
                        "Before solving complex problems, let's understand how lines and planes are constructed mathematically.")

                    tab_eq_line, tab_eq_plane = st.tabs(
                        ["1. Equation of a Line", "2. Equation of a Plane (Normal Vector Derivation)"])

                    # ------------------------------------------
                    # 基础 1: 直线方程的静态展示
                    # ------------------------------------------
                    with tab_eq_line:
                        st.markdown(
                            "To define a line in 3D space, you strictly need two elements: a **Point** it passes through, and a **Direction** it travels along.")

                        st.info(
                            "**Example Case:** Let a line pass through the point **$A(2, -1, 4)$**, and travel parallel to the direction vector **$\\vec{v} = \\langle 3, 5, -2 \\rangle$**.")

                        st.markdown("#### The Three Forms of a Line Equation")

                        # 1. Vector Equation
                        st.markdown(
                            "**1. Vector Equation:** Formed by vector addition $\\vec{r} = \\vec{a} + t\\vec{v}$")
                        st.latex(r"\vec{r} = (2\hat{i} - \hat{j} + 4\hat{k}) + t(3\hat{i} + 5\hat{j} - 2\hat{k})")

                        # 2. Parametric Equations
                        st.markdown(
                            "**2. Parametric Equations:** Breaking the vector equation into independent $x, y, z$ components")
                        st.latex(r"\begin{cases} x = 2 + 3t \\ y = -1 + 5t \\ z = 4 - 2t \end{cases}")

                        # 3. Cartesian Equation
                        st.markdown(
                            "**3. Cartesian (Symmetric) Equation:** Solving for parameter $t$ to link all three variables together")
                        st.latex(r"\frac{x - 2}{3} = \frac{y + 1}{5} = \frac{z - 4}{-2} = t")

                    # ------------------------------------------
                    # 基础 2: 平面方程与法向量的可视化推导
                    # ------------------------------------------
                    with tab_eq_plane:
                        st.markdown(
                            "To define a plane, you need a **Point** ($P$) on the plane and a **Normal Vector** ($\\vec{n}$) that is strictly perpendicular to it.")

                        # --- 重点 1：揭秘系数与法向量的关系 ---
                        st.markdown("### 1. The Core Derivation: Why does $\\vec{n}$ become the coefficients?")
                        st.markdown(
                            "Let the normal vector be $\\vec{n} = \\langle A, B, C \\rangle$, and a known point be $P_0(x_0, y_0, z_0)$. For any general point $P(x, y, z)$ on the plane, the vector $\\vec{P_0P}$ lies entirely on the plane.")
                        st.markdown(
                            "Because the normal vector is perpendicular to *every* vector on the plane, their **Dot Product must be zero**:")

                        st.latex(r"\vec{n} \cdot \vec{P_0P} = 0")
                        st.latex(r"\langle A, B, C \rangle \cdot \langle x - x_0, y - y_0, z - z_0 \rangle = 0")

                        st.markdown("Expand the dot product algebraically:")
                        st.latex(r"A(x - x_0) + B(y - y_0) + C(z - z_0) = 0")
                        st.latex(r"Ax + By + Cz = \underbrace{Ax_0 + By_0 + Cz_0}_{D \text{ (Constant)}}")

                        st.success(
                            "✨ **The Geometric Secret:** By letting the constant right side equal $D$, we get the standard Cartesian Equation **$Ax + By + Cz = D$**. This proves that the coefficients $(A, B, C)$ are literally the components of the Normal Vector!")

                        st.markdown("---")

                        # --- 重点 2：三点求平面与标准方程 ---
                        st.markdown("### 2. Formulating the Plane Equations (Given 3 Points)")
                        st.markdown(
                            "If you are given 3 points on a plane, you can form two vectors. Their **Cross Product** will generate a new vector strictly perpendicular to both, which serves as our Normal Vector $\\vec{n}$.")

                        P, Q, R = np.array([1, 1, 1]), np.array([3, 2, -1]), np.array([2, 3, 3])
                        PQ, PR = Q - P, R - P
                        norm_n = np.cross(PQ, PR)
                        constant_D = np.dot(norm_n, P)

                        col_math, col_plot = st.columns([1, 1.2])

                        with col_math:
                            st.markdown("**Example:** Let $P(1, 1, 1)$, $Q(3, 2, -1)$, $R(2, 3, 3)$.")

                            st.markdown("#### Step 1: Find Normal Vector $\\vec{n}$")
                            st.latex(
                                rf"\vec{{PQ}} = \langle {PQ[0]}, {PQ[1]}, {PQ[2]} \rangle, \quad \vec{{PR}} = \langle {PR[0]}, {PR[1]}, {PR[2]} \rangle")
                            st.latex(
                                rf"\vec{{n}} = \vec{{PQ}} \times \vec{{PR}} = \langle \mathbf{{{norm_n[0]}, {norm_n[1]}, {norm_n[2]}}} \rangle")

                            st.markdown("#### Step 2: The Two Forms of a Plane Equation")

                            # 补充：Vector Equation
                            st.markdown(
                                "**1. Vector Equation:** $\\vec{r} \cdot \\vec{n} = \\vec{a} \cdot \\vec{n}$")
                            st.markdown("Using point $P$ as our known position vector $\\vec{a}$:")
                            st.latex(
                                rf"\vec{{r}} \cdot \langle {norm_n[0]}, {norm_n[1]}, {norm_n[2]} \rangle = \langle {P[0]}, {P[1]}, {P[2]} \rangle \cdot \langle {norm_n[0]}, {norm_n[1]}, {norm_n[2]} \rangle")
                            st.latex(
                                rf"\mathbf{{\vec{{r}} \cdot \langle {norm_n[0]}, {norm_n[1]}, {norm_n[2]} \rangle = {constant_D}}}")

                            # 补充：Cartesian Equation
                            st.markdown("**2. Cartesian Equation:** $Ax + By + Cz = D$")
                            st.markdown(
                                "Since $\\vec{r} = \langle x, y, z \\rangle$, expanding the dot product directly yields:")
                            st.latex(rf"\mathbf{{{norm_n[0]}x {norm_n[1]:+}y {norm_n[2]:+}z = {constant_D}}}")

                        with col_plot:

                            fig_build = create_geogebra_base()

                            u_vec = PQ / np.linalg.norm(PQ)
                            w_vec = PR / np.linalg.norm(PR)
                            n_unit = norm_n / np.linalg.norm(norm_n)

                            uu, ww = np.meshgrid(np.linspace(-8, 8, 2), np.linspace(-8, 8, 2))
                            fig_build.add_trace(go.Surface(x=P[0] + uu * u_vec[0] + ww * w_vec[0],
                                                           y=P[1] + uu * u_vec[1] + ww * w_vec[1],
                                                           z=P[2] + uu * u_vec[2] + ww * w_vec[2],
                                                           colorscale='Greens', opacity=0.4, showscale=False,
                                                           name='Plane'))

                            fig_build.add_trace(
                                go.Scatter3d(x=[P[0], Q[0], R[0]], y=[P[1], Q[1], R[1]], z=[P[2], Q[2], R[2]],
                                             mode='markers+text', text=[' P', ' Q', ' R'],
                                             textfont=dict(color='black', size=16),
                                             marker=dict(color='black', size=5), showlegend=False))

                            add_vector_arrow(fig_build, P, Q, 'blue', 'Vector PQ')
                            add_vector_arrow(fig_build, P, R, 'green', 'Vector PR')

                            n_display = P + n_unit * 6
                            add_vector_arrow(fig_build, P, n_display, 'red', 'Normal Vector n')


                            def draw_square(fig, p_origin, vA, vB, size=0.8):
                                c1 = p_origin + vA * size
                                c2 = p_origin + vA * size + vB * size
                                c3 = p_origin + vB * size
                                fig.add_trace(go.Scatter3d(x=[c1[0], c2[0], c3[0]], y=[c1[1], c2[1], c3[1]],
                                                           z=[c1[2], c2[2], c3[2]], mode='lines',
                                                           line=dict(color='black', width=3), showlegend=False))


                            draw_square(fig_build, P, u_vec, w_vec)  # PQ ⊥ PR
                            draw_square(fig_build, P, u_vec, n_unit)  # PQ ⊥ n
                            draw_square(fig_build, P, w_vec, n_unit)  # PR ⊥ n

                            fig_build.update_layout(
                                scene=dict(aspectmode='cube', camera=dict(eye=dict(x=1.8, y=1.2, z=1.2))),
                                height=450, margin=dict(l=0, r=0, b=0, t=0), legend=dict(x=0, y=1))
                            st.plotly_chart(fig_build, use_container_width=True)
                            st.caption(
                                "✨ **Orthogonal Triad:** Notice how $\\vec{PQ}$, $\\vec{PR}$, and $\\vec{n}$ form three perfect $90^\\circ$ angles. The red Normal Vector is strictly perpendicular to the entire plane.")

                    # ==========================================
                # 模式 2: 空间关系解算 (原有的 Omni-Solver 核心)
                # ==========================================
                elif app_section == "🚀 Part B: Interaction Solver":
                    solver_mode = st.selectbox("Select Interaction Mode:", [
                        "1. Line & Plane",
                        "2. Plane & Plane",
                        "3. Line & Line"
                    ])
                    st.markdown("---")

                    # ------------------------------------------
                    # 粘贴你原本的 1. Line & Plane 代码
                    # ------------------------------------------
                    if solver_mode == "1. Line & Plane":
                        st.markdown("### 📥 Input Panel")
                        col_obj1, col_obj2 = st.columns(2)
                        with col_obj1:
                            st.markdown("**Line Definition** (Point + Direction)")
                            l_px = st.number_input("Point x", value=1.0, key='lp_px')
                            l_py = st.number_input("Point y", value=3.0, key='lp_py')
                            l_pz = st.number_input("Point z", value=2.0, key='lp_pz')
                            l_vx = st.number_input("Direction x", value=2.0, key='lp_vx')
                            l_vy = st.number_input("Direction y", value=-1.0, key='lp_vy')
                            l_vz = st.number_input("Direction z", value=-3.0, key='lp_vz')

                        with col_obj2:
                            st.markdown("**Plane Definition** ($Ax+By+Cz=D$)")
                            pA = st.number_input("Normal A", value=2.0, key='lp_pa')
                            pB = st.number_input("Normal B", value=-1.0, key='lp_pb')
                            pC = st.number_input("Normal C", value=-2.0, key='lp_pc')
                            pD = st.number_input("Constant D", value=17.0, key='lp_pd')

                        st.markdown("---")
                        st.markdown("### 🧠 Step-by-Step Solution")
                        pt_line, dir_line, norm_plane = np.array([l_px, l_py, l_pz]), np.array(
                            [l_vx, l_vy, l_vz]), np.array([pA, pB, pC])

                        # 1. 方程提取
                        st.markdown("#### Step 1: Equations")
                        st.latex(
                            rf"\text{{Line }} l: x = {l_px} + {l_vx}t, \quad y = {l_py} {l_vy:+}t, \quad z = {l_pz} {l_vz:+}t")
                        st.latex(rf"\text{{Plane }}\pi\text{{: }} {pA}x + ({pB})y + ({pC})z = {pD}")

                        # 2. 教材级角度计算
                        st.markdown("#### Step 2: Angle Calculation")
                        mag_dir, mag_norm = np.linalg.norm(dir_line), np.linalg.norm(norm_plane)
                        if mag_dir == 0 or mag_norm == 0:
                            st.error("Invalid vectors.")
                        else:
                            dot_p = np.dot(dir_line, norm_plane)
                            cos_beta = np.clip(dot_p / (mag_dir * mag_norm), -1.0, 1.0)
                            beta_deg = np.degrees(np.arccos(cos_beta))

                            st.markdown(
                                "First, find the angle $\\beta$ between the direction vector $\\vec{v}$ and the normal vector $\\vec{n}$:")
                            st.latex(
                                rf"\beta = \cos^{{-1}}\left(\frac{{\vec{{n}} \cdot \vec{{v}}}}{{|\vec{{n}}| |\vec{{v}}|}}\right) = \cos^{{-1}}\left(\frac{{{dot_p:.1f}}}{{{mag_norm:.2f} \times {mag_dir:.2f}}}\right) = {beta_deg:.2f}^\circ")

                            if beta_deg > 90:
                                acute_beta = 180 - beta_deg
                                theta = 90 - acute_beta
                                st.markdown(
                                    f"Since $\\beta > 90^\circ$, we subtract it from $180^\circ$ to find the acute inner angle:")
                                st.latex(rf"180^\circ - {beta_deg:.2f}^\circ = {acute_beta:.2f}^\circ")
                                st.markdown("Then, the acute angle $\\theta$ between the line and the plane is:")
                                st.latex(rf"\theta = 90^\circ - {acute_beta:.2f}^\circ = \mathbf{{{theta:.1f}^\circ}}")
                            else:
                                theta = 90 - beta_deg
                                st.markdown(
                                    "Since $\\beta \le 90^\circ$, the angle $\\theta$ between the line and the plane is simply:")
                                st.latex(
                                    rf"\theta = 90^\circ - \beta = 90^\circ - {beta_deg:.2f}^\circ = \mathbf{{{theta:.1f}^\circ}}")

                        # 3. 经典代入法求交点
                        st.markdown("#### Step 3: Intersection Point (Substitution Method)")
                        denominator = pA * l_vx + pB * l_vy + pC * l_vz
                        constant_term = pA * l_px + pB * l_py + pC * l_pz

                        if abs(denominator) < 1e-8:
                            st.warning("The line is strictly parallel to or inside the plane. No unique intersection.")
                            intersect_pt = None
                        else:
                            st.markdown("Substitute the line's parametric equations into the plane's equation:")
                            st.latex(
                                rf"{pA}({l_px} + {l_vx}t) + ({pB})({l_py} {l_vy:+}t) + ({pC})({l_pz} {l_vz:+}t) = {pD}")

                            st.markdown("Expand and solve for $t$:")
                            st.latex(rf"({constant_term}) + ({denominator})t = {pD}")

                            t_val = (pD - constant_term) / denominator
                            st.latex(rf"({denominator})t = {pD - constant_term} \implies \mathbf{{t = {t_val:.4f}}}")

                            intersect_pt = pt_line + t_val * dir_line
                            st.markdown("Substitute $t$ back into the line equations to get the coordinates:")
                            st.latex(
                                rf"I(x,y,z) = \mathbf{{({intersect_pt[0]:.2f}, {intersect_pt[1]:.2f}, {intersect_pt[2]:.2f})}}")

                        # 4. 完美还原教材的 3D 视图

                        fig_omni = create_geogebra_base()
                        center = intersect_pt if intersect_pt is not None else np.array([0, 0, 0])

                        u_vec = np.array([1, 0, 0]) if abs(norm_plane[0]) < 0.9 else np.array([0, 1, 0])
                        u_vec = u_vec - (np.dot(u_vec, norm_plane) / np.dot(norm_plane, norm_plane)) * norm_plane
                        u_vec, w_vec = u_vec / np.linalg.norm(u_vec), np.cross(norm_plane, u_vec) / np.linalg.norm(
                            np.cross(norm_plane, u_vec))
                        uu, ww = np.meshgrid(np.linspace(-15, 15, 2), np.linspace(-15, 15, 2))
                        fig_omni.add_trace(go.Surface(x=center[0] + uu * u_vec[0] + ww * w_vec[0],
                                                      y=center[1] + uu * u_vec[1] + ww * w_vec[1],
                                                      z=center[2] + uu * u_vec[2] + ww * w_vec[2], colorscale='Greens',
                                                      opacity=0.3, showscale=False, name='Plane π'))

                        if intersect_pt is not None:
                            n_unit = norm_plane / np.linalg.norm(norm_plane)
                            v_unit = dir_line / np.linalg.norm(dir_line)
                            if np.dot(n_unit, v_unit) < 0: v_unit = -v_unit

                            draw_len = 10.0
                            P_I = center
                            P_L = center + v_unit * draw_len
                            dist_to_plane = np.dot(P_L - P_I, n_unit)
                            P_Proj = P_L - dist_to_plane * n_unit

                            fig_omni.add_trace(go.Mesh3d(x=[P_I[0], P_L[0], P_Proj[0]], y=[P_I[1], P_L[1], P_Proj[1]],
                                                         z=[P_I[2], P_L[2], P_Proj[2]], i=[0], j=[1], k=[2],
                                                         color='blue', opacity=0.4, name='Angle Triangle'))
                            fig_omni.add_trace(go.Scatter3d(x=[P_I[0] - v_unit[0] * 10, P_L[0] + v_unit[0] * 4],
                                                            y=[P_I[1] - v_unit[1] * 10, P_L[1] + v_unit[1] * 4],
                                                            z=[P_I[2] - v_unit[2] * 10, P_L[2] + v_unit[2] * 4],
                                                            mode='lines', line=dict(color='red', width=5),
                                                            name='Line l'))
                            fig_omni.add_trace(
                                go.Scatter3d(x=[P_I[0], P_Proj[0]], y=[P_I[1], P_Proj[1]], z=[P_I[2], P_Proj[2]],
                                             mode='lines', line=dict(color='green', width=4, dash='dash'),
                                             name='Projection'))

                            add_vector_arrow(fig_omni, P_Proj, P_L, 'black', 'Normal Vector n')

                            vec_a = (P_I - P_Proj) / np.linalg.norm(P_I - P_Proj)
                            vec_b = (P_L - P_Proj) / np.linalg.norm(P_L - P_Proj)
                            sq_size = 1.0
                            c1 = P_Proj + vec_a * sq_size
                            c2 = P_Proj + vec_a * sq_size + vec_b * sq_size
                            c3 = P_Proj + vec_b * sq_size
                            fig_omni.add_trace(
                                go.Scatter3d(x=[c1[0], c2[0], c3[0]], y=[c1[1], c2[1], c3[1]], z=[c1[2], c2[2], c3[2]],
                                             mode='lines', line=dict(color='black', width=3), name='Right Angle ∟',
                                             showlegend=False))


                            def get_arc_3d(center, v1, v2, radius, num_points=20):
                                angle = np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))
                                t = np.linspace(0, angle, num_points)
                                w = v2 - np.dot(v2, v1) * v1
                                if np.linalg.norm(w) > 0: w = w / np.linalg.norm(w)
                                return center[0] + radius * (np.cos(t) * v1[0] + np.sin(t) * w[0]), center[
                                    1] + radius * (np.cos(t) * v1[1] + np.sin(t) * w[1]), center[2] + radius * (
                                                   np.cos(t) * v1[2] + np.sin(t) * w[2])


                            # --- 核心修复：计算三角形边长，自适应缩放半径 ---
                            len_hypot = np.linalg.norm(P_L - P_I)  # 斜边长 (直线)
                            len_adj = np.linalg.norm(P_Proj - P_I)  # 邻边长 (投影)
                            len_opp = np.linalg.norm(P_L - P_Proj)  # 对边长 (法向量那段)

                            # 取相关边长的 35% 作为圆弧半径，确保绝对不会飞出三角形
                            safe_r_theta = min(len_hypot, len_adj) * 0.35
                            safe_r_beta = min(len_hypot, len_opp) * 0.35

                            # β 在顶部 (P_L处，直线与法向量的夹角)
                            v_from_L_to_Proj = (P_Proj - P_L) / np.linalg.norm(P_Proj - P_L)
                            v_from_L_to_I = (P_I - P_L) / np.linalg.norm(P_I - P_L)
                            arc_beta_x, arc_beta_y, arc_beta_z = get_arc_3d(P_L, v_from_L_to_Proj, v_from_L_to_I,
                                                                            safe_r_beta)
                            fig_omni.add_trace(go.Scatter3d(x=arc_beta_x, y=arc_beta_y, z=arc_beta_z, mode='lines',
                                                            line=dict(color='orange', width=4), showlegend=False))

                            # θ 在底部 (P_I处，直线与投影的夹角)
                            v_from_I_to_Proj = (P_Proj - P_I) / np.linalg.norm(P_Proj - P_I)
                            v_from_I_to_L = (P_L - P_I) / np.linalg.norm(P_L - P_I)
                            arc_theta_x, arc_theta_y, arc_theta_z = get_arc_3d(P_I, v_from_I_to_Proj, v_from_I_to_L,
                                                                               safe_r_theta)
                            fig_omni.add_trace(go.Scatter3d(x=arc_theta_x, y=arc_theta_y, z=arc_theta_z, mode='lines',
                                                            line=dict(color='blue', width=4), showlegend=False))

                            # 动态计算文字位置 (角平分线方向，稍微比圆弧远一点点)
                            bisect_beta = v_from_L_to_Proj + v_from_L_to_I
                            bisect_beta = bisect_beta / np.linalg.norm(bisect_beta)
                            pos_beta = P_L + bisect_beta * (safe_r_beta * 1.4)
                            fig_omni.add_trace(
                                go.Scatter3d(x=[pos_beta[0]], y=[pos_beta[1]], z=[pos_beta[2]], mode='text', text=['β'],
                                             textfont=dict(color='orange', size=22), showlegend=False))

                            bisect_theta = v_from_I_to_Proj + v_from_I_to_L
                            bisect_theta = bisect_theta / np.linalg.norm(bisect_theta)
                            pos_theta = P_I + bisect_theta * (safe_r_theta * 1.4)
                            fig_omni.add_trace(
                                go.Scatter3d(x=[pos_theta[0]], y=[pos_theta[1]], z=[pos_theta[2]], mode='text',
                                             text=['θ'], textfont=dict(color='blue', size=22), showlegend=False))

                            fig_omni.add_trace(
                                go.Scatter3d(x=[P_I[0]], y=[P_I[1]], z=[P_I[2]], mode='markers+text', text=['  I'],
                                             textfont=dict(color='black', size=16), marker=dict(color='black', size=5),
                                             name='Intersection Point'))

                        fig_omni.update_layout(scene=dict(aspectmode='cube'), height=650,
                                               margin=dict(l=0, r=0, b=0, t=0))
                        st.plotly_chart(fig_omni, use_container_width=True)

                    # ------------------------------------------
                    # 粘贴你原本的 2. Plane & Plane 代码
                    # ------------------------------------------
                    elif solver_mode == "2. Plane & Plane":
                        st.markdown("### 📥 Input Panel")
                        col_p1, col_p2 = st.columns(2)
                        with col_p1:
                            st.markdown("**Plane 1** ($A_1x+B_1y+C_1z=D_1$)")
                            p1A = st.number_input("Normal A1", value=2.0, key='pp_1a')
                            p1B = st.number_input("Normal B1", value=-1.0, key='pp_1b')
                            p1C = st.number_input("Normal C1", value=-2.0, key='pp_1c')
                            p1D = st.number_input("Constant D1", value=17.0, key='pp_1d')
                        with col_p2:
                            st.markdown("**Plane 2** ($A_2x+B_2y+C_2z=D_2$)")
                            p2A = st.number_input("Normal A2", value=-4.0, key='pp_2a')
                            p2B = st.number_input("Normal B2", value=-3.0, key='pp_2b')
                            p2C = st.number_input("Normal C2", value=5.0, key='pp_2c')
                            p2D = st.number_input("Constant D2", value=10.0, key='pp_2d')

                        st.markdown("---")
                        st.markdown("### 🧠 Smart Output: Step-by-Step")
                        n1, n2 = np.array([p1A, p1B, p1C]), np.array([p2A, p2B, p2C])

                        st.markdown("#### Step 1: Equations")
                        st.latex(rf"\pi_1: {p1A}x + ({p1B})y + ({p1C})z = {p1D}")
                        st.latex(rf"\pi_2: {p2A}x + ({p2B})y + ({p2C})z = {p2D}")

                        st.markdown("#### Step 2: Angle Between Planes")
                        mag_n1, mag_n2 = np.linalg.norm(n1), np.linalg.norm(n2)

                        if mag_n1 == 0 or mag_n2 == 0:
                            st.error("Invalid Normal Vectors.")
                        else:
                            dot_n = np.dot(n1, n2)
                            cos_val = np.clip(dot_n / (mag_n1 * mag_n2), -1.0, 1.0)
                            angle_raw = np.degrees(np.arccos(cos_val))

                            st.latex(
                                rf"\text{{Let }}\beta = \cos^{{-1}}\left(\frac{{\vec{{n_1}} \cdot \vec{{n_2}}}}{{|\vec{{n_1}}| |\vec{{n_2}}|}}\right) = \cos^{{-1}}\left(\frac{{{dot_n:.1f}}}{{{mag_n1:.2f} \times {mag_n2:.2f}}}\right) = {angle_raw:.2f}^\circ")

                            if angle_raw > 90:
                                acute_angle = 180 - angle_raw
                                st.markdown(
                                    f"Since the dot product is negative, $\\beta > 90^\circ$. The acute angle $\\theta$ between the planes is:")
                                st.latex(
                                    rf"\theta = 180^\circ - {angle_raw:.2f}^\circ = \mathbf{{{acute_angle:.1f}^\circ}}")
                            else:
                                acute_angle = angle_raw
                                st.markdown(f"Since $\\beta \le 90^\circ$, the acute angle $\\theta$ is simply:")
                                st.latex(rf"\theta = \mathbf{{{acute_angle:.1f}^\circ}}")

                        direction_v = np.cross(n1, n2)
                        pt_on_line = np.array([0.0, 0.0, 0.0])
                        has_intersection = False

                        if np.linalg.norm(direction_v) > 1e-8:
                            has_intersection = True
                            det_xy = p1A * p2B - p2A * p1B
                            if abs(det_xy) > 1e-5:
                                pt_on_line[0] = (p1D * p2B - p2D * p1B) / det_xy
                                pt_on_line[1] = (p1A * p2D - p2A * p1D) / det_xy
                            elif abs(p1B * p2C - p2B * p1C) > 1e-5:
                                det_yz = p1B * p2C - p2B * p1C
                                pt_on_line[1] = (p1D * p2C - p2D * p1C) / det_yz
                                pt_on_line[2] = (p1B * p2D - p2B * p1D) / det_yz
                            else:
                                det_xz = p1A * p2C - p2A * p1C
                                pt_on_line[0] = (p1D * p2C - p2D * p1C) / det_xz
                                pt_on_line[2] = (p1A * p2D - p2A * p1D) / det_xz


                        if not has_intersection:
                            st.warning("The planes are strictly parallel, no intersection to visualize.")
                        else:
                            fig_omni = create_geogebra_base()


                            def draw_plane(fig, norm, D, center_pt, color, name):
                                u_vec = np.array([1, 0, 0]) if abs(norm[0]) < 0.9 else np.array([0, 1, 0])
                                u_vec = u_vec - (np.dot(u_vec, norm) / np.dot(norm, norm)) * norm
                                u_vec = u_vec / np.linalg.norm(u_vec)
                                w_vec = np.cross(norm, u_vec) / np.linalg.norm(np.cross(norm, u_vec))
                                uu, ww = np.meshgrid(np.linspace(-10, 10, 2), np.linspace(-10, 10, 2))
                                px = center_pt[0] + uu * u_vec[0] + ww * w_vec[0]
                                py = center_pt[1] + uu * u_vec[1] + ww * w_vec[1]
                                pz = center_pt[2] + uu * u_vec[2] + ww * w_vec[2]
                                fig.add_trace(
                                    go.Surface(x=px, y=py, z=pz, colorscale=color, opacity=0.4, showscale=False,
                                               name=name))


                            draw_plane(fig_omni, n1, p1D, pt_on_line, 'Blues', 'Plane 1')
                            draw_plane(fig_omni, n2, p2D, pt_on_line, 'Reds', 'Plane 2')

                            v_unit = direction_v / np.linalg.norm(direction_v)
                            t_arr = np.linspace(-15, 15, 2)
                            fig_omni.add_trace(
                                go.Scatter3d(x=pt_on_line[0] + t_arr * v_unit[0], y=pt_on_line[1] + t_arr * v_unit[1],
                                             z=pt_on_line[2] + t_arr * v_unit[2], mode='lines',
                                             line=dict(color='black', width=6), name='Intersection Line'))

                            n1_unit = n1 / np.linalg.norm(n1)
                            n2_unit = n2 / np.linalg.norm(n2)

                            add_vector_arrow(fig_omni, pt_on_line, pt_on_line + n1_unit * 8, 'black', 'n1')
                            add_vector_arrow(fig_omni, pt_on_line, pt_on_line + n2_unit * 8, 'black', 'n2')

                            p1_perp = np.cross(n1_unit, v_unit)
                            p2_perp = np.cross(v_unit, n2_unit)
                            add_vector_arrow(fig_omni, pt_on_line, pt_on_line + p1_perp * 8, 'green',
                                             'Vector on Plane 1')
                            add_vector_arrow(fig_omni, pt_on_line, pt_on_line + p2_perp * 8, 'green',
                                             'Vector on Plane 2')


                            def get_arc_3d(center, v1, v2, radius, num_points=20):
                                angle = np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))
                                t = np.linspace(0, angle, num_points)
                                w = v2 - np.dot(v2, v1) * v1
                                if np.linalg.norm(w) > 0: w = w / np.linalg.norm(w)
                                return center[0] + radius * (np.cos(t) * v1[0] + np.sin(t) * w[0]), center[
                                    1] + radius * (np.cos(t) * v1[1] + np.sin(t) * w[1]), center[2] + radius * (
                                                   np.cos(t) * v1[2] + np.sin(t) * w[2])


                            arc_n_x, arc_n_y, arc_n_z = get_arc_3d(pt_on_line, n1_unit, n2_unit, 4)
                            fig_omni.add_trace(go.Scatter3d(x=arc_n_x, y=arc_n_y, z=arc_n_z, mode='lines',
                                                            line=dict(color='orange', width=4),
                                                            name='Angle between Normals'))

                            p1_perp_unit, p2_perp_unit = p1_perp / np.linalg.norm(p1_perp), p2_perp / np.linalg.norm(
                                p2_perp)
                            arc_p_x, arc_p_y, arc_p_z = get_arc_3d(pt_on_line, p1_perp_unit, p2_perp_unit, 4)
                            fig_omni.add_trace(go.Scatter3d(x=arc_p_x, y=arc_p_y, z=arc_p_z, mode='lines',
                                                            line=dict(color='blue', width=4),
                                                            name='Angle between Planes'))

                            fig_omni.add_trace(
                                go.Scatter3d(x=[pt_on_line[0]], y=[pt_on_line[1]], z=[pt_on_line[2]], mode='markers',
                                             marker=dict(color='black', size=6), showlegend=False))

                            fig_omni.update_layout(scene=dict(aspectmode='cube'), height=650,
                                                   margin=dict(l=0, r=0, b=0, t=0))
                            st.plotly_chart(fig_omni, use_container_width=True)

                    # ------------------------------------------
                    # 粘贴你原本的 3. Line & Line 代码
                    # ------------------------------------------
                    elif solver_mode == "3. Line & Line":
                        st.markdown("### 📥 Input Panel")
                        col_l1, col_l2 = st.columns(2)
                        with col_l1:
                            st.markdown("**Line 1** (Point + Direction)")
                            l1_px = st.number_input("Point x", value=0.0, key='ll_1px')
                            l1_py = st.number_input("Point y", value=0.0, key='ll_1py')
                            l1_pz = st.number_input("Point z", value=0.0, key='ll_1pz')
                            l1_vx = st.number_input("Direction x", value=1.0, key='ll_1vx')
                            l1_vy = st.number_input("Direction y", value=2.0, key='ll_1vy')
                            l1_vz = st.number_input("Direction z", value=3.0, key='ll_1vz')
                        with col_l2:
                            st.markdown("**Line 2** (Point + Direction)")
                            l2_px = st.number_input("Point x", value=2.0, key='ll_2px')
                            l2_py = st.number_input("Point y", value=1.0, key='ll_2py')
                            l2_pz = st.number_input("Point z", value=-1.0, key='ll_2pz')
                            l2_vx = st.number_input("Direction x", value=-1.0, key='ll_2vx')
                            l2_vy = st.number_input("Direction y", value=1.0, key='ll_2vy')
                            l2_vz = st.number_input("Direction z", value=2.0, key='ll_2vz')

                        st.markdown("---")

                        p1, v1 = np.array([l1_px, l1_py, l1_pz]), np.array([l1_vx, l1_vy, l1_vz])
                        p2, v2 = np.array([l2_px, l2_py, l2_pz]), np.array([l2_vx, l2_vy, l2_vz])


                        st.markdown("#### Step: Angle Calculation")
                        mag_v1, mag_v2 = np.linalg.norm(v1), np.linalg.norm(v2)
                        if mag_v1 == 0 or mag_v2 == 0:
                            st.error("Invalid Direction Vectors.")
                        else:
                            dot_v = np.dot(v1, v2)
                            cos_val = np.clip(dot_v / (mag_v1 * mag_v2), -1.0, 1.0)
                            angle_raw = np.degrees(np.arccos(cos_val))

                            st.latex(
                                rf"\text{{Let }}\beta = \cos^{{-1}}\left(\frac{{\vec{{v_1}} \cdot \vec{{v_2}}}}{{|\vec{{v_1}}| |\vec{{v_2}}|}}\right) = \cos^{{-1}}\left(\frac{{{dot_v:.1f}}}{{{mag_v1:.2f} \times {mag_v2:.2f}}}\right) = {angle_raw:.2f}^\circ")

                            if angle_raw > 90:
                                acute_angle = 180 - angle_raw
                                st.markdown(
                                    f"Since $\\beta > 90^\circ$, we subtract it from $180^\circ$ to find the acute angle:")
                                st.latex(
                                    rf"\theta = 180^\circ - {angle_raw:.2f}^\circ = \mathbf{{{acute_angle:.1f}^\circ}}")
                            else:
                                st.markdown(f"Since $\\beta \le 90^\circ$, the acute angle is:")
                                st.latex(rf"\theta = \mathbf{{{angle_raw:.1f}^\circ}}")


                        fig_omni = create_geogebra_base()
                        center_view = (p1 + p2) / 2
                        t_arr = np.linspace(-15, 15, 2)
                        fig_omni.add_trace(
                            go.Scatter3d(x=p1[0] + t_arr * v1[0], y=p1[1] + t_arr * v1[1], z=p1[2] + t_arr * v1[2],
                                         mode='lines', line=dict(color='red', width=6), name='Line 1'))
                        fig_omni.add_trace(
                            go.Scatter3d(x=p2[0] + t_arr * v2[0], y=p2[1] + t_arr * v2[1], z=p2[2] + t_arr * v2[2],
                                         mode='lines', line=dict(color='blue', width=6), name='Line 2'))

                        fig_omni.update_layout(scene=dict(aspectmode='cube',
                                                          xaxis=dict(range=[center_view[0] - 15, center_view[0] + 15]),
                                                          yaxis=dict(range=[center_view[1] - 15, center_view[1] + 15]),
                                                          zaxis=dict(range=[center_view[2] - 15, center_view[2] + 15])),
                                               height=550, margin=dict(l=0, r=0, b=0, t=0))
                        st.plotly_chart(fig_omni, use_container_width=True)

elif module == "Matrice":
    st.title("📐 The Geometric Essence of Matrices")
    st.markdown("A step-by-step visual journey from basic vectors to spatial transformations.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📖 Part I: The Vector Foundation",
        "🔲 Part II: Matrix Transformations",
        "🔄 Part III: Multiplication & Composition",
        "Part IV: The Mirror Dimension (Transpose)"
    ])

    # ------------------------------------------
    # Tab 1: 向量基础
    # ------------------------------------------
    with tab1:
        st.header("Part I: The Vector Foundation")

        chapter_p1 = st.radio(
            "Select Chapter:",
            ["1. The Rulers (Basis)", "2. Traveling (Linear Combo)", "3. The Reach (Span)"],
            horizontal=True,
            key="radio_p1"
        )
        st.markdown("---")

        col_text, col_plot = st.columns([1, 1.5])

        with col_text:
            if chapter_p1 == "1. The Rulers (Basis)":
                st.markdown("### The fundamental building blocks")
                st.markdown("""
                Before a matrix can warp space, we must define the space itself.

                In standard 2D space, we use two special vectors as our ultimate reference points:
                * **$\hat{i}$ (i-hat)**: exactly 1 unit right $(1, 0)$.
                * **$\hat{j}$ (j-hat)**: exactly 1 unit up $(0, 1)$.

                Every concept in matrices relies on knowing **where these two vectors land**.
                """)

                with col_plot:
                    fig1 = create_base_figure(max_range=3)
                    draw_vector(fig1, 1, 0, "i-hat", "#e74c3c")
                    draw_vector(fig1, 0, 1, "j-hat", "#2ecc71")
                    fig1.update_layout(title="Ch 1: Standard Basis Vectors")
                    st.plotly_chart(fig1, use_container_width=True)

            elif chapter_p1 == "2. Traveling (Linear Combo)":
                st.markdown("### How to reach any destination")
                st.markdown(
                    "We reach any coordinate, like $\\vec{v}$, by **scaling** our basis vectors and **adding** them together.")

                a = st.slider("Scale i-hat (Red)", -5.0, 5.0, 2.0, 0.5)
                b = st.slider("Scale j-hat (Green)", -5.0, 5.0, 3.0, 0.5)

                st.latex(rf"\vec{{v}} = {a}\hat{{i}} + {b}\hat{{j}}")
                st.info(
                    "💡 **Bridge to Part II:** This simple act of scaling and adding is the literal definition of Matrix Multiplication!")

                with col_plot:
                    fig2 = create_base_figure(max_range=6)
                    draw_vector(fig2, 1, 0, "i-hat", "rgba(231, 76, 60, 0.3)")
                    draw_vector(fig2, 0, 1, "j-hat", "rgba(46, 204, 113, 0.3)")
                    draw_vector(fig2, a, 0, f"{a} * i-hat", "#e74c3c")
                    draw_vector(fig2, 0, b, f"{b} * j-hat", "#2ecc71")
                    draw_vector(fig2, a, 0, "", "#e74c3c", dash=True, origin=(0, b), show_arrow=False)
                    draw_vector(fig2, 0, b, "", "#2ecc71", dash=True, origin=(a, 0), show_arrow=False)
                    draw_vector(fig2, a, b, "Result v", "#9b59b6")
                    fig2.update_layout(title="Ch 2: Linear Combination")
                    st.plotly_chart(fig2, use_container_width=True)

            elif chapter_p1 == "3. The Reach (Span)":
                st.markdown("### The limits of our vectors")
                st.markdown("The **Span** is the set of all possible points you can reach by mixing two vectors.")

                c1, c2 = st.columns(2)
                with c1:
                    v1_x = st.number_input("Vector 1 X", value=1.0, step=0.5)
                    v1_y = st.number_input("Vector 1 Y", value=1.0, step=0.5)
                with c2:
                    v2_x = st.number_input("Vector 2 X", value=-2.0, step=0.5)
                    v2_y = st.number_input("Vector 2 Y", value=-2.0, step=0.5)

                show_span = st.checkbox("🌌 Show the Span", value=True)

                det = v1_x * v2_y - v1_y * v2_x
                if abs(det) < 1e-5:
                    st.error(
                        "🚨 **Dimensional Collapse!** These vectors are collinear. The span is trapped on a 1D line.")
                else:
                    st.success("✨ **Freedom!** Their span covers the entire 2D plane.")

                with col_plot:
                    fig3 = create_base_figure(max_range=8)
                    if show_span:
                        span_range = np.linspace(-6, 6, 13)
                        span_x, span_y = [], []
                        for c in span_range:
                            for d in span_range:
                                span_x.append(c * v1_x + d * v2_x)
                                span_y.append(c * v1_y + d * v2_y)
                        fig3.add_trace(go.Scatter(x=span_x, y=span_y, mode='markers',
                                                  marker=dict(size=5, color='rgba(52, 152, 219, 0.4)'),
                                                  hoverinfo='skip'))
                    draw_vector(fig3, v1_x, v1_y, "Vec 1", "#e74c3c")
                    draw_vector(fig3, v2_x, v2_y, "Vec 2", "#2ecc71")
                    fig3.update_layout(title="Ch 3: Span & Dimensionality")
                    st.plotly_chart(fig3, use_container_width=True)

    # ------------------------------------------
    # Tab 2: 矩阵变换
    # ------------------------------------------
    with tab2:
        st.header("Part II: Matrix Transformations")

        chapter_p2 = st.radio(
            "Select Chapter:",
            ["4. The Matrix is a Verb", "5. The Grand Simulator"],
            horizontal=True,
            key="radio_p2"
        )
        st.markdown("---")

        if chapter_p2 == "4. The Matrix is a Verb":
            col_text, col_plot = st.columns([1, 1])
            with col_text:
                st.markdown("### The Secret of the Matrix Columns")
                st.markdown("""
                In Part I, we learned that any point can be found by tracking $\hat{i}$ and $\hat{j}$. 

                Now, imagine **warping** the entire spatial grid. Because the grid remains parallel and evenly spaced (the definition of a *Linear* Transformation), we **only need to track where $\hat{i}$ and $\hat{j}$ land!**
                """)
                st.info("""
                A $2 \\times 2$ matrix is simply a **"record book"**:
                * **Column 1**: The new landing spot of $\hat{i}$.
                * **Column 2**: The new landing spot of $\hat{j}$.
                """)
                st.latex(r"""
                \text{Matrix } M = \begin{bmatrix} \color{red}a & \color{green}b \\ \color{red}c & \color{green}d \end{bmatrix} \implies 
                \begin{cases} 
                \text{New } \hat{i} \text{ lands at } (\color{red}a, \color{red}c) \\ 
                \text{New } \hat{j} \text{ lands at } (\color{green}b, \color{green}d) 
                \end{cases}
                """)

            with col_plot:
                fig4 = create_base_figure(max_range=4)
                draw_vector(fig4, 1, 0, "Old i", "rgba(231, 76, 60, 0.3)")
                draw_vector(fig4, 0, 1, "Old j", "rgba(46, 204, 113, 0.3)")
                draw_vector(fig4, 2, 1, "New i (Col 1)", "#e74c3c")
                draw_vector(fig4, -1, 2, "New j (Col 2)", "#2ecc71")
                fig4.update_layout(title="Ch 4: Matrix columns = Transformed Basis Vectors")
                st.plotly_chart(fig4, use_container_width=True)

        elif chapter_p2 == "5. The Grand Simulator":
            st.markdown("### Putting it all together: Matrix Multiplication")
            st.markdown(
                "Now, drag the sliders to redefine the matrix (the new landing spots of the basis vectors). Then, watch how a custom vector $\\vec{v}$ is dragged along with the warped space.")

            col_ctrl, col_plot = st.columns([1, 1.5])

            with col_ctrl:
                st.markdown("#### Matrix Definition")
                c1, c2 = st.columns(2)
                with c1:
                    i_new_x = st.slider("New i-hat X (a)", -3.0, 3.0, 1.0, 0.5)
                    i_new_y = st.slider("New i-hat Y (c)", -3.0, 3.0, 0.0, 0.5)
                with c2:
                    j_new_x = st.slider("New j-hat X (b)", -3.0, 3.0, 0.0, 0.5)
                    j_new_y = st.slider("New j-hat Y (d)", -3.0, 3.0, 1.0, 0.5)

                M = np.array([[i_new_x, j_new_x], [i_new_y, j_new_y]])

                st.markdown("#### The Target Vector $\\vec{v}$")
                c3, c4 = st.columns(2)
                with c3:
                    v_x = st.number_input("v_X (Steps of i)", value=2.0, step=0.5)
                with c4:
                    v_y = st.number_input("v_Y (Steps of j)", value=1.0, step=0.5)

                target_v = np.array([v_x, v_y])
                new_v = M @ target_v

                st.markdown("---")
                st.info(
                    f"💡 **The ultimate connection:** The original vector meant 'take {v_x} steps of red, and {v_y} steps of green'. After transformation, it **still means exactly that**, just with the *new* red and green vectors! That's what matrix multiplication is.")
                st.latex(
                    rf"\begin{{bmatrix}} \color{{red}}{i_new_x} & \color{{green}}{j_new_x} \\ \color{{red}}{i_new_y} & \color{{green}}{j_new_y} \end{{bmatrix}} \begin{{bmatrix}} {v_x} \\ {v_y} \end{{bmatrix}} = \begin{{bmatrix}} {new_v[0]:.1f} \\ {new_v[1]:.1f} \end{{bmatrix}}")

            with col_plot:
                fig5 = go.Figure()
                grid_range = 6
                for i in range(-grid_range, grid_range + 1):
                    pt1 = M @ np.array([-grid_range, i])
                    pt2 = M @ np.array([grid_range, i])
                    fig5.add_trace(go.Scatter(x=[pt1[0], pt2[0]], y=[pt1[1], pt2[1]], mode='lines',
                                              line=dict(color='rgba(150, 200, 255, 0.4)', width=1.5), hoverinfo='skip'))
                    pt3 = M @ np.array([i, -grid_range])
                    pt4 = M @ np.array([i, grid_range])
                    fig5.add_trace(go.Scatter(x=[pt3[0], pt4[0]], y=[pt3[1], pt4[1]], mode='lines',
                                              line=dict(color='rgba(150, 200, 255, 0.4)', width=1.5), hoverinfo='skip'))

                fig5.add_trace(
                    go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='black', size=8), showlegend=False))
                fig5.add_trace(
                    go.Scatter(x=[0, target_v[0]], y=[0, target_v[1]], mode='lines+markers+text', name='Original v',
                               text=['', f'Old v({v_x}, {v_y})'], textposition='bottom right',
                               textfont=dict(color='grey', size=12), line=dict(color='grey', width=2, dash='dash')))

                draw_vector(fig5, i_new_x, i_new_y, "New i-hat", "#e74c3c")
                draw_vector(fig5, j_new_x, j_new_y, "New j-hat", "#2ecc71")

                v1_scaled = v_x * np.array([i_new_x, i_new_y])
                v2_scaled = v_y * np.array([j_new_x, j_new_y])
                draw_vector(fig5, v1_scaled[0], v1_scaled[1], "", "#e74c3c", dash=True, origin=v2_scaled,
                            show_arrow=False)
                draw_vector(fig5, v2_scaled[0], v2_scaled[1], "", "#2ecc71", dash=True, origin=v1_scaled,
                            show_arrow=False)

                fig5.add_trace(
                    go.Scatter(x=[0, new_v[0]], y=[0, new_v[1]], mode='lines+markers+text', name='Transformed v',
                               text=['', f'New v({new_v[0]:.1f}, {new_v[1]:.1f})'], textposition='top right',
                               textfont=dict(color='purple', size=16), line=dict(color='purple', width=5)))

                fig5.update_layout(title="Ch 5: The Grand Simulator",
                                   xaxis=dict(range=[-6, 6], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                                   yaxis=dict(range=[-6, 6], scaleanchor="x", scaleratio=1, zeroline=True,
                                              zerolinewidth=2, zerolinecolor='black'),
                                   height=650, margin=dict(l=0, r=0, b=0, t=40))
                st.plotly_chart(fig5, use_container_width=True)

    # ------------------------------------------
    # Tab 3: 矩阵乘法与复合变换
    # ------------------------------------------
    with tab3:
        st.header("Part III: Matrix Multiplication is Composition")

        chapter_p3 = st.radio(
            "Select Chapter:",
            ["6. The Calculation vs. The Geometry", "7. Proof: Why AB ≠ BA", "8. Proof: A(BC) = (AB)C",
             "9. Proof: A(B+C) = AB + AC"],
            horizontal=True,
            key="radio_p3"
        )
        st.markdown("---")

        if chapter_p3 == "6. The Calculation vs. The Geometry":
            col_text, col_plot = st.columns([1, 1])
            with col_text:
                st.markdown("### The Bridge Between Numbers and Space")
                st.markdown("""
                You've probably memorized the tedious rule for multiplying matrices: *"Row multiplied by Column, then add them up."*

                But **why** is it defined this way?

                Because mathematically, multiplying two matrices $A \\times B$ is the exact operation of applying transformation $B$ to the space, and then applying transformation $A$ to that already-warped space. 
                """)
                st.info("""
                💡 **Rule of thumb:** Always read from **Right to Left**. 
                $AB\\vec{v}$ means:
                1. Vector $\\vec{v}$ is the starting point.
                2. Matrix $B$ acts on it first.
                3. Matrix $A$ acts on the result.
                """)
            with col_plot:
                st.latex(
                    r"\underbrace{\begin{bmatrix} a & b \\ c & d \end{bmatrix}}_{\text{Matrix A}} \underbrace{\begin{bmatrix} e & f \\ g & h \end{bmatrix}}_{\text{Matrix B}} = \underbrace{\begin{bmatrix} ae+bg & af+bh \\ ce+dg & cf+dh \end{bmatrix}}_{\text{The Combined Transformation}}")
                st.markdown(
                    "*The messy numbers on the right are simply the new coordinates of $\hat{i}$ and $\hat{j}$ after both transformations have occurred!*")

        elif chapter_p3 == "7. Proof: Why AB ≠ BA":
            st.markdown("### Step 1: The Algebraic Proof (Calculation)")
            st.markdown(
                "Let's define two very distinct matrices. Matrix $A$ is an extreme **Shear**, and Matrix $B$ is a **90° Rotation**.")
            st.latex(
                r"A (\text{Shear}) = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}, \quad B (\text{Rotate}) = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}")

            A = np.array([[1, 2], [0, 1]])
            B = np.array([[0, -1], [1, 0]])

            col_calc1, col_calc2 = st.columns(2)
            with col_calc1:
                st.markdown("**Calculate $AB$ (B first, then A):**")
                st.latex(
                    r"AB = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} \mathbf{2} & \mathbf{-1} \\ \mathbf{1} & \mathbf{0} \end{bmatrix}")
                AB = A @ B
            with col_calc2:
                st.markdown("**Calculate $BA$ (A first, then B):**")
                st.latex(
                    r"BA = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} \mathbf{0} & \mathbf{-1} \\ \mathbf{1} & \mathbf{2} \end{bmatrix}")
                BA = B @ A

            st.error(
                "🚨 **Look at the numbers:** The resulting matrices $\\begin{bmatrix} 2 & -1 \\ 1 & 0 \\end{bmatrix}$ and $\\begin{bmatrix} 0 & -1 \\ 1 & 2 \\end{bmatrix}$ are completely different. The computation proves $AB \\neq BA$. But what does this mean physically?")

            st.markdown("---")
            st.markdown("### Step 2: The Geometric Proof (Visualizing the Grids)")
            st.markdown(
                "Let's look at the entire fabric of space. Notice how the green ($\hat{j}$) and red ($\hat{i}$) basis vectors land in totally different spots!")

            col_geom1, col_geom2 = st.columns(2)
            with col_geom1:
                st.markdown("#### Universe 1: Transformation $AB$")
                fig_ab = create_base_figure(max_range=4)
                draw_warped_grid(fig_ab, np.eye(2), color='lightgrey')
                draw_warped_grid(fig_ab, AB, color='rgba(52, 152, 219, 0.4)')
                draw_vector(fig_ab, AB[0, 0], AB[1, 0], "New i", "#e74c3c")
                draw_vector(fig_ab, AB[0, 1], AB[1, 1], "New j", "#2ecc71")
                fig_ab.update_layout(height=450, margin=dict(l=0, r=0, t=30, b=0))
                st.plotly_chart(fig_ab, use_container_width=True)

            with col_geom2:
                st.markdown("#### Universe 2: Transformation $BA$")
                fig_ba = create_base_figure(max_range=4)
                draw_warped_grid(fig_ba, np.eye(2), color='lightgrey')
                draw_warped_grid(fig_ba, BA, color='rgba(155, 89, 182, 0.4)')
                draw_vector(fig_ba, BA[0, 0], BA[1, 0], "New i", "#e74c3c")
                draw_vector(fig_ba, BA[0, 1], BA[1, 1], "New j", "#2ecc71")
                fig_ba.update_layout(height=450, margin=dict(l=0, r=0, t=30, b=0))
                st.plotly_chart(fig_ba, use_container_width=True)

        elif chapter_p3 == "8. Proof: A(BC) = (AB)C":
            st.markdown("### Step 1: The Algebraic Proof (Calculation)")
            st.markdown(
                "Is matrix multiplication associative? Let's prove it by computing it both ways using three random matrices.")
            st.latex(
                r"A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}")

            col_assoc1, col_assoc2 = st.columns(2)
            with col_assoc1:
                st.markdown("**Path 1: $A(BC)$**")
                st.latex(
                    r"BC = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}")
                st.latex(
                    r"A(BC) = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix} = \mathbf{\begin{bmatrix} 2 & -2 \\ 2 & 0 \end{bmatrix}}")

            with col_assoc2:
                st.markdown("**Path 2: $(AB)C$**")
                st.latex(
                    r"AB = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 0 & 2 \end{bmatrix}")
                st.latex(
                    r"(AB)C = \begin{bmatrix} 2 & 2 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \mathbf{\begin{bmatrix} 2 & -2 \\ 2 & 0 \end{bmatrix}}")

            st.success(
                "✅ **The math confirms it:** Both groupings result in the exact same matrix $\\begin{bmatrix} 2 & -2 \\ 2 & 0 \\end{bmatrix}$.")

            st.markdown("---")
            st.markdown("### Step 2: The Geometric Truth")
            st.markdown("""
            The calculation proves it works, but **Geometry explains WHY it works**.

            Imagine you have a piece of clay (the 2D space), and you perform three actions:
            1. **$C$**: Rotate it 90 degrees.
            2. **$B$**: Stretch it by 2x.
            3. **$A$**: Shear it.

            * **$A(BC)$ means:** You hand the clay to someone who does $(BC)$ (Rotate then Stretch). Once they hand it back, you do $A$ (Shear).
            * **$(AB)C$ means:** You do $C$ (Rotate) first. Then you hand it to someone who performs the combined action $(AB)$ (Stretch then Shear).

            Because the **physical sequence of events (C ➔ B ➔ A) never changed**, the final shape of the clay MUST be identical! The parentheses only change *how we group the instructions*, not the order of the universe's physics.
            """)

        elif chapter_p3 == "9. Proof: A(B+C) = AB + AC":
            st.markdown("### Step 1: The Algebraic Proof (Calculation)")
            st.markdown("Does matrix multiplication distribute over addition? Let's test it with three matrices:")
            st.latex(
                r"A = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}")

            col_dist1, col_dist2 = st.columns(2)
            with col_dist1:
                st.markdown("**Path 1: Compute $A(B+C)$**")
                st.markdown("First, add B and C, then multiply by A.")
                st.latex(
                    r"B+C = \begin{bmatrix} 2+0 & 0-1 \\ 0+1 & 2+0 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}")
                st.latex(
                    r"A(B+C) = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix}")
                st.latex(r"A(B+C) = \mathbf{\begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}}")

            with col_dist2:
                st.markdown("**Path 2: Compute $AB + AC$**")
                st.markdown("First multiply A with B and C separately, then add the results.")
                st.latex(
                    r"AB = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 2 & 4 \\ 0 & 2 \end{bmatrix}")
                st.latex(
                    r"AC = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 2 & -1 \\ 1 & 0 \end{bmatrix}")
                st.latex(
                    r"AB + AC = \begin{bmatrix} 2+2 & 4-1 \\ 0+1 & 2+0 \end{bmatrix} = \mathbf{\begin{bmatrix} 4 & 3 \\ 1 & 2 \end{bmatrix}}")

            st.success(
                "✅ **The math confirms it:** $A(B+C)$ yields the exact same matrix as $AB + AC$. The distributive property holds!")

            st.markdown("---")
            st.markdown("### Step 2: The Geometric Truth (Why this is the soul of Linearity)")
            st.markdown("""
            To understand **WHY** this works, we must understand what Matrix Addition and Linear Transformations geometrically mean.

            * **What is $B+C$?** Geometrically, adding two matrices means adding where they send the basis vectors. If Matrix $B$ sends $\hat{i}$ to vector $\\vec{v}_B$, and Matrix $C$ sends $\hat{i}$ to $\\vec{v}_C$, then $(B+C)$ sends $\hat{i}$ to their vector sum: $\\vec{v}_B + \\vec{v}_C$ (following the parallelogram rule).

            * **Path 1: $A(B+C)$** means you first find that new diagonal vector $(\\vec{v}_B + \\vec{v}_C)$ by adding the transformations together, and **THEN** you apply transformation $A$ to warp that new vector.
            * **Path 2: $AB + AC$** means you apply transformation $A$ to $\\vec{v}_B$ first, and apply $A$ to $\\vec{v}_C$ separately. **THEN** you add those two warped vectors together.

            Why do they end up in the exact same spot? Because matrix $A$ represents a **Linear Transformation**. 

            The strict definition of "Linear" is that **grid lines remain parallel and evenly spaced**, and the origin remains fixed. Therefore, warping a parallelogram and then looking at its diagonal ($A(B+C)$) is geometrically identical to looking at the warped sides and drawing the new diagonal ($AB + AC$).
            """)

    # ------------------------------------------
    # Tab 4: 矩阵转置 (The Mirror Dimension)
    # ------------------------------------------
    with tab4:
        st.header("Chapter IV: The Mirror Dimension (Transpose)")
        st.markdown("---")

        st.markdown("""
        ### 1. The Anatomy of a Flip
        In textbooks, the **Transpose ($A^T$)** is defined as "swapping rows and columns". 
        But geometrically, it's like anchoring the matrix by its **Main Diagonal** and flipping the rest of the universe across it like a mirror.
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Original Matrix $A$**")
            a = st.number_input("a (top-left)", value=1.0, step=0.5)
            b = st.number_input("b (top-right)", value=2.0, step=0.5)
            c = st.number_input("c (bottom-left)", value=3.0, step=0.5)
            d = st.number_input("d (bottom-right)", value=4.0, step=0.5)

        A = np.array([[a, b], [c, d]])
        A_T = A.T

        with col2:
            st.markdown("**Watch the Mirror Effect:**")
            st.latex(rf"""
            A = \begin{{bmatrix}} \mathbf{{\color{{#e74c3c}}{a}}} & \color{{#3498db}}{b} \\ \color{{#9b59b6}}{c} & \mathbf{{\color{{#e74c3c}}{d}}} \end{{bmatrix}} 
            \quad \xrightarrow{{\text{{Transpose}}}} \quad 
            A^T = \begin{{bmatrix}} \mathbf{{\color{{#e74c3c}}{a}}} & \color{{#9b59b6}}{c} \\ \color{{#3498db}}{b} & \mathbf{{\color{{#e74c3c}}{d}}} \end{{bmatrix}}
            """)
            st.info(
                "💡 Notice how the red diagonal elements ($\mathbf{a}$ and $\mathbf{d}$) never move. They are the 'hinge' of the mirror!")

        st.markdown("---")
        st.markdown("### 2. The Geometric Truth: Area is Preserved!")
        st.markdown("""
        When you transpose a matrix, the basis vectors land in different spots, meaning the space is warped differently. 
        **However**, the scaling factor of the space (the **Determinant**) remains exactly the same! 
        """)

        col_plot1, col_plot2 = st.columns(2)


        def draw_transformed_space(matrix, title, line_color):
            fig = go.Figure()
            fig.add_trace(
                go.Scatter(x=[-5, 5], y=[0, 0], mode='lines', line=dict(color='black', width=1), showlegend=False))
            fig.add_trace(
                go.Scatter(x=[0, 0], y=[-5, 5], mode='lines', line=dict(color='black', width=1), showlegend=False))
            fig.add_trace(
                go.Scatter(x=[-5, 5], y=[-5, 5], mode='lines', line=dict(color='orange', width=2, dash='dash'),
                           name='Mirror (y=x)'))

            for i in range(-3, 4):
                p_start = matrix @ np.array([i, -3])
                p_end = matrix @ np.array([i, 3])
                fig.add_trace(go.Scatter(x=[p_start[0], p_end[0]], y=[p_start[1], p_end[1]], mode='lines',
                                         line=dict(color=line_color, width=1), showlegend=False))
                p_start2 = matrix @ np.array([-3, i])
                p_end2 = matrix @ np.array([3, i])
                fig.add_trace(go.Scatter(x=[p_start2[0], p_end2[0]], y=[p_start2[1], p_end2[1]], mode='lines',
                                         line=dict(color=line_color, width=1), showlegend=False))

            i_hat = matrix @ np.array([1, 0])
            j_hat = matrix @ np.array([0, 1])
            fig.add_trace(go.Scatter(x=[0, i_hat[0]], y=[0, i_hat[1]], mode='lines+markers+text', text=['', 'New i'],
                                     line=dict(color='red', width=4), name='Transformed i-hat'))
            fig.add_trace(go.Scatter(x=[0, j_hat[0]], y=[0, j_hat[1]], mode='lines+markers+text', text=['', 'New j'],
                                     line=dict(color='green', width=4), name='Transformed j-hat'))

            fig.update_layout(title=title, xaxis=dict(range=[-6, 6]),
                              yaxis=dict(range=[-6, 6], scaleanchor="x", scaleratio=1), height=400,
                              margin=dict(l=0, r=0, t=30, b=0))
            return fig


        with col_plot1:
            figA = draw_transformed_space(A, "Universe $A$", "rgba(52, 152, 219, 0.3)")
            st.plotly_chart(figA, use_container_width=True)
            det_A = np.linalg.det(A)
            st.latex(rf"\det(A) = ({a})({d}) - ({b})({c}) = \mathbf{{{det_A:.2f}}}")

        with col_plot2:
            figAT = draw_transformed_space(A_T, "Universe $A^T$", "rgba(155, 89, 182, 0.3)")
            st.plotly_chart(figAT, use_container_width=True)
            det_AT = np.linalg.det(A_T)
            st.latex(rf"\det(A^T) = ({a})({d}) - ({c})({b}) = \mathbf{{{det_AT:.2f}}}")

        st.success(
            "Notice how the shapes are flipped, but the overall area (the grid boxes) scaled by the exact same amount! $\det(A) = \det(A^T)$")

        st.markdown("---")
        st.markdown("### 3. The Shoe-Sock Property: $(AB)^T = B^T A^T$")
        st.markdown("""
        Why does the order reverse when you transpose a multiplied matrix? 
        Think of it as putting on clothes:
        1. First, you put on your **Socks** (Matrix $B$).
        2. Then, you put on your **Shoes** (Matrix $A$).
        3. You are now wearing $(AB)$.

        If you want to completely reverse the process (the Transpose), what do you do? 
        You cannot take off your socks first! You must **take off your Shoes first ($A^T$), then take off your Socks ($B^T$)**.
        """)
        st.latex(r"\mathbf{(AB)^T = B^T A^T}")