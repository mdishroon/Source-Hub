# SourceHub

SourceHub is a minimalist Python application built to organize and manage educational resources. Much like assigning a static IP to a critical piece of hardware so you always know its exact address, this tool acts as a permanent, anchored database for your coursework. It provides a clean interface to reliably store, categorize, and route your study materials by class and topic, ensuring your most important links are always exactly where you left them.

</div>

## About the Files

* **streamHub.py**: This is the main application code. It creates the website interface, builds the hidden sidebar navigation, handles secure logins, and manages all the sorting and saving.
* **sources.csv**: This file acts as your database. It is created automatically the first time you save a link and permanently holds all your saved data. (This file is ignored by Git).
* **.streamlit/secrets.toml**: This hidden file stores your secure login credentials. (This file is ignored by Git).
* **README.md**: The guide you are reading right now. It provides instructions on how to set up and use the project.

## Security Note

This application uses Streamlit Secrets to manage logins securely. Before running the app locally or deploying it, you must configure your secrets.

1. Create a `.streamlit` folder in your main project folder.
2. Inside that new folder, create a `secrets.toml` file.
3. Add your login credentials to the file like this:
   ```toml
   USERNAME = "your_username"
   PASSWORD = "your_password"
   
4. Ensure you have a .gitignore file in your main project folder containing these exact lines so your data and passwords stay private:

```plaintext
.streamlit/secrets.toml
sources.csv
```

## How to Clone and Run the Repository
If you want to run this application on your own computer, open your computer terminal and follow these steps.

1. Clone the code to your computer:
```git clone https://github.com/mdishroon/Source-Hub.git```

2. Move into the new project folder:
```cd Source-Hub``

3. Install the required packages:
```pip install streamlit pandas```

4. Start the application:
```streamlit run streamHub.py```

A new window will automatically open in your web browser showing the application.

## How to Use the Application
Whether you are running this locally or using a hosted live website, the application is designed for a clean, distraction-free experience.

1. Secure Login & Logout
When you first open the app, enter the username and password you configured in your secrets.toml file to unlock your database. Whenever you are finished, click the Log Out button at the top right of the screen to secure your session.

2. Navigation
To keep your workspace clean, the menu is hidden by default.

> [!IMPORTANT]  
> Click the small ">" arrow in the top left corner of the screen to open the sidebar.

> Use the dropdown menu to select which page you want to view.

3. Add a Source
Select "Add a Source" from the navigation menu. Type in your class name, the topic of the link, the link itself, and a short description. Click the "Save Source" button. The application will write this information directly to your database file.

4. View Sources
Select "View Sources" from the navigation menu to find your study materials. Use the first dropdown menu to pick the class you want to review. Use the second dropdown menu to pick the specific topic. Your links and descriptions will appear cleanly organized on the screen.

5. Edit or Delete Sources
Select "Edit or Delete Sources" from the navigation menu to manage your database.

> [!NOTE]  
> To fix a mistake: Click directly inside any text box in the table and type your correction.

> [!NOTE]  
> To remove a link: Click the gray box to the far left of the row you want to remove to highlight it, then press the Delete key on your keyboard.

> [!IMPORTANT]  
> You must click the "Save Changes" button below the table to make your edits permanent.