# Week 4: Web Integration & RESTful APIs

## Learning Objectives
- Build and consume RESTful APIs
- Implement authentication and authorization
- Create HTTP clients and servers
- Manage API errors and status codes
- Design efficient API architectures

## Required Course Videos
Complete the following course videos before starting this week's assignments:

1. **Day 34: API Practice - Creating a GUI Quiz App** (55min)
   - Integrating APIs with GUI applications
   - Handling API data in application logic

2. **Day 35: Keys, Authentication & Environment Variables** (1hr 4min)
   - Working with API keys
   - Securing sensitive information
   - Using environment variables

3. **Day 36: Stock Trading News Alert Project** (40min)
   - Combining multiple APIs
   - Creating notification systems

4. **Day 37: Habit Tracking Project: API Post Requests** (39min)
   - Making POST requests to APIs
   - Managing and updating remote data

5. **Day 54: Introduction to Web Development with Flask** (57min)
   - Creating a basic Flask application
   - Handling routes and requests

## Assignments

### 1. RESTful API Client
- Implement a complete API client in `api_client.py`
- Add support for GET, POST, PUT, and DELETE methods
- Handle authentication and error responses

### 2. API Integration Exercise
- Complete the multi-API integration in `api_integration_advanced.py`
- Combine data from multiple sources
- Process and transform the combined data

### 3. Flask API Server
- Create a simple Flask API server in `flask_api.py`
- Implement endpoints for CRUD operations
- Add proper error handling and status codes

### 4. Authentication System
- Implement an authentication system in `auth_system.py`
- Support API key and JWT-based authentication
- Secure sensitive endpoints

## Project Milestone: API Development

In the `PROJECT/` directory:
1. Implement a basic RESTful API for your NCAA soccer analysis system
2. Include endpoints for accessing player and team data
3. Add proper error handling and response formatting
4. Document your API design and endpoints

Implement this in the `PROJECT/src/dashboard/` directory, extending the existing Flask application.

> **🌟 CAPSTONE TIP:** The API you develop this week will serve as the interface between your capstone project's frontend and backend components. Well-designed API endpoints will make your capstone's dashboard more responsive and maintainable. Your capstone will need to expose data through APIs for visualization and user interaction, so focus on creating a clean, intuitive API design.

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [RESTful API Design Best Practices](https://restfulapi.net/)
- [JWT Authentication](https://jwt.io/introduction/)
- [Postman API Platform](https://www.postman.com/)
- [HTTP Status Codes](https://httpstatuses.com/)

## Submission
Submit your completed work following the standard pull request process described in the Getting Started guide.