## cloud-project-backend

Open terminal 
Create the project folder locally
    - Create a folder for the project called ```cloud-project-backend``` and check if it is present in the working folder

            mkdir cloud-project-backend 

   - ```cd``` into this folder

            cd cloud-project-backend

   - Open the project folder '''cloud-project-backend''' from the menu in VS Code

### Create a virtual environment for the project

- Firstly you have to initialize empty git repository. You can do that using:
        
        git init 
        
- Now you can pull this repository to your local computer. You can do that using: 

        git pull https://github.com/hf-wsb/cloud-project-backend.git

- Create a virtual environment called ```venv```

    The command below will create a new folder called ```venv```

        python -m venv venv

### Activate the new virtual environment ```venv```

In cmd terminal type:

    .\venv\Scripts\activate

### Record the dependencies for the project

- First, update the ```pip``` library

        python -m pip install --upgrade pip

- Install dependecies
        
        cd app
        pip install -r requirements.txt

---

### Finally, our environement is ready and we can launch application using command:

        SET FLASK_APP=application.py
        flask run
        
- Open your internet browser, copy url from cmd and hit enter.
- You ought to see 'Hello world'
- You can also add /hello to the ulr link
- Enter your name and hit submit button
- You should see the website which welcome you using your name :) 
- You can also try to use pylint. Close flask server and enter "pylint application.py" and you will see that code is rated on 10/10 :)
