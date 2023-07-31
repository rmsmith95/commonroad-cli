# Install
1. git clone git@github.com:rmsmith95/commonroad-cli.git
2. cd commonroad-cli
3. pip install -r requirements.txt
4. pip install .

- Tested with python 3.8

# Use
python3.8 ./commonroad_cli/main.py --commonroad "path_to_commonroad_file" --unit "kilometers"
- path length is returned
- USA_US101-4_3_T-1.xml returns a length of 0.122 kilometers
