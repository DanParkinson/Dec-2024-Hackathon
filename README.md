# Jingle Bites
# Code Institute "December 2024 - HackTeam Takeover!" <a id="top"/>

<img src="static/images/responsive-design.png"><br>
[Jingle Bites](https://jingle-bites-28089fd21e29.herokuapp.com/)

## Introduction
The present website was done as part of the December Hackathon organised by Code Institute (CI) in 2024.
The initial idea for the group project was to do a site to show recipes to the users and allow them to also input their recipes on the site.
The group Jingle Bites was composed of 6 elements, including current students and alumini from different courses by CI.

## Table of Contents
- [User Experience Design](#user-experience-design)
- [Project Brief](#project-brief)
- [Users](#users)
- [Project Plan](#project-plan)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Logo](#logo)
    - [Typography](#typography)
- [Website Features](#website-features)
    - [Homepage](#homepage)
    - [About](#about)
    - [Recipes](#recipes)
    - [Recipe](#recipe)
    - [Register](#register)
    - [Login](#login)
- [Responsive Design](#responsive-design)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)
    - [Use of AI](use-of-ai)
    - [Acknowledgements](acknowledgements)

[Back to top](#top)

## User Experience Design
A user-centred approach has been taken through the inception, design and development of this site.
Checking layouts and colours, and ultimatelly basing the website in an existing website layout, with smooth colours and appealing design.
The site was coded, with attention to the responsiveness in different screens.

### Project Brief
The project goal is to provide different Christmas recipes to users, allowing them to add their own recipes and as well as to choose their favourite recipes that they can see/review later.

The site user's goals for the site are to get information about different Christmas recipes, as the ingredients, preparation and time that takes to prepare it.
Also being able share their recipes with other users.

### Users
In order to fully understand our users needs, we asked Microsoft Co-pilot to draw up some user personas based on our project brief. We refined the prompts and after three tries and some refinement afterwards, here are the personas we used:

- Persona 1: "Emily Johnson is a 32-year-old teacher from Leeds"<br>
  She loves discovering new Christmas dessert recipes to make for her family and friends during the holiday season.<br>
  Emily wants a website where she can easily find and save her favorite recipes to try later. She also enjoys sharing her own baking creations with the community.<br>
  However, she often gets frustrated with hard-to-follow recipe instructions and the lack of ratings and reviews to gauge the quality of the recipes.<br>
  Emily appreciates detailed recipe instructions, the ability to save favorite recipes, and the option to share recipes on social media.<br>
  She values easy-to-use search functionality and high-quality images for each recipe to help her decide what to make.

- Persona 2: "Michael Williams is a 45-year-old software engineer living in Brighton"<br>
  Michael follows a vegetarian diet and is always on the lookout for new vegetarian Christmas recipes.<br>
  He likes to post and share his main course recipes with the community and enjoys engaging with other users by commenting and rating recipes.<br>
  Michael sometimes finds it difficult to find recipes that suit his dietary preferences and wishes there were more interaction opportunities within the community.<br>
  His favorite features include the ability to filter recipes by dietary preferences, post and manage his own recipes, and comment and rate other recipes.<br>
  Michael also appreciates receiving notifications for recipe interactions and having access to analytics to track the popularity of his recipes.

- Persona 3: "Sarah Smith is a 28-year-old digital marketer from Cardiff"<br>
  She often hosts Christmas parties and is always on the hunt for quick and easy appetizer recipes.
  Sarah wants a website where she can save and organize her favorite recipes in her profile. She also enjoys personalizing her account by adding a profile photo and bio.<br>
  Sarah sometimes feels overwhelmed by the sheer number of recipes available without proper organization and wishes there were more ways to filter recipes by cooking time.<br>
  Her favorite features include browsing recipes by category, personalizing her user profile with a photo and bio, and saving and organizing favorite recipes.<br>
  Additionally, Sarah values the ability to filter recipes by cooking time and having easy-to-read formats for recipe instructions.

[Back to top](#top)

## Project Plan
Initially the group got together when the team was known after the first webinar. A repository was created and colaborators were adeed to allow different members to create their branches and work locally, as necessary.
After this, different the repo, a project board was also created on GitHubOn the planning day, the draft user stories were derived with the help of MS Co-pilot, which provided a sufficient and relevant user stories including the acceptance criteria and tasks required for each user story. Some adjustments had to be made, as the scope of some of the user stories didn't fit into the project timeframe

### User Stories
Here are all the user stories that have been prioritised (all must have and some should have ones) for the current implementation of the site:
| User Stories                                    | MoSCoW priority           |  Status  |
| ----------------------------------------------- |:-------------------------:| --------:|
| Post own recipes                                | must have                 |   Done   |
| Edit and Delete Recipes                         | should have               |   Done   |
| User Profile with Photo and Bio                 | could have                |   Done   |
| Browse Recipes by Category                      | must have                 |   Done   |
| Save Favourite Recipes                          | should have               |   Done   |
| User-Friendly Navigation                        | must have                 |   Done   |
| Appealing and Simple Design                     | must have                 |   Done   |
| Responsive Design                               | must have                 |   Done   |
| Share Recipes on Social Media                   | could have                | Not Done |
| Search Recipes by Ingredient or Keyword         | could have                | Not Done |
| Filter Recipes by Dietary Preferences           | could have                | Not Done |
| Rate and Review Recipes                         | could have                | Not Done |
| Admin Moderation and Management                 | could have                | Not Done |
| Print or Save Recipes as PDF                    | could have                | Not Done |


All user stories were logged on the [GitHub Project Board](https://github.com/users/Francisca-Heii/projects/7) on GitHub repo, along with the assessment criteria and expected performance for the Hackathon, which were also prioritised as must-have, should-have and could-have.

As well as using the Project Board to track progress on our project, we also used it during testing to log any significant bugs that need to be fixed before the project deadline. These were then assigned and prioritised alongside other issues and user stories.

<img src="static/images/jingle-bites-project-board.png">

[Back to top](#top)

### Wireframes
Initial layout of website in different devices:

- Mobile view:<br>
  <img src="static/images/Wireframe-mobile-view.png">
  
- Tablet view:<br>
  <img src="static/images/Wireframe-tablet-view.png">
  
- Desktop/Laptop view:<br>
  <img src="static/images/desktop-wireframe1.png">
  <img src="static/images/desktop-wireframe2.png">


[Back to top](#top)

## Design
### Colour Scheme
This site was based on [PinchOfFun](https://pinchofyum.com/) website by suggestion of a team member and after discussion within the group.

- Colour Palette <br>
  Done using [coolors](https://coolors.co/)<br>

  <img src="static/images/coloor-palette.png">

- Contrast check <br>
  Contrast was checked using [WebAIM](https://webaim.org/resources/contrastchecker/)<br>
  
  <img src="static/images/contrast-check1.png">
  <img src="static/images/contrast-check2.png">
  <img src="static/images/contrast-check3.png">

### Logo
![logo](static/images/logo-4-+.png)<br>

[Back to top](#top)

### Typography
For the body section of the webpage, font-family used was: "Poppins", sans-serif. Example of Poppins font [Google Fonts](https://fonts.google.com/specimen/Poppins?preview.text=Jingle%20Bites)<br>
<img src="static/images/Jingle-Bites-poppins.png">

For the Logo, font-family used was: "Brush Script MT", cursive. Example of "Brush Script MT" font from [Microsoft](https://learn.microsoft.com/en-us/typography/font-list/brush-script-mt)
<img src="static/images/brush-script.png">

For the Title, font-family was: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif. Style example of "Segoe UI" from [Microsoft](https://learn.microsoft.com/en-us/typography/font-list/segoe-ui) 
<img src="static/images/segoe-ui.png">

[Back to top](#top)

## Website Features

### Common Features/Links to all pages
- Nav bar has "Home", "About" and "Recipes" links on the left side that take user to this pages.
- These links are also available on the footer, to give another option for the user to quickly move to a different page of the website.
- On the right side of the Navbar the user can choose to "Register" on the site and create his/her account to post their own recipes and share them with other users.
- The "Login" link allows the user to access the account previously created.
- Access to Social Networks

### Homepage
  <img src="static/images/homepage-final.png"><br>
- In this page the user can choose one of the 4 main categories "Starter, "Main", "Side" or Dessert" to see different recipes according to each category.
- Also has some recomended recipes below the categories which will get the user to their description once selected.

### About
  <img src="static/images/Homepage-about-1.png"><br>
  <img src="static/images/Homepage-about-2.png"><br>
- Information about the page.

### Recipes
  <img src="static/images/recipes-1.png"><br>
  <img src="static/images/recipes-2.png"><br>
- Has a option menu "All Categories" that allows the user to choose from the categories mentioned above on the homepage and search for recipes.
- Different recipes are available that the user can open by selecting/clicking in the area of the specific recipe, which slightly pops out to provide a visual output to the user that is ready to go to another page.

### Recipe
  <img src="static/images/recipe-1.png"><br>
  <img src="static/images/recipe-2.png"><br>
- Description of the recipe selected: title, brief description, ingredients, how to prepare the recipe and how many users liked the recipe.

### Register
  <img src="static/images/signup.png"><br>
- Requests different details to the user to create a personal account.

### Login
  <img src="static/images/login.png"><br>
- Allows the user to access the account created.

[Back to top](#top)

## Responsive Design
Respomsive Desgin of the content was built using components from the Bootstrap Library and CSS Media queries.

## Future Features
- Print or Save Recipes as PDF
- Admin Moderation and Management
- Filter Recipes bu Dietary Preferences
- Search Recipes by Ingredient or Keyword
- Share Recipes on Social Media

[Back to top](#top)

## Technologies Used
### Languages and Technologies
![Static Badge](https://img.shields.io/badge/HTML5-Language-blue)
![Static Badge](https://img.shields.io/badge/CSS3-Language-blue)
![Static Badge](https://img.shields.io/badge/GitHub-RepoHosting-black)
![Static Badge](https://img.shields.io/badge/Gitpod-IDE-yellow)
![Static Badge](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/JavaScript-323330?style=flat&logo=javascript&logoColor=F7DF1E)

### Libraries
![Static Badge](https://img.shields.io/badge/FontAwesome-icons-navy)
![Static Badge](https://img.shields.io/badge/GoogleFonts-Typography-blue)

### Tools and Programs
![Static Badge](https://img.shields.io/badge/Favicon.io-icons-navy)
![Static Badge](https://img.shields.io/badge/Balsamiq-Wireframes-green)
![Static Badge](https://img.shields.io/badge/MSCopilot-AI-orange)
![Static Badge](https://img.shields.io/badge/GitHubCopilot-AI-orange)

### Frameworks
![Static Badge](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Static Badge](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![Static Badge](static/images/cloudinary-squareLogo.webp)

### DataBases
![Static Badge](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)


[Back to top](#top)

## Deployment

Heroku deployment process:
- This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:
- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set your environment variables.
  - | Key | Value |
  - | --- | --- |
  - | `AWS_ACCESS_KEY_ID` | user's own value |
  - | `AWS_SECRET_ACCESS_KEY` | user's own value |
  - | `DATABASE_URL` | user's own value |
  - | `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
  - | `EMAIL_HOST_PASS` | user's own value |
  - | `EMAIL_HOST_USER` | user's own value |
  - | `SECRET_KEY` | user's own value |
  - | `STRIPE_PUBLIC_KEY` | user's own value |
  - | `STRIPE_SECRET_KEY` | user's own value |
  - | `STRIPE_WH_SECRET` | user's own value |
  - | `USE_AWS` | True |
- Heroku needs three additional files in order to deploy properly.
  - requirements.txt
  - Procfile
  - runtime.txt
  - You can install this project's requirements (where applicable) using:
  - pip3 install -r requirements.txt
- If you have your own packages that have been installed, then the requirements file needs updated using:
  - pip3 freeze --local > requirements.txt
- The Procfile can be created with the following command:
  - echo web: gunicorn app_name.wsgi > Procfile
  - replace app_name with the name of your primary Django app name; the folder where settings.py is located
- The runtime.txt file needs to know which Python version you're using:
  - type: python3 --version in the terminal.
  - in the runtime.txt file, add your Python version:
    - python-3.9.19
- For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:
- Either:
  - Select Automatic Deployment from the Heroku app.
- Or:
  - In the Terminal/CLI, connect to Heroku using this command: heroku login -i
  - Set the remote for Heroku: heroku git:remote -a app_name (replace app_name with your app name)
  - After performing the standard Git add, commit, and push to GitHub, you can now type:
    - git push heroku main
- The project should now be connected and deployed to Heroku!

[Back to top](#top)

## Testing
Validation of HTML/CSS, Lighthouse Audits.

### HTML Validation
- Used [W3C Markup Validation Service](https://validator.w3.org/#validate_by_uri) to test the HTML on all webpages and updated as needed. No errors found after fixing.
![HTML_validation](static/images/HTML-validation.png)

### CSS Validation

- Used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) to test CSS style and no errors found.
![CSS_validation](static/images/base-css-validation.png)

[Back to top](#top)

### Lighthouse Audit
- Used Chrome Dev Tools Lighthouse to audit the site for response time and accessibility. <br>
<img src="static/images/Homepage-lighthouse-performance.png">
<img src="static/images/about-lighthouse-performance.png">
<img src="static/images/recipes-lighthouse-performance.png">
<img src="static/images/recipe-lighthouse-performance.png">
<img src="static/images/signup-lighthouse-performance.png">
<img src="static/images/Homepage-lighthouse-performance.png">
<img src="static/images/login-lighthouse-performance.png">

### Python Testing
- No errors shown while testing and the automatically generated migrations don’t require any changes. <br>
<img src="static/images/python-test.png">

[Back to top](#top)

## Credits
### Use of AI
#### Code Generation
The GitHub Copilot extension was installed in our local versions of Visual Studio Code. 

#### Debugging
Copilot was used for debugging code. EIther while using VS Code or when using Dev Tools and searching about errors.

### Acknowledgements
The team has communicated very well and different members had regular huddles to check about progress of the project, as well as when needed to check code or to resolve conflicts on the code or trying to merge changes to main repo.
Different members were able to work in different parts, but also to help eachother with common tasks as needed/requested.
There was a good cooperation in the team to get the site well done, which could be seen from the initial moment.

[Back to top](#top)
