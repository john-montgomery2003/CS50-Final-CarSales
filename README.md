Capstone
===

This is a project for CS50's web programming with Python and JS. This is the 5th (and final) project of the new 2020 course.

The site - [Car](https://car.johnmontgomery.tech)

A youtube video showing the pages - [Video]()

The requirements and brief - [Docs](https://cs50.harvard.edu/web/2020/projects/final/capstone/)

Harvard's CS50 course site - [Website](https://cs50.harvard.edu/web/2020/)

Specification
------

There was very little in terms of spec for this site, with it being a project open to the student. I decided to create a car sales site (with links to the bridging work I was set for my a-level bridging work) The site is in some ways similar to commerce, but uses JS when for display and sending certain elements, including posting the messages on the contact form.

The site is designed as a webpage for a small site and is not meant for a large scale trading and sales site (like autotrader) rather its geared to a more localised shop.

I also implemented googles 'map' functionality on the contact page although at the minute this points to Australia, it can easily be manipulated to point to the business, All pages are also mobile responsive, and are designed to be usable on most devices.

I decided that, in order to look nice as well as providing functionality I would only use 1 search box, at first I thought I would attempt to create this algorithm myself, however Django's own built in 'search' worked very well for this job, and so I decided to use that instead. This allows the user to search through the variety of cars.

The car model also holds extra metadata that wasn't necessarily needed for the model (sold date, salesman, etc) but this would allow, if wanted in the future, for a better analysis on the data.
