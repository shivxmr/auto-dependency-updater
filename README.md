# Auto Dependency Updater

A GitHub Actions bot that automatically checks for outdated Python dependencies, runs tests against the new versions, and creates a pull request with the updates.

## Project Story

This project was born out of an exploration into the power of GitHub Actions. The goal was to move beyond simple CI/CD and build a truly automated, intelligent bot that could handle a common and critical task: keeping dependencies up to date. The key challenge was not just to automate the updates, but to do so safely, without blindly introducing breaking changes. This led to the core feature of this project: an integrated testing step that validates dependency updates before proposing them in a pull request.

## Features

-   **Automated Dependency Scanning:** Runs on a weekly schedule to check for outdated packages in your `requirements.txt` file.
-   **Safety-First Testing:** Before creating a pull request, the bot installs the updated dependencies and runs your project's `pytest` test suite.
-   **Intelligent Pull Requests:**
    -   If tests pass, it creates a clean pull request, ready for you to review and merge.
    -   If tests fail, it still creates a pull request but flags it with a "⚠️ Breaking Change" label and a warning in the description, so you know to investigate further.
-   **Manually Triggerable:** You can trigger the workflow at any time from the Actions tab in your repository.
-   **Highly Configurable:** The workflow is designed to be easily adapted to other Python projects.

## How It Works

The workflow is defined in `.github/workflows/dependency-updater.yml` and follows these steps:

1.  **Checkout & Setup:** The workflow checks out your repository's code and sets up a Python environment.
2.  **Install Dependencies:** It installs the current dependencies from `requirements.txt`.
3.  **Check for Updates:** It runs the `scripts/check_dependencies.py` script, which uses `pip list --outdated` to find new package versions and updates `requirements.txt` accordingly.
4.  **Detect Changes:** The workflow checks if the `requirements.txt` file was actually modified. If not, the job ends.
5.  **Test with New Dependencies:** If the file was changed, the workflow installs the new package versions and runs the test suite using `pytest`.
6.  **Create Pull Request:** Based on the test results, it creates a pull request:
    -   **On Success:** A standard PR is created.
    -   **On Failure:** A PR is created with a warning label and message.

## Setup

To use this bot in your own repository, follow these steps:

1.  **Copy the Files:** Copy the `.github`, `scripts`, and `tests` directories, as well as the `app.py`, `requirements.txt`, and `.gitignore` files, into your repository.
2.  **Customize `requirements.txt`:** Add your project's dependencies to the `requirements.txt` file.
3.  **Write Your Tests:** Create tests for your application in the `tests` directory. The bot relies on these tests to ensure that dependency updates are safe.
4.  **Permissions:** Ensure your repository's Actions settings allow workflows to create pull requests.
    -   Go to your repository's **Settings** > **Actions** > **General**.
    -   Scroll down to "Workflow permissions".
    -   Select **"Read and write permissions"**.
    -   Check the box for **"Allow GitHub Actions to create and approve pull requests"**.
    -   Click **Save**.

That's it! The bot will now run automatically and help you keep your dependencies up to date safely.
