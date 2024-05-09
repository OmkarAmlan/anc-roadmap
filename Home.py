import streamlit as st
import sqlite3
import time

st.set_page_config(
    page_title="AnC Roadmap",
    page_icon="🏅",
    layout="wide",
)

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')
            
st.title("AnC Roadmap")
st.write("Hello Aiman! Here's the little roadmap I mentioned. Just take it at your pace, and don't worry, you'll do great! I trust you. For any questions, suggestions, or dobuts, you know how to get to me. **DO NOT HESITATE.** I'm always free to make any changes so that this suits better to you!")
st.write("And finally - BEST OF LUCK!")
v_spacer(2)

con=sqlite3.connect("aiman.db")
cur=con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS aiman_table(
        id INTEGER PRIMARY KEY,
        header TEXT,
        done BOOLEAN,
        time DATETIME
    )
''')

con.commit()

flag1=False
flag2=False
flag3=False
flag4=False
flag5=False

st.subheader("SECTION 1:")
with st.form("Aptitude"):
    st.subheader("Aptittude Subsection")
    url_pap1="https://ntse.fiitjee.com/NTSE2021/QP_ODISHA_NTSE_STAGE%201%202020-21_MAT.pdf"
    url_pap2="https://ntse.fiitjee.com/NTSE2021/QP_RAJASTHAN_NTSE%20STAGE%201%202020-21_MAT.pdf"
    v_spacer(1)
    st.write("**Structure:**")
    st.write("Mostly practice oriented. Go through the question papers (200 questions in total), ideally over the course of a week. We'll go over doubts and discuss approaches in follow ups.")
    v_spacer(1)
    st.write("**Question Paper 1:** [Click Here](%s)" % url_pap1)
    st.write("**Question Paper 2:** [Click Here](%s)" % url_pap2)
    
    val_apti=st.form_submit_button("Mark Done")
    if val_apti:
        cur.execute('''
            INSERT INTO aiman_table(header, done, time)
            VALUES(?,?,?)
        ''', ("Aptitude", True, time.time()))
        con.commit()
    
    cur.execute('''
        SELECT * FROM aiman_table WHERE done = 1 AND header = "Aptitude"
    ''')
    rows = cur.fetchall()

    if rows:
        flag1=True
        st.success("**This section has been completed.**")
   
    
st.subheader("SECTION 2:")
with st.form("Excel"):
    st.subheader("Excel Subsection")
    v_spacer(1)
    st.write("**Structure:**")
    st.write("Follow along with the video aaram se. This amount of excel is sufficient. Try and do this parallel on your own system as you follow along.")
    url_video="https://www.youtube.com/watch?v=SA_SDo-cqpg"
    v_spacer(1)
    st.write("**Video Link:** [Click Here](%s)" %url_video)
    val_excel=st.form_submit_button("Mark Done")
    if val_excel:
        cur.execute('''
            INSERT INTO aiman_table(header, done, time)
            VALUES(?,?,?)
        ''', ("Excel", True, time.time()))
        con.commit()
    
    cur.execute('''
        SELECT * FROM aiman_table WHERE done = 1 AND header = "Excel"
    ''')
    rows = cur.fetchall()

    if rows:
        flag2=True
        st.success("**This section has been completed.**")
        
st.subheader("SECTION 3:")
with st.form("Python"):
    st.subheader("Python Subsection")
    v_spacer(1)
    st.write("**Structure:**")
    st.write("Follow along with the playlist. Then go over the sample questions below. That should be plenty for now. Code the solutions in python exclusively. Take 10 days for the playlist aaramse and **do only the first 7 videos**.")
    url_playlist="https://www.youtube.com/playlist?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0"
    url_sheet="https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/"
    v_spacer(1)
    st.write("**Playlist Link:** [Click Here](%s)" %url_playlist)
    st.write("**Python problems for practice (Do just from the following topics: List, String, Tuple, Dictionary, Matrix and Functions): [Click Here](%s)**" %url_sheet)
    val_python=st.form_submit_button("Mark Done")
    if val_python:
        cur.execute('''
            INSERT INTO aiman_table(header, done, time)
            VALUES(?,?,?)
        ''', ("Python", True, time.time()))
        con.commit()
    
    cur.execute('''
        SELECT * FROM aiman_table WHERE done = 1 AND header = "Python"
    ''')
    rows = cur.fetchall()

    if rows:
        flag3=True
        st.success("**This section has been completed.**")
        

with open("ObesityDataSet_raw_and_data_sinthetic.csv", "r") as file:
    data1 = file.read()        
        
v_spacer(4)
st.subheader("PROJECT 1:")

st.subheader("Data Visualization Project")
st.write("You can access the problem statement for this project after completing the previous three sections.")
val_project1=st.button("View Problem Statement 1")
if val_project1:
    if flag1 and flag2 and flag3:
        st.success("**Ayyyy, good job!. See, I said ki I believed in you. Now just go ahead and apply all of that for this project!**")
        st.write("**PROBLEM STATEMENT:** Use this given csv file to make a data visualization project. The extent of visualisation is up to you!")
        st.download_button(
                label="Download data as CSV",
                data=data1,
                file_name="dataset.csv",
                mime='text/csv',
            )
        st.warning("Refer to Streamlit and Pandas ke basics on Google and YouTube. Baaki let me know if you need some more help. I'm always available.")
    else:
        st.error("**Jhooth mat bolo. Complete previous sections first.**")
    
v_spacer(4)
st.subheader("SECTION 4:")
with st.form("ML Fundamentals"):
    st.subheader("Machine Learning Fundamentals Subsection")
    v_spacer(1)
    st.write("**Structure:**")
    st.write("Just go over this video and chill out. Side by side do write the code khudse bhi as you follow the video.")
    url_ml="https://www.youtube.com/watch?v=I7NrVwm3apg"
    st.write("**ML Video Link:** [Click Here](%s)" %url_ml)
    val_ml=st.form_submit_button("Mark Done")
    if val_ml:
        cur.execute('''
            INSERT INTO aiman_table(header, done, time)
            VALUES(?,?,?)
        ''', ("ML", True, time.time()))
        con.commit()
    
    cur.execute('''
        SELECT * FROM aiman_table WHERE done = 1 AND header = "ML"
    ''')
    rows = cur.fetchall()

    if rows:
        flag4=True
        st.success("**This section has been completed.**")
        
st.subheader("SECTION 5:")
with st.form("PowerBI"):
    st.subheader("PowerBI Subsection")
    v_spacer(1)
    st.write("**Structure:**")
    st.write("Just go over this video. And practice karte rehna.")
    url_powerbi="https://www.youtube.com/watch?v=6cV3OwFrOkk"
    st.write("**PowerBI Video Link:** [Click Here](%s)" %url_powerbi)
    val_powerbi=st.form_submit_button("Mark Done")
    if val_powerbi:
        cur.execute('''
            INSERT INTO aiman_table(header, done, time)
            VALUES(?,?,?)
        ''', ("PowerBI", True, time.time()))
        con.commit()
    
    cur.execute('''
        SELECT * FROM aiman_table WHERE done = 1 AND header = "PowerBI"
    ''')
    rows = cur.fetchall()

    if rows:
        flag5=True
        st.success("**This section has been completed.**")
        
with open("salaries (2).csv", "r") as file:
    data2 = file.read()

v_spacer(4)
st.subheader("PROJECT 2:")

st.subheader("Data Visualization Project 2")
st.write("You can access the problem statement for this project after completing the previous three sections.")
val_project2=st.button("View Problem Statement 2")
if val_project2:
    if flag1 and flag2 and flag3 and flag4 and flag5:
        st.success("**Final Stretch! I know ML ke projects we haven't done, but since that is actually my domain, we'll get into it thoda acche se. For now, these projects will place you kaafi ahead the curve! But if you wanna do some ML, go ahead! That's Bonus Points.**")
        st.write("**PROBLEM STATEMENT:** Use this given csv file to make a data visualization project (preferably PowerBI use karke this time!). The extent of visualisation is up to you!")
        st.download_button(
                label="Download data as CSV",
                data=data2,
                file_name="dataset2.csv",
                mime='text/csv',
            )
        st.warning("I recommend ki do the 2nd project with PowerBI but you can go for streamlit and pandas like the first project also.")
    else:
        st.error("**Jhooth mat bolo. Complete previous sections first.**")
    
v_spacer(4)

st.subheader("End Card")
with st.form("chill"):
    st.subheader("This is just me yapping lmao")
    v_spacer(1)
    st.write("It's fine if you're tired/sleepy or even a little intimidated. Don't be too hard on yourself. **I trust you. You will make it.**")
    st.write("Baaki here's some Lofi music and some of your favorite songs to vibe to when you're chilling/studying! And yk I'm always here if you want something! Chalo won't yap now lmao. Best of luck and happy learning!")
    val_chill=st.form_submit_button("Music?")
    if val_chill:
        url_chill="https://www.youtube.com/watch?v=JdqL89ZZwFw"
        url_taylor="https://www.youtube.com/watch?v=lv0ybTvDy6Q"
        st.write("**Lofi Music:** [Click Here](%s)" %url_chill)
        st.write("**Era Playlist:** [Click Here](%s)" %url_taylor)