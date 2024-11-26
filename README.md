# tic tac toe game

check laptop packages 
- **pip freeze**

to use packages in repositories, we need to list these as a dependency because it might not be installed in all systems or it might be shared for the laptop

One solution is creating a virtual environment and installing packages here.
1. create a virtual environment 
   - **python -m venv venv**
2. activate this virtual environment 
   - **source venv/bin/activate**
3. check the packages, should be none 
   - **pip freeze**
4. install numpy 
   - pip install numpy
5. check the packages, should be the latest numpy version 
   - **pip freeze**

6. redirect output into a file for other users of the code to understand what version of the package to install 
   - **pip freeze > requirements.txt**
7. to add more to this requirements.txt file
   - **pip install...**



to commit this into github, 
do not upload the virtual environment into github
1. add a file called **'.gitignore'**
2. write 'venv' into '.gitignore'
4. check that 'venv' folder is not there 
   - **git status**
5. add all files to be committed 
   - **git add --all**
6. add commit message
   - **git commit -m 'message'**
7. push commit
   - **git push origin main**
