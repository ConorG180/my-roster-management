<!-- Add picture/banner of programme here -->
<!-- Add Table of Contents here -->
# MyRosterManagement
MyRosterManagement is a programme designed for SME's (Small and Medium Enterprises) to aid them in staff and roster management. The main purpose the software serves is to allow managers/shift supervisors to schedule and set up shifts for employees at certain times on certain days. It is designed to aid managers/shift supervisors in not only the planning and scheduling of shifts of the company's workforce, but will also allow them to create/edit/delete roles and employees too, should circumstances for the companies change.  
Another purpose the programme will serve is to easily view the different days and months of the year, and allow managers to visualise how the workforce is scheduled on certain days and weeks. From this, managers can then tactically decide if they require more/less staff. While able to be used for any SME, it is expected to be especially useful to SMEs which incorporate and heavily rely on shift work, such as bars, restauraunts, supermarkets, shops, cafes, warehouses and courier services.  
The full <!-- **[Insert Name here later](InsertLinkToProjectHereLater)** --> programme can be accessed here.

# Wireframes
Before starting development on MyRosterManagement, Balsamiq was used to form wireframes for each separate page within the programme. Basamiq was chosen due to it's efficiency and it's ability to reproduce relatively simplistic, yet easy to understand wireframes. This helped me to visualise ideas for each of the programmes pages and features, and organise how certain features would be laid out and implemented within the programme. Each wireframe created prior to development can be seen below:  
![index.html wireframe](static/wireframes/home.png "index.html (Home page)")
![employees.html wireframe](static/wireframes/employees.png "employees.html (Employees page)")
![roles.html wireframe](static/wireframes/roles.png "roles.html (Roles page)")
![Contact modal wireframe](static/wireframes/contact-modal.png "Contact modal")
![calendar.html wireframe](static/wireframes/calendar-monthly-view.png "calendar.html (Calendar monthly view)")
![calendar.html wireframe](static/wireframes/calendar-daily-view.png "calendar.html (Calendar daily view)")

# Entity Relationship Diagram
Before starting development on MyRosterManagement, diagrams.net/draw.io was used to form an Entity Relationship Diagram (ERD) for the programme. As the programme relies heavily on models and databases, an ERD helped immensely in determining how to structure the database, including aiding in aspects such as relationships between tables, primary and foreign keys, and selecting fields for various tables. The ERD can be seen below:  
![MyRosterManagement ERD](static/entity-relationship-diagrams/my-roster-management-entity-relationship-diagram.drawio.png "MyRosterManagement ERD")

# Features
## Existing features

### Navigation
The programme offers a very simple and easy to use navigation system to navigate around the programme. This is not only in the form of moving to different pages, but also for features such as a contact modal and large buttons under each relevant table to manipulate the user's database.
#### **Images**  

### Contact us modal
Should any users experience any difficulty in using the software, there is a "Contact" modal which can be accessed on the navigation bar. This allows the user to contact the company via phone or email, and also offers means of contacting the company through social media pages.
#### **Images**  

### Footer
An attractive footer is included in the programme to offer the user a simple way of easily navigating to the social media pages of the company.
#### **Images**  

### CRUD (Create, Read, Update, Delete) functionality
On each table outlining the companies current records of employees, roles and scheduled workshifts, there are buttons which allow the user to manipulate these records. For example, a certified user may add a new employee and delete the replaced employee, and schedule their next workshift for when they wish.
#### **Images**  

### Account creation and login/logout functionality
The superuser will have the ability to create accounts for users, and will also have the ability to use CRUD functionality on the company's data. When creating a user, the superuser will also have the ability to grant these same permissions to the new user. This will prevent unauthorised users from editing/creating/deleting records, and also prevent them from registering other users.
#### **Images**  

### User permissions
As mentioned above, the programme is designed so that only authorised users can use CRUD functionality and create new users. Therefore, it is important that unauthorised users of the programme can access the information they need to gain benefit from the programme, but cannot see more personal details of the company, such as wages and employee phone numbers etc. And cannot use CRUD functionality on records. To solve this problem, all edit/delete/add buttons on each table have been hidden to unauthorised users. Furthermore, attempting to brute-force to certain URLs when logged in as an unauthorised user will simply return an `unauthorised.html` page and block the user from accessing CRUD functionality. This includes the `accounts/signup/` URL should an unauthorised user attempt to create a new user, as this could easily allow the programme to be hacked. When logged in as an unauthorised user, certain columns of certain tables are also hidden to prevent PPI (Private and Personal Information) from being accessed.
#### **Images**  

### Form validation
When adding or editing a company record, a form which contains incorrect or invalid data will be displayed back and an error message will be displayed to the user. This will let the user know why the form didn't submit correctly and allow them to easily correct their mistake before commiting the data to the database, thereby aiding in preventing invalid data being saved.
#### **Images**  

## Future features

### Calendar
A future feature to be included within the software will be a calendar view of the company's current week and month, which will display all employees set to work that day and also the times of their workshift. This feature was planned to allow the user/admin of the website to accurately plan how many employees they will have working on a certain day, and forecast any changes that may present themselves eg. a wedding in a restauraunt will require more employees than a normal day. With the calendar, an admin user will easily be able to see how many employees are working on that day, and plan accordingly. Likewise, they will also be able to lower the number of workshifts should there be a cancellation.  

This will also allow employees to see who is working at which times, which will allow them to request to swap shifts with their colleagues.

This feature was planned at the beginning of the project and a wireframe was created to express the idea visually, which can be seen below.  
#### **Images** 
![calendar.html wireframe](static/wireframes/calendar-monthly-view.png "calendar.html (Calendar monthly view)")

### Calendar day view
Another feature which extends from the calendar feature, was to include a way for the admin user to view each day separately. This feature was included so as to allow the user to see more details about a certain day. For example, each employee would have a visual representation (Similar to a bar chart) showing their exact working time. Furthermore, according to an employee's role, this bar would be color-coded, allowing the user to easily see the quantity of a certain role/skill would be present and working on the day. This feature, like the calendar, was also planned at the beginning of the project, and a wireframe was created to express the idea visually.  
#### **Images**
![calendar.html wireframe](static/wireframes/calendar-daily-view.png "calendar.html (Calendar daily view)")

### Automated email confirmation of workshift
In the future, automated emails may be implemented to notify employees who are scheduled to work on certain days. This feature would work by sending an email to the employee's recorded email address, and notifying them on what day and at what times they are scheduled to work. The email would be sent as soon as the workshift is scheduled by the admin user.   
#### **Images**  


# Technologies, frameworks, packages and libraries used
The following technologies were used in the development of this project:  
  - [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - HTML5 was used to apply the structure and to create the elements within the programme.
  - [Bootstrap](https://getbootstrap.com/) - Bootstrap was used for the majority of the styling and layout in the programme. Within bootstrap, there are also elements of JavaScript used, such as in the modal. This JavaScript is included within the Bootstrap framework.
  - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) - Custom CSS was used to add some custom styling to the programme, such as the distinctive orange styling used within the brand logo and the custom color of the social media icons.
  - [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create wireframes at the beginning of the project and aided in visualising ideas and features of the MyRosterManagement programme.
  - [Git](https://git-scm.com/) - Git was used for version control throughout this project.
  - [Gitpod](https://www.gitpod.io/) - Gitpod was used as the integrated developement environment for the project and to deploy the software.
  - [Github](https://github.com/) - Github was used store the project repository.
  - [Heroku](https://www.heroku.com) - This project was deployed using Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
  - [Python](https://www.python.org/) - was used throughout this programme in conjunction with other python-based packages and libraries to create the core functionality behind the programme. 
  - [Django](https://www.djangoproject.com/) - The Django framework for python was used to build many of the web development aspects of the programme, including user authentication, content administration and ORM.
  - [PostgreSQL](https://www.postgresql.org/) - PostgreSQL was used as an Object-relational database system in the project, and through ORM (Object-relational mapping) records were able to be Created, Read, Updated and Deleted (CRUD) from the PostgreSQL database.
  - [WhiteNoise](http://whitenoise.evans.io/en/stable/) - WhiteNoise was used as a means to allow the project to serve its own static files, as this is not possible with Django.
  - [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) - The django-allauth package was used to create the authentication, account registration and account management within the programme.
  - [Psycopg2](https://pypi.org/project/psycopg2/) - Psycopg2 was used as an adaptor for PostgreSQL, to ensure that it will work and integrate with Python and Django.
  - [Gunicorn](https://gunicorn.org/) - Gunicorn was used for the WSGI HTTP server for the project
  - [Django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/) - Django-phonenumber-field was used to for simple authentication and validation of phone numbers stored within models and used within forms throughout the programme.