# Jingle Bites
# JavaScript Group Hackathon Project <a id="top"/>
![logo](static/images/logo-4-+.png)


## Introduction
The present website was done as part of the December Hackathon organised by Code Institute (CI) in 2024.
The initial idea for the group project was to do a site to show recipes to the users and allow them to also input their recipes on the site.
The group Jingle Bites is composed of 7 students and alumini from different courses by CI, with different members working in different areas that they feel more comfortable/knowledgeable.

## Table of Contents
- [User Experience Design](#user-experience-design)
- [Project Brief](#project-brief)
- [Users](#users)
- [Project Plan](#project-plan)
- [User Stories](#user-stories)
- [Wireframes](#wireframes)
- [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Website Features](#website-features)
    - [Homepage](#homepage)
    - [Categories Page](#categories-page)
    - [Results Page](#results-page)
    - [Single Javascript Makes Multiple Pages](#single-javascript-makes-multiple-pages)
    - [Footer](#footer)
- [Responsive Design](#responsive-design)
- [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
- [Credits](#credits)
    - [Code References](code-references)
    - [Use of AI](use-of-ai)
    - [Content References](content-references)
    - [Media References](media-references)
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

[Back to top](#top)

### Wireframes
Initial layout of website in different devices:

- Mobile view:<br>
  <img src="static/images/Wireframe-mobile-view.png">
  
- Tablet view:<br>
  <img src="static/images/Wireframe-tablet-view.png">
  
- Desktop/Laptop view:<br>
  <img src="static/images/Wireframe-desktop-homepage1.png">
  <img src="static/images/Wireframe-desktop-about1.png">
  <img src="static/images/Wireframe-desktop-recipe1.png">

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

### Typography

For the body section of the webpage, font-family used was: "Poppins", sans-serif. Example of Poppins font [Google Fonts](https://fonts.google.com/specimen/Poppins?preview.text=Jingle%20Bites)<br>
<img src="static/images/Jingle-Bites-poppins.png">

For the Logo, font-family used was: "Brush Script MT", cursive. Example of "Brush Script MT" font from [Microsoft](https://learn.microsoft.com/en-us/typography/font-list/brush-script-mt)
<img src="static/images/brush-script.png">

For the Title, font-family was: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif. Style example of "Segoe UI" from [Microsoft](https://learn.microsoft.com/en-us/typography/font-list/segoe-ui) 
<img src="static/images/segoe-ui.png">

### Imagery
- B image<br>
  <img src="">

[Back to top](#top)

## Website Features
### Homepage
  <img src="static/images/homepage-final.png">

### About
  <img src="static/images/Homepage-about-1.png">
  <img src="static/images/Homepage-about-2.png">

### Recipes
  <img src="static/images/recipes-1.png">
  <img src="static/images/recipes-2.png">

### Register
  <img src="static/images/signup.png">

### Login
  <img src="static/images/login.png">


[Back to top](#top)

## Responsive Design
Most of the content is responsive to different screen sizes as it was built using components from the Bootstrap Library.
![amiresponsive](https:/)

## Future Features
- Print or Save Recipes as PDF
- Admin Moderation and Management
- Filter Recipes bu Dietary Preferences
- Search Recipes by Ingredient or Keyword
- Share Recipes on Social Media

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

The process is as follows:
1. Login to your GitHub profile.
2. Go to the [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template).
3. Click **Use this template** and then **Create a new repository**.
4. Enter the repo name and choose to create from template
5. Click **Open** with the Gitpod logo to open the Code Institute IDE workspace.
6. Open VS Code locally and click on Gitpod logo on the left. Click on right arrow next to the workspace you want to work on.
 
Once the MVP has been created in Gitpod, go to GitHub Pages to make an early deployment of the project, so that testing can be done in Dev Tools to highlight key issues that need to be resolve early on in the project.

[Back to top](#top)

## Testing
Validation of HTML/CSS, Lighthouse Audits.

### HTML Validation
- Used [W3C Markup Validation Service](https://validator.w3.org/#validate_by_uri) to test the HTML on all webpages and updated as needed. No errors found after fixing.
![HTML_validation](static/images/HTML-validation.png)

### CSS Validation

- Used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) to test CSS style and no errors found.
![CSS_validation](static/images/base-css-validation.png)


### Lighthouse Audit
- Used Chrome Dev Tools Lighthouse to audit the site for response time and accessibility. <br>
<img src="static/images/Homepage-lighthouse-performance.png">
<img src="static/images/about-lighthouse-performance.png">
<img src="static/images/recipes-lighthouse-performance.png">
<img src="static/images/recipe-lighthouse-performance.png">
<img src="static/images/signup-lighthouse-performance.png">
<img src="static/images/Homepage-lighthouse-performance.png">
<img src="static/images/login-lighthouse-performance.png">


### Bugs yet to be Fixed
- So

[Back to top](#top)

## Credits
### Code References
Many of th
<br>
Other re

### Use of AI
#### Code Generation
The GitHub Copilot extension was installed in our local versions of Visual Studio Code.

#### Debugging
Copilot was used for debugging code.

#### Code Optimisation
When coding more complicated logical 

#### Impact on Workflow
On the 

### Content References


### Media References


### Acknowledgements
Eve

[Back to top](#top)
