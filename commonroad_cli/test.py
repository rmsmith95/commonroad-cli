from main import find_min_length_route
import os


path = "../commonroad-scenarios/scenarios/recorded/NGSIM/US101/"
for xml_file in os.listdir(path):
    length = find_min_length_route(path + xml_file)
    print(length)

