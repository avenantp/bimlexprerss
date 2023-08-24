
import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, age INTEGER)')

def add_data(name, age):
    c.execute('INSERT INTO data (name, age) VALUES (?, ?)', (name, age))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM data')
    data = c.fetchall()
    return data

def main():
    st.title("Simple Database App")
    
    menu = ["Home", "View Data"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Add to Database")
        name = st.text_input("Name")
        age = st.text_input("Age", type="number")
        if st.button("Add"):
            create_table()
            add_data(name, age)
            st.success(f"Added {name} aged {age} to the database")

    elif choice == "View Data":
        st.subheader("View Data")
        all_data = view_all_data()
        st.write(all_data)

if __name__ == "__main__":
    main()
