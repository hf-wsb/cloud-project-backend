## cloud-project-backend

Open terminal 
Create the project folder locally
    - Create a folder for the project called ```cloud-project-backend``` and check if it is present in the working folder

            mkdir cloud-project-backend 

   - ```cd``` into this folder

            cd cloud-project-backend

   - Open the project folder '''cloud-project-backend''' from the menu in VS Code

### Create a virtual environment for the project

- Create a ```.py``` python file into ```cloud-project-backend``` and ```cd``` into it

        echo >> main.py

- Create a virtual environment called ```venv_name```

    The command below will create a new folder called ```venv_name```

        python -m venv venv

### Activate the new virtual environment ```venv```

In cmd terminal type:

    .\venv\Scripts\activate

### Create requirements.txt
        echo >> requirements.txt

### Record the dependencies for the project

- First, update the ```pip``` library

        python -m pip install --upgrade pip

- Then, create the dependencies file named ```requirements.txt```

        pip list > requirements.txt

---

Finally, our environement is ready and we can application using command "python3 main.py"