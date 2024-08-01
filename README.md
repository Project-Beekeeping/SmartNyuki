# SmartNyuki

## Overview

Smart Beekeeping is a web application designed to monitor hive conditions and send notifications based on data thresholds. The project utilizes Django for the backend and pure HTML, CSS, and JavaScript for the frontend.

## Features

- **Hive Monitoring**: Monitor various hive parameters such as temperature, humidity, sound, and weight.
- **Threshold Notifications**: Receive notifications when certain thresholds for parameters are exceeded.
- **Push Notifications**: Notifications are displayed both as browser notifications and under the notifications section in the web app.
- **Firebase Integration**: Fetch data from Firebase and trigger notifications based on real-time data.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: Firebase
- **Push Notifications**: Firebase Cloud Messaging (FCM)

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- Node.js and npm (for frontend dependencies)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/Project-Beekeeping/SmartNyuki.git
    cd smart-beekeeping
    ```

2. **Create and Activate Virtual Environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate    # This is for windows
    source venv/bin/activate  # This is for Linux
    ```

3. **Install Backend Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Setup Firebase**:
    - Create a Firebase project.
    - Set up Firestore database.
    - Obtain Firebase configuration and place it in the frontend.

5. **Run Migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the Development Server**:
    ```sh
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to Static Directory**:
    ```sh
    cd accounts/static
    ```

2. **Install Frontend Dependencies** (if any):
    ```sh
    npm install
    ```

3. **Build Frontend Assets** (if using any build tools):
    ```sh
    npm run build
    ```

## Usage

- Access the web application at `http://localhost:8000/`.
- Log in using the superuser credentials.
- Navigate to the hive monitoring dashboard to view real-time data.
- Configure threshold values for notifications.
- Check notifications in the notifications section.

## Project Structure

smart-beekeeping/
├── accounts/
│ ├── static/
│ │ ├── images/
│ │ ├── js and css files
│ ├── templates/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ └── views.py
├── SmartNyuki/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── project-login2-6c049-firebase-adminsdk-gh0yz-c6e5174321.json
├── README.md
└── requirements.txt



## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Thanks to the team members and JKUAT for the support and resources.
- Special thanks to Build with Microsoft for the modules and badges that helped in developing this project.

## Contact

For any queries, please contact Methusella at methusellanyongesa057@gmail.com or via [Twitter](https://x.com/METH_969).
