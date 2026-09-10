import streamlit as st
import random

# =========================================================
# SBF - STUDY BEGINS FOR FUTURE
# =========================================================

st.set_page_config(
    page_title="SBF | Study Begins for Future",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "points" not in st.session_state:
    st.session_state.points = 0

if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = []

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HERO */

.hero {
    padding: 40px;
    border-radius: 25px;
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

/* CARD */

.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

.card h3 {
    margin-bottom: 8px;
}

/* SECTION TITLE */

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 20px;
}

/* QUOTE */

.quote {
    background-color: #fff7ed;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🚀 SBF")

    st.caption("Study Begins for Future")

    st.divider()

    page = st.radio(
        "📌 Navigation",
        [
            "🏠 Home",
            "🎓 Explore Courses",
            "🧠 Take a Quiz",
            "🧭 Career Guidance",
            "📊 My Progress",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.subheader("⭐ Your Stats")

    st.write("🏆 Points:", st.session_state.points)
    st.write("📚 Completed:", len(st.session_state.completed_lessons))

# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero">
        <h1>🚀 Welcome to SBF</h1>
        <p>Study Begins for Future</p>
        <p>Learn Today. Build Your Future. 🌟</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
    🚀 Start Learning. Start Building Your Future!
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">
        <h3>🎓 Explore Courses</h3>
        <p>Learn useful skills step by step.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h3>🧠 Take a Quiz</h3>
        <p>Practice and test your knowledge.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">
        <h3>🧭 Career Guidance</h3>
        <p>Discover your career opportunities.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="quote">
    💡 Small progress every day leads to big success!
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌟 Why SBF?")

    st.write("📚 Learn useful skills")
    st.write("🎯 Discover your talents")
    st.write("💼 Find career opportunities")
    st.write("🧭 Get career guidance")
    st.write("📱 Turn scrolling time into learning time")

# =========================================================
# EXPLORE COURSES
# =========================================================

elif page == "🎓 Explore Courses":

    st.markdown("""
    <div class="hero">
    <h1>🎓 Explore Courses</h1>
    <p>Choose a course and start learning.</p>
    </div>
    """, unsafe_allow_html=True)

    course = st.selectbox(
        "Choose Your Course",
        [
            "Python Programming",
            "Artificial Intelligence",
            "Data Science",
            "Web Development",
            "DBMS",
            "Full Stack Development"
        ]
    )

    # =====================================================
    # PYTHON
    # =====================================================

    if course == "Python Programming":

        st.subheader("🐍 Python Programming")

        lessons = {
            "1️⃣ Python Basics":
            "Python is a simple and powerful programming language used for web development, AI, data science and automation.",

            "2️⃣ Variables and Data Types":
            "Variables store data. Common data types are int, float, string and boolean.",

            "3️⃣ Operators":
            "Operators perform operations such as addition, subtraction, multiplication and comparison.",

            "4️⃣ Conditions":
            "Conditions use if, elif and else to make decisions in programs.",

            "5️⃣ Loops":
            "Loops repeat tasks. Python mainly uses for loops and while loops.",

            "6️⃣ Functions":
            "Functions are reusable blocks of code that perform a specific task.",

            "7️⃣ OOP":
            "Object Oriented Programming uses concepts like classes and objects."
        }

        for lesson, description in lessons.items():

            with st.expander(lesson):

                st.write(description)

                if lesson == "1️⃣ Python Basics":

                    st.code("""
print("Hello, SBF!")
""", language="python")

                elif lesson == "2️⃣ Variables and Data Types":

                    st.code("""
name = "Prasanna"
age = 19

print(name)
print(age)
""", language="python")

                elif lesson == "3️⃣ Operators":

                    st.code("""
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
""", language="python")

                elif lesson == "4️⃣ Conditions":

                    st.code("""
age = 18

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
""", language="python")

                elif lesson == "5️⃣ Loops":

                    st.code("""
for i in range(5):
    print(i)
""", language="python")

                elif lesson == "6️⃣ Functions":

                    st.code("""
def greet():
    print("Welcome to SBF")

greet()
""", language="python")

                elif lesson == "7️⃣ OOP":

                    st.code("""
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Prasanna")

print(student.name)
""", language="python")

                if st.button(
                    "✅ Mark as Completed",
                    key=lesson
                ):

                    if lesson not in st.session_state.completed_lessons:

                        st.session_state.completed_lessons.append(lesson)

                        st.session_state.points += 10

                        st.success("Lesson completed! +10 Points 🎉")

                    else:

                        st.info("You already completed this lesson!")

    # =====================================================
    # ARTIFICIAL INTELLIGENCE
    # =====================================================

    elif course == "Artificial Intelligence":

        st.subheader("🤖 Artificial Intelligence")

        st.write("### What is Artificial Intelligence?")

        st.write(
            "Artificial Intelligence, or AI, is the ability of "
            "machines and computers to perform tasks that normally "
            "require human intelligence."
        )

        st.write("### Important AI Topics")

        topics = [
            "🤖 Introduction to AI",
            "🧠 Machine Learning",
            "📊 Data and AI",
            "🔍 Deep Learning",
            "💬 Natural Language Processing",
            "👁️ Computer Vision"
        ]

        for topic in topics:

            with st.expander(topic):

                st.write(
                    "Learn the basic concepts and real-world "
                    "applications of " + topic
                )

    # =====================================================
    # DATA SCIENCE
    # =====================================================

    elif course == "Data Science":

        st.subheader("📊 Data Science")

        topics = [
            "Introduction to Data Science",
            "Python for Data Science",
            "NumPy",
            "Pandas",
            "Matplotlib",
            "Data Visualization"
        ]

        for topic in topics:

            with st.expander(topic):

                st.write(
                    topic + " is an important skill in Data Science."
                )

    # =====================================================
    # WEB DEVELOPMENT
    # =====================================================

    elif course == "Web Development":

        st.subheader("🌐 Web Development")

        topics = [
            "HTML",
            "CSS",
            "JavaScript",
            "Responsive Web Design"
        ]

        for topic in topics:

            with st.expander(topic):

                st.write(
                    "Learn " + topic +
                    " step by step and build websites."
                )

    # =====================================================
    # DBMS
    # =====================================================

    elif course == "DBMS":

        st.subheader("🗄️ Database Management System")

        topics = [
            "Introduction to DBMS",
            "Database",
            "Tables",
            "Primary Key",
            "Foreign Key",
            "SQL",
            "ER Model"
        ]

        for topic in topics:

            with st.expander(topic):

                st.write(
                    topic +
                    " is an important concept in Database Management Systems."
                )

    # =====================================================
    # FULL STACK
    # =====================================================

    elif course == "Full Stack Development":

        st.subheader("💻 Full Stack Development")

        st.write(
            "Full Stack Development includes both Frontend "
            "and Backend development."
        )

        st.write("### Frontend Skills")

        st.write("HTML")
        st.write("CSS")
        st.write("JavaScript")

        st.write("### Backend Skills")

        st.write("Python")
        st.write("Databases")
        st.write("APIs")

# =========================================================
# QUIZ
# =========================================================

elif page == "🧠 Take a Quiz":

    st.markdown("""
    <div class="hero">
    <h1>🧠 Take a Quiz</h1>
    <p>Test your knowledge!</p>
    </div>
    """, unsafe_allow_html=True)

    questions = [
        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automatic Internet",
                "Advanced Information",
                "Applied Intelligence"
            ],
            "answer": "Artificial Intelligence"
        },

        {
            "question": "Which language is popular for AI?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "SQL"
            ],
            "answer": "Python"
        },

        {
            "question": "What does HTML stand for?",
            "options": [
                "HyperText Markup Language",
                "HighText Machine Language",
                "Hyper Tool Language",
                "Home Text Markup Language"
            ],
            "answer": "HyperText Markup Language"
        },

        {
            "question": "Which one is a database?",
            "options": [
                "MySQL",
                "HTML",
                "CSS",
                "Python"
            ],
            "answer": "MySQL"
        }
    ]

    if "current_question" not in st.session_state:

        st.session_state.current_question = random.choice(questions)

    q = st.session_state.current_question

    st.subheader(q["question"])

    answer = st.radio(
        "Choose your answer:",
        q["options"]
    )

    if st.button("Submit Answer"):

        if answer == q["answer"]:

            st.success("🎉 Correct Answer!")

            st.session_state.points += 10
            st.session_state.quiz_score += 10

        else:

            st.error(
                "❌ Wrong Answer! Correct answer is: "
                + q["answer"]
            )

# =========================================================
# CAREER GUIDANCE
# =========================================================

elif page == "🧭 Career Guidance":

    st.markdown("""
    <div class="hero">
    <h1>🧭 Career Guidance</h1>
    <p>Explore your future opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

    careers = {
        "🤖 AI Developer":
        "Build intelligent applications using Artificial Intelligence.",

        "💻 Python Developer":
        "Develop software and applications using Python.",

        "🌐 Web Developer":
        "Build websites and web applications.",

        "📊 Data Scientist":
        "Analyze data and discover useful insights.",

        "🛡️ Cyber Security":
        "Protect computer systems and networks."
    }

    for career, description in careers.items():

        with st.expander(career):

            st.write(description)

            st.write("### Skills to Learn")

            st.write("✔ Programming")
            st.write("✔ Problem Solving")
            st.write("✔ Communication")
            st.write("✔ Continuous Learning")

# =========================================================
# MY PROGRESS
# =========================================================

elif page == "📊 My Progress":

    st.markdown("""
    <div class="hero">
    <h1>📊 My Progress</h1>
    <p>Track your learning journey.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "⭐ Total Points",
            st.session_state.points
        )

    with col2:
        st.metric(
            "📚 Lessons Completed",
            len(st.session_state.completed_lessons)
        )

    with col3:
        st.metric(
            "🧠 Quiz Score",
            st.session_state.quiz_score
        )

    st.write("### 📈 Learning Progress")

    progress = min(
        len(st.session_state.completed_lessons) / 10,
        1.0
    )

    st.progress(progress)

    st.write(
        "Keep learning every day. You are improving! 🚀"
    )

# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero">
    <h1>📚 About SBF</h1>
    <p>Study Begins for Future</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
SBF is a student-focused learning platform.

The goal of SBF is to help students use their free time
to learn useful skills and build a better future.

Instead of wasting time scrolling, students can learn,
practice and discover new opportunities.
""")

    st.markdown("""
    <div class="quote">
    🚀 Learn Today. Build Tomorrow. Create Your Future!
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    "<center>🚀 SBF | Study Begins for Future | Keep Learning 🌟</center>",
    unsafe_allow_html=True
)
