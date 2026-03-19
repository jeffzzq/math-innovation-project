import streamlit as st

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(page_title="Chapter 1: The Architecture of Logic", page_icon="🧩", layout="wide")

st.title("🧩 Chapter 1: The Architecture of Logic")
st.markdown("""
> *"No one shall expel us from the paradise that Cantor has created for us." — David Hilbert*
""")
st.divider()

# ==========================================
# 4 Tabs for a Complete, Rigorous Academic Narrative
# ==========================================
tab_trigger, tab_revolution, tab_crisis, tab_bridge = st.tabs([
    "🌌 1. The Forbidden Infinity & The Trigger",
    "⚔️ 2. The Cantor Revolution",
    "🔥 3. Paradoxes & The ZFC Rescue",
    "🌉 4. The Bridge to Probability"
])

# --- Tab 1: The Pre-Cantor World & The Fourier Trigger ---
with tab_trigger:
    st.header("The Forbidden Infinity")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("The Classical Dogma")
        st.markdown("""
        Before 1874, "Infinity" was the ultimate taboo in mathematics.

        * **Aristotle's Rule:** *"Infinitum actu non datur"* (Actual infinity does not exist).
        * **Carl Friedrich Gauss (1831):** The "Prince of Mathematics" strictly forbade it. He declared: *"I protest against the use of infinite magnitude as something completed... Infinity is merely a façon de parler (a figure of speech)."*

        For 2,000 years, mathematicians only accepted **Potential Infinity** (a process that never ends, like limits in Calculus). They completely rejected **Actual Infinity** (an infinite collection existing as a completed, single object).
        """)

    with col2:
        st.subheader("The Fourier Anomaly (Why Sets?)")
        st.markdown("""
        Georg Cantor didn't invent Set Theory just to play with philosophical logic. He was trying to solve a practical physics problem involving **Fourier Series** (the mathematics of waves).

        * **The Problem (The Wave Recipe):** It was known that any complex wave (like a soundwave) could be built by adding simple sine waves. The question was: Is there only *one unique recipe* for every wave?
        * **The Anomaly (The Glitches):** The recipe was unique for smooth waves. But what if the wave had "glitches" or broken points? Cantor discovered the recipe was still unique even if the wave had an *infinite* number of these glitches.
        * **The Crisis (The Black Box):** To mathematically prove this, he couldn't just say "there are infinite glitches." Before Cantor, "Infinity" was a blurry black box. He had no vocabulary to measure *how many* or *how dense* those infinite points were.
        * **The Invention (The Microscope):** He created the **"Set"** as a mathematical microscope. By gathering all these infinite broken points into a single "container" (a Set), he could strip away the generic "infinite" label and examine their internal structure. 

        **The Result:** He proved that some infinities are "thinner" (countable) and others are "thicker" (uncountable). 

        **Without this invention, we could never define 'Probability Density' later. We would be stuck counting discrete fingers and toes forever.**
        """)

# --- Tab 2: The Cantor Revolution (Visual Revamp) ---
with tab_revolution:
    st.header("🌌 Shattering the Illusion of Infinity")

    # 顶部人物高光
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/e7/Georg_Cantor2.jpg",
                 caption="Georg Cantor: The Prophet of Sets")
    with col_txt:
        st.subheader("The Man Who Saw Too Much")
        st.write("""
        In 1874, math changed forever. Cantor didn't just 'find' infinity; he built a hierarchy for it. 
        He was the first to treat infinity not as a never-ending process, but as a **completed object**.
        """)
        st.info(
            "💡 **Core Insight:** If you can pair every element of two sets without any leftovers, they are the SAME size.")

    st.divider()

    # 【排版重构：使用 Subtabs 代替 Columns】
    sub_tab_math, sub_tab_history = st.tabs(["📐 The Mathematics", "⚔️ The History (War of Titans)"])

    with sub_tab_math:
        st.subheader("I. The New Ruler: Bijection")
        st.markdown("""
        How do you measure something that never ends? You can't count it, but you can **pair it**.

        * **The Principle:** Two sets have the same size (**Cardinality**) if every element in Set A can be paired with exactly one partner in Set B, leaving no one behind.
        * **The Shock:** Using this, Cantor proved that the set of all integers $\{1, 2, 3, \dots\}$ is the *exact same size* as the set of all even numbers $\{2, 4, 6, \dots\}$. 
        """)
        st.latex(r"n \longleftrightarrow 2n")

        # 【新增】：希尔伯特旅馆彩蛋
        st.info("""
        🏨 **The Paradox of the Grand Hotel (David Hilbert)**

        How do you fit a new guest into a hotel that is already FULL? 
        In a hotel with $\\aleph_0$ rooms, you simply ask guest $n$ to move to room $n+1$. 

        * **The Insight:** In the infinite world, $\\aleph_0 + 1 = \\aleph_0$. 
        * **The Lesson:** An infinite set is defined by the fact that it can be put into a one-to-one correspondence with a proper subset of itself. This isn't a "bug" in math; it's the defining "feature" of infinity.
        """)

        st.markdown("""
        He named this base-level infinity **$\\aleph_0$ (Aleph-null)**—the first letter of the Hebrew alphabet—symbolizing the 'First Floor' of the infinite hotel.
        """)

        st.divider()
        st.subheader("II. The Diagonal Proof: The Uncountable")
        st.markdown("""
                If $\\aleph_0$ (integers) is the first floor of infinity, is there a second? Cantor used the **Diagonal Argument** to prove that Real Numbers (decimals) are a strictly 'larger' infinity.

                * **The Challenge:** Imagine you claim you have an infinite list that contains *every* possible decimal in the universe. You number them: 1st, 2nd, 3rd, and so on.
                * **Cantor's Trick:** Cantor looks at your list to build a *new* number. He looks at the **diagonal**: he takes the 1st digit of your 1st number and changes it. He takes the 2nd digit of your 2nd number and changes it. He does this forever. 
                * **The Trap:** He then asks: *"Is my new number on your list?"* The answer is NO. It cannot be your 1st number (the 1st digit is different). It cannot be your 2nd number (the 2nd digit is different). It escapes your infinite list completely!
                * **The Result:** Because Cantor can *always* build a missing number, your list can never hold all decimals. Real numbers **cannot be counted**. They are an uncountable, 'thicker' infinity.
                """)

        st.latex(r"2^{\aleph_0} > \aleph_0")

    with sub_tab_history:
        st.subheader("III. The War of the Titans")
        st.markdown("""
        Cantor's work wasn't just debated; it was treated as **heresy**. The backlash came from every corner of the intellectual world, driving him into deep isolation.

        * **The Mentor turned Nemesis:** **Leopold Kronecker** was the most brutal. He famously said, *"God made the integers; all else is the work of man."* He used his power as a journal editor to kill Cantor's career.
        * **The Tragic Toll:** Cantor spent his final days in a psychiatric clinic, feeling forgotten by the world he had revolutionized.
        """)

        st.divider()

        st.subheader("IV. The Clash of the Demigods")
        st.markdown(
            "But the true philosophical war over Cantor’s soul was fought between the two undisputed kings of the era:")

        # --- Dossier 1: The Attacker ---
        st.markdown("### The Attacker")

        # 【排版修改：创建左右列，比例 1:2.5】
        col_img1, col_txt1 = st.columns([1, 2.5])

        with col_img1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/a/a3/Henri_Poincar%C3%A9_in_1880s.jpg",
                     caption="Henri Poincaré: The Last Universalist")
        with col_txt1:
            st.warning("""
            #### 🦅 Henri Poincaré (The Intuitionist)
            He was the last human to master *every* branch of mathematics, practically inventing **Topology**. 

            **⚔️ HOW & WHY he opposed Cantor:**
            * **The Core Belief (Constructivism):** Poincaré believed mathematics must be grounded in human intuition. You can only claim a mathematical object exists if you can build it step-by-step, in a finite number of steps.
            * **The Attack on "Actual Infinity":** To Poincaré, infinity was merely "Potential"—a process of counting that never stops. Cantor's sin was treating infinity as an "Actual" completed object (like putting all infinite integers into a single bag called $\\aleph_0$). 
            * **The Verdict:** He saw Cantor's Set Theory—especially definitions that refer to themselves (which caused Russell's Paradox)—as meaningless wordplay. It wasn't math; it was a logical disease that alienated math from physical reality.

            *"Most of the ideas of Cantor's set theory are a disease from which one hopes that mathematics will one day be cured."*
            """)

        st.divider()

        # --- Dossier 2: The Defender ---
        st.markdown("### The Defender")

        # 【排版修改：创建左右列，比例 1:2.5】
        col_img2, col_txt2 = st.columns([1, 2.5])

        with col_img2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/7/79/Hilbert.jpg",
                     caption="David Hilbert: The Master Architect")
        with col_txt2:
            st.info("""
            #### 🏛️ David Hilbert (The Formalist)
            In the year 1900, Hilbert famously proposed **23 unsolved problems** that dictated the entire 20th century of mathematics.

            **🛡️ HOW & WHY he supported Cantor:**
            * **The Core Belief (Formalism):** Hilbert didn't care if you couldn't "physically construct" an infinite set. To him, mathematics is a game played with symbols. **If a set of logical rules is consistent (has no contradictions), then the mathematical objects within it perfectly EXIST.**
            * **The Defense of the "Skyscraper":** Hilbert recognized Set Theory as the ultimate "Atomic Theory." Geometry, Calculus, Probability—all of them could be translated into the universal language of Sets. To throw away Cantor's infinities meant demolishing the foundation of modern math.
            * **The Verdict:** He championed the **Axiomatic Method** (which later became ZFC). He believed human reason could conquer the infinite simply by laying down strict rules, defying the old belief that "infinity belongs only to God."

            *"No one shall expel us from the paradise that Cantor has created for us."*
            """)

        # 【全新插入区：不改动原文本，纯追加哥尔丹与希尔伯特的冲突】
        st.error("""
        🔥 **The Price of Formalism:** Hilbert's defense of this abstract, "non-constructive" logic did not come easily. When a young Hilbert first used this Cantor-style reasoning to prove a major theorem—using pure logic to prove something *must* exist without actually constructing it—the old guard was horrified. 

        Paul Gordan, the leading mathematician of the time, flat-out rejected Hilbert's paper with the legendary cry:
        > *"Das ist nicht Mathematik. Das ist Theologie!"* > *(This is not mathematics. This is theology!)*
        """)

        # --- The Ultimate Consequence ---
        st.markdown("### ⚡ The Fallout for Probability")
        st.markdown("""
        Hilbert won. Mathematics was industrialized. Because Set Theory survived this philosophical war, mathematicians in the 1930s finally had the pure, abstract "programming language" needed to build **Measure Theory**—the absolute foundation of modern Probability and AI.
        """)
# --- Tab 3: Paradoxes & The ZFC Rescue (The Core Logic) ---
with tab_crisis:
    st.header("The Third Mathematical Crisis")

    st.markdown("""
    For 30 years, mathematicians thought Cantor's **"Naive Set Theory"** was perfect. Its core rule was dangerously simple: *"If you can describe a collection of objects with words, it becomes a valid Set."* It felt like magic. But in 1901, a 29-year-old British philosopher named **Bertrand Russell** realized this "magic" was a ticking time bomb.
    """)

    st.divider()

    col3, col4 = st.columns([1, 1])
    with col3:
        st.subheader("💥 Russell's Paradox (1901)")
        st.markdown("""
        Russell wrote a letter to the great logician Gottlob Frege, asking a simple question that instantly destroyed Frege's life's work.

        **The Formal Paradox:**
        In Naive Set Theory, you are allowed to define a set $R$ of all sets that do not contain themselves:
        $$R = \{x \mid x \\notin x\}$$

        Now, Russell asked the fatal question: **Does $R$ contain itself? ($R \\in R$?)**
        $$R \\in R \\iff R \\notin R$$

        * If **Yes** ($R \\in R$), then it violates its own rule, so it **Cannot**.
        * If **No** ($R \\notin R$), then it qualifies for its own rule, so it **Must**.
        """)

        st.error("""
        ✂️ **The Barber Metaphor (To visualize the logic):**
        Imagine a town with a strict rule: *The Barber shaves all men, and ONLY those men, who do not shave themselves.*

        **Who shaves the Barber?**
        If he shaves himself, he breaks the rule. If he doesn't, he must go to the Barber (himself). Logic collapsed. Mathematics was suddenly built on a fatal contradiction.
        """)

    with col4:
        st.subheader("🛡️ The ZFC Rescue (Axiom of Separation)")
        st.markdown("""
        To save mathematics, Ernst Zermelo and Abraham Fraenkel rebuilt Set Theory into a high-security fortress: the **ZFC Axioms**. They solved the paradox by destroying the "God Mode" of set creation.

        * **The Flaw:** Previously, you could conjure a set out of thin air just by speaking a rule ($x \\notin x$). 
        * **The ZFC Fix (The Cookie Cutter Rule):** You can NO LONGER create a set from nothing. You must first start with a pre-existing, safe "dough" (a known Set $A$). Only then can you apply your rule to carve out a subset.

        **The New Mathematical Law:**
        $$R = \{x \\in A \\mid x \\notin x\}$$
        """)

        st.success("""
        ⚙️ **How the Formula Killed the Barber:**
        Let's ask the fatal question again in ZFC: **Is $R \\in R$?**

        1. If $R \\in R$, it must satisfy the condition $R \\notin R$. This is a contradiction, so we know for sure that **$R \\notin R$**.
        2. In the old theory, $R \\notin R$ meant it automatically gets added to the set $R$. 
        3. **BUT in ZFC**, to be in $R$, you must *also* be a resident of Town $A$ ($x \\in A$). 

        Therefore, the only logical conclusion without breaking math is:
        $$R \\notin A$$

        ZFC doesn't crash. It rigorously proves a cold, hard fact: **"This paradoxical Barber simply does not exist in Town $A$."** By forcing every rule inside the boundaries of an existing set, ZFC locked the paradox out forever.
        """)
    # --- Tab 4: The Bridge to Probability (Functions & Intervals) ---
    with tab_bridge:
        st.header("The Architecture of the Unknown")
        st.markdown("""
        Why must we study Sets before Probability? Because in 1933, Andrey Kolmogorov used Set Theory to permanently define the rules of chance.
        """)

        st.subheader("1. The Vocabulary of Probability")
        st.markdown("""
        Without Set Theory, probability is just gambling. With it, it becomes a rigorous science of space:
        * **The Universal Set ($\Omega$):** Becomes the **Sample Space** (Every possible future).
        * **A Subset ($A \subseteq \Omega$):** Becomes an **Event** (A specific future we care about).
        * **Intersection ($A \cap B$) & Union ($A \cup B$):** Become the mathematical engines for calculating the probability of multiple events happening simultaneously or alternatively.
        """)

        # 【新增】：维恩图的致敬彩蛋
        st.info("""
        💡 **Dossier Note: The UI of Logic**
        In 1880, an English logician named **John Venn** created the ultimate visual tool to save students from insanity. By drawing overlapping circles to map out logical universes, he invented the **Venn Diagram**. It remains the graphical engine that powers all our probability calculations today.
        """)

        st.divider()
        st.subheader("2. Redefining Functions (The Birth of Random Variables)")

        st.markdown("""
            For centuries, mathematics was trapped in the **"Age of Formulas."** To giants like Newton and Euler, a function had to be a neat algebraic equation, like $y = x^2 + 1$. Math was strictly about calculating numbers. 

            **The 1837 Rebellion:** Long before Set Theory was formally born, a German mathematician named **Dirichlet** realized that formulas were too restrictive. He declared that a function doesn't need an equation at all. It only needs a rule of correspondence: if you give me an input from a **Domain** (the source), I will point to a unique output in a **Range** (the destination). 
            """)

        st.markdown("""
            This exact mindset laid the groundwork for Cantor's Set Theory. Cantor took Dirichlet's concept and applied it to infinite sets, permanently changing a function from a "calculating machine" into a **Bridge connecting any two sets**—even if one set contains "concepts" and the other contains "numbers."
            """)

        st.info("""
            🎯 **The "Random Variable" is just a Translator**

            This software update to logic explains the most crucial tool in probability: the **Random Variable ($X$)**. Despite its confusing name, it is simply a **Mapping Function ($f: \Omega \\to \mathbb{R}$)** born from Dirichlet's logic.

            Think of a game of Darts:
            * **The Domain (Sample Space $\Omega$):** The chaotic, physical reality of where the dart lands (e.g., "Bullseye" or "Miss"). This is the *random* part.
            * **The Range (Real Numbers $\mathbb{R}$):** The points on the scoreboard (e.g., "50" or "0").
            * **The Random Variable ($X$):** This is simply the **Scoring Rule**. It translates the physical event ("Bullseye") into a strict mathematical number ("50").

            **Why is this a superpower?** Because Calculus cannot integrate words like "Heads", "Tails", or "Bullseyes". By translating chaotic reality into numbers, the Random Variable allows us to force the physical world into the mathematical laboratory.
            """)

        st.divider()

        st.subheader("3. Discrete Counting vs. Continuous Measure")
        st.markdown("""
        Set theory gives us the ultimate rule for handling distributions in Chapter 3:

        * **Countable Sets (Discrete):** Like rolling dice. We can calculate probability by summing the weights of individual elements (Probability Mass).
        * **Uncountable Sets (Continuous Intervals):** Because an interval like $[0, 1]$ contains a higher infinity ($2^{\aleph_0}$) of points, the probability of hitting one exact mathematical point is **strictly zero**. 
        """)

        # 【新增】：抹果酱与零的真相
        st.warning("""
        > **The Reality of the Zero:** In a continuous universe, the probability of any *exact* point is zero ($P(X=x) = 0$). Does this mean the event is impossible? No. It means mathematical "points" have no width, hence no weight. In reality, we never measure points; we measure **intervals** (e.g., measuring exactly 5.0 actually means an interval from 4.99 to 5.01). 
        >
        > **The Role of Density:** The height of a curve at a point $x$ is not its probability, but its **Density** (how thick the probability "mass" is packed). To find the actual probability, we must calculate the **Area** over a range.
        """)

        st.markdown("""
        **The Final Conclusion:** We cannot "count" continuous probability; we must "measure" it. This mandates the use of integrals, areas under curves, and the **Probability Density Function (PDF)**.
        """)