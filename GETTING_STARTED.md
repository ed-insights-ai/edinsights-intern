# Getting Started with ED-Insights.AI Internship

This guide will help you set up your development environment and understand the workflow for the NCAA Division II Soccer Player Analysis internship program.

## Course Access

### 1. Course Video Access
- Sign up for a subscription to Udemy and enroll in the course "100 Days of Code: The Complete Python Pro Bootcamp"
- Send an expense request for the subscription to founder@edinsights.ai
- Each week has specific required videos that align with the assignments
- Watch the videos before attempting the corresponding assignments
- Take notes and code along with the videos for better understanding
- If the video content is already familiar, skip it or watch at double speed to save time

### 2. Video Schedule
- Plan to watch approximately 5-6 hours of course videos per week
- The weekly README files list the specific videos required for that week
- Videos are referenced by day number and title (e.g., "Day 1: Working with Variables in Python")

## Development Environment Setup

### 1. Python Installation
- Install Python 3.12 or later from [python.org](https://www.python.org/downloads/)
- Verify installation with `python --version` in your terminal

### 2. Git Setup
- Install Git from [git-scm.com](https://git-scm.com/downloads)
- Configure your Git identity:
  ```
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

### 3. GitHub Setup
- Create a GitHub account if you don't have one
- Fork this repository to your GitHub account by clicking the "Fork" button on the repository page
- Clone your fork to your local machine:
  ```
  git clone https://github.com/YOUR-USERNAME/edinsights-intern.git
  cd edinsights-intern
  ```

### 4. Virtual Environment
- Create a virtual environment using `uv`:
  ```
  uv create venv
  ```
- Activate the virtual environment:
  - Windows: `venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`
- For more information on `uv`, refer to the [uv documentation](https://example.com/uv-docs)

### 5. Dependencies
- Install project dependencies:
  ```
  pip install -r PROJECT/requirements.txt
  ```

## GitHub Workflow

1. **Fork the Repository**
   - Fork the `edinsights-intern` repository to your GitHub account.

2. **Clone Your Fork**
   - Clone your forked repository to your local machine:
     ```
     git clone https://github.com/YOUR-USERNAME/edinsights-intern.git
     cd edinsights-intern
     ```

3. **Create a Branch for Your Work**
   - Create a new branch for your weekly or feature-specific work:
     ```
     git checkout -b week-X
     ```

4. **Make Changes**
   - Work on your assignments or project milestones in the appropriate directories.

5. **Commit Your Changes**
   - Stage and commit your changes:
     ```
     git add .
     git commit -m "Week X: Brief description of your work"
     ```

6. **Push Your Branch**
   - Push your branch to your forked repository:
     ```
     git push origin week-X
     ```

7. **Create a Pull Request**
   - Go to your forked repository on GitHub and create a Pull Request to merge your branch into the `main` branch of the original repository.

8. **Review and Merge**
   - Wait for feedback or approval from the repository maintainers before merging.

## Communication

For questions or issues:
1. Check existing documentation in the repository
2. Submit a GitHub issue with clear details about your question or problem
3. Use appropriate labels for your issues

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

## Weekly Schedule

Each week follows this general pattern:
1. Watch the required course videos
2. Study the supplementary materials in the week's folder
3. Complete the coding assignments
4. Apply your knowledge to the project milestone
5. Submit your work via pull request by the weekly deadline

## Time Management

The program is designed to require approximately 20 hours per week:
- 5-6 hours: Watching course videos
- 8-10 hours: Completing assignments and exercises
- 5-7 hours: Working on project milestones

## Capstone Project

After completing the 10-week course, you'll have a **dedicated 4-week window** to develop your capstone project. This is a critical component of the program where you'll apply all the skills you've learned to build a complete NCAA Soccer Player Analysis System.

### Capstone Timeline
- **Weeks 8-10 of course**: Planning and proof-of-concept
- **4 weeks after course**: Full implementation 
- **Final deadline**: Submit completed capstone at the end of the 4-week implementation period

### Capstone Documentation
Carefully review these resources to understand the capstone requirements:
- [Capstone Guidelines](PROJECT/docs/capstone_guidelines.md)
- [Course to Capstone Connection](PROJECT/docs/course_to_capstone.md)

Throughout the course, pay special attention to components marked with 🌟 **CAPSTONE TIP** - these highlight material that will be particularly important for your final project.

Good luck with your internship!