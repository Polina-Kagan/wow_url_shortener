# Django URL Shortening Service

## 📌 Project Description

This project is a web application for shortening URLs with a user authentication system, built using the Django framework. It's designed from the ground up, without relying on front-end frameworks like Bootstrap, ensuring a unique and customizable user interface.

## 🚀 Key Features

**Django-powered Backend**: Utilizing Django's robust features for secure and efficient server-side operations
**Authentication**: User registration and login system implemented with Django's auth system
**Personal Account:** Personalized space for each user, leveraging Django's user model
**URL Shortening**: Creation of short versions of long URL addresses
**Link Management**: View and manage created shortened links
**Redirection**: Automatic redirection to the original URL when using the shortened version

## 🛠 Technical Details

**Django Framework**
Built on Django, leveraging its MVT (Model-View-Template) architecture
Utilizes Django's ORM for database operations
Takes advantage of Django's built-in admin interface for easy management

**Home Page and "About Us"**
Static pages with informational content, rendered using Django templates

**Authentication System**
Implements Django's authentication system
Custom login form with username and password validation
Error handling for authentication with message display using Django messages framework

**Personal Account**
Utilizes Django's user model for storing and displaying user information
Implements logout functionality using Django's auth views
Custom views for user data updates

**Link Management Page**
Custom Django models for storing shortened URLs
Django forms for creating new shortened links
Uniqueness check for shortened names using Django's model validation
ListView for displaying all links created by the user

**Redirection Mechanism**
Custom Django view for handling redirections
Efficient database queries for quick redirection to the original URL

## 🎨 Design Features

The project uses custom CSS styles, providing a unique and consistent appearance across the entire application. Django's template system is used for rendering HTML pages.

## 🔜 Development Plans

:bulb: Adding click statistics for links using Django's database models
:bulb: Implementing a RESTful API using Django REST Framework for integration with other services
:bulb: Improving the mobile version of the site with responsive Django templates
:bulb: Enhancing security features using Django's security middlewares

## 🤝 Contributing

:handshake: I'm open to collaboration! If you have ideas for improving the project, feel free to create an issue or submit a pull request. Familiarity with Django is a plus!

## 📄 License

This project is distributed under the MIT license. Details can be found in the LICENSE file.

## 🚀 Getting Started

To run this project locally:

Clone the repository
Install the required dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the Django development server: python manage.py runserver

:warning: Make sure you have Python and Django installed on your system.
