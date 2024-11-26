# tic tac toe game

to use packages in repositories, we need to list these as a dependency because it might not be installed in all systems or it might be shared for the laptop

**pip freeze** to check laptop packages 

One solution is creating a virtual environment and installing packages here.
1. **python -m venv venv** - create a virtual environment 
2. **source venv/bin/activate** - activate this virtual environment 
3. **pip freeze** - check existing packages, there should be none
4. **pip install numpy** - install numpy 
5. **pip freeze** - check the packages, should be the latest numpy version 
6. **pip freeze > requirements.txt** - redirect output into a file for other users of the code to understand what version of the package to install 
7. **pip install...** - to add more to this requirements.txt file 


When committing this into github, do not upload the virtual environment
1. add a file called **'.gitignore'**
2. write 'venv' into '.gitignore'
3. **git status** - check that 'venv' folder is not there 
4. **git add --all** - add all or specific files to be committed 
5. **git commit -m 'message'** - add commit message
6. - **git push origin main** - push commit

To ensure you have all the packages as the previous developer:
**pip install -r requirements.txt**