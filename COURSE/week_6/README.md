# Week 6: Advanced Web & Databases

## Overview
This week focuses on database integration and advanced web development concepts essential for building a comprehensive soccer analytics platform. You'll learn how to design and implement database schemas, connect Python applications to databases, and build advanced web features with authentication and dynamic forms.

## Skills & Difficulty Chart

| Challenge | Main Skills | Difficulty | Application to Capstone |
|-----------|-------------|------------|-------------------------|
| 1. Database Schema Design | Database Modeling, SQL | ⭐⭐⭐☆☆ | Create data structure for soccer stats |
| 2. SQLAlchemy ORM Implementation | ORM, Python Classes | ⭐⭐⭐☆☆ | Connect Python code to database |
| 3. Flask-WTF Forms | Web Forms, Validation | ⭐⭐⭐⭐☆ | Create data entry for soccer statistics |
| 4. Advanced Flask Application | Auth, CRUD Operations | ⭐⭐⭐⭐☆ | Build secure analytics platform |

## Learning Objectives
- Design and implement database schemas for soccer analytics
- Connect Python applications to databases using ORM
- Build advanced web applications with authentication
- Create dynamic web forms and interfaces for data entry
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

### 1. Database Schema Design 📊
- Design a database schema in `database_schema.py`
- Create tables for soccer players, teams, matches, and statistics
- Implement relationships between tables
- See [detailed challenge README](challenges/database_schema_README.md)

### 2. SQLAlchemy ORM Implementation 🔄
- Implement the ORM models in `orm_models.py`
- Create classes for soccer database tables
- Add CRUD operations for each model
- See [detailed challenge README](challenges/orm_models_README.md)

### 3. Flask-WTF Forms 📝
- Create forms with Flask-WTF in `flask_forms.py`
- Implement validation and error handling
- Connect forms to soccer database operations
- See [detailed challenge README](challenges/flask_forms_README.md)

### 4. Advanced Flask Application 🔐
- Build an advanced Flask app in `advanced_flask_app.py`
- Include authentication for secure access to soccer data
- Implement CRUD operations via web interface
- See [detailed challenge README](challenges/advanced_flask_app_README.md)

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
- [Entity-Relationship Diagrams Tutorial](https://www.lucidchart.com/pages/er-diagrams)
- [Flask Login Documentation](https://flask-login.readthedocs.io/en/latest/)
- [Sports Database Design Examples](https://www.vertabelo.com/blog/a-sports-data-model/)
- [NCAA Sports Database Schema Examples](https://data.world/sports/ncaa-football-statistics)

## Submission
Submit your completed work following the standard pull request process described in the Getting Started guide.