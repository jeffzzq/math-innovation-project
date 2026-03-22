import streamlit as st

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(page_title="The Math Roots | Probability & Distributions", page_icon="📜", layout="wide")

# ==========================================
# Sidebar Navigation
# ==========================================
st.sidebar.title("Table of Contents")
chapter = st.sidebar.radio(
    "Select a chapter to read:",
    [
        "📖 Chapter 1: History of Probability",
        "📐 Chapter 2: Probability Distributions"
    ]
)

# ==========================================
# Chapter 1: History of Probability (Pure Text Epic)
# ==========================================
if chapter == "📖 Chapter 1: History of Probability":

    st.title("📜 The Epic of Probability")
    st.markdown(
        "From the desperate guesses of gamblers to the ultimate laws of the universe, this is a 400-year intellectual adventure.")
    st.divider()

    # Using Tabs for a book-reading experience
    tab_prologue, tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎭 Prologue (16th C.)",
        "✉️ Act I (1654)",
        "💀 Act II (1662)",
        "🌊 Act III (1688)",
        "📈 Act IV (18th C.)",
        "🏰 Act V (1933)"
    ])

    with tab_prologue:
        st.header("🎭 Prologue: The Brilliant Rule-Breaker")

        st.markdown("""
        In **16th-century Italy**, if you wanted to predict the future, you consulted an astrologer. But **Gerolamo Cardano** was a different breed. He was Europe's most sought-after physician, a ruthless mathematician, and... a hopelessly addicted gambler. 
        """)

        # --- 修正后的三次方程真相：毁约与完善 ---
        st.info("""
        #### 🗡️ The Broken Oath: The Cubic Equation
        Before he analyzed dice, Cardano shook the mathematical world. He is famous for publishing the complete solution to the **Cubic Equation** in his 1545 masterpiece, *Ars Magna*. 

        **The Controversy:** He learned a partial solution from a rival mathematician, Tartaglia, after swearing a sacred blood oath never to publish it. But when Cardano later discovered an even older manuscript with the same solution, he found his loophole. He broke his oath to Tartaglia, but he didn't plagiarize. Instead, **Cardano perfected it**. He expanded the fragmented rules into a unified theory of 13 cases, and in doing so, he accidentally stumbled into the terrifying, uncharted territory of **Imaginary Numbers**. 
        """)

        st.divider()

        # --- 左右分列保持不变，强化他在绝境中的计算 ---
        col1, col2 = st.columns([1.5, 1])

        with col1:
            st.subheader("The Desperation at the Dice Table")
            st.markdown("""
            A man willing to break a sacred oath for algebra is a man willing to decode the secrets of luck. Cardano was severely addicted to gambling. He once pawned his wife's jewelry and his own furniture just to stay at the card table. 

            Driven by pure financial desperation, he wrote *Liber de Ludo Aleae* (The Book on Games of Chance). He was the first human to mathematically realize that rolling two fair dice yields exactly **36 possible outcomes**. He proved that "luck" wasn't magic—it was just counting.
            """)
            st.latex(r"P = \frac{f}{n}")
            st.caption("*(Where $f$ represents favorable outcomes, and $n$ represents all possible outcomes.)*")

        with col2:
            st.warning("""
            #### ⚡ The Blasphemy
            Today, $P = f/n$ is middle-school math. But in the 1500s? It was **pure blasphemy**. 

            People firmly believed that a dice roll was controlled directly by God or the stars. To say you could *calculate* God's will using simple fractions was a dangerous, radical idea that stripped the divine mystery away from the universe.
            """)

        st.divider()

        # --- 悲剧结尾 ---
        st.error("""
        🩸 **The Final Tragedy:** Cardano could calculate the dice, but he couldn't calculate his own life's ruin. His eldest son was beheaded for murder, and Cardano himself was later arrested by the Roman Inquisition for the ultimate heresy: **casting a horoscope for Jesus Christ.** His groundbreaking probability manuscript lay hidden in a drawer for over a century, missing its chance to change the world in his lifetime.
        """)
    with tab3:
        st.header("🌊 Act III: The Casino of Oceans")

        st.markdown("""
        Probability didn't just stay in the aristocratic salons of Paris or the gambling dens of Italy. It had to survive the brutal, salt-stained reality of the **17th-century Age of Discovery**. 

        In London and Amsterdam, the ocean wasn't just water—it was the world's most terrifying and lucrative casino. The chips were human lives, wooden galleons, and cargo holds full of nutmeg and black pepper.
        """)

        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("🌶️ The Spice Roulette")
            st.markdown("""
            A single merchant ship sailing to the East Indies took two years round-trip. The stakes were binary and absolute:
            * **The Jackpot:** If the ship returned safely, the spices could yield a **1,000% return on investment**. You became a lord overnight.
            * **The Ruin:** If it met a monsoon off the Cape of Good Hope, or pirates in the Malacca Strait, you lost everything and went to debtor's prison.

            Merchants realized that putting all their money on *one* ship was just playing Russian Roulette with the sea. They needed a way to **commodify fear**.
            """)

        with col2:
            st.subheader("☕ The Data Hub: Lloyd's Coffee")
            st.markdown("""
                        By the 1680s, a smoky room on Tower Street in London run by Edward Lloyd became the most important data center in the world. 

                        It wasn't just a place to drink coffee. It was a raw intelligence exchange. **Weather-beaten captains—survivors of brutal monsoons, scurvy, and pirate cannon fire—would trade rumors over their pipes:** *Which routes had the most shipwrecks this season? Which shipbuilder's hulls survived the storms?* Edward Lloyd began compiling this chaotic gossip into a printed newsletter: **Lloyd's News**—the world's first database of maritime risk.
                        """)

        st.divider()

        # --- 引入“Underwriter”的词源，极度硬核的细节 ---
        st.info("""
        #### ✍️ The Literal "Under-writers"
        Here is how modern insurance was born from raw probability data. A wealthy investor wouldn't back a whole ship anymore. Instead, a document detailing the ship, its route, and its cargo would be passed around the tables at Lloyd's Coffee House. 

        Investors would write their names **literally *under* the text** (hence the birth of the word **"Under-writer"**), stating how much risk they were willing to take in exchange for a percentage of the profits (the premium). They were mathematically slicing up the variance of the ocean.
        """)

        # --- 核心认知升级 ---
        st.success("""
        #### 🧠 The Core Cognition: The Shift from Individual to Aggregate
        This was probability's first true industrial application, and it required a massive philosophical leap. 

        The underwriters realized a profound mathematical truth: **You cannot predict the fate of *one specific ship*.** The ocean is too chaotic. **But, if you look at *100 ships*, the chaos smooths out into a predictable curve.** If data showed that historically 5 out of 100 ships sink, you just set your premiums high enough to cover those 5 losses, and the remaining 95 guarantee your wealth. **They stopped asking *"Will God sink this ship?"* and started calculating *"What is the expected value of this fleet?"***
        """)
        # --- 追加的世纪回响（The Immortal Legacy） ---
        st.markdown("""
                > **🏛️ The Immortal Legacy:** > That smoky room on Tower Street didn't just fade into the history books. It evolved into **Lloyd's of London**, the world's leading insurance and reinsurance market, and it is still operating today. 
                > 
                > Three centuries later, they are still doing exactly what Edward Lloyd's weather-beaten patrons did—pricing the unknown using probability. But today, instead of wooden galleons and black pepper, they underwrite **SpaceX rockets, global cyber-attacks, and even the vocal cords of rock stars.** >
                > The mathematical spell cast in that 17th-century coffee house is still running the 21st-century world.
                """)
    with tab2:
        st.header("💀 Act II: The Mathematics of the Grim Reaper")

        st.markdown("""
        While French mathematicians were elegantly calculating the odds of dice games in Parisian salons, **1660s London** was facing an apocalypse. The Bubonic Plague was ravaging the city. The air smelled of vinegar and death.

        Yet, from this unimaginable horror, a completely different branch of probability was born: **Statistics**.
        """)

        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.subheader("📜 The Gruesome Ledger")
            st.markdown("""
            To track the plague, the London government published weekly **Bills of Mortality**. 

            The data collection was crude and terrifying. The government employed "Searchers of the Dead"—usually illiterate, elderly parish women who would ring a bell, enter infected homes, inspect the corpses, and yell out the cause of death.

            The resulting lists were a chaotic, morbid mess. Causes of death included:
            * *Plague*
            * *Bitten by a mad dog*
            * *Grief*
            * *Teeth* (Dental infections)
            * *King's Evil* (Scrofula)
            """)
            #

        with col2:
            st.subheader("🧵 The Unlikely Genius: John Graunt")
            st.markdown("""
            The man who decoded this chaos wasn't a university-trained mathematician. **John Graunt was a haberdasher**—a merchant who sold buttons, needles, and cloth. 

            But Graunt had a peculiar obsession. While others saw the *Bills of Mortality* as just a terrifying list of doomed neighbors, Graunt saw **a dataset**. 

            He spent years painstakingly aggregating decades of these messy weekly reports into massive tables. He wasn't asking *"Why did God take this person?"* Instead, he asked a dangerously modern question: **"What is the mathematical pattern of death?"**
            """)

        st.divider()

        # --- 核心发现：生命表与惊人的常数 ---
        st.error("""
        #### 📉 The Chilling Discovery: The "Constants" of Mortality
        Graunt published *Natural and Political Observations Made upon the Bills of Mortality* in 1662. What he found shocked the world: **Death is not random.**

        1. **The First Life Table:** He calculated the probability of a Londoner surviving to a certain age. He proved that exactly **36% of children died before age 6**. 
        2. **The Sex Ratio:** He was the first human to mathematically prove that slightly more males are born than females (to offset the higher male mortality rate).
        3. **Macroscopic Determinism:** He discovered that while you can never predict *who* will commit suicide or die from an accident tomorrow, the **percentage** of suicides and accidents in a city of millions remains terrifyingly stable year after year. 
        """)

        # --- 核心认知升级 ---
        st.success("""
        #### 🧠 Core Cognition: The Birth of "Political Arithmetic"
        Graunt's work caused a paradigm shift in human thought. He proved that **individual unpredictability disappears in the aggregate.** A single human life is subject to chaos, free will, and tragic accidents. But a population of 100,000 humans operates like a clockwork machine governed by strict mathematical laws. This realization birthed demography, epidemiology, and the exact mathematical foundation required for the modern **Life Insurance** industry.
        """)

    with tab1:
        st.header("✉️ Act III: The Unfinished Game & The Time Travelers")

        # 去掉鼠疫/航海的剧透，直接进入 1654 年的背景设定，保留你的原句结构
        st.markdown("""
        A profound revolution was brewing in the sunlit châteaux of France. The year was **1654**.

        It started not with scientists, but with a hardcore gambler: **Antoine Gombaud, the Chevalier de Méré**. He brought a seemingly impossible paradox to his friend, the tortured young genius **Blaise Pascal**.
        """)

        st.divider()

        # --- 使用 Subtabs 分层展示 ---
        subtab1, subtab2, subtab3 = st.tabs([
            "🎲 The Dilemma",
            "✉️ Pascal & Fermat",
            "🧠 Expected Value"
        ])

        with subtab1:
            # --- 悬案：未完成的赌局 (完全使用你的原文本) ---
            st.error("""
            #### 💰 The Dilemma: The Problem of Points 
            Two noblemen are playing a game of coin flips. The first to win **3 rounds** takes the pot of **100 gold coins**.

            Suddenly, the King's guards raid the tavern. The game is forced to stop early. 
            At this moment: **Player A has won 2 rounds. Player B has won 1 round.**

            **How should they divide the 100 gold coins fairly?**
            * *The Naive Way:* A has twice as many points (2:1), so give A 66 coins and B 33. **(Pascal realized this was mathematically wrong.)**
            """)

            st.markdown("""
            Pascal was stuck. He wrote a letter to a reclusive lawyer in Toulouse who moonlighted as a mathematical god: **Pierre de Fermat**. Over the summer of 1654, a frantic exchange of letters between these two titans birthed modern probability.

            They realized a terrifying truth: **To divide the gold today, you cannot look at the past. You must mathematically map out the futures that never happened.**
            """)

        with subtab2:
            # --- 左右分列：双王的脑回路 (完全使用你的原文本) ---
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("📐 Pascal's Path: Branching Realities")
                st.markdown("""
                Pascal approached it like a time-traveling physicist. He mapped out the **branching tree of possible futures**:

                If they had played the next round:
                1. **Timeline 1 (50% chance):** Player A wins the next flip. A reaches 3 points and takes all 100 coins.
                2. **Timeline 2 (50% chance):** Player B wins. The score is tied 2-2. They must play one final tie-breaker flip.
                    * If A wins the tie-breaker (25% overall): A gets 100.
                    * If B wins the tie-breaker (25% overall): B gets 100.

                **Pascal's Calculation for A:** $50\% + 25\% = 75\%$. 
                Player A deserves **75 gold coins**, leaving B with **25**.
                """)
                st.caption(
                    "He later generalized this using the famous **Pascal's Triangle** to handle any number of remaining rounds.")

            with col2:
                st.subheader("🌌 Fermat's Path: The God's-Eye View")
                st.markdown("""
                Fermat was a pure combinatoric genius. He hated branching timelines because they had different lengths. Instead, he forced the universe into symmetry. 

                He said: *"Let's imagine they **must** play exactly 2 more dummy rounds, no matter what."*
                There are only 4 possible symmetrical outcomes for the next two flips:
                * **A** wins, **A** wins (A takes pot)
                * **A** wins, **B** wins (A takes pot)
                * **B** wins, **A** wins (A takes pot)
                * **B** wins, **B** wins (B takes pot)

                Out of 4 possible parallel universes, A wins the pot in 3 of them. 
                **Fermat's Calculation:** $\frac{3}{4}$ for A, $\frac{1}{4}$ for B. **Exactly the same answer.**
                """)

        with subtab3:
            # --- 惠更斯的期望值 (完整英文版文本原封不动) ---
            st.subheader("🧠 Core Cognition Upgrade: The True Birth of Expected Value")

            st.markdown(r"""
            As mentioned earlier, **Christiaan Huygens** didn't just invent "Expected Value" out of thin air in his study. He was deeply inspired after hearing the details of Pascal and Fermat's correspondence regarding the "Problem of Points" during his visit to Paris in 1655, which led him to systematic research.

            His path to expected value went a step further than Pascal and Fermat: **he attempted to establish a universal system of "fair price in games of chance".**
            """)

            with st.container():
                st.markdown(r"""
                #### 1. Huygens' Starting Point: Fair Exchange
                Huygens didn't entangle himself in complex combinatorics (Fermat's method) or recursion (Pascal's method). He proposed a concept with a strong commercial mindset:

                > "If, before a game begins, you have $p$ chances to win $a$, and $q$ chances to win $b$, how much is this chance itself 'worth'?"

                He believed that in a fair game, the value of a right should equal the amount you are willing to pay to acquire that right.
                """)

            with st.container():
                st.markdown(r"""
                #### 2. His Deductive Logic: Imagine Playing with a Fair Scale
                In his book *On Reasoning in Games of Chance* (*De ratiociniis in ludo aleae*), Huygens provided three core propositions, gradually deriving the expected value:

                * **Proposition 1**: If you have an equal chance (50/50) of getting $a$ or $b$, then the value of this chance is $\frac{a+b}{2}$.
                    * *Intuitive understanding*: This is like buying insurance or making a trade; taking the average is the fairest balance point.
                * **Proposition 2**: If you have $p$ chances to get $a$, and $q$ chances to get $b$ (assuming all chances are equally probable).
                    Huygens proved, by constructing a complex equivalent game with equal stakes, that the value of this chance must be:

                    $$ \text{Value} = \frac{p \cdot a + q \cdot b}{p + q} $$
                """)

            with st.container():
                st.markdown(r"""
                #### 3. He Turned 'Chance' into an 'Asset'
                This is Huygens' greatest contribution. Pascal and Fermat were merely solving a specific dispute of "how to divide these 100 coins."

                But in Huygens' hands, he turned the "probability of winning money" into a calculable **numerical asset**.

                * **Pascal / Fermat**: Discussed "how to divide it when it ends."
                * **Huygens**: Discussed "how much this chance is worth now, before it starts or while it's ongoing."

                He officially gave a name to this "how much it is worth" amount, calling it *Expectatio* in Latin (which is our modern **Expectation / Expected Value**).
                """)

            st.success(r"""
            ### 🎯 Summary: What exactly did Huygens do?

            * **The Paris Catalyst & Beyond (1657)**: After visiting Paris and uncovering Pascal and Fermat's principles regarding the "Problem of Points," Huygens didn't just copy their homework. He **extended** the concept of expectation, creating universal rules to calculate odds in much more complicated situations—such as scaling the math up to handle games with three or more players.
            * **A Physicist's Intuition**: Don't forget, Huygens was a master physicist (inventor of the pendulum clock). He introduced the physics concept of the **"center of gravity"** into probability. The expected value is the mathematical fulcrum. If the left side is the probability and payout of winning, and the right side is losing, the expected value is the exact point that keeps the scale perfectly balanced.
            * **Laying the True Foundation**: He published his treatise *De ratiociniis in ludo aleæ* (On Reasoning in Games of Chance). This was the **first successful attempt in history at laying down the foundations of probability theory**. For the next half-century, this was the definitive textbook that taught the world how to calculate the unknown.
            """)
    with tab4:
        st.header("📈 Act IV: The Bell Curve, Complex Bridges & Inverse Reality")
        st.markdown(
            "Entering the **18th and early 19th centuries**, probability exploded. It evolved from a gambler's counting trick into the absolute language of physics, astronomy, and philosophy.")

        st.divider()

        # ==========================================
        # 创建子标签页 (Sub-tabs) 按时间线折叠内容
        # ==========================================
        subtab1, subtab2, subtab3, subtab4 = st.tabs([
            "🌉 1. De Moivre & Euler",
            "⚖️ 2. Bernoulli & LLN",
            "🔍 3. Bayes & Laplace",
            "🔭 4. Gauss & Error"
        ])

        # ------------------------------------------
        # 1. De Moivre & The Euler Connection
        # ------------------------------------------
        with subtab1:
            st.subheader("🌉 1. The Master Architect: Abraham de Moivre")
            st.markdown("""
            Before we measure the chaos of the stars or the reliability of a system, we must talk about the man who gave probability its modern engine. **Abraham de Moivre**, a French Protestant refugee in London coffeehouses, didn't just play with dice—he transformed probability from a gambler's intuition into a rigorous branch of mathematics.
            """)

            st.markdown("### 🎲 Part I: The Grammar of Probability")

            col_p1, col_p2, col_p3 = st.columns(3)

            with col_p1:
                st.info(r"""
                #### 📖 The Rulebook (1718)
                **The Problem:** Gamblers relied on raw intuition for complex sequences or conflicting outcomes, but lacked universal mathematical laws. 

                **The Fix:** In *The Doctrine of Chances*, De Moivre didn't use Venn diagrams ($\cup, \cap$) because Set Theory didn't exist yet. Instead, he used pure verbal logic to build the grammar we still use today. He rigorously defined two foundational concepts:
                * **Independent Events:** He invented the **Multiplication Rule** ($P(A \text{ and } B) = P(A) \times P(B)$) for events that don't influence each other.
                * **Mutually Exclusive Events:** He formalized the **Addition Rule** ($P(A \text{ or } B) = P(A) + P(B)$) for "incompatible" outcomes that can never happen simultaneously.
                """)

            with col_p2:
                st.warning(r"""
                #### 🧮 Taming Infinity (1730)
                **The Problem:** The Binomial formula requires calculating $\binom{n}{k} = \frac{n!}{k!(n-k)!}$. If you flip a coin 1000 times, $1000!$ is a number with **2,568 digits**. It was physically uncomputable.

                **The Fix:** De Moivre discovered the magic constant $\sqrt{2\pi}$ and helped create **Stirling's Approximation**: $n! \approx \sqrt{2\pi n} (n/e)^n$. He turned an infinite wall of multiplication into a simple exponential shortcut.
                """)

            with col_p3:
                st.success(r"""
                #### 🌊 The Bell Curve (1733)
                **The Problem:** Even with shortcuts, calculating the exact probability of getting between 4900 and 5100 heads in 10,000 flips required adding 200 massive fractions together.

                **The Fix:** De Moivre proved a miracle. As $n \to \infty$, the jagged, discrete staircase of the Binomial distribution perfectly smooths out into the continuous curve $y = c \cdot e^{-x^2}$. He invented the **Normal Distribution** as the ultimate limit of coin flips.
                """)

            st.divider()

            st.markdown("### 📐 Part II: The Complex Bridge to Euler")
            st.markdown("""
            Beyond probability, De Moivre built the mathematical skeleton that allowed future geniuses to connect geometry with algebra.
            """)

            with st.expander("🛠️ Deep Dive: Proving De Moivre & Deriving Euler", expanded=False):
                tab_induction, tab_euler = st.tabs(["1️⃣ The Domino Proof (De Moivre)", "2️⃣ The Limit Engine (Euler)"])

                with tab_induction:
                    st.markdown("### Proving De Moivre's Theorem")
                    st.write("Let's watch the math unfold step-by-step using **Mathematical Induction**.")

                    st.info("#### 🔍 Phase 1: Seeing the Pattern")

                    st.markdown(r"""
                    **Step 1: The Base Case ($n=1$)**
                    $$
                    (\cos x + i \sin x)^1 = \cos x + i \sin x
                    $$
                    *(Trivially true. The first domino falls.)*

                    **Step 2: The Double Angle ($n=2$)**
                    Square the complex number algebraically:
                    $$
                    \begin{aligned}
                    (\cos x + i \sin x)^2 &= (\cos^2 x - \sin^2 x) + i(2 \sin x \cos x) \\
                    &= \cos(2x) + i \sin(2x)
                    \end{aligned}
                    $$
                    *(Magic! The power of 2 slipped inside the angle.)*

                    **Step 3: The Chain Reaction ($n=3$)**
                    Multiply the $n=2$ result by one more term:
                    $$
                    \begin{aligned}
                    (\cos x + i \sin x)^3 &= [\cos(2x) + i \sin(2x)] \cdot [\cos x + i \sin x] \\
                    &= [\cos(2x)\cos x - \sin(2x)\sin x] + i [\sin(2x)\cos x + \cos(2x)\sin x] \\
                    &= \cos(3x) + i \sin(3x)
                    \end{aligned}
                    $$
                    """)

                    st.success("#### 🚀 Phase 2: The Infinite Dominoes (Induction)")

                    st.markdown(r"""
                    **1. The Assumption ($n=k$)**
                    Assume the dominoes fall all the way to some arbitrary integer $k$:
                    $$
                    (\cos x + i \sin x)^k = \cos(kx) + i \sin(kx)
                    $$

                    **2. The Inductive Step ($n=k+1$)**
                    Multiply our assumption by one more term and group them:
                    $$
                    \begin{aligned}
                    (\cos x + i \sin x)^{k+1} &= [\cos(kx) + i \sin(kx)] \cdot [\cos x + i \sin x] \\
                    &= [\cos(kx)\cos x - \sin(kx)\sin x] + i [\sin(kx)\cos x + \cos(kx)\sin x] \\
                    &= \cos(kx + x) + i \sin(kx + x) \\
                    &= \cos((k+1)x) + i \sin((k+1)x)
                    \end{aligned}
                    $$
                    **Q.E.D.** By proving that step $k$ perfectly creates step $k+1$, we have locked the universe into this rule forever.
                    """)

                with tab_euler:
                    st.markdown("### The Bridge to Euler's Formula")
                    st.write(
                        "How did Euler use De Moivre's rotating angles to create $e^{ix} = \cos x + i \sin x$? We will derive it using the **limit definition of $e$**.")

                    st.warning("#### ⚙️ Setting up the Engine")
                    st.markdown(r"""
                    We know from calculus that $e$ is defined as a limit to infinity:
                    $$
                    e^z = \lim_{n \to \infty} \left(1 + \frac{z}{n}\right)^n
                    $$
                    Let's plug in an imaginary number, $z = ix$:
                    $$
                    e^{ix} = \lim_{n \to \infty} \left(1 + \frac{ix}{n}\right)^n
                    $$
                    """)

                    st.info("#### 📐 Converting to Polar Form")
                    st.markdown(r"""
                    For the complex number inside the bracket: $1 + i\frac{x}{n}$. 
                    * **Modulus:** $R = \sqrt{1^2 + (x/n)^2} \to 1$ as $n \to \infty$.
                    * **Argument:** $\theta = \arctan(x/n) \approx \frac{x}{n}$ for very small values.

                    So, our complex number becomes:
                    $$
                    1 \cdot \left(\cos\left(\frac{x}{n}\right) + i \sin\left(\frac{x}{n}\right)\right)
                    $$
                    """)

                    st.success("#### 🌉 De Moivre's Final Assist")
                    st.markdown(r"""
                    Substitute this polar form back into our limit equation, and apply **De Moivre's Theorem**:
                    $$
                    \begin{aligned}
                    e^{ix} &= \lim_{n \to \infty} \left[ \cos\left(\frac{x}{n}\right) + i \sin\left(\frac{x}{n}\right) \right]^n \\
                    &= \lim_{n \to \infty} \left[ \cos\left(n \cdot \frac{x}{n}\right) + i \sin\left(n \cdot \frac{x}{n}\right) \right] \\
                    &= \cos x + i \sin x
                    \end{aligned}
                    $$
                    **The Impact:** Euler used De Moivre's engine of rotating complex numbers to drive the concept of limits to infinity. **This is the true root of the math.**
                    """)

        # ------------------------------------------
        # 2. Bernoulli & The Law of Large Numbers
        # ------------------------------------------
        with subtab2:
            import numpy as np
            import pandas as pd
            import streamlit as st

            st.subheader("⚖️ 2. The Anchor of Reality: Jacob Bernoulli (1713)")
            st.markdown("""
            Before we can talk about errors or curves, we must answer a terrifying philosophical question: **How do we know that rolling a die 1,000,000 times will actually average out to 3.5?** In his masterpiece *Ars Conjectandi* (The Art of Conjecturing), **Jacob Bernoulli** spent 20 years proving mathematically that randomness isn't entirely chaotic—it has "gravity."
            """)

            st.info(r"""
            #### ⚓ The Law of Large Numbers (LLN)
            Bernoulli proved that as the number of trials ($n$) approaches infinity, the observed empirical frequency will absolutely converge to the true theoretical probability. 

            $$\lim_{n \to \infty} P\left( \left| \frac{X}{n} - p \right| < \epsilon \right) = 1$$

            **Decoding the Formula (Seeing the Math):**
            * **$n$**: The number of trials (e.g., how many times you flip the coin).
            * **$\frac{X}{n}$**: The **Empirical Reality** (The actual percentage of Heads you got in real life).
            * **$p$**: The **Theoretical Truth** (The perfect $0.5$ probability).
            * **$\epsilon$ (Epsilon)**: A ridiculously tiny margin of error.
            * **$\lim_{n \to \infty}$ & $= 1$**: As trials go to infinity, the probability of reality matching theory becomes exactly $1$ ($100\%$).

            *Translation:* "No matter how chaotic the short-term is, if you flip a coin enough times, it is a $100\%$ mathematical certainty that your real-world result will perfectly lock onto the theoretical truth."
            """)

            st.markdown(
                "**The Impact:** He gave humanity confidence. He proved that we don't need to know the mind of God to predict the future; we just need a large enough sample size. This is the bedrock of modern statistics and the entire insurance industry.")

            # 动态可视化：大数定律模拟器
            st.markdown("### 🎲 Start Seeing LLN: The Chaos Simulator")
            st.write(
                "Drag the slider to increase the number of coin flips. Watch how the 'Empirical Reality' violently swings at first, but is eventually pulled toward the 'Theoretical Truth' by mathematical gravity.")

            col_sim1, col_sim2 = st.columns([2, 1])
            with col_sim1:
                n_flips = st.slider("Total Coin Flips ($n$)", min_value=10, max_value=5000, value=100, step=50)
            with col_sim2:
                st.write("")  # 占位对齐
                st.write("")
                run_sim = st.button("🔄 Toss the Coins!")

            if run_sim or 'lln_data' not in st.session_state:
                flips = np.random.choice([0, 1], size=5000)
                running_avg = np.cumsum(flips) / np.arange(1, 5001)
                st.session_state['lln_data'] = running_avg

            current_data = st.session_state['lln_data'][:n_flips]

            chart_data = pd.DataFrame({
                'Empirical Reality (Running Average)': current_data,
                'Theoretical Truth (p=0.5)': 0.5
            })

            st.line_chart(chart_data, color=["#FF4B4B", "#000000"])

            st.caption(
                "Notice the extreme volatility on the left (Small $n$). As you move right, the red line gets mathematically 'trapped' by the black anchor line.")

            # ------------------------------------------
            # 3. The Inverse Revolution (Bayes & Laplace)
            # ------------------------------------------
            import streamlit as st

            # ------------------------------------------
            # 3. The Inverse Revolution (Bayes & Laplace)
            # ------------------------------------------
            import streamlit as st

            # ------------------------------------------
            # 3. The Inverse Revolution (Bayes & Laplace)
            # ------------------------------------------
            with subtab3:
                st.subheader("🔍 3. The Inverse Revolution (Bayes & Laplace)")
                st.markdown("""
                Until the late 18th century, probability was strictly **forward-looking** (Deductive): predicting the data given a known underlying truth.

                But an English minister named **Thomas Bayes (1763)** and the French mathematical giant **Pierre-Simon Laplace (1774)** flipped the universe upside down. They asked the **inverse** question (Inductive): *"Given the data we just observed, what is the probability that our hypothesis is the truth?"*
                """)

                col_b1, col_b2 = st.columns([1, 1.5])
                with col_b1:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")
                    st.caption("*The mathematical engine of Artificial Intelligence.*")

                    st.info("""
                    **The Proof:**
                    By the definition of conditional probability, the probability of both A and B occurring simultaneously is:

                    $P(A \cap B) = P(A|B)P(B)$

                    It can also be written symmetrically as:

                    $P(A \cap B) = P(B|A)P(A)$

                    Equating the two gives:

                    $P(A|B)P(B) = P(B|A)P(A)$

                    Dividing both sides by $P(B)$ yields Bayes' Theorem.
                    """)

                with col_b2:
                    st.success("""
                    #### 🧠 What Did Laplace Actually Do?
                    While Thomas Bayes discovered the initial concept, his work was narrowly focused and published posthumously. **Laplace is the one who built the engine.**

                    1. **The Generalization:** Laplace independently discovered the theorem and formalized it into the rigorous mathematical equation we use today.
                    2. **The Law of Total Probability:** He introduced the expansion of the denominator $P(B)$ into $P(B|A)P(A) + P(B|A')P(A')$, making the formula universally applicable.
                    3. **The Application:** He moved probability out of gambling halls and applied it to the physical universe, establishing the foundation of modern statistical inference.
                    """)

                    # --- Laplace's Saturn Masterpiece ---
                st.markdown("<br>", unsafe_allow_html=True)
                with st.expander("🪐 THE ULTIMATE BAYESIAN FLEX: How Laplace Weighed Saturn", expanded=True):
                    st.markdown("""
                        In the late 18th century, astronomy faced a crisis known as the **"Great Inequality."** Jupiter appeared to be accelerating, while Saturn was slowing down. Newton's laws of gravity dictated that the planets were pulling on each other, but to predict their future orbits, Laplace needed to know their exact masses. **But how do you weigh a gas giant 1.2 billion kilometers away?**

                        Laplace turned the entire solar system into a massive Bayesian inference engine, utilizing data spanning from ancient Babylonian eclipses in 240 BC to modern Parisian telescopes.

                        #### 1. Defining the Variables
                        * **The Hypothesis ($A$):** The mass of Saturn is a specific continuous value, $m$.
                        * **The Evidence ($B$):** Decades of imperfect, error-prone telescope observations recording Saturn's orbital coordinates.

                        #### 2. The Engine at Work: Modeling the Errors
                        Instead of looking for one "absolute" mass, Laplace calculated a **probability distribution** of all possible masses. Here is how he mapped physical reality to the formula:

                        * **The Prior $P(A)$:** He started with a uniform, uninformative prior, assuming all mathematically reasonable planetary masses were initially equally likely.
                        * **The Likelihood $P(B|A)$:** *This was the revolutionary modeling step.* Laplace knew telescopes and human eyes were flawed. He pioneered the concept of an **error curve** (an early version of the Normal/Gaussian Distribution). He mathematically simulated exactly where Saturn *should* be if its mass was $m$. He then calculated the probability of astronomers observing the actual, flawed data $B$ under this assumption. The further an observation was from his predicted physical model, the exponentially lower the likelihood.
                        * **The Evidence $P(B)$:** To find the total probability of observing this specific set of data, he used advanced calculus to integrate the weighted likelihoods across the entire continuous spectrum of possible masses.

                        #### 3. The Posterior $P(A|B)$ & The Famous Bet
                        The math updated his belief. By multiplying the likelihoods of thousands of data points, the posterior probability curve narrowed into a massive, razor-sharp spike at a specific mathematical value. 

                        In 1815, Laplace published his finding: Saturn's mass was exactly $\\frac{1}{3512}$ of the Sun's mass. 

                        Because he had a complete posterior probability distribution, he didn't just provide a single number; he used the area under his curve to calculate a strict confidence interval. He famously wrote:
                        > *"I bet 11,000 to 1 that the error of this result is not even one-hundredth of its value."*

                        #### 🚀 The Modern Verdict
                        Almost **170 years later**, humanity launched the *Voyager* spacecraft. By analyzing the Doppler shift in radio signals as Voyager flew past Saturn, NASA measured the gravitational pull directly and calculated the planet's true mass. 

                        Laplace's Bayesian mathematical model from 1815 was off by exactly **0.63%**. He would have won his bet.
                        """)

                # --- Interactive Calculator ---
                st.markdown("---")
                st.markdown("### 🪙 Interactive Tracker: The Rigged Coin Experiment")
                st.markdown(
                    "Let's scale down from planets to a rigged coin. You suspect a coin might be double-headed (Hypothesis $A$). Watch how Laplace's expanded formula forces your belief to update as you observe more heads in a row.")

                col_calc1, col_calc2 = st.columns([1, 1.5])

                with col_calc1:
                    st.write("**Set up your experiment:**")
                    prior_percent = st.slider(
                        "Prior P(A): Initial suspicion it's rigged (%)",
                        min_value=0.01, max_value=50.0, value=1.0, step=0.01
                    )
                    flips = st.slider(
                        "Evidence: Consecutive Heads observed (n)",
                        min_value=1, max_value=20, value=5, step=1
                    )

                with col_calc2:
                    # Dynamic Math Calculations
                    p_a = prior_percent / 100.0
                    p_not_a = 1.0 - p_a

                    # P(B|A) is getting n heads from a rigged double-headed coin
                    p_b_given_a = 1.0
                    # P(B|A') is getting n heads from a fair coin
                    p_b_given_not_a = 0.5 ** flips

                    p_b = (p_b_given_a * p_a) + (p_b_given_not_a * p_not_a)
                    posterior = (p_b_given_a * p_a) / p_b

                    st.write("**Live Formula Calculation:**")

                    st.latex(fr"P(B|A) = 1^{{{flips}}} = 1 \quad \text{{(Rigged likelihood)}}")
                    st.latex(fr"P(B|A') = 0.5^{{{flips}}} = {p_b_given_not_a:.6f} \quad \text{{(Fair likelihood)}}")

                    # Expanding the denominator
                    st.latex(fr"P(B) = (1 \cdot {p_a:.4f}) + ({p_b_given_not_a:.6f} \cdot {p_not_a:.4f}) = {p_b:.6f}")

                    # Bayes Theorem
                    st.latex(fr"P(A|B) = \frac{{1 \cdot {p_a:.4f}}}{{{p_b:.6f}}}")

                    st.markdown(f"### Resulting Posterior: **{posterior * 100:.2f}%**")
                    st.caption(
                        f"*Observation: After {flips} heads, the math forces your suspicion to shift from {prior_percent:.2f}% to {posterior * 100:.2f}%.*")
        # ------------------------------------------
        # 4. Gauss, Ceres & The Ruler of Error
        # ------------------------------------------
        # ------------------------------------------
        # 4. Gauss, Ceres & The Ruler of Error
        # ------------------------------------------
        with subtab4:
            st.subheader("🔭 4. The Shape of Chaos & The Ruler of Error")
            st.markdown("""
            By the 19th century, probability shifted from gambling to astronomy. In 1801, the dwarf planet **Ceres** was discovered, but astronomers quickly lost it behind the sun. How do you find the *true* orbit hidden in the chaotic data?
            """)

            # 直接展示原本 expander 里的内容
            st.markdown("### 🏔️ The Birth of the Normal Distribution (Gauss Distribution)")

            st.info(r"""
            #### 🌌 1. The Anatomy of a Mistake (What did they actually see?)
            When 19th-century astronomers tried to track the missing planet Ceres, they didn't see a mathematical "Bell Curve." They saw a messy, chaotic cloud of dots scattered around where the planet should be. 

            **Gauss asked a simple question: Why is it a cloud?**
            Because a single "bad measurement" isn't just one mistake. It is a microscopic war of tiny forces:
            * A gust of wind pushes the telescope left ($-1$).
            * The candlelight heat expands the glass right ($+1$).
            * The astronomer's eye twitches left ($-1$).

            **The Law of Canceling Out:**
            Imagine combining 100 of these tiny random forces for a single observation.
            * **The Extreme Edges (Very Rare):** For a dot to land extremely far to the right ($+100$), *every single* tiny force (wind, heat, eye) must accidentally push right at the *exact same millisecond*. The odds of this perfect storm are practically zero.
            * **The Massive Center (Very Common):** What happens most of the time? The wind pushes left, but the heat pushes right. **They cancel each other out.** There are millions of ways for random forces to mix and cancel out to $0$.

            **The Revelation:** Gauss realized that if you stack all these scattered dots together, the center will pile up into a massive mountain (because canceling is easy), and the edges will stay completely flat (because extreme bad luck is rare). 

            He didn't invent the shape; he realized that **Nature's chaotic forces naturally stack themselves into a Bell Curve.**
            """)

            st.warning(r"""
                    #### ⚖️ 2. The Solution: Squaring the Error
                    To find the *true* center of this chaotic cloud, Gauss needed a way to measure the total "spread." 
                    If he just added the raw errors together, a mistake of $+2$ degrees and $-2$ degrees would cancel out to $0$ (which implies perfect accuracy—a complete lie).

                    **Translating the Math:**
                    Gauss took every single scattered observation ($x$) and measured its distance from the true center point ($\mu$, pronounced "mu"). This gave him the raw error: $(x - \mu)$.

                    Then, he **squared** every distance: $(x - \mu)^2$. 
                    But wait... why the square? Why not just use **Absolute Value** $|x - \mu|$ to remove the negative signs?

                    1. **Positivity:** Both squaring and absolute value turn negative errors into positive numbers, stopping the $+2$ and $-2$ from secretly canceling each other out.

                    2. **The Penalty (The Strict Judge):** * **Absolute Value** is a lenient judge. An error of $4$ is just a penalty of $4$. It treats one massive mistake the exact same as four tiny $1$-degree mistakes.
                       * **Squaring** is a strict judge. A small error of $1$ is just $1^2 = 1$. But a massive outlier of $4$ gets brutally punished as $4^2 = 16$. This forces the mathematical center to respect and adjust for extreme mistakes.

                    3. **The Calculus Secret (V vs. U):** 
                       An absolute value graph forms a sharp **V-shape**. In calculus, you cannot take the derivative of a sharp corner! A squared graph forms a perfectly smooth **U-shape** (a parabola), allowing Gauss to use calculus to easily find the exact mathematical bottom (the minimum error).
                    """)

            st.divider()

            st.success(r"""
            #### 📐 3. The Historical Paradox: Standard Deviation vs. Variance
            Wait a minute. To calculate Standard Deviation, you mathematically *must* calculate the squared average first. So why was "Standard Deviation" named in 1894, but "Variance" wasn't named until 1918? 

            It's a story of three different geniuses looking at the exact same math:

            * **1. The Unnamed Engine (Gauss, 1809):** Gauss invented the math (Sum of Squares) to find planets. To him, it was just an algebra trick to do calculus. He didn't bother giving it a fancy statistical name.

            * **2. Standard Deviation ($\sigma$) is born (Karl Pearson, 1894):** Decades later, biologists used Gauss's math to measure human traits. But they hit a wall: If you measure height in *centimeters*, squaring the error gives you *square centimeters* (an area!). 
              To fix the unit, Karl Pearson took the square root ($\sqrt{\text{squares}}$) to bring the measurement back to normal centimeters. He officially named this final, readable physical ruler **Standard Deviation**.



            * **3. Variance ($\sigma^2$) gets its name (R.A. Fisher, 1918):**
              The founder of modern statistics, Fisher, realized that while Standard Deviation is easy to read, the **square itself** has a magical, hidden property: **The Pythagorean Theorem**.

              Imagine two independent errors: Wind ($Error_A$) and Atmospheric shimmer ($Error_B$). Because they are independent, they act at 90-degree angles to each other. To find the total error, you **cannot** just add the lengths ($A + B \neq C$). You MUST add their squares ($A^2 + B^2 = C^2$).

              Fisher realized the square is the fundamental "additive" building block of nature. He finally gave it a name: **Variance**.
              * **Variance ($A^2, B^2$):** The Lego bricks. They can be added together.
              * **Standard Deviation ($A, B$):** The final ruler. It cannot be added together.
            """)
    import streamlit as st

    with tab5:
        st.header("🏰 Act V: The Axiomatic Revolution")
        st.subheader("Protagonist: Andrey Kolmogorov (1933)")

        st.markdown("""
        Before 1933, probability was considered a "dirty" branch of mathematics. It was tied to physical coins, dice, and gambling intuitions. When mathematicians tried to calculate probabilities involving *infinity* (like picking a random point on a continuous line), the old rules broke down into paradoxes. 

        Enter **Andrey Kolmogorov**, a 30-year-old Russian mathematician. He published *Foundations of the Theory of Probability* and executed one of the greatest unifications in scientific history. **He stripped away the coins and dice, and translated probability entirely into the rigorous language of Set Theory and Measure Theory.**
        """)

        st.markdown("---")
        st.markdown("### 📖 The Translation: Probability as Geometry")
        st.markdown(
            "Kolmogorov realized that calculating probability is exactly the same as measuring the **area** or **volume** of a shape. He created a dictionary to translate real-world chaos into pure mathematics:")

        # Use columns to show the "Dictionary"
        col_dict1, col_dict2 = st.columns(2)
        with col_dict1:
            st.info("""
            **Real World (The Chaos)**
            * "Everything that could possibly happen"
            * "A specific scenario we care about"
            * "Event A OR Event B happens"
            * "Event A AND Event B happen"
            * "Impossible event"
            """)
        with col_dict2:
            st.success("""
            **Kolmogorov's Math (Set Theory)**
            * $\\Omega$ (Sample Space: The universal set)
            * $A \subseteq \\Omega$ (An Event is just a subset)
            * $A \cup B$ (Union of sets)
            * $A \cap B$ (Intersection of sets)
            * $\\emptyset$ (The Empty Set)
            """)

        st.markdown("---")
        st.markdown("### 📐 The Three Axioms of Probability")
        st.markdown(
            "Once probability was defined as subsets, Kolmogorov established three unbreakable rules. If a function $P$ satisfies these three rules, it is a valid probability. No physical experiments required.")

        col_ax1, col_ax2, col_ax3 = st.columns(3)

        with col_ax1:
            st.markdown("#### I. Non-negativity")
            st.latex(r"P(A) \ge 0")
            st.caption(
                "You cannot have a negative probability, just like a shape cannot have a negative physical area.")

        with col_ax2:
            st.markdown("#### II. Normalization")
            st.latex(r"P(\Omega) = 1")
            st.caption("The probability of 'something' happening is 100%. The total area of the universe is 1.")

        with col_ax3:
            st.markdown("#### III. Additivity")
            st.latex(r"\text{If } A \cap B = \emptyset,")
            st.latex(r"P(A \cup B) = P(A) + P(B)")
            st.caption(
                "If two subsets don't overlap (mutually exclusive), their combined probability is simply the sum of their individual areas.")

        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("🌌 WHY WAS THIS A BIG DEAL? (The Measure Theory Magic)", expanded=True):
            st.markdown("""
            **It solved the problem of Infinity.**

            Imagine throwing a dart at a continuous number line between 0 and 1. What is the probability of hitting *exactly* $0.5000000...$? 

            Under the old rules, there are infinitely many points. The probability is $\\frac{1}{\\infty} = 0$. Every single point has a probability of 0. But if you add them all up, the dart *must* hit the line, so the total probability is 1. **How can a bunch of zeroes add up to 1?**

            **Kolmogorov's Measure Theory fixed this.** He said we don't count *points*; we measure *length*. 
            * The probability of hitting a single point is indeed 0 (a point has no length). 
            * But the probability of hitting between $0.4$ and $0.6$ is $0.2$, because the *length* of that subset is $0.2$.

            By turning probability into the calculation of "measure" (length, area, volume), Kolmogorov allowed probability to inherit all the rigorous tools of Calculus and Real Analysis. Probability was finally recognized as an orthodox, foundational branch of modern mathematics.
            """)


# ==========================================
# Chapter 2: Probability Distributions (Placeholder)
# ==========================================
elif chapter == "📐 Chapter 2: Probability Distributions":

    st.title("📐 The Shape of Chaos (Distributions)")
    st.markdown(
        "When events become numbers, and the discrete becomes continuous. This is the territory of the Normal, Poisson, Binomial, and Cauchy distributions.")
    st.divider()

    st.info(
        "🚧 **Director's Note:** The content for distributions (and those interactive charts you actually need) will unfold here...")