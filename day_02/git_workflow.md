Git has a “more-than-one-way-to-do-it” philosophy.  So, most Git projects adopt a particular workflow and a set of practices to keep things moving smoothly.  For our Data Science Boot Camp, we are going to do the following.

### Summary:
  1. Individual work (on challenge sets) will live in branches:  *first-steps*, *eda-and-reg*, and *sup-learning*
  2. Pair programming work will live on branch:  *pairs*
  3. Project work will live outside of your class repository
  4. For each of your personal branches (not the group project), you’ll submit a PR for that branch. So, you’ll have PRs for first-steps, eda-and-reg, sup-learning, and pairs.  Then, whenever you push to one of those branches, the PR will show us your most recent set of work.
  5. When you create the branch:  
    1. *git push --set-upstream origin <branchname>*
    2. Open a PR for that branch (then we can see your work as you push it)

### For Individual Work
There’s an introductory git assignment and it tells you exactly what to do.  Follow those directions.

There are two large individual assignments, one in week one and one in week two.  Each of these assignments will get their own branch.
  * For week one, when you start working on the *Exploratory Data Analysis and Regression* jupyter notebook:
    * save, add, and commit any in-progress work you want to keep
    * switch to the master branch (*git checkout master*)
    * make sure your repo is up-to-date (*git pull*)
    * *git checkout -b eda-and-reg*
    * make a copy of the template notebook in the *day_02 directory*:  *EDA and Regression Challenges YourName.ipynb*
    * make one commit (or more, if needed) for each challenge you complete
      * Complete a challenge, save the notebook, add it to the index (if necessary), and commit
    * To return to the branch later, save and commit any in-progress work and then *git checkout eda-and-reg*

  * For week two, when you start working on the *Supervised Learning* jupyter notebook, you will:
    * save, add, and commit any in-progress work you want to keep
    * switch to the master branch (*git checkout master*)
    * make sure your repo is up-to-date (*git pull*)
    * *git checkout -b sup-learning*
    * make a copy of the template notebook in the *day_06*: *Supervised Learning Challenges YourName.ipynb*
    * make at least one commit for each challenge you complete
      * Complete a challenge, save the notebook, add it to the index (if necessary), and commit
    * To return to the branch later, save and commit any in-progress work and then git checkout sup-learning

### For Pair Programming
You will also be doing pair programming work, as warm-ups and to broaden your Python chops, in the mornings.  All of this work should be on the same branch.  When you have made a good solution to the pair challenge (a .py file) with your partner:
  * For the first pair program, create a branch for your pair challenges:
    * save, add, and commit any in-progress work you want to keep
    * switch to the master branch and update your repo
    * *git checkout -b pairs*
    * Copy/move your solution to the repo, add it to the index, and commit it
  * Later, when you already have the pairs branch created:
    * save, add, and commit any in-progress work you want to keep
    * switch to the master branch and update your repo
    * *git checkout pairs*
    * Copy/move your solution to the repo, add it to the index, and commit it

### For Group Projects
Your group may use whatever git workflow you find most convenient.  However, we have one constraint:  do not use any member’s class repo as the project git repo.  Instead, create a new github project (either public or internally), and then fork+clone or clone it to give individual members access to the master project repo.
