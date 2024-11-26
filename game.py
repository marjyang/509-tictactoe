import numpy as np

# check laptop packages - pip freeze
# need to list numpy as a dependency because it might not be installed in all systems or it might be shared for the laptop
# there are two ways to do so
# 1. create a virtual environment 
#    - python -m venv venv
# 2. activate this virtual environment 
#    - source venv/bin/activate
# 3. check the packages, should be none 
#    - pip freeze
# 4. install numpy 
#    - pip install numpy
# 5. check the packages, should be the latest numpy version 
#    - pip freeze

# 6. redirect output into a file for other users of the code to understand what version of the package to install 
#    - pip freeze > requirements.txt
# 7. to add more to this requirements.txt file

user_move = input("please enter your move as x,y coordinates.")
print(f"you entered: {user_move}")


# to commit this into github, 
# git add ---
# git status
# do not upload the virtual environment into github