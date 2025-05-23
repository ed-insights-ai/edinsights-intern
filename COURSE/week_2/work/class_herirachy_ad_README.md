# Summary of Changes
## Improved Code Organization

- Arranged classes in proper inheritance order:  
  `Person → Player/StaffMember → Goalkeeper/FieldPlayer/Coach → Team`
- Added the required `import random` statement

## Enhanced Demonstration Code

- `create_team_roster()` now returns a `Team` object instead of a list
- Improved match simulation to demonstrate all class features
- Added formatted output for better readability

## Better Structure

- Consistent docstrings across all classes
- Main execution block clearly showcases each feature
- Improved relationships:  
  `Team` now contains `Players` and `StaffMembers`