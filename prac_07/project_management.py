import datetime
from project import Project

def load_projects(filename):
    projects = []
    with open(filename, 'r') as f:
        next(f)  # skip header line
        for line in f:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as f:
        f.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            f.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    print("Incomplete projects: ")
    for project in sorted(projects, key=lambda x: x.priority):
        if not project.is_complete():
            print(f"  {project}")
    print("Completed projects: ")
    for project in sorted(projects, key=lambda x: x.priority):
        if project.is_complete():
            print(f"  {project}")


def filter_projects_by_date(projects):
    date_input = input("Show projects that start after date (dd/mm/yy): ")
    date_obj = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date > date_obj]

    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(project)


def add_new_project():
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)

def update_project(projects):
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)





def main():
    projects = load_projects("projects.txt")
    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'a':
            project = add_new_project()
            projects.append(project)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'q':
            save_projects("projects.txt", projects)  # Save before exiting
            print("Thank you for using custom-built project management software.")
            break


if __name__ == "__main__":
    main()

