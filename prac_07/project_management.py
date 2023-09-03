import datetime

MENU = f"- (L)oad projects  " \
       f"- (S)ave projects  " \
       f"- (D)isplay projects  " \
       f"- (F)ilter projects by date" \
       f"- (A)dd new project  " \
       f"- (U)pdate project" \
       f"- (Q)uit"

def main():
    projects = []
    non_compeleted_projects = []
    compeleted_projects = []
    print(MENU)
    choice = input().upper()
    while choice != "Q":
        if choice == "L":
            places_file = open("projects.txt", "r")
            for line in places_file.readlines():
                place = line.strip().split("    ")
                projects.append(place)
            print(projects[:])