# Challenge 1: Soccer Match Reports

This challenge focuses on using file operations to manage soccer match reports.

## Overview

Soccer teams and leagues need to store, access, and manipulate match data efficiently. In this challenge, you'll implement functions that handle text-based match reports, demonstrating essential file operations in a soccer context.

## Learning Focus

- Reading from text files
- Writing to text files
- Handling file errors with try/except
- Manipulating file contents
- Working with file paths and directories

## Key Concepts Explained

### File Operations Basics

**Reading Files**:
```python
# Basic pattern for reading a file
with open(filepath, 'r') as file:
    content = file.read()  # Reads entire file as a string
    # OR
    lines = file.readlines()  # Reads file as a list of lines
```

**Writing Files**:
```python
# Basic pattern for writing to a file
with open(filepath, 'w') as file:  # 'w' overwrites the file
    file.write(content)

# Basic pattern for appending to a file
with open(filepath, 'a') as file:  # 'a' appends to the file
    file.write(new_content)
```

**Error Handling**:
```python
# Basic pattern for handling file errors
try:
    with open(filepath, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"File not found: {filepath}")
except PermissionError:
    print(f"Permission denied: {filepath}")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Functions to Implement

### 1. `read_match_report`

This function reads a match report file and returns its contents.

**Tips:**
- Use a context manager (`with` statement) to safely open and close the file
- Handle potential errors like the file not existing
- Make sure to read the entire file content

**Pseudocode:**
```
function read_match_report(filepath):
    try:
        open the file at filepath in read mode using a context manager
        read the entire file content
        return the content
    except FileNotFoundError:
        raise FileNotFoundError with a message about the missing match report
```

**Example Usage:**
```python
try:
    report = read_match_report("match_report_20230815.txt")
    print(report)
except FileNotFoundError as e:
    print(e)
```

### 2. `write_match_report`

This function writes a match report to a file.

**Tips:**
- Use a context manager to safely open and close the file
- Support both writing a new file and appending to an existing file
- Handle potential errors in the writing process

**Pseudocode:**
```
function write_match_report(filepath, report_content, append=False):
    try:
        if append is True:
            open the file at filepath in append mode
        else:
            open the file at filepath in write mode
            
        write report_content to the file
        return True to indicate success
    except IOError:
        raise IOError with a message about being unable to write the report
```

**Example Usage:**
```python
match_report = """
Match: FC Barcelona vs Real Madrid
Date: 2023-08-15
Score: 3-2
Scorers: Lewandowski (2), Pedri; Vinicius, Bellingham
"""
write_match_report("classico_report.txt", match_report)
```

### 3. `find_matches_by_team`

This function searches through multiple match reports to find matches involving a specific team.

**Tips:**
- Read each file in a directory to find matches
- Use string operations to check if the team name appears in the report
- Return a list of file paths containing the team

**Pseudocode:**
```
function find_matches_by_team(reports_directory, team_name):
    create an empty list for matching_reports
    
    try:
        for each file in the reports_directory:
            if file is a text file:
                read the file content
                if team_name appears in the content:
                    add file path to matching_reports
        
        return matching_reports
    except Exception:
        raise with an appropriate error message
```

**Example Usage:**
```python
barcelona_matches = find_matches_by_team("match_reports/", "Barcelona")
print(f"Found {len(barcelona_matches)} matches with Barcelona")
```

### 4. `update_match_result`

This function updates the score in an existing match report.

**Tips:**
- Read the entire file first
- Use string replacement to update the score
- Write the updated content back to the file
- Count and return the number of replacements

**Pseudocode:**
```
function update_match_result(filepath, old_score, new_score):
    try:
        read the file content
        
        if old_score doesn't appear in the content:
            return 0 (no replacements made)
        
        replace old_score with new_score in the content
        write the updated content back to the file
        
        return the number of replacements (should be 1 normally)
    except FileNotFoundError:
        raise with an appropriate error message
```

**Example Usage:**
```python
replacements = update_match_result("classico_report.txt", "3-2", "3-3")
print(f"Updated {replacements} match result(s)")
```

### 5. `create_match_report_directory`

This function creates a directory structure for organizing match reports by season and competition.

**Tips:**
- Create directories if they don't exist
- Handle errors that might occur during directory creation
- Support nested directory structures

**Pseudocode:**
```
function create_match_report_directory(base_path, season, competition):
    try:
        create a directory path by joining base_path, season, and competition
        check if the directory exists
        if it doesn't exist:
            create the directory and any necessary parent directories
        return True on success
    except Exception:
        raise with an appropriate error message
```

**Example Usage:**
```python
create_match_report_directory("match_reports", "2023-2024", "Champions_League")
```

## Testing Your Implementation

Run the file with:

```python
python file_operations.py
```

The provided `main()` function will test your implementations with sample data. Make sure all test cases pass without errors.

## Further Exploration

After completing the challenge, consider:

1. How would you modify these functions to work with binary files like match videos or PDF reports?

2. Could you implement a simple search function that finds matches based on criteria like goals scored or specific events?

3. How might you structure a more complex match report format that includes detailed statistics?

## Connect to Capstone

For your NCAA soccer analysis capstone, effective file operations will be essential for:

- Storing match reports and statistics in a consistent format
- Processing data from multiple sources
- Organizing data by seasons, teams, or competitions
- Creating a reliable backup and archival system

These skills form the foundation of your data management strategy, ensuring that your analysis is built on well-organized and accessible information.