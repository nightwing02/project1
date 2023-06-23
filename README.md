# Project Name: Flask Login and Registration Web Application

This project is a login and registration web application developed using Flask, a Python web framework. The application allows users to create an account, log in, update their passwords using email OTP (One-Time Password), and utilizes MySQL as the database management system. The passwords stored in the database are encrypted for enhanced security, and the project also incorporates Google reCAPTCHA for spam prevention.

## Features

1. **User Registration:** Users can create an account by providing their email address and password. The password is securely encrypted before storing it in the database.

2. **User Login:** Registered users can log in using their email and password. The application validates the credentials against the stored encrypted password in the database.

3. **Password Update with Email OTP:** Users can request a password update by entering their registered email address. The application generates a unique OTP and sends it to the user's email. Upon successful OTP verification, users can update their password.

4. **MySQL Database:** The project uses MySQL as the database management system for storing user account information, including encrypted passwords.

5. **Password Encryption:** The application employs encryption techniques to secure user passwords stored in the database. This ensures that even if the database is compromised, passwords remain protected.

6. **Google reCAPTCHA:** The project integrates with Google reCAPTCHA to prevent automated bots and spam. Users are required to pass the reCAPTCHA verification during registration and other relevant actions.

## Technologies Used

- **Flask:** The project utilizes Flask, a lightweight and flexible web framework in Python, to handle HTTP requests, routing, and rendering web templates.

- **Python:** The backend logic of the web application is developed using Python, providing a robust and scalable foundation for the project.

- **MySQL:** MySQL database is used to store and retrieve user account information. It offers a reliable and efficient solution for managing structured data.

- **Encryption Libraries:** The project utilizes encryption libraries in Python to encrypt and decrypt user passwords before storing and verifying them.

- **Google reCAPTCHA:** The web application integrates with the Google reCAPTCHA API to incorporate the reCAPTCHA verification process for enhanced security.

## Installation and Setup

1. **Python and Flask:** Ensure that Python is installed on your system. You can download and install the latest version of Python from the official Python website. Install Flask by running the following command:

   ```bash
   pip install flask
   ```

2. **MySQL Database:** Install MySQL database on your machine. You can download the installer from the official MySQL website and follow the installation instructions.

3. **Clone the Repository:** Clone this project repository to your local machine using the following command:

   ```bash
   git clone <repository_url>
   ```

4. **Database Configuration:** Open the project and locate the configuration file where database settings are stored (e.g., `config.py` or `app.py`). Modify the database configuration parameters in the file to match your MySQL database credentials.

5. **Google reCAPTCHA:** Sign up for a reCAPTCHA API key from the Google reCAPTCHA website. Add the obtained key to the project configuration file.

6. **Dependencies:** Install the project dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

7. **Run the Application:** Start the Flask development server by executing the following command:

   ```bash
   flask run
   ```

8. **Access the Application:** Open a web browser and enter the URL `http://localhost:5000` to access the login and registration web application. You should now be able to register, login, and perform other actions provided by the application.

## Project Structure

The project follows a standard Flask web application structure,

 containing the following directories and files:

- **`app.py`:** The main application file that initializes and configures the Flask application and defines the routes and views.

- **`templates/`:** Contains HTML templates for rendering web pages and forms.

- **`static/`:** Includes static files such as CSS stylesheets, JavaScript files, and images.

- **`models.py`:** Defines the database models and schema for storing user information.

- **`config.py`:** Contains configuration settings for the application, including database connection details and API keys.

- **`requirements.txt`:** Lists the project's dependencies for easy installation.

- **`README.md`:** Provides information about the project, installation instructions, and usage guidelines.

## Contributions

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please submit them via GitHub issues. Feel free to fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for more information.

## Acknowledgments

We would like to express our gratitude to the Flask, MySQL, and reCAPTCHA communities for their excellent tools and resources that made this project possible.

Thank you for using this Flask login and registration web application! We hope it meets your needs and provides a secure and user-friendly experience for your users.
