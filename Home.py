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
import requests  # <--- 新增的库，用来连网拿云端数据！

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
# 🚀 强制植入 Google Analytics (用于搜索验证)
# ==========================================
ga_id = "G-6N2EPBE323"
ga_code = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{ga_id}');
</script>
"""
# 使用 st.html 强行把脚本塞进页面（Streamlit 1.34.0+ 推荐）
st.html(ga_code)

# 同时也把之前的 Meta Tag 也加上去，双重保险！
st.markdown(
    '<meta name="google-site-verification" content="a8uPEIvVdeSAhH52jfcLKWuEC_rq5NHiN7ZJnjTFgrU" />',
    unsafe_allow_html=True
)
# ==========================================
# 2. 主程序入口
# ==========================================
def main():
    # --- 侧边栏 Logo ---
    st.sidebar.markdown("### 🌳 The Math Roots")
    st.sidebar.caption("Matrikulasi Innovation Project")
    st.sidebar.divider()

    # ==========================================
    # 👇👇👇 永久云端计数器 (JSONBin) 👇👇👇
    # ==========================================
    try:
        # 从 Streamlit Secrets 里读取密码 (确保你已经在后台配置好了)
        BIN_ID = st.secrets["JSONBIN_ID"]
        API_KEY = st.secrets["JSONBIN_KEY"]
        URL = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
        HEADERS = {
            "X-Master-Key": API_KEY,
            "Content-Type": "application/json"
        }

        # 利用 session_state 确保每个访客点开只算 1 次
        if 'has_visited' not in st.session_state:
            st.session_state.has_visited = True

            # 1. 连上云端，获取最新真实人数
            req = requests.get(URL, headers=HEADERS)
            data = req.json()
            count = data['record']['count']

            # 2. 有新访客，数字 +1
            count += 1

            # 3. 把新数字写回云端，永久保存！
            requests.put(URL, json={"count": count}, headers=HEADERS)

        else:
            # 如果是同一访客在各个页面切来切去，只读取数字，不加 1
            req = requests.get(URL, headers=HEADERS)
            count = req.json()['record']['count']

    except Exception as e:
        # 终极防崩保护：如果网络断了或者没配密码，优雅保底显示 112 (你截图里的数字)
        count = 112

    # 在侧边栏极其醒目的位置展示！
    st.sidebar.metric(label="🔥 Total Page Views", value=count, help="Total number of times this universe has been accessed.")
    st.sidebar.divider()
    # ==========================================
    # 👆👆👆 计数器代码结束 👆👆👆
    # ==========================================

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
    st.subheader("🏛️ The Six Volumes of Discovery")
    st.write("Select a volume from the sidebar to step into the labyrinth.")

    # 使用 columns 来做一个漂亮的网格布局
    c1, c2 = st.columns(2)

    with c1:
        st.info("""
        ### 📖 Volume I: Number Systems
        **The Genesis of Quantity.** Witness the struggle to expand the boundaries of reality. From the resistance against negative debts to the 'mental torture' of imaginary roots, explore how breaking the rules unlocked the geometry of the universe.
        """)

        st.warning("""
        ### 📖 Volume III: Linear Algebra
        **The Spatial Fabric.** Step beyond the limitations of human sight. Visualize vectors, cross products, and matrices—the invisible geometric engines that orchestrate everything from modern physics to artificial intelligence.
        """)

        st.error("""
        ### 📖 Volume V: Set Theory
        **The Architecture of the Void.** Descend into the absolute bedrock of logic. Witness Georg Cantor’s dangerous dance with multiple infinities, the paradoxes that broke the mathematical world, and the obsessive quest to define reality from an empty set.
        """)

    with c2:
        st.success("""
        ### 📖 Volume II: Sequences & Series
        **The Rhythm of Infinity.** How do we grasp the endless? Watch the battle to tame infinite growth, the birth of the natural constant $e$, and how chaotic curves are forced into perfect, infinite polynomials.
        """)

        st.error("""
        ### 📖 Volume IV: The Calculus Saga
        **The War on Infinity.** A 2000-year epic. Experience the paralyzing paradoxes of antiquity, the fierce race to calculate motion, and the ultimate triumph of grounding 'change' into pure, rigorous logic.
        """)

        st.info("""
        ### 📖 Volume VI: Probability & Statistics
        **The Taming of Chaos.** From smoky 17th-century gambling dens to the rigorous axioms of modern science. Watch humanity weaponize mathematics to predict the unpredictable, quantify ignorance, and conquer the ultimate frontier of uncertainty.
        """)

    st.divider()

    # --- 3. 底部结语 ---


# ==========================================
# 执行运行
# ==========================================
if __name__ == "__main__":
    main()