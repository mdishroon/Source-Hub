import streamlit as st
import pandas as pd
import os

# collapse the sidebar by default
st.set_page_config(initial_sidebar_state="collapsed")

# name of save file
FILE_NAME = "sources.csv"

# check if the user is logged in yet
if "logged_in" not in st.session_state:
    # if not, set their status to false
    st.session_state.logged_in = False

# function to load data from the save file
def load_data():
    # check if the save file exists on the computer yet
    if os.path.exists(FILE_NAME):
        # if it does, open it and turn it into a table
        return pd.read_csv(FILE_NAME)
    else:
        # if no file exists, make an empty table with our column headers
        return pd.DataFrame(columns=["Class", "Topic", "Link", "Description"])

# function to save new data into the file
def save_data(data_table):
    # save the table into file, do not save row numbers
    data_table.to_csv(FILE_NAME, index=False)

# PAGE 0: LOGIN SCREEN
# if the user is not logged in, only show the login box
if st.session_state.logged_in == False:
    st.title("Welcome to SourceHub")
    st.write("Please log in to access your secure database.")
    
    # create input boxes for username and password
    user_input = st.text_input("Username")
    # the type setting hides the typing with dots
    pass_input = st.text_input("Password", type="password")
    
    # create a button to check the login
    if st.button("Log In"):
        # pull the secret username and password from the secure file
        try:
            USERNAME = st.secrets["USERNAME"]
            PASSWORD = st.secrets["PASSWORD"]
        except FileNotFoundError:
            st.error("Secrets file is missing. Please check the README for setup instructions.")
            st.stop()
        except KeyError:
            st.error("Secrets file is improperly configured. Please check the README.")
            st.stop()

        # check if the typed words match reords
        if user_input == USERNAME and pass_input == PASSWORD:
            # change the status to true
            st.session_state.logged_in = True
            # refresh the page immediately to hide the login screen
            st.rerun()
        else:
            # show an error if they do not match
            st.error("Incorrect username or password.")

# THE MAIN APPLICATION
# if the user is logged in, show the actual application
if st.session_state.logged_in == True:
    
    # create a header row by splitting the screen into two columns
    col1, col2 = st.columns([8, 2])
    
    # put the title in the left column
    with col1:
        st.title("SourceHub")
        
    # logout button
    with col2:
        # empty space for logout button alignment
        st.write("")
        st.write("")
        # create the logout button
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()

    # load the saved data into memory when page opens
    df = load_data()

    # sidebar menu
    st.sidebar.title("Menu")
    
    # dropdown menu
    page_selection = st.sidebar.selectbox(
        "Navigation", 
        ["Add a Source", "View Sources", "Edit or Delete Sources"],
        label_visibility="hidden"
    )

    # PAGE 1: ADD A SOURCE
    if page_selection == "Add a Source":
        st.header("Add a New Source")
        
        # create input boxes for the user to type in
        class_name = st.text_input("Class Name (e.g., Cybersecurity)")
        topic = st.text_input("Link Topic (e.g., Routing)")
        source_link = st.text_input("Source Link")
        description = st.text_area("Short Description")
        
        # create a button to save the new source
        if st.button("Save Source"):
            # make sure all boxes have text before saving
            if class_name and topic and source_link and description:
                # group the new data together into a new small table
                new_entry = pd.DataFrame([{
                    "Class": class_name,
                    "Topic": topic,
                    "Link": source_link,
                    "Description": description
                }])
                
                # glue the new small table to the bottom of our main table
                df = pd.concat([df, new_entry], ignore_index=True)
                
                # send the updated main table to the save file
                save_data(df)
                
                # show a success message
                st.success("Source saved permanently!")
            else:
                # show an error if something is missing
                st.error("Please fill out all fields.")

    # PAGE 2: VIEW SOURCES
    elif page_selection == "View Sources":
        st.header("View My Sources")
        
        # check if our table has any rows of data
        if len(df) > 0:
            # get a list of all unique classes
            unique_classes = df["Class"].unique()
            
            # create a dropdown to pick a class
            selected_class = st.selectbox("Select a Class", unique_classes)
            
            # filter the table to only show the picked class
            class_data = df[df["Class"] == selected_class]
            
            # get a list of all unique topics for this class
            unique_topics = class_data["Topic"].unique()
            
            # create a dropdown to pick a topic
            selected_topic = st.selectbox("Select a Topic", unique_topics)
            
            # filter the table again to only show the picked topic
            final_data = class_data[class_data["Topic"] == selected_topic]
            
            # show the links and descriptions for this topic
            for index, row in final_data.iterrows():
                st.subheader("Link:")
                st.write(row["Link"])
                st.write("**Description:**")
                st.write(row["Description"])
                # draw a line to separate each saved link
                st.markdown("---")
        else:
            # tell the user if there are no sources yet
            st.write("No sources saved yet. Go to the Add menu to create one.")

    # PAGE 3: EDIT OR DELETE SOURCES
    elif page_selection == "Edit or Delete Sources":
        st.header("Manage My Sources")
        st.write("To edit: Click inside any box and change the text.")
        st.write("To delete: Click the gray box to the far left of a row, then press the Delete key on your keyboard.")
        
        # check if our table has any rows of data
        if len(df) > 0:
            # show an interactive table that the user can edit
            edited_df = st.data_editor(df, num_rows="dynamic")
            
            # create a button to save the changes made in the table
            if st.button("Save Changes"):
                # send the new edited table to the save file
                save_data(edited_df)
                st.success("Database updated successfully!")
        else:
            st.write("No sources to edit yet.")