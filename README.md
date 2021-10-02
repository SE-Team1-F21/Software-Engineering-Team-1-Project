# Software-Engineering-Team-1-Project

## Team Members and their roles
1. Jose Martinez - Free
1. Carson Reed - Front-end
1. Diego Castro - Front-end
1. Alex Mercado - Back-end
1. Steve Liang - Back-end



# Sprint I
### Front-end
Splash screen and player menu implementation, where each (for now) is contained within two html files.
>splash.html for splash

>game.html for game menu

Not final. Feel free to add more files if you need to. Just providing a base line

These files are contained within the "templates" folder. This is necessary for communicating with flask for the backend

The form "submit" button in `splash.html` should generate the `game.html` page.

### Instructions for running Flask
1. Install flask if it's not already installed 
   ```
   pip3 install Flask
   ```
2. Terminal commands for getting flask to run
   ```
   export FLASK_APP=main
   flask run
   ```
   



### Back-end

##### Storing Data
1. Receive input from frontend
1. Flask processing data and pass to **psycopg2**
1. Store in database

##### Fetching Data
1. Using Python library **psycopg2** to fetch data from database
1. Store fetched data into list
1. Pass data in Flask and rendering data to frontend





