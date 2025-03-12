import streamlit as st

@st.experimental_dialog("Contact Me")
def show_contact_form():
    st.text_input("First Name")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./George Ndungu PIC.jpg", width=230)

with col2:
    st.title("George Ndung'u", anchor=False)
    st.write(
        "I am a recent computer science graduate with a strong foundation in programming, data structures, and algorithms. I have completed courses in C++ and Java. I am highly interested in trading technology, having developed a machine learning model to predict synthetic trades, and I am currently working on a trading bot with real-time data integration through the Deriv API. I am skilled in Python, especially for applications in machine learning and Streamlit, and I am setting up a robust backend with MySQL. My projects reflect a keen focus on financial tech, practical problem-solving, and a drive to innovate in automated trading."
    )
    if st.button(" ✌Contact Me"):
        show_contact_form()
    


st.title("Connect with Me")


st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/george-ndungu-20a302254/)")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Latesh-Splendler)")





st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 2 Years experience extracting actionable insights fron data
    - Strong hands-on experience and Knowledge in Python,Java,C++ and JavaScript
    - Good Understanding of the financial market(Forex Trading)
    - Proficient in using MySQL and PostgreSQL databases
    - Excellent team-player and showing a strong sense of inovation on tasks
"""
)    

st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
- Bachelor of Science in Computer Science, Cooperative Unversity
- Diploma in Computer Science, Cooperative University
- Programming: Python,Java,C++,JavaScript,C,VBA
- Data Structures: Arrays,Linked Lists,Stacks,Queues,Graphs,Trees
- Modeling: Linear Regression,Random Forest
- Database: Postgres, MySQL

"""
)
st.title("Contact Form")

st.write("Please fill out the form below to get in touch!")


name = st.text_input("Full Name")
email = st.text_input("Email Address")
subject = st.selectbox("Subject", ["General Inquiry", "Support", "Feedback", "Other"])
message = st.text_area("Message")

# Submit button
if st.button("Submit"):
    if name and email and message:
        st.success(f"Thank you for reaching out, {name}! We will get back to you shortly.")
        st.write("Your message details:")
        st.write(f"**Subject**: {subject}")
        st.write(f"**Message**: {message}")
    else:
        st.error("Please fill in all the required fields.")



