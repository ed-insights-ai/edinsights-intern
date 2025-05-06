# Week 6: Advanced Web & Databases

## Learning Objectives
- Design and implement database schemas
- Connect Python applications to databases
- Build advanced web applications with authentication
- Create dynamic web forms and interfaces
- Implement CRUD operations in web applications

## Required Course Videos
Complete the following course videos before starting this week's assignments:

1. **Day 56: Rendering HTML/Static files and Templates** (40min)
   - Serving static files
   - Using template engines
   - Creating reusable layouts

2. **Day 57: Templating with Jinja in Flask Applications** (38min)
   - Jinja templating language
   - Template inheritance
   - Passing variables to templates

3. **Day 58: Web Foundation Bootstrap** (1hr 40min)
   - Using Bootstrap for responsive design
   - Grid systems and components
   - Styling web applications

4. **Day 60: Make POST Requests with Flask and HTML Forms** (4min)
   - Processing form submissions
   - Handling different HTTP methods
   - Form validation

5. **Day 63: Databases with SQLite and SQLAlchemy** (12min)
   - Database design principles
   - Working with SQLite
   - Using SQLAlchemy ORM

## Assignments

### 1. Database Schema Design
- Design a database schema in `database_schema.py`
- Create tables for players, teams, matches, and statistics
- Implement relationships between tables

### 2. SQLAlchemy ORM Implementation
- Implement the ORM models in `orm_models.py`
- Create classes for database tables
- Add CRUD operations for each model

### 3. Flask-WTF Forms
- Create forms with Flask-WTF in `flask_forms.py`
- Implement validation and error handling
- Connect forms to database operations

### 4. Advanced Flask Application
- Build an advanced Flask app in `advanced_flask_app.py`
- Include authentication and user management
- Implement CRUD operations via web interface

## Project Milestone: Database Integration

In the `PROJECT/` directory:
1. Implement a SQLAlchemy database for your NCAA soccer analysis system
2. Create models for players, teams, matches, and statistics
3. Add data import functionality from your web scraper
4. Implement a basic web interface for viewing the database content

Work on this in the `PROJECT/src/` directory, adding appropriate database models and integration code.

> **🌟 CAPSTONE TIP:** The database design you create this week will be the foundation of your capstone project's data storage. A well-structured database with proper relationships will allow for efficient queries and analysis in your capstone. Pay special attention to the schema design, as making major changes later will be difficult. Your capstone will need to store large amounts of soccer statistics, so think about optimization and indexing.

## Resources
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Database Design Principles](https://www.sqlshack.com/database-design-principles/)

## Submission
Submit your completed work following the standard pull request process described in the Getting Started guide.