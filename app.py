import streamlit as st

# ==============================
# SBF - Study Begins for Future
# ==============================

st.set_page_config(
    page_title="SBF - Study Begins for Future",
    page_icon="🚀",
    layout="wide"
)

# ---------- SIDEBAR ----------
st.sidebar.title("🚀 SBF")
st.sidebar.write("Study Begins for Future")

menu = st.sidebar.radio(
    "📌 Menu",
    [
        "🏠 Home",
        "🎓 Courses",
        "📝 Quiz",
        "📚 Learn Skills",
        "🎯 Discover Your Talent",
        "💼 Opportunities",
        "🧭 Career Guidance"
    ]
)

# ---------- HOME ----------
if menu == "🏠 Home":

    st.title("🚀 SBF")
    st.subheader("Study Begins for Future")

    st.write("### Learn Today. Build Your Future. 🌟")

    st.divider()

    st.header("👋 Welcome to SBF!")

    st.write("""
    SBF is a student learning platform.

    📚 Learn useful skills

    🎓 Explore courses

    📝 Test your knowledge

    🎯 Discover your talent

    💼 Find opportunities

    🧭 Get career guidance
    """)

    st.success("🚀 Start learning. Start building your future!")

# ---------- COURSES ----------
elif menu == "🎓 Courses":

    st.title("🎓 SBF Courses")

    st.write("Choose a course and start learning.")

    course = st.selectbox(
        "Select a Course",
        [
            "🐍 Python Programming",
            "🤖 Artificial Intelligence",
            "📊 Data Science",
            "🌐 Web Development",
            "🗄️ DBMS",
            "💻 Full Stack Development"
        ]
    )

    st.divider()

    if course == "🐍 Python Programming":

        st.header("🐍 Python Programming")

        lesson = st.selectbox(
            "Select Lesson",
            [
                "Lesson 1 - Python Basics",
                "Lesson 2 - Variables",
                "Lesson 3 - Data Types",
                "Lesson 4 - Operators",
                "Lesson 5 - Conditions",
                "Lesson 6 - Loops",
                "Lesson 7 - Functions",
                "Lesson 8 - OOP"
            ]
        )

        if lesson == "Lesson 1 - Python Basics":

            st.subheader("Python Basics")

            st.write(
                "Python is a popular programming language "
                "used in software development, AI and data science."
            )

            st.code('print("Hello World!")', language="python")

        elif lesson == "Lesson 2 - Variables":

            st.subheader("Variables")

            st.write("Variables are used to store values.")

            st.code(
                'name = "Student"\nage = 19\nmarks = 85',
                language="python"
            )

        elif lesson == "Lesson 3 - Data Types":

            st.subheader("Data Types")

            st.write("""
            Common Python data types:

            • int - Integer numbers

            • float - Decimal numbers

            • str - Text

            • bool - True or False

            • list - Collection of values
            """)

        elif lesson == "Lesson 4 - Operators":

            st.subheader("Operators")

            st.write("Operators are used to perform operations.")

            st.code(
                'a = 10\nb = 5\n\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a / b)',
                language="python"
            )

        elif lesson == "Lesson 5 - Conditions":

            st.subheader("Conditions")

            st.write("Conditions help programs make decisions.")

            st.code(
                'marks = 80\n\nif marks >= 40:\n    print("Pass")\nelse:\n    print("Fail")',
                language="python"
            )

        elif lesson == "Lesson 6 - Loops":

            st.subheader("Loops")

            st.write("Loops repeat a block of code.")

            st.code(
                'for i in range(1, 6):\n    print(i)',
                language="python"
            )

        elif lesson == "Lesson 7 - Functions":

            st.subheader("Functions")

            st.write("Functions are reusable blocks of code.")

            st.code(
                'def greet(name):\n    return "Hello " + name\n\nprint(greet("Student"))',
                language="python"
            )

        elif lesson == "Lesson 8 - OOP":

            st.subheader("Object-Oriented Programming")

            st.write("OOP means Object-Oriented Programming.")

            st.code(
                'class Student:\n    def __init__(self, name):\n        self.name = name',
                language="python"
            )

    elif course == "🤖 Artificial Intelligence":

        st.header("🤖 Artificial Intelligence")

        st.write("""
        Learn the fundamentals of Artificial Intelligence.

        Topics:

        • Introduction to AI

        • History of AI

        • Types of AI

        • Intelligent Agents

        • Machine Learning

        • Deep Learning

        • AI Applications
        """)

    elif course == "📊 Data Science":

        st.header("📊 Data Science")

        st.write("""
        Learn how to work with data.

        Topics:

        • Python

        • NumPy

        • Pandas

        • Statistics

        • Data Visualization

        • Machine Learning
        """)

    elif course == "🌐 Web Development":

        st.header("🌐 Web Development")

        st.write("""
        Learn how websites are created.

        Topics:

        • HTML

        • CSS

        • JavaScript

        • Frontend Development

        • Backend Basics
        """)

    elif course == "🗄️ DBMS":

        st.header("🗄️ Database Management System")

        st.write("""
        Learn database concepts.

        Topics:

        • Database Basics

        • ER Diagram

        • Keys

        • SQL

        • Normalization

        • Transactions
        """)

    elif course == "💻 Full Stack Development":

        st.header("💻 Full Stack Development")

        st.write("""
        Learn both frontend and backend development.

        Topics:

        • HTML

        • CSS

        • JavaScript

        • Python

        • Backend

        • Databases

        • Projects
        """)

# ---------- QUIZ ----------
elif menu == "📝 Quiz":

    st.title("📝 SBF Quiz")

    st.write("Test your knowledge! 🚀")

    q1 = st.radio(
        "1. Which language is used to build this app?",
        ["Java", "Python", "C++", "PHP"]
    )

    q2 = st.radio(
        "2. What does AI stand for?",
        [
            "Artificial Intelligence",
            "Automatic Internet",
            "Advanced Input",
            "Application Interface"
        ]
    )

    q3 = st.radio(
        "3. Which is used for data analysis in Python?",
        ["Pandas", "HTML", "CSS", "Java"]
    )

    q4 = st.radio(
        "4. Which keyword defines a function?",
        ["function", "def", "fun", "define"]
    )

    q5 = st.radio(
        "5. Which one is a database language?",
        ["SQL", "CSS", "PNG", "HTML"]
    )

    if st.button("🚀 Submit Quiz"):

        score = 0

        if q1 == "Python":
            score = score + 1

        if q2 == "Artificial Intelligence":
            score = score + 1

        if q3 == "Pandas":
            score = score + 1

        if q4 == "def":
            score = score + 1

        if q5 == "SQL":
            score = score + 1

        st.divider()

        st.header("🏆 Your Result")

        st.write("Score:", score, "/ 5")

        if score == 5:
            st.success("🌟 Excellent! Perfect Score!")

        elif score >= 3:
            st.success("👏 Good job! Keep learning!")

        else:
            st.warning("📚 Keep practicing!")

# ---------- LEARN SKILLS ----------
elif menu == "📚 Learn Skills":

    st.title("📚 Learn Useful Skills")

    skill = st.selectbox(
        "Choose a skill",
        [
            "Python",
            "Artificial Intelligence",
            "Data Science",
            "Communication Skills",
            "Problem Solving"
        ]
    )

    if skill == "Python":
        st.write("🐍 Learn programming and build projects.")

    elif skill == "Artificial Intelligence":
        st.write("🤖 Learn AI and Machine Learning concepts.")

    elif skill == "Data Science":
        st.write("📊 Learn data analysis and visualization.")

    elif skill == "Communication Skills":
        st.write("🗣️ Improve English communication and presentation skills.")

    elif skill == "Problem Solving":
        st.write("🧠 Improve logical thinking and problem-solving skills.")

# ---------- TALENT ----------
elif menu == "🎯 Discover Your Talent":

    st.title("🎯 Discover Your Talent")

    interest = st.selectbox(
        "What do you enjoy?",
        [
            "Coding",
            "Maths",
            "Design",
            "Communication",
            "Business"
        ]
    )

    if st.button("🔍 Explore My Interest"):

        if interest == "Coding":
            st.success("💻 Software Development or AI may interest you.")

        elif interest == "Maths":
            st.success("📊 Data Science or Analytics may interest you.")

        elif interest == "Design":
            st.success("🎨 UI/UX or Web Design may interest you.")

        elif interest == "Communication":
            st.success("🗣️ Communication, teaching or management may interest you.")

        elif interest == "Business":
            st.success("💼 Business Analytics or Entrepreneurship may interest you.")

# ---------- OPPORTUNITIES ----------
elif menu == "💼 Opportunities":

    st.title("💼 Student Opportunities")

    st.write("Explore opportunities for your future.")

    st.checkbox("🎓 Scholarships")

    st.checkbox("💻 Internships")

    st.checkbox("🏆 Hackathons")

    st.checkbox("📜 Certifications")

    st.checkbox("📚 Online Courses")

    st.info("Keep checking opportunities and apply regularly.")

# ---------- CAREER ----------
elif menu == "🧭 Career Guidance":

    st.title("🧭 Career Guidance")

    career = st.selectbox(
        "Choose your career goal",
        [
            "Software Developer",
            "AI Engineer",
            "Data Scientist",
            "Cyber Security",
            "Government Jobs"
        ]
    )

    st.divider()

    if career == "Software Developer":

        st.header("💻 Software Developer Roadmap")

        st.write(
            "Python → DSA → Web Development → Projects → Internship → Job"
        )

    elif career == "AI Engineer":

        st.header("🤖 AI Engineer Roadmap")

        st.write(
            "Python → Maths → Machine Learning → Deep Learning → AI Projects"
        )

    elif career == "Data Scientist":

        st.header("📊 Data Scientist Roadmap")

        st.write(
            "Python → NumPy → Pandas → Statistics → Machine Learning → Projects"
        )

    elif career == "Cyber Security":

        st.header("🔐 Cyber Security Roadmap")

        st.write(
            "Networking → Linux → Security Basics → Security Projects"
        )

    elif career == "Government Jobs":

        st.header("🏛️ Government Job Roadmap")

        st.write(
            "Aptitude → Reasoning → English → General Awareness → Mock Tests"
        )

# ---------- FOOTER ----------
st.divider()

st.caption("© 2026 SBF - Study Begins for Future 🚀")
