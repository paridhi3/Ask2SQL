# from dotenv import load_dotenv
# load_dotenv()      # loading all environment variables from .env file

# import streamlit as st
# import os
# import sqlite3
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # function to load Gemini Pro Model and get SQL query as responses
# model = genai.GenerativeModel('gemini-pro-vision')
# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt[0], question]) # prompt:how the model should behave, question:text given by user which will get converted to SQL query
#     return response.text

# # Function to execute SQL query on database and retrieve results
# def read_sql_query(sql, db):
#     conn = sqlite3.connect(db)
#     cur =  conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# # Define prompt
# prompt = [
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\n
#     For example,\n
#     Example 1 - "How many entries of records are present?" for which, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
#     \n
#     Example 2 - "Tell me all the students studying in Data Science class?" for which, 
#     the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; 
#     Also, the SQL code should not have ``` in beginning or end and SQL word in output
#     """
# ]

# # Streamlit App
# st.set_page_config(page_title="Ask2SQL")
# st.markdown("<h1>Ask2SQL</h1>", unsafe_allow_html=True)
# st.markdown("<h2>Generate instant SQL queries by asking simple questions</h2>", unsafe_allow_html=True)

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # Initialize session state for chat history visibility if it doesn't exist
# if 'show_chat_history' not in st.session_state:
#     st.session_state['show_chat_history'] = False

# question = st.text_input("Ask a question:", key="input")

# submit = st.button("Submit")
# # When submit is clicked
# if submit:
#     sql_query = get_gemini_response(question, prompt)  
#     response = read_sql_query(sql_query, "student.db")
    
#     st.markdown("<h3>Answer:</h3>", unsafe_allow_html=True)

#     st.markdown("<u>SQL Query:</u>", unsafe_allow_html=True)
#     st.code(sql_query)
    
#     st.markdown("<u>Results:</u>", unsafe_allow_html=True)
#     for row in response:
#         print(row)
#         st.text(row)
    
#     # Append user input and response to chat history
#     st.session_state['chat_history'].append(("You", question))
#     st.session_state['chat_history'].append(("SQL Query", sql_query))
#     st.session_state['chat_history'].append(("Result", response))

# # Button to toggle chat history visibility
# if st.button("Show Chat History"):
#     if not st.session_state['chat_history']:
#         st.write("No chat history yet.")
#     else:
#         st.session_state['show_chat_history'] = not st.session_state['show_chat_history']

# # Only display chat history if the button has been toggled to show
# if st.session_state['show_chat_history'] and st.session_state['chat_history']:
#     st.subheader("Chat History:")
#     for role, text in st.session_state['chat_history']:
#         st.write(f"{role}: {text}")

from dotenv import load_dotenv
load_dotenv()      # loading all environment variables from .env file

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro Model and get SQL query as responses
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question]) # prompt:how the model should behave, question:text given by user which will get converted to SQL query
    return response.text

# Function to execute SQL query on database and retrieve results
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur =  conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\n
    For example,\n
    Example 1 - "How many entries of records are present?" for which, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \n
    Example 2 - "Tell me all the students studying in Data Science class?" for which, 
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science"; 
    Also, the SQL code should not have ``` in beginning or end and SQL word in output
    """
]

# Streamlit App
st.set_page_config(page_title="Ask2SQL")
st.markdown("<h1>Ask2SQL</h1>", unsafe_allow_html=True)
st.markdown("<h2>Generate instant SQL queries by asking simple questions</h2>", unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Initialize session state for chat history visibility if it doesn't exist
if 'show_chat_history' not in st.session_state:
    st.session_state['show_chat_history'] = False

question = st.text_input("Ask a question:", key="input")

submit = st.button("Submit")
# When submit is clicked
if submit:
    sql_query = get_gemini_response(question, prompt)  
    response = read_sql_query(sql_query, "student.db")
    
    st.markdown("<h3>Answer:</h3>", unsafe_allow_html=True)

    st.markdown("<u>SQL Query:</u>", unsafe_allow_html=True)
    st.code(sql_query)
    
    st.markdown("<u>Results:</u>", unsafe_allow_html=True)
    if response:  # Check if response is not None
        for row in response:
            print(row)
            st.text(row)
    else:
        st.text("No results found.")
    
    # Append user input and response to chat history
    st.session_state['chat_history'].append(("You", question))
    st.session_state['chat_history'].append(("SQL Query", sql_query))
    st.session_state['chat_history'].append(("Result", response))

# Button to toggle chat history visibility
if st.button("Show Chat History"):
    if not st.session_state['chat_history']:
        st.write("No chat history yet.")
    else:
        st.session_state['show_chat_history'] = not st.session_state['show_chat_history']

# Only display chat history if the button has been toggled to show
if st.session_state['show_chat_history'] and st.session_state['chat_history']:
    st.subheader("Chat History:")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")
