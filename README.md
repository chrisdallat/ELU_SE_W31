Week30:

Instructions:
In this assignment, you will work on improving the quality of a provided codebase through static analysis and code review. The main objective is to identify and address code quality issues, potential bugs, and adherence to coding standards using a static analysis tool. You will document the issues you discover and describe how you fixed them.

Codebase:
You can find a simple Python codebase that calculates and displays the total price of items in a shopping cart on this repository: https://github.com/shoklah/ELU_SE_W31. The codebase consists of a single Python script named `shopping_cart.py`. However, this script contains several issues related to code quality, potential bugs, and adherence to coding standards.

Tasks:

1. Static Analysis:
   - Choose a Python static analysis tool (e.g., `pylint`, `flake8`, `bandit`).
   - Run the chosen tool on the `shopping_cart.py` script to identify and document code quality issues, potential bugs, and deviations from coding standards.

2. Issue Resolution:
   - Fix the issues identified by the static analysis tool in the codebase.
   - Commit your changes with meaningful commit messages describing each fix.

3. Code Review:
   - Review the fixed code to ensure that the identified issues have been adequately addressed.
   - If you find any additional issues during your review, repeat the process of fixing and committing.

Submission Guidelines:
1. Fork the provided GitHub repository and clone it to your local machine.
2. Choose and run a static analysis tool on the `shopping_cart.py` script.
3. Fix the identified issues.
4. Commit your changes with clear commit messages.
5. If needed, repeat the issue resolution process after your review.
6. Provide the link to your public forked repository with the fixed code.

Week 31: Test and Deploy Quality Software
Due Oct 1 by 11:59pm Points 100 Submitting a text entry box or a file upload

Objective:
In this assignment, you will build upon your previous work of improving code quality by incorporating continuous integration (CI) and automated testing using GitHub Actions. The goal is to ensure that the codebase retains its quality over time through automated checks and tests.

Codebase:
You will continue to work with the codebase from the previous assignment. If you haven't already, fork the repository https://github.com/shoklah/ELU_SE_W31
Links to an external site. to your GitHub account.

Tasks:
    GitHub Actions Setup:
   - Navigate to the repository you forked in the previous assignment.
   - Create a new directory in the repository root named `.github/workflows`.
   - Inside this directory, create a YAML file (e.g., `ci.yml`) to configure GitHub Actions.

    Automated Static Analysis:
   - Utilize the chosen static analysis tool (e.g., `pylint`, `flake8`, `bandit`) to add a step in your GitHub Actions workflow that performs automated static analysis on the `shopping_cart.py` script.
   - Configure the workflow to run the static analysis step whenever changes are pushed to the repository.

    Automated Testing:
   - Implement a testing framework for the `shopping_cart.py` script. You can use Python's built-in `unittest` library or any other testing framework you prefer.
   - Create a testing step in the GitHub Actions workflow to execute the test suite you've created.
   - Ensure that the workflow runs the tests every time changes are pushed.

Submission Guidelines:

    Workflow Integration:
   - Ensure that the GitHub Actions workflow correctly executes the static analysis tool and tests as specified in the tasks.

    Link:
   - Provide the link to your public forked repository that demonstrates the integrated GitHub Actions workflow and includes the updated documentation.



