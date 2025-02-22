# Hammond Hustle!

![Device View](media/readme-media/deviceview/DeviceViewImage.png)

Click the link to view the live app [Hammond Hustle](https://hammond-hustle-6962877d2ab9.herokuapp.com/)

Achieve your fitness goals by unlocking your true potential!

Welcome to Hammond Hustle, the go-to fitness site for individuals committed to their health and wellness. Built on the powerful Django framework, this app allows you to book personalized training sessions with our expert trainers, tailored to meet your fitness goals. Users can create profiles, track bookings, and stay organized with an easy-to-use scheduling system. Whether you’re just starting out or looking to elevate your performance, Hammond Hustle offers the guidance and expertise you need to succeed. Join today to train with our specialists and take the next step in your fitness journey.

***

## Contents


## Project Aims
- Provide a platform for users to book personalized training sessions with expert trainers.

- Allow users to manage bookings after the booking has been completed.

- Offer a visually appealing and user-friendly interface that makes navigation seamless and booking sessions straightforward.

- Ensure the app's scalability, allowing it to accommodate a growing number of users, trainers, and bookings over time.

- Offer robust security features to protect user data, ensuring compliance with privacy regulations and providing a safe user experience.

- Continuously improve the app through regular updates, feature enhancements, and bug fixes based on user feedback.

Overall, the goal of Hammond Hustle is to offer an accessible, professional booking system for fitness enthusiasts to connect with specialist trainers and make consistent progress toward their health and fitness goals.

## How to use it

Here are the steps to use **Hammond Hustle**:

1. Create an account: To get started, you will need to create an account by entering your email address, and password.

2. Update your profile: After creating an account, you can update your profile information, with personal information, such as your name, to help others get to know you better.

3. Make a booking: navitage to the make a 'Make a Booking' screen where you can enter your details, chose your coach and get booked in for a session.

4. Edit a booking: navigate to the your bookings screen, if you want to change the date or time of a booking or even cancel the booking altogether, you can do so in here.

With these steps, you should be able to easily use **Hammond Hustle** to find, create and edit bookings.

## User Stories & Epics
All user stories were entered as issues in a GitHub Kanban project follow the link to see the project:
[Project Link](https://github.com/users/Brad-Hammond/projects/2)

### Epic: Booking: The ability for users to create and manage their own bookings, including updating the date if needed.
- [3]- As a user I can book and manage sessions so that I can tailor them to my needs
- [9] - As a User I can edit the date and time of a booking to better suit my needs

### Epic: Prebooked Days: The ability for users to not be able to book prebooked days.
- [6]- As a user I can see if a session time has already been booked so that I do not double book a time with a coach

### Epic: Employee View: The ability for employees to manage / approve users bookings.
- [7]- As a employee I can see my own bookings so that I do not see my colleagues bookings
- [10]- As a employee I can mark a booking as completed so that the employee knows the booking is completed
- [4]- As a employee I can accept or reject user bookings so that I can fit the booking in with other clients

### Epic: Login and Singup: The ability for users to login and signup.
- [1]- As a site user I can sign up and log in so that i can make an account on the site

### Epic: Admin View: The ability for admins to have all levels of access.
- [2]- As a admin I can access all other levels of access so that I can check on the site overall

### Epic: Good UX Practice: The ability for users to stay on the same browser across the site.
- [8]- As a user I can stay on the same browser tab across the site so that I do not get confused of being on a different browser

### Incomplete User Stories for future developement
- [5]- As a employee I can leave feedback on a users session so that they can improve for next time

## Design
### ERD
![ERD](media/readme-media/erd/ERDImage.png)


### Wireframes
#### Index / Homepage
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileBaseHTML.png" alt="Index M Screen">
</details>

Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopBaseHTML.png" alt="Index D Screen">
</details>

#### Login
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileLoginHTML.png" alt="Login M Screen">
</details>
Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopLoginHTML.png" alt="Login D Screen">
</details>

#### Signup
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileSignupHTML.png" alt="Signup M Screen">
</details>
Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopSignupHTML.png" alt="Signup D Screen">
</details>

#### Your Booking
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileYourBookingsHTML.png" alt="Your Booking M Screen">
</details>
Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopYourBookingHTML.png" alt="Your Booking D Screen">
</details>

#### My Account
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileMyAccountHTML.png" alt="My Account M Screen">
</details>
Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopMyAccountHTML.png" alt="My Account D Screen">
</details>

#### Create Booking
Mobile
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/mobile/MobileCreateBookingHTML.png" alt="Create Booking M Screen">
</details>
Desktop
<details>
<summary>Click to view</summary>
<img src="media/readme-media/wireframes/desktop/DesktopCreateBookingHTML.png" alt="Create Booking D Screen">
</details>

### Navigation / Flow Plan
![Navigation Plan](media/readme-media/erd/FlowImage.png)

## Features
### Existing Features
Below are the main features of Hammond Hustle.

### Users

#### Base
##### NavBar
- The company name is visible on all nav bar sizes.
- The nav bar has a toggle feature on smaller devices.
- When a user is logged in, the nav features different links for authenticated users only.

![nav 1](media/readme-media/features/NavNotLoggedIn.png)
![nav 2](media/readme-media/features/NavLoggedIn.png)
![nav 3](media/readme-media/features/NavToggleFeat.png)

##### Hero Image / Button
- At the top of the base/index page, there is a make a booking button.
- If not logged in, this redirects the user to the login page.

![Hero Button](media/readme-media/features/HeroImageWithButton.png)

##### Trainer Section
- The trainer section includes images of the trainers.
- On desktop, they also have a hover animation.
- The nav link correctly links to this section on all files.

![Trainers](media/readme-media/features/TeamSection.png)

##### About Section
- The about section includes a small paragraph about the company.
- The nav link correctly links to this section on all files.

![About Section](media/readme-media/features/AboutSection.png)

#### Signup / Login
##### Signup
- The signup form informs the user of what data each input field requires.
- If the user is an employee, they can enter their employee code here.
- If the user enters incorrect details or misses a section, it pops up with an error message.

![singup form](media/readme-media/features/SignUpForm.png)
![error message](media/readme-media/features/PleaseFillMessage.png)

##### Login
- The login form requires correct username and password.
- If incorrect details are entered, a message appears and the user must retry.

![login form](media/readme-media/features/LogInForm.png)
![login error message](media/readme-media/features/IncorrectLoginMessage.png)

#### Bookings
##### Create Booking Form
- The create booking includes numerous input fields for the user to fill.
- All data fields must be filled otherwise the same error message with the signup form will appear.
- The DOB and Session date and time use a calender picker to make it easier for users.
- When a user choses a time with a specific coach, if that day is already booked - it will be greyed out on the calender.
- Bookings with coaches last all day so you cannot have multiple times on one day per coach.

![create booking](media/readme-media/features/CreateBookingForm.png)
![create date greyed](media/readme-media/features/CreateBookingDateGreyed.png)

##### Your Bookings
- The your booking screen has all bookings for that user.
- The status will be pending until a coach (employee) approves it.
- Once a booking is approved, the status changes from pending to approved.

![Your Booking](media/readme-media/features/YourBookingSection.png)

##### Edit Booking
- The edit booking screen allows the user to edit a booking which has already been booked.
- Like the create booking form, the dates are greyed out with already booked sessions.

![edit booking](media/readme-media/features/EditBookingForm.png)
![edit date greyed](media/readme-media/features/EditBookingDateGreyed.png)

#### Account
##### My Account
- The my account section allows users to update their personal info.
- Again, if not filled out correctly or a datafield is missing info, an error mesage will appear.

![my account](media/readme-media/features/MyAccountForm.png)

### Employee

##### Your Booking
- On the 'Your Bookings' screen for employees, their view is similar.
- However, on theirs they can see users who want to book with them.
- Employees can reject, approve, and once approved they can mark as completed.

![employee booking](media/readme-media/features/EmployeeBookings.png)

### Admin

##### Your Booking
- As the admin, they can see all bookings, apprvoed, completed or rejected.
- They also have the option to delete or edit these.

![admin booking](media/readme-media/features/AdminYourBooking.png)


### Future Features
#### Leave and View Feedback
- This was a feature which I wanted to implement however it fell out of scope due to time constraints.
- This feature would allow employees to leave feedback on the session for users and then users could view this feedback.

#### Coach Videos
- This feature would have a section on the page of coaches going over some basic tips and tricks.
- Due to time constraints I could not implement this feature but it will be added in the future.

#### Profile Pictures
- This feature would allow users to upload a profile picture to the site.
- Due to time constraints, I could not implement this feature, but it will be added in the future.

***

## Technologies Used

- HTML5
- CSS3
- Python
- Javascript
- django-allauth
- django-crispy-forms
- Postgre

## Testing

A separate testing document has been created as [TESTING.md](TESTING.md)

### Fixed Bugs

#### Date Picker Disabling Booked Dates Incorrectly
- The date picker in the booking form was not correctly disabling previously booked dates.
- To fix this, I modified the JavaScript code to parse booked_times_json correctly and used the disable option in flatpickr to prevent users from selecting already-booked dates:

```javascript
const bookedTimes = JSON.parse("{{ booked_times_json|escapejs }}");
flatpickr("#session_time", {
    enableTime: true,
    dateFormat: "Y-m-dTH:i",
    altInput: true,
    altFormat: "F j, Y h:i K",
    minDate: "today",
    disable: bookedTimes.map((date) => date)
});
```

#### JavaScript Toggle Menu Not Working on Smaller Screens
- The navigation menu toggle button (☰) was not functioning on mobile screens.
- To fix this I added the toggleMenu function to each relevant template (e.g., base.html and manage_bookings.html) to ensure that the toggle functionality was available across different pages:

```javascript
<script>
    function toggleMenu() {
        const menu = document.getElementById("nav-menu");
        menu.classList.toggle("active");
    }
</script>
```

## Important Note // Please Read
- The secret key has been regenerated and put in my env.py file which is hidded.
- The secret key in earlier deployment is no longer valid as it has been regenerated.
- I have regenerated the secret key twice, so the key in earlier deployement and commits is no longer in use.
- I used [Djecrety](https://djecrety.ir/) to generate my new secret keys.
- All employee logins have been made so this cannot be done again - however I have supplied all of their login details when submitting.

## Deployment
### Cloning & Forking
#### Fork
1. On GitHub.com, navigate to the [Brad-Hammond/Hammond-Hustle](https://github.com/Brad-Hammond/Hammond-Hustle/tree/main) repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/)
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [Brad-Hammond/Hammond-Hustle](https://github.com/Brad-Hammond/Hammond-Hustle/tree/main) repository.
4. Above the list of files click the button that says 'Gitpod'.
5. Once open you will need to install the libraries, you can do this by typing "pip3 install -r requirements.txt" into the terminal
6. Open the .env file in the project directory and change the key pair values to match your credentials.

### Remote Deployment 
1. Log in to Heroku
2. Click 'Create new app'.
3. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
4. You can use an external databAse for example postgre or use 'Heroku Postgres' under the Add-ons section.
5. Go to settings section and click 'Reveal Config Vars' in the Config vars section.
6. Add ALLOWED_HOSTS and the value as the name of you project with '.herokuapp.com' appended to the end.
7. Add CLOUDINARY_URL and the value as your cloudinary API key.
8. Add EMAIL_HOST_PASSWORD and the value as the password for the email service.
9. Add EMAIL_HOST_USER and the value as the the email address for the email service.
10. Add SECRET_KEY and the value as a complex string which will be used to provide cryptographic signing.
11. Add DATABASE_URL if you are using a different database than Heroku Postgres.
12. Navigate to the 'Deploy' page
13. Select 'GitHub' from the 'Deployment method' section
14. Enter your github account details and select the forked/ clone repository.
15. Select 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
16. Once built, click the 'View' button to load the URL.

### Database
A Postgres database has been used for this project, provided by ElephantSQL.

1. Open your web browser and go to the [ElephantSQL](https://www.elephantsql.com/) website.
2. Sign up for a free account or log in if you already have an account.
3. Once you have logged in, you will be taken to the Dashboard. From here, click on the "Create New Instance" button.
4. You will now be taken to a page where you can configure your new database instance. Choose the "Tiny Turtle" plan which is free.
5. Select the region where you want to host your database. The closest region to you is usually the best choice.
6. Choose a name for your instance, this will be the name of your database.
7. Choose a username and password for your instance.
8. Click on the "Create" button to create your new database instance.
1. The database url was stored in a config var: 'DATABASE_URL' on Heroku. This variable was then used in the settings.py to connect to the database.
10. Click on the "Details" tab to view your instance details.
11. Look for the "URI" field, which contains the connection details you need to connect to your database. The URI should start with: 'postgres://'

he models were migrated to the database by entering the following commands in the the gitpod terminal:

python3 manage.py makemigrations
python3 manage.py migrate

The live link can be found here - [Hammond Hustle](https://hammond-hustle-6962877d2ab9.herokuapp.com/)

## Credits
- Credits to [Device Frames](https://deviceframes.com/) for the different devices image in the ReadMe
- HTML, CSS and Javascript code help was taken from w3schools - [W3Schools](https://www.w3schools.com/)
- Django Documentation - [Django](https://docs.djangoproject.com/en/4.1/)
- Credits to [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI%2B-%2BUK%2B-%2BSearch%2B-%2BBrand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=635720257674&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjw8pKxBhD_ARIsAPrG45kfZu0iDMkC26LnD1BA9bVqqhFchKG1Ib_SZOD-r7-C87RpU2b6i1EaAsbWEALw_wcB&nab=2&utm_referrer=https%3A%2F%2Fwww.google.com%2F) for the learning matertial
- Credits to [Wireframe](https://wireframe.cc/) for the mock wireframes images
- Credits to my mentor for pushing and helping me through this project
- Credits to Flatpicker for the date picker used
- For all images used, credits to [Pexels](https://www.pexels.com/)