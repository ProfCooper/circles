# Introduction to unit testing in GitHub Classroom

## Overview

In this session, we will learn about workflows for unit testing by doing some hands-on examples to get a feel for how this works.  In our examples, we are using a workflow to automatically perform unit testing on python scripts and to check that they conform to the `flake8` style guide.

The session is broken into two parts:

1. Edit a python script to ensure it passes all the unit tests.
1. Add new unit tests and amend your python script to pass those also.

Getting workflows and unit testing right can be fiddly, but it is incredibly powerful and is an important aspect of programming and software development.

## Part I: fixing a script

In this repository you will find:

- this `README.md` file;
- a `sources` folder containing the python script `circle.py`, which contains user-defined functions that must pass specific tests;
- a `tests` folder containing the python script `test_circle.py`, which specifies the unit tests that `circle.py` must pass.

Your repository will *fail* the unit tests.  You can see what happened when the tests were triggered by navigating to the `Actions` menu.  There you will see a list of instances when the repository workflow was triggered - find the most recent one and click through the tests to try to understand why the workflow run failed.

Assuming you haven't changed anything in your branch, you should find that the `codestyle` test was passed, but that the `unittests` test was failed.  This is because the function `circumference` in `sources/circle.py` doesn't compute the correct answer.

#### Exercise 1
1. Edit the `circumference` function in `sources/circle.py` so that the workflow run passes.

## Part II: adding new unit tests

The unit tests for `sources/circle.py` are specified in the `tests/test_circle.py` file.  Currently it contains two tests, clustered into a single series.

Suppose we want the user to create an `area` function, which takes the radius as a variable `radius` and optionally takes the number of decimal places required as a variable `dp` with default value of 3.  It should return the area of the circle with specified radius to the required number of decimal places.

#### Exercise 2
1. Amend the `test_circle.py` file to include a second series of (at least two) tests, designed to check if the user-defined `area` function works correctly.
1. After you have specified the unit tests for the `area` function, edit the `sources/circle.py` script to define an `area` function that passes your unit tests.
1. Ensure that the workflow run passes - note that you may have introduced style violations, which you should correct based on the feedback from the `codestyle` test in the workflow.
