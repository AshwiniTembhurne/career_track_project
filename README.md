

 # CareerTrack     ![CareerTrack Logo](static/images/logo.png)  

 ## Table of Contents

1. [Introduction](#introduction)
2. [User Experience Design](#user-experience-design)
3. [Wireframes](#wireframes)
4. [Agile Development Process](#agile-development-process)
4. [Features](#features)

## Introduction

CareerTrack is a robust web application designed to streamline the job application process for users. It provides a platform for job seekers to manage and track their job applications effectively, helping them stay organized and informed throughout their job search journey. 

Built with Django, Bootstrap, and a responsive design in mind, CareerTrack aims to provide a seamless and intuitive user experience across all devices. Whether you're applying for your first job or switching careers, CareerTrack helps you keep track of all your job applications in one place, ensuring you never miss an opportunity.

## User Experience Design

### User Stories

- **As a new user**, I want to sign up easily so that I can start using the app.
- **As a returning user**, I want to log in quickly and securely to access my dashboard.
- **As a user**, I want to add job applications so that I can track them.
- **As a user**, I want to view the status of my job applications on my dashboard.
- **As an admin**, I want to manage users and view all job applications.
- **As an admin**, I want to be able to delete users if necessary.

### Wireframes

Wireframes were created during the planning phase to visualize the layout of key pages such as the home page, login, signup, user dashboard, and admin dashboard. Below are the wireframes:

- **Home Page**: ![Home Page Wireframe](static/images/home_page_wireframe.png)
- **User Dashboard**: ![User Dashboard Wireframe](static/images/user_dashboard_wireframe.png)
- **Admin Dashboard**: ![Admin Dashboard Wireframe](static/images/admin_dashboard_wireframe.png)
                      ![Admin Dashboard View User List Wireframe](static/images/admin_viewuser_list.png)
- **Job Application Management**: ![Job Application Wireframe](static/images/job_application_wireframe.png)

### User Flow Diagram

The user flow diagram illustrates the different pathways a user can take within the application, from registration to managing job applications:

![User Flow Diagram](static/images/user_flow_diagram.png)

### ERD Diagram

The Entity-Relationship Diagram (ERD) outlines the database structure of CareerTrack, including the relationships between users, job applications, and roles.

![ERD Diagram](static/images/erd_diagram.png)

## Agile Development Process

CareerTrack was developed using Agile methodologies, with the project being divided into sprints. Each sprint focused on different aspects of the application, from user authentication to job application management.For user story management, I utilized GitHub's Project Board (also known as Kanban board) to organize and track the progress of tasks and user stories efficiently,[Here is the link of GitHub's Project Board](https://github.com/users/AshwiniTembhurne/projects/4/views/1)

### Sprint Overview

- **Sprint 1**: User authentication, registration, and basic dashboard setup.
- **Sprint 2**: Job application management features.
- **Sprint 3**: Admin panel and user management.
- **Sprint 4**: Responsive design and final testing.

## Features

- **User Registration and Authentication**: Secure registration and login system with user roles (admin and standard user).
- **Dashboard**: Personalized user dashboard showing the status of job applications.
- **Admin Panel**: An admin dashboard with additional controls, including user management and application tracking.
- **Job Application Management**: Users can add, edit, view, and delete job applications, along with the ability to track their status.
- **Responsive Design**: Fully responsive design ensuring usability across mobile, tablet, and desktop devices.
- **Notifications**: Alert system for successful actions like logging in, signing up, and managing applications.

## Testing

### Manual Testing

Each feature was manually tested across different devices and browsers to ensure functionality and responsiveness. This included:

- **Form Validation**: Ensuring that all forms (registration, login, application management) behave as expected, with appropriate error handling.
- **Navigation**: Verifying that all navigation links work correctly.
- **Responsive Design**: Testing on devices ranging from smartphones to desktops to ensure the site is fully responsive.

### Automated Testing

Automated tests were written using Django’s testing framework to ensure that the critical functionalities of the application perform as expected:

- **User Registration**: Tests to ensure new users can register.
- **Login/Logout**: Tests to confirm that users can log in and log out securely.
- **Job Application Management**: Tests to ensure that users can add, edit, and delete job applications.

### Issues and Resolutions

- **Responsive Issues**: Early testing revealed some issues with responsiveness on mobile devices. These were resolved by adjusting the CSS and using Bootstrap’s grid system.
- **Form Validation**: There were initial issues with form validation where users could submit forms without proper data. These were fixed by implementing Django's built-in form validation.

## Deployment

### Prerequisites

- **Python 3.8+**
- **Django 3.2+**
- **Bootstrap 5**

### Steps for Local Deployment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AshwiniTembhurne/career_track_project.git

2. **Navigate to your project directory**:
   cd careertrack

3. **Install dependencies**:
   pip install -r requirements.txt

4. **Run migrations**:
  python3 manage.py migrate

5. **Run the server**:
   python3 manage.py runserver

6. **Access the application**:
  Open your browser and go to http://127.0.0.1:8000/

  ### Deployment on Heroku

1. **Create a Heroku app**:
  heroku create careertrack

2. **Push to Heroku**:
  git push heroku main

3. **Set up environment variables on Heroku**:
  Configure your database and other environment variables in the Heroku dashboard.

4. **Run migrations**:
  heroku run python manage.py migrate

5. **Open the app**:
  Visit your deployed app using the URL provided by Heroku.


  ## Credits

  - Django Documentation: For providing comprehensive guidance on building web applications with Django.
  - Bootstrap: For the responsive front-end framework used throughout the project.
  - Font Awesome & Bootstrap Icons: For providing the icons used in the application.
  - Favicon used in the application.