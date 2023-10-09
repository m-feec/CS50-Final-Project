# CS50-Final-Project

CS50 Project
Silver Guide
Video Demo: https://www.youtube.com/watch?v=BxJLpRFGWts
Description: 
Work: I have created every item needed for the flask framework: app.py, forum.db, helpers.py, static dictionary with CSS file, JavaScript and pictures dictionary, templates dictionary with all HTML. app.py - I used the same libraries that we used in pset9 (without the os one) because of my work based on finance logic. I have created the first route to the index page. layout.html- before I moved on to the index page I created a layout HTML with a navbar. navbar- I tried some of the Bootstrap navbars but to gain better knowledge of front-end work I tried to create a responsive navbar that can be easily manipulated anytime. I started with W3school with the CSS Navigation Bar section. From there I moved to YouTube. I have watched the Kevin Powell "Responsive navbar tutorial". Learned about "span" I thought about the burger navbar on mobile. That's why I watched the Web Dev Simplified "Responsive Navbar tutorial", which included information about how to use span to create a burger icon, and how to toggle active after the user clicks on the mobile app (plus cool CSS look). index.html - The main concept was about showing information while the user is scrolling down the page. The first information I searched comes from a Youtube channel named Beyond Fireship. The author used IntersectionObserver in JavaScript. To get a better understanding of this example I watched and learned more from Web Dev Simplified's video named "Learn Intersection Observer In 15 min". After that, I get back to the knowledge Beyond Fireship showed me in his video named "Subtle, yet Beautiful Scroll Animations". Both videos used display: grid; so I dived into W3school.com to get a proper understanding of this feature. At this moment I can create on scroll page with an Intersection observer and place it nicely in the middle with a grid display. Now I wanted to create nice-looking cards to show pieces of information to the users. I search for a long time to find inspiration and find out the Online Tutorials Youtube channel with the "Real Glassmorphism Card Hover Effects" video. I really liked the concept and I have created my own version of this card for my project. I wanted 3 cards in a row so I created a new CSS section with display flex. Moving down I wanted to have an animated chart. After researching and trying to animate one with chart.js I give up and move forward. The page ended up with a normal picture of the chart. Down Below I created one last card with a new CSS class for new content. big6.html - Moving to the next page I have created a new route in app.py and a new HTML page. There is also a title section (the same one I created on the index page with a different bg picture). In the second part of the page, we have two sections with 3 cards in the row (so display: flex). I wanted to show information when the user hovers over the card. I learned this from Kevin Powell's Youtube channel exactly from "CSS Card with hover animation and mobile fallback video". I also learned more about transitions in CSS from this video and from the Beyond Fireship's channel (also to get a better understanding I read the W3schools information about transition and animation!). The author show also a solution for a mobile phone but I had a different concept for this one so I searched for Touch event in JavaScript. After watching Web Dev Simplified's video named "Learn JavaScript Touch Events in 17 minutes" I knew what to do! forum.db- I wanted to create a page for users to chat with each other. Like in discord. I needed a new database in sqlite3 one for users to log in and the second for comments. I wanted to show who write a comment and when he did that. The first table is a shorter version of the one we used in the problem set 9 the second table have date and time, comments user_id, and needed to be GRPUP BY datetime(). I did it later in the app.py app.py forum page- I used the same login_required from pset 9 to type comments in the forum section. Also in the same route for login and register. The new route is the forum one. When the user type comment we go through POST and we want to insert this comment into the table with the date and time. When we go through GET we send all comments with authors and time to HTML forum.html- a simple 2-section page with a form to type comments and a second to display comments. about.html- Simple page to post every creator who teaches me a new skill. Most of my work in CSS was just working out many concepts I had in my head. If something looks nice to me I lived it in the final product. Thank You CS50 It was a great journey together. I will continue learning to program all because of This amazing course!
About

