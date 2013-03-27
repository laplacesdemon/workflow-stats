WORKFLOW STATS
==============

`*WARNING* Mac OSX only`

The programs/apps in this project helps you keep track of your software usage and store useful statistics about your working habits.

ROADMAP
-------

1. Monitor app usage [Done - See `monitor_app.py`]
2. Motinor task usage (by manually entering what are you working on at that moment)
3. Taking iSight camera screenshot each time you log on
4. Bundle this app in a package that can be added to start app programs (or a automator script)
5. Bundle this app in an OSX app that has an interface and submit it to the store.

INSTALLATION
------------

At this stage the project is really tiny, so no complicated installation stuff here. Just clone the repo, create the virtualenv and run the programs.
Following are more detailed steps:

Clone the project

    git clone https://github.com/laplacesdemon/workflow-stats

Install virtualenv if it's not installed before                                                                                                                                                                                         

    pip install virtualenv

Use following to set up the project

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt

Please note that installing `pyobjc` might be tricky. See `http://pythonhosted.org/pyobjc/` for installation details.

Monitor App Usage
-----------------

`monitor_app.py` is a command-line tool that keeps track of the apps you used. On stopping the app with <Ctrl-C> prints the app usage and stores them in an sqlite3 db. 

    ./monitor_app.py

I have copied this source file from `https://gist.github.com/glenbot/3425960` and did some contributions.
