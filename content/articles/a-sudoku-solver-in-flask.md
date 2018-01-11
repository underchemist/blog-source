Title: A sudoku solver in Flask
Tags: python
Modified: 2018-01-10 17:43
Date: 2017-11-05
Summary: I wrote a small flask app hosted on Heroku using old code I had written a few years ago.
Status: published

# The idea
I've always wanted to learn how to use [Flask]('http://flask.pocoo.org/docs/0.12/') properly. I've never gotten through a flask tutorial that has an example app, so I decided to adapt a [sudoku solving library]('https://github.com/underchemist/sudopy') I made quite awhile ago. Although I tried being super smart when I wrote this and tried to implement a version of Donald Knuth's [dancing links]('https://en.wikipedia.org/wiki/Dancing_Links') I ended up only writing a backtracking algorithm. I figured this is still good enough to solve most inputs within a couple of seconds and that's fine for my purposes.

# Result
I learned a lot about HTML, CSS, bootstrap, and even jquery. It's 2017 but for a long time I thought I was too high brow for web development and never bothered to learn it (Recently dropping out of my graduate degree has made me rethink some things).

[![https://gyazo.com/3a651c8d3caea847cc792da48f0475d5](https://i.gyazo.com/3a651c8d3caea847cc792da48f0475d5.png)](https://gyazo.com/3a651c8d3caea847cc792da48f0475d5)

This is look so far of the app.

Starting out I didn't really know how to make anything look nice so I actually went to the site for [2048](https://gabrielecirulli.github.io/2048/) and copied a lot of the CSS and HTML structure.
Like as in the sudoku grid cells are just smaller and have different padding rules to be 9x9 instead of 4x4. At this point nothing was functional on the site, there weren't even any buttons, it was literally just a title and non-functional sudoku grid.

I learned a bit more about forms and also added bootstrap templating so buttons didn't look terrible. Then I had to figure out how send data through forms to run it through my solver and spit it back out through another rendered template. I wasn't sure how all the input boxes in my form would come together through a ```request.form``` call, but after some testing the response was a ```Dict``` with the keys being the name attribute of the ```<input>``` tags in the form element and the values the whatever was in the input cells. With a bit of massaging it was easy to convert this into something readable by sudopy.

At this point I wanted to add convenience functionality, so I had to learn some javascript/jquery. To input a puzzle you had to click one of the squares, tab to the next one, and so on until you tabbed 9 * 9 = 81 times. I wanted to add the ability to paste specially formatted strings directly into the puzzle grid, have the input cursor auto-focus to the next square, and clear any inputs from the grid.

[![https://gyazo.com/eab89821a22161aa92bb295c972934df](https://i.gyazo.com/eab89821a22161aa92bb295c972934df.gif)](https://gyazo.com/eab89821a22161aa92bb295c972934df)

[![https://gyazo.com/0eb1568cbfcd9cbb9083cf366da307d8](https://i.gyazo.com/0eb1568cbfcd9cbb9083cf366da307d8.gif)](https://gyazo.com/0eb1568cbfcd9cbb9083cf366da307d8)

[![https://gyazo.com/884cd67fca8bbafdb7af26b01ba91782](https://i.gyazo.com/884cd67fca8bbafdb7af26b01ba91782.gif)](https://gyazo.com/884cd67fca8bbafdb7af26b01ba91782)

The hardest thing to learn was that in order for the scripts to run properly they required all the DOM elements to be loaded first. It took me so long to figure out I need to wrap my functions in ```document.ready``` calls.

Adding a footer was a little challenging for me, but mainly because I don't know how to match colors. I ended up on purple because it seemed good to me but I can see how it might not be for everyone. Testing how the site looked at this point on my desktop and laptop made my realize somethings were broken on a smaller screen. I had to fiddle a lot with the CSS and create some new div class containers but I think now it works all right.

The final touch was adding a fade in animation with css and keyframes. I wanted to do for page loads but I ended up just doing it for the solved puzzle text and back button on page load. Since everything else in the page is pretty static it works quite well. That's it, the final project app file structure is down below.

```
/
│   .gitattributes
│   .gitignore
│   environment.yml
│   Flask-sudoku-app.sublime-project
│   Flask-sudoku-app.sublime-workspace
│   local_config.py
│   Procfile
│   README.md
│   requirements.txt
│   run.py
│
├───app
│   │   sudopy.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───static
│   │       bootstrap-social.css
│   │       clear.js
│   │       favicon.ico
│   │       mappaste.js
│   │       nextinput.js
│   │       styles.css
│   │
│   ├───templates
│   │       base.html
│   │       index.html
│   │       solution.html
│   │
│   └───__pycache__
│           sudopy.cpython-36.pyc
│           views.cpython-36.pyc
│           __init__.cpython-36.pyc
│
└───__pycache__
        local_config.cpython-36.pyc
```

[You can try it out for yourself!](http://sudoku-solver.herokuapp.com/)