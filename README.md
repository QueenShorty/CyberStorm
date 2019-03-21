# CyberStorm
Here is where all our code for assignments and challenges will be posted

# Git Setup

1. Download git bash [here](https://git-scm.com/download/win)
2. Copy this [link](https://github.com/QueenShorty/CyberStorm.git)
3. open git bash - It should open once finished installing 
4. Nagivate to desired locaiton in git bash
    a. Use command cd "file name"
    b. If unsure where you are you can use dir command
5. Run command: git clone https://github.com/QueenShortyCyberStorm.git
6. This command pulls the most updated code down into the file you selected, naming it CyberStorm. 

## Git Commands

### git pull
- Pulls all the updated code and including new branches 
### git push
To push all your new changes
### git status
allows you to see which files have changes, need to be commited
### git add .
adds all files with changes to stagging - make sure to check the status so your not commiting files you don't need to
### git commit -m "message"
Permanently stores your changes from staging to the repository
### git checkout "branch name"
allows you to checkout a branch to work in
### git branch "new_branch_name"
commands creates a new branch. Make sure to be in master before running this command
### git branch 
tells you which branc your on
### git merge "branch_name"
merges branch_name into current branch. always merge master branch into current branch before pusing to new branch to master
### git push --set-upstream "name" master
when you create a new branch you need to push to origin

## Branch Structure
I have created a branch called WorkingInProgress - this is where we will be working on all our assingments and challenges. 

Once our assingments/challenges have been completed and working we will merge changes into master

There also will be a branch for each person on the team - these branches are only for that user to push their indivudual assignments too.

## File Structure
In side of WorkingInProgess will be two folders - Assignments and Challengs. 

Option - we can also create a folder for the files or task 

In your own branch you may create your folders how you like.

## Naming Conventions
Inside of Assignmenst and Challengs folder which are located in Branch WorkingInProgess, each file will be named with the title of the homework or doucments needed to complete the homework/assignments