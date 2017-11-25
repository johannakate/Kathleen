# Kathleen's website - Flask Python application

To run the app:

If Kathleen folder/project already exists:

`mkdir Kathleen-JKG-edits`

Change directories into new folder

`cd Kathleen-JKG-edits`

Git clone forked project

`git clone git@github.com:johannakate/Kathleen.git`

Change directories into cloned project

`cd ../Kathleen-JKG-edits/Kathleen`

Create virtual environment for Python app

`virtualenv env`

Run virtual environment in OSX (can tab complete the folders after typing "source b")

`source bin/env/activate`

This should show (env) in the commandline indicating environment is activated

Install the requirements

`pip install -r requirements.txt`

Export the FLASK_APP variable so Flask knows which file to enter into

`export FLASK_APP=server.py`

Run the applications

`flask run`