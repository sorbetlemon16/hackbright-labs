"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a github account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    if not row:
        print(f"Can't find {github}")

    else:
        print(f"Student: {row[0]} {row[1]}")
        print(f"GitHub account: {row[2]}")


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """

    QUERY = """
        INSERT INTO students (first_name, last_name, github)
          VALUES (:first_name, :last_name, :github)
        """

    db_cursor = db.session.execute(QUERY, {'first_name': first_name,
                                           'last_name': last_name,
                                           'github': github})

    db.session.commit()

    print(f"Successfully added student: {first_name} {last_name}")


def get_project_by_title(title):
    """Given a project title, print information about the project."""

    QUERY = """
        SELECT title, description, max_grade
        FROM projects
        WHERE title = :title
        """

    db_cursor = db.session.execute(QUERY, {'title': title})

    row = db_cursor.fetchone()

    if not row:
        print(f"Can't find project {title}")

    else:
        print(f"Title: {row[0]}")
        print(f"Description: {row[1]}")
        print(f"Max Grade: {row[2]}")


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""

    QUERY = """
        SELECT grade
        FROM grades
        WHERE student_github = :github
          AND project_title = :title
        """

    db_cursor = db.session.execute(QUERY, {'github': github, 'title': title})

    row = db_cursor.fetchone()

    if not row:
        print(f"Can't find grade for {github} in {title}")

    else:
        print(f"Student {github} in project {title} received grade of {row[0]}")


def project_exists(title):
    """Check to see if a project exists in the db. Return boolean value.

    Note: it doesn't make sense to use this in get_project_by_title, etc, since
    it would mean an unnecessary extra query.
    """

    QUERY = """
        SELECT *
        FROM projects
        WHERE title = :title
        """

    db_cursor = db.session.execute(QUERY, {'title': title})

    # this will return true if fetchone got a result; false otherwise
    return db_cursor.fetchone() != None


def student_exists(github):
    """Check to see if a student exists in the db. Return boolean value.

    Note: it doesn't make sense to use this in get_student_by_github, etc, since
    it would mean an unnecessary extra query.
    """

    QUERY = """
        SELECT *
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    # this will return true if fetchone got a result; false otherwise
    return db_cursor.fetchone() != None


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""

    # check to see if the project exists
    if not project_exists(title):
        print(f"Could not assign grade for {title}: no such project")
        return

    # check to see if the student exists
    if not student_exists(github):
        print(f"Could not assign grade for {github}: no such project")
        return

    QUERY = """
        INSERT INTO grades (student_github, project_title, grade)
          VALUES (:github, :title, :grade)
        """

    db_cursor = db.session.execute(QUERY, {'github': github,
                                           'title': title,
                                           'grade': grade})

    db.session.commit()

    print(f"Successfully assigned grade of {grade} for {github} in {title}")


# ADVANCED PARTS FROM Further Study FOLLOW


def make_new_project(title, description, max_grade):
    """Create new project and print confirmation.

    Given a title, description, and maximum grade, create a new project
    in the database and print a confirmation message.
    """

    QUERY = """
        INSERT INTO projects (title, description, max_grade)
          VALUES (:title, :description, :max_grade)
        """

    db.session.execute(QUERY, {'title': title, 'description': description,
                               'max_grade': max_grade})
    db.session.commit()
    print(f"Successfully added project: {title} {description} {max_grade}")


def get_grades_by_github(github):
    """Show all grades a student has received, given their github name."""

    QUERY = """
        SELECT project_title, grade
        FROM grades
        WHERE student_github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    rows = db_cursor.fetchall()

    if not rows:
        print(f"Student {github} has received no grades")

    else:
        for row in rows:
            title, grade = row
            print(f"Student {github} received grade of {grade} for {title}")


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            if len(args) != 1:
                print("Invalid, please use: student [github name]")

            else:
                github = args[0]
                get_student_by_github(github)

        elif command == "new_student":
            if len(args) != 3:
                print("Invalid, please use: new_student [first] [last] [github]")

            else:
                first_name, last_name, github = args  # unpack!
                make_new_student(first_name, last_name, github)

        elif command == "project":
            if len(args) != 1:
                print("Invalid, please use: project [title]")

            else:
                title = args[0]
                get_project_by_title(title)

        elif command == "grade":
            if len(args) != 2:
                print("Invalid, please use: grade [github] [title]")

            else:
                github, title = args
                get_grade_by_github_title(github, title)

        elif command == "assign_grade":
            if len(args) != 3:
                print("Invalid, please use: assign_grade [github] [title] [grade]")

            else:
                github, title, grade = args
                assign_grade(github, title, grade)

        # NEW COMMANDS IN ADVANCED

        elif command == "new_project":
            # This is tricky, since the description could be many words --
            # it isn't just a single word in args.
            #
            # So, they're in order of "title", "max_grade", "description"
            # and description becomes everything after max_grade

            if len(args) < 3:
                print("Invalid, please use: new_project [title] [max-grade] [description]")

            else:
                title = args[0]
                max_grade = int(args[1])
                description = " ".join(args[2:])

                make_new_project(title, description, max_grade)

        elif command == "student_grades":
            if len(args) != 1:
                print("Invalid, please use: grades [github]")

            else:
                github = args[0]
                get_grades_by_github(github)


if __name__ == "__main__":
    connect_to_db(app)

    handle_input()

    # To be tidy, we'll close our database connection -- though, since this
    # is where our program ends, we'd quit anyway.

    db.session.close()
