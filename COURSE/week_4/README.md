# Week 4: Soccer Web APIs & Integration

## Learning Objectives
- Understand the basics of RESTful APIs
- Learn how to consume external soccer data APIs
- Create simple web endpoints with Flask
- Grasp authentication concepts for web services
- Design basic API structures for soccer data

## Skills & Difficulty Levels

| Skill | Difficulty | Description |
|-------|------------|-------------|
| HTTP Methods | ⭐⭐ Beginner-Intermediate | Understanding GET, POST, PUT, DELETE |
| API Requests | ⭐⭐ Beginner-Intermediate | Making API calls with parameters and headers |
| JSON Response Handling | ⭐⭐ Beginner-Intermediate | Processing JSON responses from APIs |
| API Error Handling | ⭐⭐ Beginner-Intermediate | Managing API errors and status codes |
| Flask Basics | ⭐⭐⭐ Intermediate | Creating simple web server routes |
| Route Parameters | ⭐⭐ Beginner-Intermediate | Working with URL parameters in Flask |
| Request Validation | ⭐⭐ Beginner-Intermediate | Validating incoming API requests |
| API Authentication | ⭐⭐⭐ Intermediate | Understanding API keys and basic auth |
| Multi-API Integration | ⭐⭐⭐ Intermediate | Combining data from multiple sources |
| JWT Concepts | ⭐⭐⭐ Intermediate | Understanding token-based authentication |

## Required Course Videos
Complete the following course videos before starting this week's challenges:

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

## Coding Challenges

This week's challenges focus on understanding concepts rather than building complete systems. Each challenge provides significant starter code to help you focus on key API concepts.

### Challenge 1: Soccer Data API Client
- **Difficulty**: ⭐⭐ (Beginner-Intermediate)
- File: `api_client.py`
- README: `challenges/api_client_README.md`
- Create a client to fetch soccer team and player data
- Learn how to make API requests and handle responses

### Challenge 2: Soccer Data Integration
- **Difficulty**: ⭐⭐ to ⭐⭐⭐ (Beginner-Intermediate to Intermediate)
- File: `api_integration_advanced.py`
- README: `challenges/api_integration_advanced_README.md`
- Combine data from multiple soccer API sources
- Process and transform combined soccer data

### Challenge 3: Soccer Team API Server
- **Difficulty**: ⭐⭐⭐ (Intermediate)
- File: `flask_api.py`
- README: `challenges/flask_api_README.md`
- Create a simple API for soccer team data using Flask
- Learn how to handle different HTTP methods and status codes

### Challenge 4: Basic API Authentication
- **Difficulty**: ⭐⭐⭐ (Intermediate)
- File: `auth_system.py`
- README: `challenges/auth_system_README.md`
- Implement basic authentication for a soccer API
- Understand key authentication concepts

## Project Milestone: Soccer API Design

In the `PROJECT/` directory, create a document outlining:

1. API Endpoints for NCAA Soccer Data
   - List the key endpoints your system will need
   - Describe the purpose and functionality of each endpoint
   - Define URL patterns (e.g., `/api/teams/{team_id}`)

2. Data Models
   - Outline the JSON structure for key resources (teams, players, matches)
   - Define required and optional fields
   - Provide example responses

3. API Documentation
   - Document HTTP methods supported for each endpoint
   - List query parameters and their functions
   - Include sample requests and responses

4. Simple Implementation
   - Create a basic Flask app with 2-3 working endpoints
   - Implement at least one GET and one POST endpoint
   - Add basic error handling

Save your API design document as `api_design.md` in your personal project folder, and implement the basic Flask app in the `PROJECT/src/dashboard/` directory.

> **🌟 CAPSTONE TIP:** Focus on designing a clean, intuitive API rather than a complex one. A well-designed API with clear endpoints and consistent responses will be much more valuable for your capstone project than a complex API that's difficult to use. Your API design should make it easy to access the NCAA soccer data you'll be collecting and analyzing.

## Understanding RESTful APIs

RESTful APIs are a standard way to expose data and functionality to applications. Here are the key concepts:

### HTTP Methods

- **GET**: Retrieve data (e.g., get a list of teams)
- **POST**: Create new data (e.g., add a new player)
- **PUT/PATCH**: Update existing data (e.g., update team information)
- **DELETE**: Remove data (e.g., delete a match record)

### URL Structure

RESTful APIs use predictable URL patterns:

- Collection: `/teams` - represents all teams
- Specific resource: `/teams/123` - represents team with ID 123
- Nested resources: `/teams/123/players` - all players on team 123

### Status Codes

APIs use HTTP status codes to indicate results:

- **2xx**: Success (200 OK, 201 Created, 204 No Content)
- **4xx**: Client error (400 Bad Request, 404 Not Found)
- **5xx**: Server error (500 Internal Server Error)

### Web Service Diagram

```
┌─────────────┐         HTTP Request         ┌─────────────┐
│             │ ──────────────────────────→  │             │
│ Client App  │     GET /api/teams/123       │  API Server │
│             │                              │  (Flask)    │
│             │ ←────────────────────────────│             │
└─────────────┘         HTTP Response        └─────────────┘
                   200 OK + Team JSON data
```

## Challenge Progression

The challenges are designed to build understanding progressively:

1. **Challenge 1**: Learn to consume external soccer APIs
2. **Challenge 2**: Practice combining data from multiple API sources
3. **Challenge 3**: Create your own soccer API endpoints
4. **Challenge 4**: Add simple authentication to protect API endpoints

Each challenge focuses on understanding specific concepts rather than building a complete system.

## How to Approach This Week

1. Make sure you understand the basic concepts of RESTful APIs before starting
2. Read the challenge README files carefully for concept explanations
3. Examine the starter code to understand the structure before making changes
4. Focus on getting simple functionality working before attempting advanced features
5. Test your API endpoints with the provided examples
6. Use the included diagrams to understand request and response flows
7. Don't worry about building a complete system - focus on learning the concepts
8. Apply what you've learned to create your API design document

## Resources
- [RESTful API Design Guidelines](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [Flask Quick Start](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Python Requests Library](https://requests.readthedocs.io/en/latest/)
- [JWT Authentication Overview](https://jwt.io/introduction/)
- [Football (Soccer) API Documentation](https://www.api-football.com/documentation-v3)
- [Postman - API Testing Tool](https://www.postman.com/)

## Submission
Submit your completed work following the standard pull request process described in the Getting Started guide.