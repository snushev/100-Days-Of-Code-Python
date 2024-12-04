# Password Manager

This is a simple password manager application built with Python and Tkinter. The application allows users to generate and save passwords for different websites.

## Features
- Generate random passwords with letters, numbers, and symbols.
- Save generated passwords along with website and email information.
- User interface with labels, entries, and buttons.

## How to Use
1. Enter the website name in the "Website" field.
2. Enter your email or username in the "Email/Username" field.
3. Click the "Generate Password" button to create a new password.
4. Click the "Add" button to save the password along with the website and email information.

## Code Structure
The code consists of several functions and widgets:
- `generate_password`: Generates a random password based on user requirements.
- `save`: Saves the entered website, email, and password to a file named `data.txt`.
- `Tkinter` widgets: Labels, entries, and buttons for user interaction.

## Dependencies
- `tkinter`: For creating the graphical user interface.
- `random`: For generating random passwords.

## Screenshot
![Password Manager Screenshot](https://i.imgur.com/WgQ64NI.png)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to contribute to this project by submitting pull requests or reporting issues. Happy coding!