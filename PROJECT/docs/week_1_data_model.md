# NCAA Soccer Player Analysis Data Model

This document outlines a proposed data model based on the Week 1 data collection planning analysis. This model serves as a foundation for the database schema implementation in the capstone project.

## Core Entities

### Player
```
Player {
    player_id (PK)
    first_name
    last_name
    date_of_birth
    height_cm
    weight_kg
    primary_position
    secondary_position
    dominant_foot
    jersey_number
    academic_year
    redshirt_status
    eligibility_remaining
    academic_major
    hometown
    previous_team_id (FK)
    recruitment_ranking
    injury_history_id (FK)
}
```

### Team
```
Team {
    team_id (PK)
    team_name
    university
    conference
    division
    head_coach
    assistant_coaches
    home_venue
    team_colors
    mascot
    foundation_year
    website_url
}
```

### Match
```
Match {
    match_id (PK)
    date
    time
    home_team_id (FK)
    away_team_id (FK)
    venue
    attendance
    weather_conditions
    field_condition
    referee
    broadcast_status
    competition_type
    season_phase
    home_score
    away_score
    match_duration
    overtime_periods
    match_status
}
```

### PlayerPerformance
```
PlayerPerformance {
    performance_id (PK)
    player_id (FK)
    match_id (FK)
    team_id (FK)
    position_played
    minutes_played
    start_minute
    end_minute
    goals
    assists
    shots
    shots_on_target
    passes_attempted
    passes_completed
    tackles
    interceptions
    fouls_committed
    fouls_suffered
    yellow_cards
    red_cards
    offsides
    ball_touches
    duels_won
    duels_lost
    distance_covered_km
    max_speed_kmh
    sprint_count
}
```

### AdvancedMetrics
```
AdvancedMetrics {
    metric_id (PK)
    performance_id (FK)
    expected_goals
    expected_assists
    xg_chain
    xg_buildup
    progressive_passes
    key_passes
    final_third_entries
    defensive_actions
    pressing_actions
    pressing_success_rate
    possession_won_attacking_third
    progressive_carries
    aerial_duels_won
    aerial_duels_lost
    clean_sheet_contribution
    build_up_involvement
    calculation_timestamp
    calculation_method_version
}
```

### GameContext
```
GameContext {
    context_id (PK)
    match_id (FK)
    score_state
    time_segment
    tactical_formation_home
    tactical_formation_away
    possession_percentage_home
    possession_percentage_away
    game_state_description
    high_pressure_period
}
```

### PlayerGameContext
```
PlayerGameContext {
    id (PK)
    performance_id (FK)
    context_id (FK)
    minutes_in_context
    actions_in_context
    success_rate_in_context
}
```

## Relationship Diagram

```
Player 1──┐
          │
          │ N
Team 1────┼────N Match
          │
          │ N
          │
          └───N PlayerPerformance 1────1 AdvancedMetrics
                      │
                      │ N
                      │
                      └────N PlayerGameContext N────1 GameContext
```

## Additional Support Tables

### Position
```
Position {
    position_id (PK)
    position_name
    position_category
    position_abbreviation
    position_description
}
```

### Season
```
Season {
    season_id (PK)
    start_date
    end_date
    season_name
    regular_season_start
    regular_season_end
    postseason_start
    postseason_end
}
```

### Conference
```
Conference {
    conference_id (PK)
    conference_name
    division
    region
    number_of_teams
    conference_champion_id (FK)
    conference_website
}
```

### InjuryHistory
```
InjuryHistory {
    injury_id (PK)
    player_id (FK)
    injury_type
    body_location
    start_date
    end_date
    matches_missed
    severity
    recurrence
    treatment_notes
}
```

### TrainingSession
```
TrainingSession {
    session_id (PK)
    team_id (FK)
    date
    duration
    session_type
    focus_area
    intensity_level
}
```

### PlayerTraining
```
PlayerTraining {
    id (PK)
    player_id (FK)
    session_id (FK)
    attendance_status
    performance_rating
    notes
}
```

## Implementation Notes

1. **Normalization Level**: The schema follows third normal form (3NF) to reduce data redundancy while maintaining practical query performance.

2. **Temporal Data**: Performance data is stored at the match level but can be aggregated to different time periods (weekly, monthly, season) through queries.

3. **Position Flexibility**: The schema supports players appearing in different positions across matches.

4. **Context Awareness**: The GameContext and PlayerGameContext tables enable analyzing performance in specific game situations.

5. **Extensibility**: The design allows for adding new metrics without schema changes by potentially using JSON columns for experimental metrics.

6. **Data Volume Considerations**: 
   - Assuming 30 players per team
   - 200 NCAA Division II teams
   - 20 matches per season
   - ~120,000 player performance records per season

7. **Indexing Strategy**:
   - Primary keys: B-tree indexes
   - Foreign keys: B-tree indexes
   - Frequently queried fields: player_id, team_id, match_id, date
   - Consider composite indexes for common query patterns

8. **Data Partitioning**:
   - Consider partitioning large tables (PlayerPerformance) by season for improved query performance

This data model serves as a starting point and should be refined during the implementation phase of the capstone project based on specific requirements and performance considerations.