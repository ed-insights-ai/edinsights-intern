# Challenge 1: Soccer Stats Fundamentals

This challenge helps you practice basic Python operations while introducing you to common calculations used in soccer analytics.

## Overview

Soccer analytics relies on many simple calculations and data transformations. In this challenge, you'll implement five fundamental operations that real soccer analysts use regularly.

## Learning Focus

- Variable assignment and data types
- String manipulation
- Basic arithmetic operations
- Conditional logic
- Function implementations

## Tips for Each Function

### 1. `calculate_goals_per_game`

This function calculates a player's scoring efficiency.

**Tips:**
- Check if `games_played` is zero to avoid division by zero
- Use the `sum()` function to add up all goals
- Remember to return a float value for the average

**Pseudocode:**
```
function calculate_goals_per_game(goals, games_played):
    if games_played equals 0:
        return 0
    
    total_goals = sum of all goals in the goals list
    average = total_goals / games_played
    
    return average
```

**Real-world application:** Scouts and analysts use goals-per-game to compare strikers' efficiency and normalize scoring across players with different numbers of appearances.

### 2. `reverse_team_name`

This function handles string manipulation in a soccer context.

**Tips:**
- Python strings can be reversed using slicing with a negative step: `text[::-1]`
- No special handling is needed for spaces or punctuation - just reverse the entire string

**Pseudocode:**
```
function reverse_team_name(team_name):
    reversed_name = team_name reversed (characters in reverse order)
    return reversed_name
```

**Real-world application:** While reversing team names might seem like a fun exercise, string manipulation is essential for cleaning and standardizing team names from different data sources.

### 3. `count_words_in_chant`

This function helps analyze soccer fan culture by counting words in chants.

**Tips:**
- The `split()` method breaks a string into a list of words
- By default, `split()` uses whitespace as the separator
- The length of the resulting list gives you the word count

**Pseudocode:**
```
function count_words_in_chant(chant):
    words = split chant into a list using whitespace as separator
    count = length of words list
    return count
```

**Real-world application:** Text analysis of soccer chants, team mottos, and player interviews can provide insights into team culture and fan engagement.

### 4. `km_to_miles`

This function converts between metric and imperial measurement systems.

**Tips:**
- The conversion is a simple multiplication
- Make sure to maintain precision in your calculations
- Return the result as a float

**Pseudocode:**
```
function km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
```

**Real-world application:** When analyzing player movement data from different sources, you might need to convert between measurement systems, especially when comparing European and American statistics.

### 5. `is_palindrome_formation`

This function analyzes soccer formations for symmetry.

**Tips:**
- Remove any non-alphanumeric characters first (like the `-` in formations)
- Compare the formation with its reverse
- Make sure to handle edge cases (empty strings, etc.)

**Pseudocode:**
```
function is_palindrome_formation(formation):
    # Remove any hyphens or spaces
    clean_formation = formation with all "-" characters removed
    
    # Check if the clean formation reads the same forward and backward
    if clean_formation equals clean_formation reversed:
        return True
    else:
        return False
```

**Real-world application:** Symmetrical formations often have different tactical properties than asymmetrical ones. Analysts study formation symmetry to understand tactical balance and defensive coverage.

## Testing Your Code

Run the file by executing:

```python
python python_basics.py
```

If your implementations are correct, you should see output that matches the expected results in the docstrings.

## Further Exploration

After completing the challenge, consider:

1. How would you modify `calculate_goals_per_game` to handle weighted goals (e.g., goals against stronger teams count more)?

2. Could you enhance `is_palindrome_formation` to detect formations with similar but not identical symmetry (e.g., "4-3-3" and "3-3-4")?

3. What other soccer-related metrics could you calculate using these basic operations?

## Connect to Capstone

These functions represent the type of data manipulation you'll need for your NCAA soccer analysis capstone. As you work through this challenge, think about:

- What player statistics will be most valuable to track?
- How will you need to transform raw data into meaningful metrics?
- What types of string manipulation might be necessary for player and team names?

Good luck, and remember that these fundamentals will be the building blocks for more complex analytics later in the course!