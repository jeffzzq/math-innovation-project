import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats
from fractions import Fraction
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import scipy.integrate as integrate
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, \
    convert_xor
import re

# ==========================================
# 1. 全局页面配置 (必须放最上面！)
# ==========================================
st.set_page_config(
    page_title="The Math Roots | Preface",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. 主程序入口
# ==========================================
def main():
    # --- 侧边栏 Logo ---
    st.sidebar.markdown("### 🌳 The Math Roots")
    st.sidebar.caption("Matrikulasi Innovation Project")
    st.sidebar.divider()

    # --- 1. 序言区域 (The Preface) ---
    st.title("The Math Roots 🌳")
    st.markdown("### *A Chronicle of Human Reason.*")

    st.markdown("""
    > *"Mathematics is not a straight line drawn from ignorance to truth. It is a rugged, fragmented epic written by the collective struggle of humanity."*

    The history of mathematics is profoundly heavy. 

    For millennia, it grew slowly from the mud of sheer necessity—ancient scribes tracking the stars, merchants measuring the floods of rivers, and distant scholars daring to grasp the terrifying void of 'Zero'. It is an architecture built brick by brick across empires, traded along the Silk Road, and preserved through the Dark Ages. 

    **Yet, this evolution was never peaceful.** Time and again, humanity hit impenetrable walls. We were paralyzed by the paradoxes of infinity. We were baffled by equations that demanded answers that "did not exist." We were trapped in flat geometries that could not describe a curved reality. During these long intellectual winters, hard work alone was never enough.

    To break the siege, it required leaps of sheer, unreasonable intuition. It required generations of rebellious minds willing to break the very rules of logic they were taught—to invent imaginary dimensions, to calculate with the 'ghosts' of vanished quantities, and to force chaos to surrender to symmetry. 

    **Welcome to The Math Roots.** Here, we do not merely memorize the formulas left behind as the spoils of these wars. We trace the roots of the logic. We relive the desperate bottlenecks of history, and we visualize the exact moments when human reason shattered the boundaries of what was thought possible.
    """)

    st.divider()

    # --- 2. 卷宗大纲 (The Volumes) ---
    st.subheader("🏛️ The Four Volumes of Discovery")
    st.write("Select a volume from the sidebar to step into the labyrinth.")

    # 使用 columns 来做一个漂亮的网格布局，模拟四大卷宗
    c1, c2 = st.columns(2)

    with c1:
        st.info("""
        ### 📖 Volume I: Number Systems
        **The Genesis of Quantity.** Witness the struggle to expand the boundaries of reality. From the resistance against negative debts to the 'mental torture' of imaginary roots, explore how breaking the rules unlocked the geometry of the universe.
        """)

        st.success("""
        ### 📖 Volume II: Sequences & Series
        **The Rhythm of Infinity.** How do we grasp the endless? Watch the battle to tame infinite growth, the birth of the natural constant $e$, and how chaotic curves are forced into perfect, infinite polynomials.
        """)

    with c2:
        st.warning("""
        ### 📖 Volume III: Linear Algebra
        **The Spatial Fabric.** Step beyond the limitations of human sight. Visualize vectors, cross products, and matrices—the invisible geometric engines that orchestrate everything from modern physics to artificial intelligence.
        """)

        st.error("""
        ### 📖 Volume IV: The Calculus Saga
        **The War on Infinity.** A 2000-year epic. Experience the paralyzing paradoxes of antiquity, the fierce race to calculate motion, and the ultimate triumph of grounding 'change' into pure, rigorous logic.
        """)

    st.divider()

    # --- 3. 底部结语 ---



# ==========================================
# 执行运行
# ==========================================
if __name__ == "__main__":
    main()