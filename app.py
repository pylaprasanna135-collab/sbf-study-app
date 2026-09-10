import streamlit as st
import random

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SBF | Study Begins for Future",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "started" not in st.session_state:
    st.session_state.started = False

if "points" not in st.session_state:
    st.session_state.points = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "completed" not in st.session_state:
    st.session_state.completed = 0

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #f7f9fc 0%, #eef3ff 100%);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827 0%, #1e293b 100%);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.sidebar-title {
    font-size: 26px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.sidebar-subtitle {
    text-align: center;
    font-size: 13px;
    opacity: 0.75;
    margin-bottom: 30px;
}

/* Header */

.hero {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    padding: 35px;
    border-radius: 24px;
    color: white;
    box-shadow: 0 15px 40px rgba(79,70,229,0.20);
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin: 0;
    font-weight: 800;
}

.hero p {
    font-size: 17px;
    margin-top: 10px;
    opacity: 0.92;
}

/* Cards */

.card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.07);
    border: 1px solid #e5e7eb;
    min-height: 145px;
}

.card-icon {
    font-size: 32px;
}

.card-title {
    font-size: 17px;
    font-weight: 700;
    margin-top: 10px;
    color: #111827;
}

.card-text {
    color: #64748b;
    font-size: 14px;
    margin-top: 6px;
}

/* Section */

.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #111827;
    margin-top: 28px;
    margin-bottom: 18px;
}

/* Feature */

.feature {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border-left: 5px solid #6366f1;
    box-shadow: 0 6px 20px rgba(15,23,42,0.06);
    margin-bottom: 15px;
}

.feature h3 {
    margin: 0;
    color: #111827;
}

.feature p {
    color: #64748b;
}

/* Quote */

.quote {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #9a3412;
}

/* Buttons */

.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    border: none;
    padding: 10px 20px;
}

/* Progress */

.progress-box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.07);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📚 SBF</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Study Begins for Future</div>',
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "🏠 Dashboard",
            "📖 Study",
            "🧠 Quiz",
            "🎯 Goals",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.markdown("### ⭐ Your Progress")

    st.metric(
        "Points",
        st.session_state.points
    )

    st.metric(
        "Completed",
        st.session_state.completed
    )

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Welcome to SBF 👋</h1>
        <p>
            Study smarter. Build skills. Create your future.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.started:

        st.markdown("""
        <div class="card">
            <div class="card-icon">🚀</div>
            <div class="card-title">Ready to begin?</div>
            <div class="card-text">
                Start your learning journey with SBF.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Learning", use_container_width=True):
            st.session_state.started = True
            st.session_state.points += 10
            st.rerun()

    else:

        st.success("Your learning journey has started! Keep going 💪")

    st.markdown(
        '<div class="section-title">✨ What You Can Do</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-icon">📖</div>
            <div class="card-title">Study</div>
            <div class="card-text">
                Learn important concepts in a simple way.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🧠</div>
            <div class="card-title">Practice</div>
            <div class="card-text">
                Test your knowledge with interactive quizzes.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-icon">🎯</div>
            <div class="card-title">Improve</div>
            <div class="card-text">
                Track your progress and reach your goals.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📊 Your Dashboard</div>',
        unsafe_allow_html=True
    )

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric(
            "⭐ Points",
            st.session_state.points
        )

    with p2:
        st.metric(
            "📝 Quiz Score",
            st.session_state.quiz_score
        )

    with p3:
        st.metric(
            "🏆 Completed",
            st.session_state.completed
        )

    st.markdown("""
    <div class="quote">
        💡 "Small progress every day leads to big results."
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# STUDY PAGE
# =========================================================

elif page == "📖 Study":

    st.markdown("""
    <div class="hero">
        <h1>📖 Study Zone</h1>
        <p>Learn something new today.</p>
    </div>
    """, unsafe_allow_html=True)

    subjects = {
        "🐍 Python": "Programming fundamentals, logic and problem solving.",
        "🌐 HTML": "Build the structure of modern web pages.",
        "🗄️ DBMS": "Learn databases, tables, keys and relationships.",
        "🤖 Artificial Intelligence": "Explore AI concepts and intelligent systems.",
        "📊 Aptitude": "Improve your mathematical and logical reasoning."
    }

    for subject, description in subjects.items():

        st.markdown(f"""
        <div class="feature">
            <h3>{subject}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            f"Start {subject}",
            key=subject,
            use_container_width=True
        ):
            st.session_state.points += 5
            st.session_state.completed += 1
            st.success(f"{subject} study session started! +5 points 🎉")

# =========================================================
# QUIZ PAGE
# =========================================================

elif page == "🧠 Quiz":

    st.markdown("""
    <div class="hero">
        <h1>🧠 Quick Quiz</h1>
        <p>Challenge yourself and improve your knowledge.</p>
    </div>
    """, unsafe_allow_html=True)

    questions = [
        {
            "q": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automatic Internet",
                "Advanced Information",
                "Applied Innovation"
            ],
            "answer": "Artificial Intelligence"
        },
        {
            "q": "Which language is widely used for AI?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "SQL"
            ],
            "answer": "Python"
        },
        {
            "q": "Which one is a database system?",
            "options": [
                "MySQL",
                "HTML",
                "Python",
                "CSS"
            ],
            "answer": "MySQL"
        },
        {
            "q": "What does HTML stand for?",
            "options": [
                "HyperText Markup Language",
                "HighText Machine Language",
                "Hyper Tool Multi Language",
                "Home Text Markup Language"
            ],
            "answer": "HyperText Markup Language"
        },
        {
            "q": "Which device is known as the brain of a computer?",
            "options": [
                "CPU",
                "Keyboard",
                "Monitor",
                "Mouse"
            ],
            "answer": "CPU"
        }
    ]

    if "quiz_question" not in st.session_state:
        st.session_state.quiz_question = random.choice(questions)

    question = st.session_state.quiz_question

    st.markdown(
        '<div class="section-title">Question</div>',
        unsafe_allow_html=True
    )

    st.info(question["q"])

    answer = st.radio(
        "Choose your answer:",
        question["options"]
    )

    if st.button("✅ Submit Answer", use_container_width=True):

        if answer == question["answer"]:

            st.success("🎉 Correct answer!")

            st.session_state.points += 10
            st.session_state.quiz_score += 10

        else:

            st.error(
                f"❌ Not quite. Correct answer: {question['answer']}"
            )

        st.session_state.quiz_question = random.choice(questions)

# =========================================================
# GOALS PAGE
# =========================================================

elif page == "🎯 Goals":

    st.markdown("""
    <div class="hero">
        <h1>🎯 Future Goals</h1>
        <p>Dream big. Learn daily. Build your future.</p>
    </div>
    """, unsafe_allow_html=True)

    goals = [
        ("💻", "Become a Skilled Developer"),
        ("🤖", "Build AI Projects"),
        ("🌐", "Improve Web Development"),
        ("🧠", "Strengthen Coding Logic"),
        ("📚", "Prepare for Competitive Exams"),
        ("🚀", "Build a Successful Career")
    ]

    for icon, goal in goals:

        st.markdown(f"""
        <div class="feature">
            <h3>{icon} {goal}</h3>
            <p>Keep learning and take one step forward every day.</p>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ABOUT PAGE
# =========================================================

elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero">
        <h1>ℹ️ About SBF</h1>
        <p>Study Begins for Future</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-icon">📚</div>
        <div class="card-title">Study Begins for Future</div>
        <div class="card-text">
            SBF is a student-focused learning platform designed
            to make studying simple, interactive and motivating.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🌟 Our Vision</div>',
        unsafe_allow_html=True
    )

    st.write(
        "To help students learn useful skills, practice regularly "
        "and confidently prepare for their future."
    )

    st.markdown("""
    <div class="quote">
        🚀 Learn Today • Build Tomorrow • Create Your Future
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    "<center>📚 SBF • Study Begins for Future • Keep Learning 🚀</center>",
    unsafe_allow_html=True
)
