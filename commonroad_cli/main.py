import argparse
import os
import sys
#sys.path.append('../commonroad-route-planner/commonroad_route_planner')
from commonroad.common.file_reader import CommonRoadFileReader
#import commonroad_route_planner
#import commonroad_route_planner.route_planner
from commonroad_route_planner.route_planner import RoutePlanner



"""
Your goal is to create a Command Line Interface (CLI) tool, using Python, that can read CommonRoad scenarios [1, 2], find the optimal routes using the
CommonRoad Route Planner [3] and return the length of the routes either in kilometers or miles, depending on the preference of the user.

You will be evaluated for:
Your ability to take loosely defined requirements and deliver a complete solution.
The software engineering quality of your tool:
Your code is expected to be clean, consistent, and tested.
The tool must be packaged efficiently to allow fast deployment.
"""


def find_min_length_route(commonroad_file):
    # read in scenario and planning problem set
    if not os.path.isfile(commonroad_file):
        print('commonroad file not found')
        return None
    scenario, planning_problem_set = CommonRoadFileReader(commonroad_file).open()
    planning_problem = list(planning_problem_set.planning_problem_dict.values())[0]

    # plan and retrieve routes
    route_planner = RoutePlanner(scenario,
                         planning_problem,
                         backend=RoutePlanner.Backend.NETWORKX,
                         reach_goal_state=False)
    candidate_holder = route_planner.plan_routes()
    list_routes, num_route_candidates = candidate_holder.retrieve_all_routes()
    print(f"Number of route candidates: {num_route_candidates}")
    
    # find the minimum length route
    min_route = None
    for length in list_routes:
        if length.path_length[-1] <= list_routes[0].path_length[-1]:
            min_route = length
    if min_route is None:
        return None
    return min_route.path_length[-1]


def main():
    argparser = argparse.ArgumentParser(
        description=__doc__)
    argparser.add_argument(
        '--commonroad',
        metavar='C',
        default='',
        help='Choose an absolute path of a commonroad file to find the length of')
    argparser.add_argument(
        '--unit',
        metavar='U',
        default='meters',
        help='Choose the route length unit [kilometers, miles, meters]')
    args = argparser.parse_args()

    length = find_min_length_route(args.commonroad)
    if length is None:
        print('length not found')
        return None
    
    if args.unit == 'miles':
        length = length * 0.000621371
        print(f"Length: {length} miles")
    elif args.unit == 'kilometers':
        length = length * 0.001
        print(f"Length: {length} kilometers")
    else:
        print(f"Length: {length} meters")
    return length


if __name__ == '__main__':
    main()

