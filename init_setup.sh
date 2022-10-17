echo[$(date)]:"START"
echo[$(date)]:"CREATING ENV WITH PYTHON 3.8"
conda create --prefix ./env python=3.8 -y
echo[$(date)]:"ACTIVATING THE ENV"
source activate ./env
echo[$(date)]:"INSTALLING DEV REQUIREMENTS"
pip install -r requirements_dev.txt
echo[$(date)]:"END"