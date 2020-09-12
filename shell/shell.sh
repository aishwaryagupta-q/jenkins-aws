# added 
jenkins    ALL = NOPASSWD: ALL
# to sudoers of my GCE


sudo apt-get install python3
sudo apt-get install python3-pip

# pip3 install virtualenv
sudo apt-get install python3-venv
python3 -m venv venv
# windows
venv/Scripts/activate
# ubuntu
source venv/bin/activate

pip3 install flask
python -m pip install --upgrade pip
pip3 install --user -r requirements.txt
pip3 install pylint
pip3 install pytest

pylint --rcfile ..filename.cfg pythonfile.py
python -m unittest tests/test_routes.py
pip3 freeze > requirements.txt
 