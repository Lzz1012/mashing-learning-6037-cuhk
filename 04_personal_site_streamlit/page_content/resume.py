import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Jane Doe")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** zongzhe2223@163.com
    - **Phone:** 19892934178
    - **Address:** 123 Main St, Anytown, USA
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled software engineer with over 5 years of experience in developing scalable web applications. Proven ability to lead teams, manage projects, and improve software performance. Seeking a challenging role to utilize my technical expertise and problem-solving skills.
    """)

    

    st.header("Education")
    st.markdown("""
    **Bachelor of Business Analytics**
    - Macau University of Science and Technology
    - *Graduated: May 2023*
    - GPA: 3.4/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Databases:** MySQL, PostgreSQL, MongoDB
    - **Tools:** Git, Docker, Jenkins, AWS
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)


    st.header("Projects")
    st.markdown("""
    **E-commerce Website**
    - Developed a full-stack e-commerce application using React and Django.
    - Integrated payment gateways and implemented user authentication.

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native  """)
   

    st.header("Interests")
    st.markdown("""
    - Open-source contributions
    - Blogging about technology trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 