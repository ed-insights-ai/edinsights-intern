#!/usr/bin/env python3

"""
Pretty Soccer Analytics Display
-------------------------------
This script implements the soccer analytics functions from functions.py
but displays the results using rich for prettier console output.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Create console instance
console = Console()

def calculate_win_percentage(wins, draws, losses):
    """
    Calculate the win percentage for a soccer team.
    
    The formula is: (wins + draws * 0.5) / total_matches * 100
    
    Args:
        wins (int): Number of wins
        draws (int): Number of draws
        losses (int): Number of losses
        
    Returns:
        float: The win percentage (0-100)
    """
    total_matches = wins + draws + losses
    if total_matches == 0:
        return 0.0
    return (wins + draws * 0.5) / total_matches * 100


def format_player_info(first_name, last_name, position, team=None, jersey_number=None):
    """
    Format player information into a standard string representation.
    
    Args:
        first_name (str): Player's first name
        last_name (str): Player's last name
        position (str): Player's position
        team (str, optional): Player's team. Defaults to None.
        jersey_number (int, optional): Player's jersey number. Defaults to None.
        
    Returns:
        str: Formatted player information
    """
    info = f"{first_name} {last_name} ({position}"
    if jersey_number:
        info += f", #{jersey_number}"
    info += ")"
    if team:
        info += f" - {team}"
    return info


def calculate_points(*match_results):
    """
    Calculate total points earned from a series of match results.

    In soccer, a win is worth 3 points, a draw is worth 1 point,
    and a loss is worth 0 points.

    Args:
        *match_results: Variable number of match results ('W', 'D', or 'L')

    Returns:
        int: Total points earned
    """
    points = 0
    for result in match_results:
        if result == 'W':
            points += 3
        elif result == 'D':
            points += 1
        # Loss ('L') adds 0 points, so no need to handle explicitly
    return points


def analyze_match_stats(team_stats, opponent_stats):
    """
    Analyze match statistics and determine areas of strength and weakness.
    
    Args:
        team_stats (dict): Dictionary containing team statistics
        opponent_stats (dict): Dictionary containing opponent statistics
        
    Returns:
        dict: Dictionary containing analysis results
    """
    possession_difference = team_stats['possession'] - opponent_stats['possession']
    shots_accuracy = round((team_stats['shots_on_target'] / team_stats['shots']) * 100, 2) if team_stats['shots'] > 0 else 0
    passing_accuracy = round((team_stats['passes_completed'] / team_stats['passes']) * 100, 2) if team_stats['passes'] > 0 else 0

    strengths = []
    weaknesses = []

    for key in team_stats:
        if key in opponent_stats and key != 'fouls':  # Exclude 'fouls' from default comparison
            if team_stats[key] > opponent_stats[key]:
                strengths.append(key)
            elif team_stats[key] < opponent_stats[key]:
                weaknesses.append(key)

    # Special handling for fouls (lower is better)
    if team_stats['fouls'] < opponent_stats['fouls']:
        strengths.append('fouls')
    elif team_stats['fouls'] > opponent_stats['fouls']:
        weaknesses.append('fouls')

    return {
        'possession_difference': possession_difference,
        'shots_accuracy': shots_accuracy,
        'passing_accuracy': passing_accuracy,
        'strengths': strengths,
        'weaknesses': weaknesses
    }


def generate_league_table(team_results):
    """
    Generate a league table (standings) from team results.
    
    Args:
        team_results (dict): Dictionary where keys are team names and values are lists
                            of match results ('W', 'D', or 'L')
        
    Returns:
        list: List of dictionaries with team stats, sorted by points
    """
    league_table = []

    for team, results in team_results.items():
        played = len(results)
        won = results.count('W')
        drawn = results.count('D')
        lost = results.count('L')
        points = won * 3 + drawn * 1

        league_table.append({
            'team': team,
            'played': played,
            'won': won,
            'drawn': drawn,
            'lost': lost,
            'points': points
        })

    league_table.sort(key=lambda x: x['points'], reverse=True)
    return league_table


def display_win_percentage():
    """Display win percentage with rich formatting"""
    console.print(Panel.fit(
        "[bold cyan]Win Percentage Calculator[/bold cyan]\n\n"
        "This calculator determines a team's win percentage based on their match results.",
        title="Function 1", 
        border_style="cyan"
    ))
    
    result = calculate_win_percentage(10, 5, 5)
    
    console.print(f"\nCalculate: [bold]10 wins, 5 draws, 5 losses[/bold]")
    console.print(f"Win Percentage = [bold green]{result:.2f}%[/bold green]")
    console.print(f"Formula: (wins + 0.5 * draws) / total_matches * 100")
    console.print(f"         (10 + 0.5 * 5) / 20 * 100 = {result:.2f}%\n")


def display_player_info():
    """Display player info with rich formatting"""
    console.print(Panel.fit(
        "[bold magenta]Player Information Formatter[/bold magenta]\n\n"
        "This formatter creates a standardized display of player information.",
        title="Function 2", 
        border_style="magenta"
    ))
    
    player1 = format_player_info("Lionel", "Messi", "Forward", "Inter Miami", 10)
    player2 = format_player_info("Cristiano", "Ronaldo", "Forward")
    
    console.print("\n[bold]Player 1:[/bold]")
    console.print(Panel(player1, style="green"))
    
    console.print("\n[bold]Player 2:[/bold]")
    console.print(Panel(player2, style="yellow"))


def display_points_calculation():
    """Display points calculation with rich formatting"""
    console.print(Panel.fit(
        "[bold blue]Match Points Calculator[/bold blue]\n\n"
        "This calculator determines total points earned based on match results.\n"
        "Win (W) = 3 points, Draw (D) = 1 point, Loss (L) = 0 points",
        title="Function 3", 
        border_style="blue"
    ))
    
    results = ['W', 'D', 'W', 'L', 'D']
    points = calculate_points(*results)
    
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Match", style="dim", width=6)
    table.add_column("Result", width=6)
    table.add_column("Points", justify="right", width=6)
    
    for i, result in enumerate(results, 1):
        result_style = "green" if result == 'W' else "yellow" if result == 'D' else "red"
        points_value = 3 if result == 'W' else 1 if result == 'D' else 0
        table.add_row(f"{i}", f"[{result_style}]{result}[/{result_style}]", f"{points_value}")
    
    console.print("\n[bold]Match Results:[/bold]")
    console.print(table)
    console.print(f"\n[bold]Total Points: [green]{points}[/green][/bold]")


def display_match_analysis():
    """Display match analysis with rich formatting"""
    console.print(Panel.fit(
        "[bold red]Match Statistics Analyzer[/bold red]\n\n"
        "This analyzer compares team vs opponent statistics to identify strengths and weaknesses.",
        title="Function 4", 
        border_style="red"
    ))
    
    team_stats = {
        'possession': 60,
        'shots': 15,
        'shots_on_target': 7,
        'passes': 500,
        'passes_completed': 450,
        'corners': 7,
        'fouls': 10
    }
    
    opponent_stats = {
        'possession': 40,
        'shots': 10,
        'shots_on_target': 3,
        'passes': 300,
        'passes_completed': 250,
        'corners': 3,
        'fouls': 15
    }
    
    analysis = analyze_match_stats(team_stats, opponent_stats)
    
    # Create a comparison table
    table = Table(show_header=True, header_style="bold red")
    table.add_column("Statistic", style="dim")
    table.add_column("Our Team", justify="right")
    table.add_column("Opponent", justify="right")
    table.add_column("Difference", justify="right")
    
    for stat in team_stats:
        # Determine if this is a strength or weakness
        style = ""
        diff = ""
        
        if stat == 'fouls':
            # For fouls, lower is better
            diff_value = opponent_stats[stat] - team_stats[stat]
            diff = f"{diff_value:+d}"
            style = "green" if diff_value > 0 else "red" if diff_value < 0 else ""
        else:
            diff_value = team_stats[stat] - opponent_stats[stat]
            diff = f"{diff_value:+d}"
            style = "green" if diff_value > 0 else "red" if diff_value < 0 else ""
        
        table.add_row(
            stat.replace('_', ' ').title(),
            f"{team_stats[stat]}", 
            f"{opponent_stats[stat]}",
            f"[{style}]{diff}[/{style}]" if style else diff
        )
    
    console.print("\n[bold]Match Statistics Comparison:[/bold]")
    console.print(table)
    
    # Display analysis results
    console.print("\n[bold]Key Metrics:[/bold]")
    console.print(f"Possession Difference: [{'green' if analysis['possession_difference'] > 0 else 'red'}]{analysis['possession_difference']:+d}%[/{'green' if analysis['possession_difference'] > 0 else 'red'}]")
    console.print(f"Shots Accuracy: [bold]{analysis['shots_accuracy']:.1f}%[/bold]")
    console.print(f"Passing Accuracy: [bold]{analysis['passing_accuracy']:.1f}%[/bold]")
    
    strengths_text = Text("\n[Strengths]", style="bold green")
    for strength in analysis['strengths']:
        strengths_text.append(f"\n• {strength.replace('_', ' ').title()}")
    
    weaknesses_text = Text("\n[Weaknesses]", style="bold red")
    for weakness in analysis['weaknesses']:
        weaknesses_text.append(f"\n• {weakness.replace('_', ' ').title()}")
    
    analysis_panel = Panel.fit(
        Text.assemble(strengths_text, "\n\n", weaknesses_text),
        title="Analysis Summary",
        border_style="yellow"
    )
    
    console.print(analysis_panel)


def display_league_table():
    """Display league table with rich formatting"""
    console.print(Panel.fit(
        "[bold green]League Table Generator[/bold green]\n\n"
        "This generator creates a sorted league standings table from match results.",
        title="Function 5", 
        border_style="green"
    ))
    
    team_results = {
        'Team A': ['W', 'W', 'D', 'L', 'W'],
        'Team B': ['L', 'W', 'D', 'W', 'D'],
        'Team C': ['D', 'L', 'L', 'D', 'L']
    }
    
    standings = generate_league_table(team_results)
    
    # Display team results first
    console.print("\n[bold]Team Results:[/bold]")
    for team, results in team_results.items():
        result_string = ""
        for result in results:
            if result == 'W':
                result_string += "[green]W[/green] "
            elif result == 'D':
                result_string += "[yellow]D[/yellow] "
            else:
                result_string += "[red]L[/red] "
        
        console.print(f"{team}: {result_string}")
    
    # Create league table
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Pos", style="dim", width=4)
    table.add_column("Team", min_width=10)
    table.add_column("Played", justify="center")
    table.add_column("W", justify="center")
    table.add_column("D", justify="center")
    table.add_column("L", justify="center")
    table.add_column("Points", justify="center")
    
    for i, team in enumerate(standings, 1):
        table.add_row(
            f"{i}", 
            f"[bold]{team['team']}[/bold]", 
            f"{team['played']}", 
            f"[green]{team['won']}[/green]", 
            f"[yellow]{team['drawn']}[/yellow]", 
            f"[red]{team['lost']}[/red]", 
            f"[bold]{team['points']}[/bold]"
        )
    
    console.print("\n[bold]League Table:[/bold]")
    console.print(table)


def main():
    """Display all soccer analytics functions with rich formatting"""
    console.print("\n")
    console.print(Panel.fit(
        "[bold]Soccer Analytics Toolkit[/bold]\n\n"
        "A collection of functions for analyzing soccer data with rich formatting",
        title="⚽ Soccer Analytics", 
        subtitle="NCAA Division II Analysis",
        border_style="bright_blue"
    ))
    
    console.print("\n")
    display_win_percentage()
    console.print("\n" + "="*80 + "\n")
    
    display_player_info()
    console.print("\n" + "="*80 + "\n")
    
    display_points_calculation()
    console.print("\n" + "="*80 + "\n")
    
    display_match_analysis()
    console.print("\n" + "="*80 + "\n")
    
    display_league_table()
    console.print("\n")


if __name__ == "__main__":
    main()