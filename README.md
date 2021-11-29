# Brainworks

## Project 5 - E-Commerce Applications
<img src="#">

The aim of this project was to build a Full-Stack site based on business logic used to control a centrally-owned dataset. This includes setting up an authentication mechanism and providing the ability to make purchases.

Brainworks sells brain teasers, puzzles and logic games to the general public. They cater for all age groups and have a wide variety to choose from. There is also a fun brainteaser section for users to test their brain power.

The live site can be found <a href="" target="_blank" rel="noopener">here</a>. (Note: Right click on link to open a new tab).

# Table of Contents
1. [UX](https://github.com/Michelle3334/brainworks#ux)
    * [Website owner goals](https://github.com/Michelle3334/brainworks#website-owner-business-goals)
    * [User stories](https://github.com/Michelle3334/brainworks#user-stories)
    * [Wireframes](https://github.com/Michelle3334/brainworks#wireframes)
    * [Design](https://github.com/Michelle3334/brainworks#design)
2. [Features](https://github.com/Michelle3334/brainworks#features)
3. [Database Schema](https://github.com/Michelle3334/brainworks#database-schema)
4. [Technologies Used](https://github.com/Michelle3334/brainworks#technologies-used)
5. [Testing](https://github.com/Michelle3334/brainworks#testing)
    * [Functionality testing](https://github.com/Michelle3334/brainworks#functionality-testing)
    * [Code Validation](https://github.com/Michelle3334/brainworks#code-validation)
    * [Compatibility testing](https://github.com/Michelle3334/brainworks#compatibility-testing)
    * [Performance testing](https://github.com/Michelle3334/brainworks#performance-testing)
    * [User stories testing](https://github.com/Michelle3334/brainworks#user-stories-testing)
    * [Bugs](https://github.com/Michelle3334/brainworks#bugs)
6. [Deployment](https://github.com/Michelle3334/brainworks#deployment)
7. [Credits](https://github.com/Michelle3334/brainworks#credits)
8. [Acknowledgments](https://github.com/Michelle3334/brainworks#acknowledgements)

# UX
## Website owner business goals
* I would like to be able to add a product to the store.
* I would like to be able to delete a product from the store.
* I would like to be able to edit a product.

## User Stories
### New user goals:
* I would like to be able to view the products.
* I would like to view information about individual products.
* I would like to be able to register for an account.
* I would like email confirmation after registering for an account.
* I would like to be able to get in contact with the website owner.
### Returning user goals:
* I would like to be able to login or logout.
* I would like to be able to recover my lost password.
* I would like to have a personalised profile to view order history and amend my details.
* I would like to be able to sort or filter products.
* I would like to be able to search for a product.
I would like to be able to select and adjust a quantity of an item to purchase.
* I would like to view the items in my shopping cart.
* I would like to view the order confirmation after checking out.
* I would like to receive an email confirmation after placing an order.

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

## Wireframes
I used Balsamiq to create the wireframes.

### Desktop view
* Home page 
<img src="media/home_desktop.PNG" >

* Contact
<img src="media/contact_desktop.PNG">

* Products
<img src="media/products_desktop.PNG">

* Product detail
<img src="media/item_desktop.PNG">

* Brainteasers:
<img src="media/teasers_desktop.PNG">

* Sign In
<img src="media/signin_desktop.PNG">

* Register
<img src="media/register_desktop.PNG">

* Profile
<img src="media/profile_desktop.PNG">

* Cart
<img src="media/cart_desktop.PNG">

* Checkout
<img src="media/checkout_desktop.PNG">

### Mobile view
* Home page
<img src="media/home_mobile.PNG">

* Contact 
<img src="media/contact_mobile.PNG">

* Products
<img src="media/products_mobile.PNG">

* Product detail
<img src="media/item_mobile.PNG">

* Brainteasers:
<img src="media/teasers_mobile.PNG">

* Sign In
<img src="media/signin_mobile.PNG">

* Register
<img src="media/register_mobile.PNG">

* Profile
<img src="media/profile_mobile.PNG">

* Cart
<img src="media/cart_mobile.PNG">

* Checkout
<img src="media/checkout_mobile.PNG">

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

## Design
### Colors
The main colors used in this project:
* Background color: 
* Font color: 

### Fonts
Sans-Serif is used as the backup font. 

### Images
Images were sourced from 

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

# Features
## Existing Features
### Navigation Bar
   
    
### Products
   



### Contact
   * This page invites the user to submit comments or suggestions to help improve the website.
   * On submission of the form the user is provided with a confirmation message.
   * The information provided is sent to an active gmail account. 


### Profile page
    
* If the user is logged in they are able to view and update their profile.


## Future features
* 

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

# Database Schema
### User Profile model
* Django's user and admin model was utilised, with some modifications for the user profile display and update.
<img src="media/dbm_userprofile.PNG">

### Products app
<img src="media/dbm_products.PNG">
<img src="media/dbm_categories.PNG">

### Cart app
<img src="media/dbm_order.PNG">
<img src="media/dbm_items.PNG">


# Technologies Used:
### Programming Languages:
* CSS, HTML, Javascript, Python and Django.
### Database framework
* Postgres.
### Git
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
### Github
* GitHub was used to store the projects code after being pushed from Git.
### Bootstrap 5
* Bootstrap was used to for design and to make the website responsive.
### Balsamiq
* Balsamiq was used to create the wireframes during the design process.

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

# Testing
## Functionality Testing
### Manual testing
* I used Google Chrome developer tools throughout the development process for testing and solving problems with style and display issues.
* I used Github Project and Issues to track tasks. After each task completion, I would fully test it before moving on to the next task.
* All links were tested multiple times during the development process and again once the project was completed to ensure that all pages were linked correctly.
* All Forms and form elements were tested to ensure that they work as they should, with user feedback on errors as well as user feedback on successful submission.

### Django testing framework

* The majority of the view, models and forms were tested using the unit testing functionality in Django, these tests can be viewed in the <code>test_forms.py</code>, <code>test_views.py</code> and <code>test_models.py</code> files in the various apps. The remainder were tested manually during the functional testing both during development and after completion.

    <img src="#">
    
* **Home app**

    <img src="#">

* **Products app**

    <img src="#">

* **Cart app**

    <img src="#">

* **Checkout app**

    <img src="#">

* **Profiles app**

    <img src="#">

## Code Validation
**1. CSS Validation using <a href="https://jigsaw.w3.org/css-validator/#validate_by_input" target="_blank" rel="noopener">W3C CSS Validator Services</a>.**


<img src="#">

**2. <a href="http://pep8online.com/">PEP8</a> was used to test the Python code**



**3. <a href="https://beautifytools.com/javascript-validator.php">Beautify Tools</a> was used to test the Javascript snippets.**



[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

## Compatibility Testing
* The website was tested on Google Chrome, and Samsung cellphones.
* The website was viewed on a variety of device sizes such as Desktop, Samsung S10, Samsung tablet and Iphone 11, I also used the responsive function when inspecting the pages to view various sizes. 

## Performance testing
I ran the Lighthouse tool to check performance of the website. 
Screenshots of the final test are presented below:
* Desktop
    * Home page
    <img src="#">
    
    * Gallery
    <img src="#">
    
    * About page
    <img src="#">

* Mobile
    * Home page
    <img src="#">
    
    * Gallery
    <img src="#">
    
    * About page
    <img src="#">

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

## User Stories testing

### New user goals
1. I would like to be able to view the products.
2. I would like to view information about individual products.
3. I would like to be able to register for an account.
4. I would like email confirmation after registering for an account.
5. I would like to be able to get in contact with the website owner.

### Returning user goals:
1. I would like to be able to login or logout.
2. I would like to be able to recover my lost password.
3. I would like to have a personalised profile to view order history and amend my details.
4. I would like to be able to sort or filter products.
5. I would like to be able to search for a product.
6. would like to be able to select and adjust a quantity of an item to purchase.
7. I would like to view the items in my shopping cart.
8. I would like to view the order confirmation after checking out.
9. I would like to receive an email confirmation after placing an order.

### As a website owner:
1. I would like to be able to add a product to the store.
2. I would like to be able to delete a product from the store.
3. I would like to be able to edit a product.

## Bugs


[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

# Deployment
The project was deployed to GitHub Pages using the following steps, I used Gitpod as a development environment where I commited all changes to git version control system. I used the push command in Gitpod to save changes into GitHub.

### Deployment to Heroku
Before creating a Heroku app make sure your project has these two files:

* requirements.txt - You can create one by using <code>pip3 freeze > requirements.txt</code>
* Procfile - You can create one by using echo web: <code>python run.py > Procfile</code>

### Create application:

1. Navigate to Heroku's site <a href="https://id.heroku.com/login" target="_blank" rel="noopener">here</a>. (Note: Right click on link to open a new tab).
2. Register and/or Login as applicable.
3. Click on the new button in the top right and select "Create new app".
4. Enter the app name and region closest to you.
5. Click the create app button.

### Set environment variables:

1. Click on the settings tab and then click "Reveal config vars".

2. Config variables added throughout project:
(add image of variables)

### Setting up database in deployment

1. Temporarily add the <code>DATABASE_URL</code> to <code>settings.py</code>:

    <code>DATABASES = {
'default': dj_database_url.parse('your_postgres_database_url')
}</code>

2. Migrate the data from development to production version.

    * To migrate the database models in the project to the Postgres database you can use the following command:

    <code>python3 manage.py migrate</code>

3. You will then need a superuser for the Postgres database too. To create one you can use the following command:

    <code>python3 manage.py createsuperuser</code>

4. Remove the Postgres database URL from settings.py as this should not in any case be deployed to GitHub for security reasons.

6. To connect your Heroku app to be deployed from a Github repository, you can follow these steps:

    * Open the heroku app page on the deploy tab and select GitHub - Connect to GitHub.
    * Sign into GitHub if not already.
    * A prompt to find a Github repository to connect to will then be displayed.
    * Enter the repository name for the project and click search.
    * Once the repository has been found, click the connect button.
6. Once you have your GitHub repository connected, without leaving deploy tab:

    * Under Automatic deploys section, choose the branch you want to deploy from and then click the "Enable Automatic Deploys" button.
    * To deploy your app to Heroku click the "Deploy Branch" button.

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)

# Credits
## Code
* 

## Content
* 

## Media
* 

## Acknowledgements
* My mentor for support, advice and feedback.
* The students on Slack for peer review and comments.
* Code Institute Tutor support for help with coding issues.
* My family and friends for their support, feedback and testing.

[Back to Table of Contents](https://github.com/Michelle3334/brainworks#table-of-contents)