# Challenge 2: Game Flow Control

This challenge focuses on using Python's control flow structures (conditionals and loops) to model and analyze soccer match scenarios.

## Overview

Soccer matches follow patterns and rules that can be modeled with programming logic. In this challenge, you'll implement five functions that use conditionals and loops to analyze different aspects of soccer matches and player performance.

## Learning Focus

- If/elif/else conditional statements
- For and while loops
- Boolean logic
- Sequence processing
- Accumulation patterns

## Tips for Each Function

### 1. `goal_commentary`

This function generates a commentary stream based on minute-by-minute match events.

**Tips:**
- Create an empty list to store the commentary strings
- Use a for loop to iterate through minutes 1 to n
- Use if/elif/else structure to determine what commentary to add for each minute
- Check divisibility by 3 and 5 using the modulo operator `%`
- Remember to check for "Spectacular Play!" first (divisible by both 3 and 5)

**Pseudocode:**
```
function goal_commentary(n):
    create empty commentary_list
    
    for minute from 1 to n:
        if minute is divisible by both 3 and 5:
            add "Spectacular Play!" to commentary_list
        else if minute is divisible by 3:
            add "Goal!" to commentary_list
        else if minute is divisible by 5:
            add "Save!" to commentary_list
        else:
            add "Minute minute" to commentary_list (where "minute" is the current number)
    
    return commentary_list
```

**Real-world application:** Commentary generation algorithms help create automated match reports and highlight potential key moments in games for further analysis.

### 2. `is_prime_jersey_number`

This function identifies if a jersey number has the special property of being prime.

**Tips:**
- A number less than 2 is not prime
- For a number n, you only need to check divisibility up to the square root of n
- Use a for loop to check all potential divisors
- Return False immediately if you find a divisor
- Return True if no divisors are found after checking all candidates

**Pseudocode:**
```
function is_prime_jersey_number(number):
    if number < 2:
        return False
    
    for i from 2 to square_root(number):
        if number is divisible by i:
            return False
    
    return True
```

**Real-world application:** Soccer analysts sometimes look for patterns in jersey number selection. Prime numbers are often worn by distinctive players with unique playing styles.

### 3. `find_season_extremes`

This function identifies the highest and lowest scoring matches in a season.

**Tips:**
- Initialize your highest and lowest variables with the first score in the list
- Loop through the rest of the scores, comparing each with your current highest/lowest
- Update your variables whenever you find a new extreme
- Return both values as a tuple

**Pseudocode:**
```
function find_season_extremes(match_scores):
    if match_scores is empty:
        return (None, None)
    
    highest = match_scores[0]
    lowest = match_scores[0]
    
    for score in match_scores:
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
    
    return (highest, lowest)
```

**Real-world application:** Understanding scoring extremes helps analysts identify outlier matches that may require special tactical analysis.

### 4. `calculate_performance_tier`

This function converts numerical player ratings into categorical performance tiers.

**Tips:**
- Use if/elif/else ladder for the different rating ranges
- Start with the highest tier and work down
- Make sure your conditions cover all possible inputs
- Be careful about the boundary values (e.g., exactly 80)

**Pseudocode:**
```
function calculate_performance_tier(player_rating):
    if player_rating >= 90 and player_rating <= 100:
        return "World Class"
    else if player_rating >= 80 and player_rating < 90:
        return "Elite"
    else if player_rating >= 70 and player_rating < 80:
        return "Quality"
    else if player_rating >= 60 and player_rating < 70:
        return "Average"
    else:
        return "Development Prospect"
```

**Real-world application:** Scouting departments use tiered rankings to quickly categorize player quality and potential in their databases.

### 5. `cumulative_goal_difference`

This function tracks how a team's performance evolves throughout a season.

**Tips:**
- Create an empty list to store the cumulative differences
- Initialize a variable to track the running total
- Loop through each match's goal difference
- Add each match difference to your running total
- Append the new running total to your results list

**Pseudocode:**
```
function cumulative_goal_difference(goal_differences):
    cumulative = []
    running_total = 0
    
    for difference in goal_differences:
        running_total = running_total + difference
        cumulative.append(running_total)
    
    return cumulative
```

**Real-world application:** Cumulative goal difference charts are used to visualize team performance trends throughout a season, identifying good and bad runs of form.

## Testing Your Code

Run the file by executing:

```python
python control_flow.py
```

If your implementations are correct, you should see output that matches the expected results in the docstrings.

## Further Exploration

After completing the challenge, consider:

1. How would you modify `goal_commentary` to include more match events like penalties, yellow cards, or injuries?

2. Can you enhance `cumulative_goal_difference` to also track points accumulated over the season?

3. What other patterns could you detect in match data using control flow structures?

## Connect to Capstone

These functions represent the decision-making logic you'll need for your NCAA soccer analysis capstone. As you work through this challenge, think about:

- What soccer events and patterns will you need to identify in your data?
- How will you convert raw numbers into meaningful performance categories?
- What accumulation patterns might reveal trends in team or player performance?

Mastering control flow is essential for building the analytical components of your capstone project!