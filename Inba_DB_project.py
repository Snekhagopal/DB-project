# Import necessary modules
import mysql.connector
conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password="Snekha@2503"
)
cursor = conn.cursor()
# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS StudentDB")
# Use the database
cursor.execute("USE StudentDB")
# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
   id INT AUTO_INCREMENT PRIMARY KEY, # Unique ID for each student, auto-incremented
   name VARCHAR(255), # Student's name as a string
   age INT, # Student's age as an integer
   grade VARCHAR(50) # Student's grade as a string
)
""")
conn.close() # Close the database connection
# Import Streamlit and other libraries
import streamlit as st # Library for creating web apps
import pandas as pd # Library for handling tabular data
import matplotlib.pyplot as plt # Library for data visualization
# Function to insert data into the Students table
def insert_data(name, age, grade):
 conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Snekha@2503",
 database='StudentDB' # Specify the database to use
 )
 cursor = conn.cursor()
 cursor.execute(
 "INSERT INTO Students (name, age, grade) VALUES (%s, %s, %s)",
 (name, age, grade) # Insert data using parameterized queries to prevent SQL injection
 )
 conn.commit() # Commit the transaction to save the data
 conn.close() # Close the connection
# Function to retrieve all data from the Students table
def get_data():
 conn = mysql.connector.connect(
 host="localhost",
 user="root",
 password="Snekha@2503",
 database='StudentDB' # Specify the database to use
 )
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM Students") # Fetch all records from the Students table
 data = cursor.fetchall() # Retrieve all rows
 conn.close() # Close the connection
 return data
# Streamlit app layout
st.title("Student Data Management") # Display the title of the app
with st.form("Add Student"): # Create a form for adding a new student
     name = st.text_input("Name") # Input field for the student's name
     age = st.number_input("Age", min_value=1, step=1) # Input field for the student's age
     grade = st.text_input("Grade") # Input field for the student's grade
     submitted = st.form_submit_button("Add Student") # Submit button for the form
     if submitted:
      insert_data(name, age, grade) # Call the insert function with the input values
      st.success(f"Added {name} to the database!") # Display a success message
# Display data in the app
st.subheader("Students Data") # Subheading for the table

students_data = get_data() # Retrieve data from the database

df = pd.DataFrame(students_data, columns=["ID", "Name", "Age", "Grade"]) # Convert data into a DataFrame

st.table(df) # Display the data as a table
# Function to fetch data for visualization
def fetch_data_for_viz():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Snekha@2503",
    database='StudentDB' # Specify the database to use
    )
    cursor = conn.cursor()
    cursor.execute("SELECT age, grade FROM Students") # Fetch age and grade for visualization
    data = cursor.fetchall() # Retrieve all rows
    conn.close() # Close the connection
    return pd.DataFrame(data, columns=['Age', 'Grade']) # Convert data into a DataFrame
# Visualization in the app
st.subheader("Age Distribution by Grade") # Subheading for the chart

df_viz = fetch_data_for_viz() # Fetch data for visualization

fig, ax = plt.subplots()

df_viz.groupby('Grade')['Age'].mean().plot(kind='bar', ax=ax) # Plot a bar chart showing average age by grade

st.pyplot(fig) # Display the chart in the app
