import re
import sys

if __name__ == '__main__':
    print("Handy Haversacks")
    bags_containers = {}
    looking_for_bags = ["shiny gold"]
    counter = 0
    regex = re.compile(" bags*\.*")

    for line in sys.stdin:
        # We separate the main bag color from the bags that It can contain
        bag_color, can_contain_bag_colors = line.rstrip().split(" bags contain ")
        can_contain = {}

        for contain_bag_color in can_contain_bag_colors.split(", "):
            # We work with the bag colors a specific bag color can contain.
            #
            contain_bag_color = regex.sub("", contain_bag_color)
            quantity, color = contain_bag_color.split(" ", maxsplit=1)
            can_contain.setdefault(color, quantity)

        bags_containers.setdefault(bag_color, can_contain)

    # We start calculating how many bags can contain atleast one "shiy gold" bag
    match_bags = set()
    visited_bags = set()
    for actual_bag in looking_for_bags:
        visited_bags.add(actual_bag)
        for bag in bags_containers.keys():
            for x in bags_containers.get(bag).keys():
                if actual_bag == x:
                    match_bags.add(actual_bag)
                    if bag not in visited_bags:
                        looking_for_bags.append(bag)
                    # Add to counter
                    counter += 1
    visited_bags.remove("shiny gold")
    print(f"visited bags {visited_bags}")



    print(f"Bags that contain a {looking_for_bags[0]} bag in it: {len(visited_bags)}")


    # not 6
    # not 434