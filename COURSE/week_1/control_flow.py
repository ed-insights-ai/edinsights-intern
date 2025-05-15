"""
Control Flow Challenge: Soccer Edition
-------------------------------------
Complete the following functions according to their docstrings.
This exercise focuses on conditional statements and loops in Python
while introducing you to soccer match concepts.
"""

def goal_commentary(n):
    """
    Implement a soccer commentary generator based on goal patterns.
    """
    commentary = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            commentary.append("Spectacular Play!")
        elif i % 3 == 0:
            commentary.append("Goal!")
        elif i % 5 == 0:
            commentary.append("Save!")
        else:
            commentary.append(f"Minute {i}")
    return commentary

def is_prime_jersey_number(number):
    """
    Check if a jersey number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_season_extremes(match_scores):
    """
    Find the highest and lowest scoring matches in a season.
    """
    highest_score = match_scores[0]
    lowest_score = match_scores[0]
    for score in match_scores:
        if score > highest_score:
            highest_score = score
        if score < lowest_score:
            lowest_score = score
    return highest_score, lowest_score

def calculate_performance_tier(player_rating):
    """
    Convert a player's numerical rating to a performance tier.
    """
    if 90 <= player_rating <= 100:
        return "World Class"
    elif 80 <= player_rating < 90:
        return "Elite"
    elif 70 <= player_rating < 80:
        return "Quality"
    elif 60 <= player_rating < 70:
        return "Average"
    else:
        return "Development Prospect"

def cumulative_goal_difference(goal_differences):
    """
    Calculate the cumulative goal difference over a season.
    """
    cumulative = []
    total = 0
    for diff in goal_differences:
        total += diff
        cumulative.append(total)
    return cumulative

def main():
    """Run some examples to test your functions."""
    print("Testing goal_commentary...")
    print(f"goal_commentary(15) = {goal_commentary(15)}")
    
    print("\nTesting is_prime_jersey_number...")
    print(f"is_prime_jersey_number(7) = {is_prime_jersey_number(7)}")
    print(f"is_prime_jersey_number(10) = {is_prime_jersey_number(10)}")
    
    print("\nTesting find_season_extremes...")
    print(f"find_season_extremes([2, 0, 5, 1, 3]) = {find_season_extremes([2, 0, 5, 1, 3])}")
    
    print("\nTesting calculate_performance_tier...")
    print(f"calculate_performance_tier(85) = {calculate_performance_tier(85)}")
    
    print("\nTesting cumulative_goal_difference...")
    print(f"cumulative_goal_difference([1, -1, 2, 0, -2]) = {cumulative_goal_difference([1, -1, 2, 0, -2])}")

if __name__ == "__main__":
    main()