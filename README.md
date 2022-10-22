![My-Roster-Management logo](static/images/my-roster-management-logo.png "My-Roster-Management logo")
# Table of Contents
- [Table of Contents](#table-of-contents)
- [MyRosterManagement](#myrostermanagement)
- [UX design](#ux-design)
  - [Color scheme](#color-scheme)
  - [Layout](#layout)
- [Wireframes](#wireframes)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Features](#features)
  - [Existing features](#existing-features)
    - [Navigation](#navigation)
      - [**Images**](#images)
        - [**Logged in as Admin**](#logged-in-as-admin)
        - [**Logged in as non-Admin**](#logged-in-as-non-admin)
        - [**Logged out**](#logged-out)
        - [**Table buttons**](#table-buttons)
    - [Contact us modal](#contact-us-modal)
      - [**Images**](#images-1)
    - [Footer](#footer)
      - [**Images**](#images-2)
    - [CRUD (Create, Read, Update, Delete) functionality](#crud-create-read-update-delete-functionality)
      - [**Images**](#images-3)
        - [**CRUD functionality on table**](#crud-functionality-on-table)
        - [**Adding record form**](#adding-record-form)
        - [**Editing record form**](#editing-record-form)
    - [Account creation and login/logout functionality](#account-creation-and-loginlogout-functionality)
      - [**Images**](#images-4)
        - [**Account registration form**](#account-registration-form)
        - [**Signin form**](#signin-form)
        - [**Signout confirmation**](#signout-confirmation)
    - [User permissions](#user-permissions)
      - [**Images**](#images-5)
        - [**Unauthorized user view of table**](#unauthorized-user-view-of-table)
        - [**Unauthorized message if brute-forcing a URL is attempted**](#unauthorized-message-if-brute-forcing-a-url-is-attempted)
    - [Form validation](#form-validation)
      - [**Images**](#images-6)
  - [Future features](#future-features)
    - [Calendar](#calendar)
      - [**Images**](#images-7)
    - [Calendar day view](#calendar-day-view)
      - [**Images**](#images-8)
    - [Automated email confirmation of workshift](#automated-email-confirmation-of-workshift)
- [Testing and bugs](#testing-and-bugs)
- [Technologies, frameworks, packages and libraries used](#technologies-frameworks-packages-and-libraries-used)
- [Deployment](#deployment)
  - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Acknowledgements](#acknowledgements)

# MyRosterManagement
MyRosterManagement is a programme designed for SME's (Small and Medium Enterprises) to aid them in staff and roster management. The main purpose the software serves is to allow managers/shift supervisors to schedule and set up shifts for employees at certain times on certain days. It is designed to aid managers/shift supervisors in not only the planning and scheduling of shifts of the company's workforce, but will also allow them to create/edit/delete roles and employees too, should circumstances for the companies change.  
Another purpose the programme will serve is to easily view the different days and months of the year, and allow managers to visualise how the workforce is scheduled on certain days and weeks. From this, managers can then tactically decide if they require more/less staff. While able to be used for any SME, it is expected to be especially useful to SMEs which incorporate and heavily rely on shift work, such as bars, restauraunts, supermarkets, shops, cafes, warehouses and courier services.  

The full [My-Roster-Management](https://my-roster-management.herokuapp.com/) programme can be accessed here.

# UX design
## Color scheme
The color scheme chosen for this programme is based on a simple color scheme of blue, white and various shades of orange. Colors are used rather sparingly in the programme so as to portray a more professional and non-distracting aesthetic. Whilst it may be beneficial to create eye-catching designs in certain projects (Such as a website landing page) it was concluded that ease-of-use and practicality was of more importance in this specific project.  
Bootstrap is used in the programme so as to easily and efficiently style the various template HTML files. There is also a custom styles.css file to allow for custom styling amongst bootstrap's default files, such as the the brand color of orange used in the logo and hover effects on the buttons. 

## Layout
The grid feature in bootstrap was used to easily and efficiently provide a responsive layout for the website. Bootstraps grid system is based and built from the CSS flexbox feature. This layout was chosen for a number of reasons. Using the grid feature within Bootstrap, elements within the project can very easily be manipulated, hidden, unhidden, swapped, replaced or repositioned in the future if needed. This is especially handy when working on a layout for smaller devices, as certain elements which are not deemed necessary can be hidden if needed, and be prevented from taking up excess space on smaller screens. Furthermore, the very nature of Bootstraps grid is based on a mobile-first design, which easily allows the project to be built responsively and work on devices of all sizes.


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
The programme offers a very simple and easy to use navigation system to navigate around the programme. This is not only in the form of moving to different pages, but also for features such as a contact modal and large buttons under each relevant table to manipulate the user's database. The navbar will look slightly different depending on wether the user is logged in as an admin-user, a non-admin user, or logged out.
#### **Images**  
##### **Logged in as Admin**
![navigation bar logged in as admin](static/images/navigation-bar-logged-in-as-admin.png "navigation bar logged in as admin")
##### **Logged in as non-Admin**
![navigation bar logged in as non-admin](static/images/navigation-bar-logged-in-as-non-admin.png "navigation bar logged in as non-admin")
##### **Logged out**
![navigation bar logged out](static/images/navigation-bar-logged-out.png "navigation bar logged out")

##### **Table buttons**
![table navigation buttons](static/images/navigation-buttons.png "table navigation buttons")

### Contact us modal
Should users experience any difficulty in using the software, there is a "Contact" modal which can be accessed on the navigation bar. This allows the user to contact the company via phone or email, and also offers means of contacting the company through social media pages.
#### **Images**  
![contact modal](static/images/contact-modal.png "contact modal")

### Footer
An attractive footer is included in the programme to offer the user a simple way of easily navigating to the social media pages of the company.
#### **Images**  
![footer](static/images/footer.png "footer")

### CRUD (Create, Read, Update, Delete) functionality
On each table outlining the companies current records of employees, roles and scheduled workshifts, there are buttons which allow an authorized user to manipulate these records. For example, an authorized user may add a new employee and delete the replaced employee, and edit any details about the new employee if they wish.
#### **Images**  
##### **CRUD functionality on table**
![crud functionality displayed on employee table](static/images/crud-functionality-employee-table.png "crud functionality displayed on employee table")
##### **Adding record form**
![adding record to table form](static/images/crud-functionality-add-employee-form.png "adding record to table form")
##### **Editing record form**
![editing record on table form](static/images/crud-functionality-edit-employee-form.png "editing record on table form")

### Account creation and login/logout functionality
The superuser will have the ability to create accounts for users, and will also have the ability to use CRUD functionality on the company's data. When creating a user, the superuser will also have the ability to grant these same permissions to the new user. This will prevent unauthorised users from editing/creating/deleting records, and also prevent them from registering other users.  

Registered users can then log into the programme using their username and password, and will have different permissions depending on wether they are authorized or not.  
#### **Images**  
##### **Account registration form**
![register user form](static/images/register-user-form.png "register user form")

##### **Signin form**
![signin form](static/images/signin-form.png "signin form")

##### **Signout confirmation**
![signout confirmation](static/images/signout-confirmation.png "signout confirmation")

### User permissions
As mentioned above, the programme is designed so that only authorised users can use CRUD functionality and create new users. Therefore, it is important that unauthorised users of the programme can access the information they need to gain benefit from the programme, but cannot see more personal details of the company, such as wages and employee phone numbers etc. and cannot use CRUD functionality on records. To solve this problem, all edit/delete/add buttons on each table have been hidden to unauthorised users. Furthermore, attempting to brute-force to certain URLs when logged in as an unauthorised user will simply return an `unauthorised.html` page and block the user from accessing CRUD functionality. This includes the `accounts/signup/` URL should an unauthorised user attempt to create a new user, as this could easily allow the programme to be hacked. When logged in as an unauthorised user, certain columns of certain tables are also hidden to prevent PPI (Private and Personal Information) from being accessed.
#### **Images**  

##### **Unauthorized user view of table**
![Unauthorized user view of table](static/images/unauthorized-user-view-of-employee-table.png "Unauthorized user view of table")

##### **Unauthorized message if brute-forcing a URL is attempted**
![Unauthorized message if attempting to brute-force a URL](static/images/unauthorized-view-from-brute-forcing-url.png "Unauthorized message if attempting to brute-force a URL")

### Form validation
When adding or editing a company record, a form which contains incorrect or invalid data will be displayed back and an error message will be displayed to the user. This will let the user know why the form didn't submit correctly and allow them to easily correct their mistake before commiting the data to the database, thereby aiding in preventing invalid data being saved.  
#### **Images**  
![form validation type 1](static/images/form-validation-type-1.png "form validation type 1")
![form validation type 2](static/images/form-validation-type-2.png "form validation type 2")

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

# Testing and bugs
For all testing, please refer to the [TESTING.md](TESTING.md) file.

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
  - [Django](https://www.djangoproject.com/) - The Django framework for python was used to build many of the web development aspects of the programme, including user authentication and content administration, and also allowed the use of ORM to manipulate the database.
  - [PostgreSQL](https://www.postgresql.org/) - PostgreSQL was used as an Object-relational database system in the project, and through ORM (Object-relational mapping) records were able to be Created, Read, Updated and Deleted (CRUD) from the PostgreSQL database.
  - [WhiteNoise](http://whitenoise.evans.io/en/stable/) - WhiteNoise was used as a means to allow the project to serve its own static files, as this is not possible with Django.
  - [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) - The django-allauth package was used to create the authentication, account registration and account management within the programme.
  - [Psycopg2](https://pypi.org/project/psycopg2/) - Psycopg2 was used as an adaptor for PostgreSQL, to ensure that it will work and integrate with Python and Django.
  - [Gunicorn](https://gunicorn.org/) - Gunicorn was used for the WSGI HTTP server for the project
  - [Django-phonenumber-field](https://pypi.org/project/django-phonenumber-field/) - Django-phonenumber-field was used to for simple authentication and validation of phone numbers stored within models and used within forms throughout the programme.

# Deployment
The live deployed application can be found at [My-Roster-Management](https://my-roster-management.herokuapp.com/).

## Local Deployment
*Gitpod* IDE was used to write the code for this project.
​
To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/my-roster-management.git`  
​
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.  
​
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/my-roster-management)

### Heroku Deployment
​This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
​
Deployment steps are as follows, after account setup:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
​
Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile
​
You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`
​
The Procfile can be created with the following command: `echo web: node index.js > Procfile`
​
For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`
​
The frontend terminal should now be connected and deployed to Heroku.

# Credits
## Content
The sources below were used when trying to solve intricate problems within the programme and played a solid role in helping me to build this project.
  - [W3schools](https://www.w3schools.com/) was used as a learning resource to learn more about various python functions and concepts, and also assisted in learning about the intricacies of Django and the Jinja templating language.
  - The [Django documentation](https://docs.djangoproject.com/en/4.1/) was extremely helpful in solving problems, as it allowed me to research in detail about the various features and capabilities that Django has to offer.  
  - Corey Schafer's [Youtube channel](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) was instrumental in assisting me when working with python and Django, and allowed me to fully utilise the technologies in my programme.
  - [Stack Overflow](https://stackoverflow.com/) was used as a learning resource and helped me with any questions I had whilst building the project. It was also used to look through existing questions asked by users who had similar problems/issues to those which were faced when building this project.

## Acknowledgements
I want to thank the following people and companies for their help in providing solid technical support whilst developing this project.
  - Tim Nelson (Code Institute mentor).
  - [Code Institute](https://codeinstitute.net/ie/).