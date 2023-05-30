# Online Coding Web Application

This is an online coding web application built with Flask, JavaScript, CodeMirror, HTML, CSS, and Socket.io. The application allows mentors to share code blocks with their mentees in real time. The server is hosted on Digital Ocean.

## Features

- Lobby page to choose code blocks
- Real-time code collaboration between mentors and students
- Syntax highlighting for JavaScript code using CodeMirror
- Mentor has read-only access to the code block
- Students can edit and update the code block

## Technologies Used

- Framework: Flask
- Front-end: JavaScript, CodeMirror, HTML, CSS
- Back-end: Flask
- Real-time Communication: Socket.io
- Hosting: Digital Ocean

## Getting Started

To run the application, follow these steps:

1. Download all the files from the repository.
2. Set up a server environment to host the application.
3. Start the server using the appropriate command or method for your environment.
4. Access the application by navigating to the server's URL.

> If you want access to my own server for testing, please send me a message to request the link.

## Usage

1. Open the web browser and navigate to the application's URL.
2. On the lobby page, choose a code block from the list.
3. You will be redirected to the code block page.
4. If you are the first user, you will be the mentor and have read-only access to the code block. If you are a subsequent user, you will be a student and can edit the code block.
5. It is important for both the mentor and the student to enter the same code block, or the code will not load for the student.
6. Any changes made to the code block will be displayed in real time.
7. Be cautious when leaving the website or closing the tab before exiting the code using the provided button. Sudden disconnections or leaving the page without proper exit may cause issues in recognizing mentors.

## Known Bugs

- In order to view and collaborate on a code block, both the mentor and student must enter the same code block. Failure to do so will result in the code not loading for the student.
- If the connection is lost, such as network collapse or exiting the Chrome tab without using the provided exit button, there may be difficulties in recognizing mentors. Please be mindful of how you leave the website.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
