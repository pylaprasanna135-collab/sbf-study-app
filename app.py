import streamlit as st

# ==============================
# SBF - STUDY BEGINS FOR FUTURE
# ==============================

st.set_page_config(
    page_title="SBF - Study Begins for Future",
    page_icon="🚀",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 22px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    margin: 10px;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="main-title">🚀 SBF</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Study Begins for Future 🌟</div>',
    unsafe_allow_html=True
)

st.divider()


# ==============================
# SIDEBAR
# ==============================

st.sidebar.title("🚀 SBF")

menu = st.sidebar.radio(
    "📌 Explore SBF",
    [
        "🏠 Home",
        "🎓 Courses",
        "📝 Quiz",
        "🎯 Discover Talent",
        "💼 Opportunities",
        "🧭 Career Guidance"
    ]
)


# ==============================
# HOME
# ==============================

if menu == "🏠 Home":

    st.title("👋 Welcome to SBF!")

    st.write("""
    ### Learn Today. Build Your Future. 🚀

    SBF is a learning platform designed for students.

    Explore courses, test your knowledge,
    discover your interests and build your career.
    """)

    st.divider()

    st.header("🌟 Explore SBF")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
        🎓 COURSES

        Learn:
        • Python
        • AI
        • Data Science
        • Web Development
        """)

    with col2:
        st.success("""
        📝 QUIZ

        Test your knowledge.

        Earn points and improve your skills!
        """)

    with col3:
        st.warning("""
        🧭 CAREER

        Discover career paths.

        Build your future roadmap!
        """)

    st.divider()

    st.header("🔥 Daily Motivation")

    st.success(
        "💡 Small progress every day leads to big success!"
    )


# ==============================
# COURSES
# ==============================

elif menu == "🎓 Courses":

    st.title("🎓 Explore Courses")

    st.write("Choose a course and explore its topics! 🚀")

    course = st.selectbox(
        "📚 Select Your Course",
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


    # PYTHON

    if course == "🐍 Python Programming":

        st.header("🐍 Python Programming")

        st.write(
            "Learn Python step-by-step from basics to projects."
        )

        with st.expander("📖 1. Python Basics"):

            st.write("""
            Python is a popular programming language.

            It is used in:

            • Artificial Intelligence
            • Data Science
            • Web Development
            • Automation
            """)

            st.code(
                'print("Hello World!")',
                language="python"
            )


        with st.expander("📦 2. Variables"):

            st.write(
                "Variables store information."
            )

            st.code(
                '''name = "Prasanna"
age = 19

print(name)
print(age)''',
                language="python"
            )


        with st.expander("🔢 3. Data Types"):

            st.write("""
            Important Data Types:

            • int → Numbers

            • float → Decimal numbers

            • str → Text

            • bool → True or False

            • list → Multiple values
            """)


        with st.expander("⚙️ 4. Operators"):

            st.code(
                '''a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)''',
                language="python"
            )


        with st.expander("🔀 5. Conditions"):

            st.code(
                '''marks = 80

if marks >= 40:
    print("Pass")

else:
    print("Fail")''',
                language="python"
            )


        with st.expander("🔄 6. Loops"):

            st.code(
                '''for i in range(1, 6):
    print(i)''',
                language="python"
            )


        with st.expander("⚙️ 7. Functions"):

            st.code(
                '''def greet(name):

    return "Hello " + name


print(greet("Student"))''',
                language="python"
            )


        with st.expander("💻 8. Mini Projects"):

            st.write("""
            Project Ideas:

            • Calculator

            • Number Guessing Game

            • Student Marks Calculator

            • To-Do List
            """)


        with st.expander("📝 Python Quiz"):

            answer = st.radio(
                "Which keyword is used to define a function?",
                ["function", "def", "fun"]
            )

            if st.button("Check Python Answer"):

                if answer == "def":
                    st.success("🎉 Correct Answer!")

                else:
                    st.error("❌ Try Again!")


    # AI

    elif course == "🤖 Artificial Intelligence":

        st.header("🤖 Artificial Intelligence")

        st.write(
            "Explore the exciting world of AI! 🧠"
        )


        with st.expander("🌟 What is Artificial Intelligence?"):

            st.write("""
            Artificial Intelligence enables machines
            to perform tasks that normally require
            human intelligence.
            """)


        with st.expander("🧠 Machine Learning"):

            st.write("""
            Machine Learning helps computers
            learn patterns from data.
            """)


        with st.expander("🤖 Deep Learning"):

            st.write("""
            Deep Learning uses neural networks
            to solve complex problems.
            """)


        with st.expander("👁️ Computer Vision"):

            st.write("""
            Computer Vision allows computers
            to understand images and videos.
            """)


        with st.expander("💬 Natural Language Processing"):

            st.write("""
            NLP helps computers understand
            human language.

            Example:
            Chatbots and voice assistants.
            """)


        with st.expander("🚀 AI Project Ideas"):

            st.write("""
            • AI Chatbot

            • Image Classifier

            • Smart Attendance System

            • Recommendation System
            """)


    # DATA SCIENCE

    elif course == "📊 Data Science":

        st.header("📊 Data Science")

        with st.expander("📌 Introduction to Data Science"):

            st.write(
                "Data Science helps us analyze and understand data."
            )


        with st.expander("🐍 Python for Data Science"):

            st.write("""
            Important libraries:

            • NumPy

            • Pandas

            • Matplotlib
            """)


        with st.expander("📊 Data Visualization"):

            st.write("""
            Data visualization represents data
            using charts and graphs.
            """)


        with st.expander("📈 Statistics"):

            st.write("""
            Important concepts:

            • Mean

            • Median

            • Mode

            • Probability
            """)


        with st.expander("🤖 Machine Learning"):

            st.write("""
            Machine Learning helps predict
            results using data.
            """)


    # WEB DEVELOPMENT

    elif course == "🌐 Web Development":

        st.header("🌐 Web Development")

        with st.expander("📄 HTML"):

            st.write(
                "HTML creates the structure of a website."
            )


        with st.expander("🎨 CSS"):

            st.write(
                "CSS makes websites beautiful."
            )


        with st.expander("⚡ JavaScript"):

            st.write(
                "JavaScript makes websites interactive."
            )


        with st.expander("🎨 Frontend Development"):

            st.write("""
            Frontend includes:

            • HTML

            • CSS

            • JavaScript
            """)


        with st.expander("🖥️ Backend Development"):

            st.write("""
            Backend handles:

            • Server

            • Database

            • Application Logic
            """)


    # DBMS

    elif course == "🗄️ DBMS":

        st.header("🗄️ Database Management System")


        with st.expander("📚 Database Basics"):

            st.write(
                "A database stores and organizes information."
            )


        with st.expander("🔗 ER Diagram"):

            st.write(
                "ER Diagram represents entities and relationships."
            )


        with st.expander("🔑 Keys"):

            st.write("""
            Types of Keys:

            • Primary Key

            • Foreign Key

            • Candidate Key
            """)


        with st.expander("💻 SQL"):

            st.code(
                '''SELECT * FROM students;''',
                language="sql"
            )


        with st.expander("📊 Normalization"):

            st.write(
                "Normalization organizes data and reduces duplication."
            )


    # FULL STACK

    elif course == "💻 Full Stack Development":

        st.header("💻 Full Stack Development")

        with st.expander("🎨 Frontend"):

            st.write("""
            Learn:

            • HTML

            • CSS

            • JavaScript
            """)


        with st.expander("⚙️ Backend"):

            st.write("""
            Learn:

            • Python

            • APIs

            • Servers
            """)


        with st.expander("🗄️ Database"):

            st.write("""
            Learn:

            • SQL

            • Database Design
            """)


        with st.expander("🚀 Full Stack Projects"):

            st.write("""
            Project Ideas:

            • Student Management System

            • E-Commerce Website

            • Learning Platform

            • Portfolio Website
            """)


# ==============================
# QUIZ
# ==============================

elif menu == "📝 Quiz":

    st.title("📝 Knowledge Challenge")

    st.write("🎯 Answer the questions and test yourself!")


    q1 = st.radio(
        "1️⃣ What does AI stand for?",
        [
            "Automatic Internet",
            "Artificial Intelligence",
            "Advanced Input"
        ]
    )


    q2 = st.radio(
        "2️⃣ Which language is used for AI?",
        [
            "Python",
            "HTML",
            "CSS"
        ]
    )


    q3 = st.radio(
        "3️⃣ Which library is used for data analysis?",
        [
            "Pandas",
            "HTML",
            "JavaScript"
        ]
    )


    q4 = st.radio(
        "4️⃣ SQL is used for?",
        [
            "Databases",
            "Drawing",
            "Gaming"
        ]
    )


    q5 = st.radio(
        "5️⃣ HTML is used for?",
        [
            "Website Structure",
            "Data Analysis",
            "Machine Learning"
        ]
    )


    if st.button("🚀 Submit My Quiz"):

        score = 0


        if q1 == "Artificial Intelligence":
            score += 1

        if q2 == "Python":
            score += 1

        if q3 == "Pandas":
            score += 1

        if q4 == "Databases":
            score += 1

        if q5 == "Website Structure":
            score += 1


        st.divider()

        st.header("🏆 Your Result")

        st.metric(
            "Your Score",
            f"{score} / 5"
        )

        percentage = score * 20

        st.progress(percentage / 100)

        st.write(
            f"📊 Percentage: {percentage}%"
        )


        if score == 5:

            st.success(
                "🏆 PERFECT! You are amazing! 🌟"
            )

        elif score >= 3:

            st.success(
                "👏 Great Job! Keep learning!"
            )

        else:

            st.warning(
                "📚 Practice more and try again!"
            )


# ==============================
# DISCOVER TALENT
# ==============================

elif menu == "🎯 Discover Talent":

    st.title("🎯 Discover Your Talent")

    st.write(
        "Answer based on what you enjoy! 🚀"
    )


    interest = st.selectbox(
        "What do you enjoy most?",
        [
            "💻 Coding",
            "🔢 Maths",
            "🎨 Design",
            "🗣️ Communication",
            "💼 Business"
        ]
    )


    if st.button("🔍 Discover My Talent"):


        if interest == "💻 Coding":

            st.success("""
            💻 You may enjoy:

            • Software Development

            • AI Engineering

            • Web Development
            """)


        elif interest == "🔢 Maths":

            st.success("""
            📊 You may enjoy:

            • Data Science

            • Data Analytics

            • Machine Learning
            """)


        elif interest == "🎨 Design":

            st.success("""
            🎨 You may enjoy:

            • UI/UX Design

            • Web Design

            • Graphic Design
            """)


        elif interest == "🗣️ Communication":

            st.success("""
            🗣️ You may enjoy:

            • Teaching

            • Management

            • Human Resources
            """)


        elif interest == "💼 Business":

            st.success("""
            💼 You may enjoy:

            • Business Analytics

            • Entrepreneurship

            • Marketing
            """)


# ==============================
# OPPORTUNITIES
# ==============================

elif menu == "💼 Opportunities":

    st.title("💼 Student Opportunities")

    st.write(
        "Explore opportunities and build your future! 🚀"
    )


    with st.expander("🎓 Scholarships"):

        st.write("""
        Scholarships can help students
        continue their education.

        Keep checking official scholarship portals.
        """)


    with st.expander("💻 Internships"):

        st.write("""
        Internships provide real-world experience.

        Build projects and apply for internships.
        """)


    with st.expander("🏆 Hackathons"):

        st.write("""
        Hackathons help students:

        • Build Projects

        • Work in Teams

        • Learn New Skills

        • Win Prizes
        """)


    with st.expander("📜 Free Certifications"):

        st.write("""
        Certifications can improve your resume.

        Learn new skills and earn certificates!
        """)


    with st.expander("🌟 Career Tip"):

        st.success(
            "💡 Learn skills + Build projects + Practice regularly!"
        )


# ==============================
# CAREER GUIDANCE
# ==============================

elif menu == "🧭 Career Guidance":

    st.title("🧭 Career Guidance")

    career = st.selectbox(
        "🎯 Choose Your Dream Career",
        [
            "💻 Software Developer",
            "🤖 AI Engineer",
            "📊 Data Scientist",
            "🔐 Cyber Security",
            "🏛️ Government Jobs"
        ]
    )


    st.divider()


    if career == "💻 Software Developer":

        st.header("💻 Software Developer Roadmap")

        st.info("""
        STEP 1 → Learn Python

        STEP 2 → Learn DSA

        STEP 3 → Learn Web Development

        STEP 4 → Build Projects

        STEP 5 → Internship

        STEP 6 → Job 🚀
        """)


    elif career == "🤖 AI Engineer":

        st.header("🤖 AI Engineer Roadmap")

        st.info("""
        STEP 1 → Python

        STEP 2 → Mathematics

        STEP 3 → Machine Learning

        STEP 4 → Deep Learning

        STEP 5 → AI Projects

        STEP 6 → AI Career 🚀
        """)


    elif career == "📊 Data Scientist":

        st.header("📊 Data Scientist Roadmap")

        st.info("""
        STEP 1 → Python

        STEP 2 → NumPy

        STEP 3 → Pandas

        STEP 4 → Statistics

        STEP 5 → Machine Learning

        STEP 6 → Projects
        """)


    elif career == "🔐 Cyber Security":

        st.header("🔐 Cyber Security Roadmap")

        st.info("""
        STEP 1 → Networking

        STEP 2 → Linux

        STEP 3 → Security Basics

        STEP 4 → Python

        STEP 5 → Security Projects

        STEP 6 → Cyber Security Career
        """)


    elif career == "🏛️ Government Jobs":

        st.header("🏛️ Government Job Roadmap")

        st.info("""
        STEP 1 → Aptitude

        STEP 2 → Reasoning

        STEP 3 → English

        STEP 4 → General Awareness

        STEP 5 → Current Affairs

        STEP 6 → Mock Tests
        """)


# ==============================
# FOOTER
# ==============================

st.divider()

st.caption(
    "© 2026 SBF - Study Begins for Future 🚀 | Learn • Grow • Build"
)
