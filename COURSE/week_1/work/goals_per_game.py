#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = ["rich", "pandas"]
# ///

import csv
import os
import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

def load_data_from_csv(csv_file):
    """
    Load player goals data from a CSV file.

    Args:
        csv_file (str): Path to the CSV file

    Returns:
        dict: Dictionary mapping player names to their goals data
    """
    if not os.path.exists(csv_file):
        console.print(f"[bold red]Error: File {csv_file} not found[/]")
        return {}

    player_data = {}

    df = pd.read_csv(csv_file)

    for _, player in df.groupby('player_name'):
        name = player['player_name'].iloc[0]
        goals_list = player['goals'].tolist()
        games_played = len(goals_list)

        player_data[name] = {
            'goals': goals_list,
            'games_played': games_played
        }

    return player_data

def calculate_goals_per_game(goals, games_played):
    """
    Calculate the average goals per game for a soccer player.

    Args:
        goals (list): A list of goals scored in each game
        games_played (int): Number of games played

    Returns:
        float: The average goals per game, or 0 if no games were played

    Example:
        >>> calculate_goals_per_game([1, 0, 2, 1], 4)
        1.0
    """
    if games_played == 0:
        return 0.0

    total_goals = sum(goals)
    return total_goals / games_played


def display_result(title, goals, games, result):
    """Display calculation results in a Rich panel"""
    content = Text()
    content.append(f"Goals: {goals}\n", style="cyan")
    content.append(f"Games played: {games}\n", style="cyan")
    content.append(f"Average goals per game: ", style="cyan")
    content.append(f"{result:.2f}", style="bold green")

    panel = Panel(
        content,
        title=title,
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)


def display_player_stats(player_data):
    """Display player statistics in a Rich table"""
    table = Table(title="Player Statistics", show_header=True, header_style="bold magenta")
    table.add_column("Player", style="cyan")
    table.add_column("Goals", style="cyan")
    table.add_column("Games", style="cyan", justify="center")
    table.add_column("Average", style="green", justify="right")

    for player_name, data in player_data.items():
        goals = data['goals']
        games = data['games_played']
        avg = calculate_goals_per_game(goals, games)
        table.add_row(player_name, str(goals), str(games), f"{avg:.2f}")

    console.print(table)


def main():
    # Title display
    console.print("[bold blue underline]Soccer Player - Goals Per Game Calculator[/]\n")

    # Load data from CSV
    csv_file = "player_goals.csv"
    player_data = load_data_from_csv(csv_file)

    if not player_data:
        # If CSV loading fails, use example data
        console.print("[yellow]Using example data instead...[/]\n")

        # Example with hard-coded data (fallback)
        test_goals = [1, 0, 2, 1]
        test_games = 4
        result = calculate_goals_per_game(test_goals, test_games)
        display_result("Example Case", test_goals, test_games, result)

        # Test edge case with no games played
        result_no_games = calculate_goals_per_game([], 0)
        display_result("Edge Case - No Games Played", [], 0, result_no_games)

        # Test with more examples
        test_cases = [
            ([2, 1, 3, 0, 1], 5),
            ([0, 0, 0], 3),
            ([5], 1),
        ]

        table = Table(title="Additional Test Cases", show_header=True, header_style="bold magenta")
        table.add_column("Goals", style="cyan")
        table.add_column("Games", style="cyan", justify="center")
        table.add_column("Average", style="green", justify="right")

        for goals, games in test_cases:
            avg = calculate_goals_per_game(goals, games)
            table.add_row(str(goals), str(games), f"{avg:.2f}")

        console.print(table)
    else:
        # Display player statistics from CSV data
        display_player_stats(player_data)


if __name__ == "__main__":
    main()