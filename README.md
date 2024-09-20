# CaptchaWithJavaScript

# Photo Captcha Verification

## Overview

The **Photo Captcha Verification** is a web application designed to verify human users by asking them to identify images from specific categories (birds or drones). This interactive captcha helps ensure that users are not bots while enhancing user engagement.
You also can play a matching game with this application.

## Features

- **Dynamic Image Selection**: Randomly selects images from the categories of birds and drones.
- **User Interaction**: Users can click on images to select them, providing a seamless experience.
- **Real-Time Feedback**: Immediate validation of user selections, confirming whether the correct images were chosen.
- **Responsive Design**: Optimized for a seamless experience across various devices.


## Technologies Used

- **HTML5**
- **CSS3**
- **JavaScript**

## Getting Started

### Prerequisites

- A web browser (e.g., Chrome, Firefox, Safari).
- Basic understanding of HTML and JavaScript (optional).

### Installation Steps

1. **Download and Extract Images**:
   - Download the `images.zip` file from the repository.
   - Extract the contents to ensure you have the following structure:
     ```
     images/
     ├── bird/
     │   ├── bird1.jpg
     │   ├── bird2.jpg
     │   └── ...
     ├── drone/
     │   ├── drone1.jpg
     │   ├── drone2.jpg
     │   └── ...
     └── other/
         ├── other1.jpg
         ├── other2.jpg
         └── ...
     ```

2. **Clone the Repository**:
   ```
   git clone https://github.com/potuu/CaptchaWithJavaScript.git
Navigate to the Project Directory:

```
cd CaptchaWithJavaScript
```
Open the Application:

Launch index.html in your preferred web browser.
How to Use
Click the "Start Verification" button to begin.
Follow the prompt to select images from the specified category (either birds or drones).
Click on the images to select them, and then click the "Confirm" button.
Receive immediate feedback regarding your selections.


**Usage with Docker**

Pulling a Docker Image
To pull a Docker image from a repository, you can use the following command:

```
docker pull potuu/CaptchaWithJavaScript
```
Explanation:
CaptchaWithJavaScript is the name of the Docker image you want to pull.
Running a Docker Container
Once you have pulled the image, you can run a container using the following command:

```
docker run -p 8080:80 <username>/captcha-web
```
Explanation:
-p 8080:80 maps port 80 of the container to port 8080 on your host machine. This allows you to access the application running inside the container through your browser.
potuu/CaptchaWithJavaScript is the name of the image you just pulled.

Environment:
Ensure that your project is set up in Docker Desktop. This allows you to manage your containers and images easily.

Accessing the Application:
After running the above command, you can access your application by navigating to http://localhost:8080 in your web browser. This URL points to the mapped port on your local machine.

Contributing
Contributions are welcome! To contribute to the project:

Fork the repository.
Create a new branch:
```
git checkout -b feature/YourFeature
```
Make your changes and commit them:
```
git commit -m 'Add some feature'
```
Push to the branch:
```
git push origin feature/YourFeature
```
Open a pull request.
