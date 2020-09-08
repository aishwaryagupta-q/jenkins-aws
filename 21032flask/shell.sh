pip install virtualenv
python3 -m venv venv
venv/Scripts/activate

pip install flask
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pylint
pip install pytest

pylint --rcfile ..filename.cfg pythonfile.py
python -m unittest tests/tets_routes.py
pip freeze > requirements.txt
 