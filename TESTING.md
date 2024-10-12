

[<< Back to ReadMe](README.md)

## Manual Tests
Manual testing occurred regularly throughout local development. Tests are documented below.

### index
|Test #|Test|Results|Evidence|
| --- | --- | --- | --- |
|1|Nav bar shortens when screen size is smaller|Pass|The nav has a toggle when on smaller screens<br>
![nav](media/readme-media/testing/NavDesktop.png)<br>
![nav small](media/readme-media/testing/NavMobile.png) |
|2|Login/ Sign up button disappears when user is logged in|Pass| the button on the index page disappears when the user is logged in and shows up if the user has not been authenticated<br>
![login ](media/readme-media/testing/NavDesktop.png)<br>
![mp login](media/readme-media/testing/LogInLink.png) |

### Login
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1| login form has the correct validation|Pass| a user must fully enter all details corretly before logging in|

![login](media/readme-media/features/LogInForm.png)
![login error](media/readme-media/features/IncorrectLoginMessage.png)

### Signup
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1| signup form has the correct validation|Pass| a user must fully enter all details corretly before signing up|

![signup](media/readme-media/features/SignUpForm.png)

### My Account
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1| my account form has the correct validation|Pass| a user must fully enter all details corretly before the form is submitted|

![my account](media/readme-media/features/MyAccountForm.png)

### Create Booking
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1|create booking form has the correct validation|Pass| a user must fully enter all details corretly before the booking is created|
|2|users cannot double book on sessions|Pass| days which are already booked are greyed out and not bookable|

![create booking](media/readme-media/features/CreateBookingForm.png)
![create booking greyed](media/readme-media/features/CreateBookingDateGreyed.png)

### Your Bookings
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1|As a user, I can see my bookings, at any stage (rejected, accepted etc)|Pass| a user can see all bookings|
|2|As a user, they can edit or delete their bookings|Pass| next to their booking info is links for editing or deleting bookings|
|3|As a employee, they can accept, reject and mark bookings as completed|Pass| next to the booking info is the option to reject or accept. Once accepeted they can mark as completed|
|4|As a admin, see all bookings and also edit or delete these|Pass| all bookings are visible and editing and viewing is possible|

![your booking](media/readme-media/features/YourBookingSection.png)
![employee booking](media/readme-media/features/EmployeeBookings.png)
![your booking](media/readme-media/features/AdminYourBooking.png)

### Edit Booking
|Test #|Test|Results|Evidence|
| --- | --- | --- |--- |
|1|When editing a booking, prebooked days are greyed out|Pass| booked days are greyed out|

![edit booking](media/readme-media/features/EditBookingForm.png)
![edit booking greyed](media/readme-media/features/EditBookingDateGreyed.png)

## User Story Testing

[Project Stories](https://github.com/users/Brad-Hammond/projects/2)

[User story 1]([#1](https://github.com/users/Brad-Hammond/projects/2/views/1?pane=issue&itemId=80907031&issue=Brad-Hammond%7CHammond-Hustle%7C1)) - I know I am done with the 'As a site user I can sign up and log in so that i can make an account on the site' user story when as a user i can signup and login on the site - PASS


