# [Ask2SQL](https://paridhi3-ask2sql-app-luklck.streamlit.app/)

Ask2SQL is a Streamlit web application that allows you to generate instant SQL queries by asking simple questions using Google Gemini Pro. It seamlessly converts your English questions into SQL queries and executes them on a SQLite database.

The following data is used:

### STUDENT TABLE
| ID      | Name    | Course         | Grade | Marks |
|---------|---------|----------------|-------|-------|
| 1001    | Paridhi | Data Science   | A     | 90    |
| 1002    | Rishabh | Data Science   | B     | 100   |
| 1003    | Swastika| Data Science   | A     | 86    |
| 1004    | Aaryan  | DEVOPS         | A     | 50    |
| 1005    | Rahul   | DEVOPS         | A     | 35    |
| 1006    | Sanya   | Data Science   | B     | 92    |
| 1007    | Aman    | DEVOPS         | B     | 65    |
| 1008    | Vikram  | Data Science   | A     | 78    |
| 1009    | Ishita  | AI             | A     | 88    |
| 1010    | Raj     | AI             | B     | 72    |
| 1011    | Ananya  | Cyber Security | A     | 95    |
| 1012    | Kabir   | Cyber Security | B     | 68    |
| 1013    | Priya   | Data Science   | A     | 89    |
| 1014    | Nisha   | DEVOPS         | B     | 55    |
| 1015    | Tara    | AI             | A     | 91    |
| 1016    | Varun   | Cyber Security | A     | 73    |

## Features

- **Natural Language to SQL Conversion**: Generate SQL queries instantly by asking simple questions.
  
- **Google Gemini Pro AI Integration**: Utilizes Google Gemini Pro AI for natural language understanding.

- **Real-time Query Execution**: Executes SQL queries on a SQLite database and displays query results in real-time.

- **Chat History**: Maintains chat history for user interactions, allowing you to review previous interactions.

## How to Use

1. **Input Field**: Enter your question in the "Input" field.

2. **Submit Button**: Click the "Submit" button to generate the SQL query.

3. **Answer Display**: The application will display the generated SQL query and the query results below.

4. **Show Chat History**: Click the "Show Chat History" button to view the chat history, including all interactions between the user and the AI model.

## Technologies Used

1. Python

2. Streamlit

3. Google Gemini Pro

4. SQLite3
