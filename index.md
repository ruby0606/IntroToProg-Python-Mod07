# Assignment 7: Pickling data and Exception Handling 

## Introduction
In this document, I wrote down the steps I took to create a script to display a menu to the user, request user to choose a menu option, add “Name” and “ID” lists, store lists as a pickle, unpickle and read data from binary files. I watched the videos from Module 7, reviewed the list of other exceptions from the web, and read the seventh chapter from the book “Python Programming for Absolute Beginners”. I encountered some challenges in pickling and reading from the file but was able to resolve them and also added some exceptions.

## Step 1: Load Data and display menu
I displayed a menu with four options to the user. I requested the user to add “names” and “ids” in two lists.

## Step 2: Pickle data
Pickling means to preserve your piece of data in the format you stored. I saved each list (names and ids) as a pickle onto a binary file called “Appdata”. 

## Step 3: Unpickle data	
When user selects this action, data is read from the selected file, the lists are unpickled and displayed back to the user.

## Step 4: Exception handling
I created four exception handling cases: 
1.	When user enters a menu choice that is not in the integer format
2.	When user enters “ID” that is not in the integer format
3.	When user tries to open a file that does not exist
4.	When user messes up the pickled binary file and tries to unpickle the information
Step 5: Exit program
When user selects this action, a message is displayed to the user and they exit from the program

## Step 6: Results in pyCharm
Results in PyCharm showing the user performing each of the actions succesfully:
 
Fig 1.1: Screenshot of the result in Pycharm 
 
Fig 1.2 Screenshot of the exceptions in Pycharm
 
1.3 Screenshot of the unpickling exception in PyCharm

## Step 7: Results in Terminal
Results in Terminal displaying all user actions 
 
Fig 2: Screenshot of the result in Terminal 

## Step 8: Github link
https://github.com/ruby0606/IntroToProg-Python-Mod07

Summary
I started with a basic trial file where I defined my list data in the program instead of requesting user to add information. I then attempted pickling/unpickling actions and verified how the information looks. Once I was able to complete this properly, I went onto requesting data from user and performing these actions and dealing with exceptions. It was challenging to ensure all actions could be completed successfully and to ensure that errors were caught gracefully. 

















<Editing notes>

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/ruby0606/IntroToProg-Python-Mod07/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

# This is a sample web page for this assignment

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ruby0606/IntroToProg-Python-Mod06/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
