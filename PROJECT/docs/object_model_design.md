# NCAA Soccer Analysis System - Object Model Design

---

## 1. Core Classes and Object Model

### Core Entity Classes

#### Competition Management

- **Division**
  - id: int
  - name: str (Division I, II, III)
  - max_scholarships: int
  - compliance_rules: List[ComplianceRule]
  - created_at: datetime
  - updated_at: datetime

- **Conference**
  - id: int
  - name: str
  - division: Division
  - teams: List[Team]
  - reporting_standards: Dict

- **Season**
  - id: int
  - year: int
  - start_date: date
  - end_date: date
  - division: Division
  - academic_calendar: AcademicCalendar
  - matches: List[Match]

#### Team and Player

- **Team**
  - id: int
  - name: str
  - conference: Conference
  - division: Division
  - home_stadium: Stadium
  - coaching_staff: List[Coach]
  - current_roster: List[Player]
  - team_stats: TeamStatistics

- **Player**
  - id: int
  - first_name: str
  - last_name: str
  - student_id: str (encrypted)
  - eligibility_status: EligibilityStatus
  - academic_info: AcademicRecord
  - position: Position
  - jersey_number: int
  - height: float
  - weight: float
  - dominant_foot: str
  - recruit_info: RecruitmentRecord
  - performance_stats: PlayerStatistics
  - injury_history: List[InjuryRecord]

#### Match and Event

- **Match**
  - id: int
  - home_team: Team
  - away_team: Team
  - venue: Stadium
  - datetime: datetime
  - season: Season
  - match_officials: List[Official]
  - weather_conditions: WeatherData
  - attendance: int
  - match_events: List[MatchEvent]
  - formations: List[Formation]
  - match_stats: MatchStatistics

- **MatchEvent**
  - id: int
  - match: Match
  - event_type: EventType
  - timestamp: float
  - player: Player
  - team: Team
  - location: Coordinates
  - outcome: str
  - related_player: Player (optional)
  - metadata: Dict

#### Tactical

- **Formation**
  - id: int
  - match: Match
  - team: Team
  - start_time: float
  - end_time: float
  - shape: str (e.g., "4-4-2")
  - player_positions: List[PlayerPosition]
  - phase: str (attacking/defensive/transition)

- **PlayerPosition**
  - player: Player
  - formation: Formation
  - tactical_role: str
  - avg_x: float
  - avg_y: float
  - movement_radius: float
  - heat_map: HeatMapData

---

### Supporting Classes

#### NCAA-Specific

- **EligibilityStatus**
  - player: Player
  - current_year: int (1-4 or graduate)
  - games_played: int
  - games_remaining: int
  - redshirt_status: bool
  - transfer_status: TransferStatus
  - compliance_flags: List[ComplianceIssue]

- **AcademicRecord**
  - player: Player
  - gpa: float
  - major: str
  - credit_hours: int
  - academic_standing: str
  - progress_toward_degree: float

- **RecruitmentRecord**
  - player: Player
  - high_school: str
  - club_team: str
  - recruitment_rating: float
  - contact_log: List[ContactRecord]
  - official_visits: List[OfficialVisit]
  - commitment_date: date
  - scholarship_amount: float

#### Analytics

- **PlayerStatistics**
  - player: Player
  - season: Season
  - matches_played: int
  - minutes_played: float
  - goals: int
  - assists: int
  - shots: int
  - passes_completed: int
  - tackles_won: int
  - distance_covered: float
  - sprint_count: int
  - expected_goals: float
  - expected_assists: float

- **TeamStatistics**
  - team: Team
  - season: Season
  - matches_played: int
  - wins: int
  - draws: int
  - losses: int
  - goals_for: int
  - goals_against: int
  - possession_avg: float
  - pass_accuracy: float
  - pressing_intensity: float

- **TacticalAnalysis**
  - match: Match
  - team: Team
  - formation_changes: List[Formation]
  - passing_network: PassingNetwork
  - pitch_control: PitchControlData
  - pressing_triggers: List[PressingEvent]
  - transition_effectiveness: float

---

### Event Type Hierarchy

- **EventType**
  - name: str
  - category: str

- **PassEvent** (inherits from MatchEvent)
  - pass_length: float
  - pass_angle: float
  - is_progressive: bool
  - under_pressure: bool
  - body_part: str

- **ShotEvent** (inherits from MatchEvent)
  - shot_type: str
  - distance_to_goal: float
  - angle_to_goal: float
  - xG_value: float
  - body_part: str
  - is_first_time: bool

- **DefensiveEvent** (inherits from MatchEvent)
  - action_type: str (tackle/interception/block)
  - duel_won: bool
  - recovery_location: str

---

## 2. Class Diagrams and Relationships

### Core Relationships

- Division (1) → (*) Conference
- Division (1) → (*) Season
- Conference (1) → (*) Team
- Team (1) → (*) Player [current roster]
- Team (*) ↔ (*) Match [home/away teams]
- Match (1) → (*) MatchEvent
- Match (1) → (*) Formation
- Formation (1) → (*) PlayerPosition
- Player (1) → (*) PlayerPosition
- Player (1) → (1) EligibilityStatus
- Player (1) → (1) AcademicRecord
- Player (1) → (*) MatchEvent

### Inheritance Hierarchy

```
MatchEvent (Abstract Base)
    ├── BallEvent
    │   ├── PassEvent
    │   ├── ShotEvent
    │   └── DribbleEvent
    ├── DefensiveEvent
    │   ├── TackleEvent
    │   ├── InterceptionEvent
    │   └── BlockEvent
    └── SetPieceEvent
        ├── CornerEvent
        ├── FreeKickEvent
        └── PenaltyEvent
```

### Composition & Aggregation

- Team **has-a** TeamStatistics (composition)
- Player **has-a** PlayerStatistics (composition)
- Player **has-a** AcademicRecord (composition)
- Match **has-a** MatchStatistics (composition)
- Formation **has-a** List<PlayerPosition> (composition)
- Conference **uses** List<Team> (aggregation)
- Season **uses** List<Match> (aggregation)
- Team **uses** List<Player> (aggregation - players can transfer)

### Multiplicity Examples

- One Division has many Conferences (1:*)
- One Conference has many Teams (1:*)
- One Team has many Players (1:*) at a given time
- One Player can have many Teams over career (*:*)
- One Match has exactly two Teams (1:2)
- One Match has many Events (1:*)
- One Formation has 11 PlayerPositions (1:11)

---

## 3. Design Decisions and Patterns

### Inheritance Structure

- **Event Hierarchy:**  
  Uses single inheritance with abstract base class `MatchEvent` for shared properties (timestamp, location, player). Specialized events inherit and add specific attributes, enabling polymorphism and type safety.

- **Player-Team Temporal Relationship:**  
  Uses composition with temporal validity (e.g., `PlayerTeamHistory` tracks all affiliations with start/end dates), supporting transfers and eligibility tracking.

### Encapsulation

```python
class Player:
    def __init__(self, student_id: str):
        self.__student_id = self._encrypt(student_id)  # Private, encrypted
        self._eligibility_status = None  # Protected
        self.jersey_number = None  # Public
    
    @property
    def student_id(self):
        # Read-only access with audit logging
        self._log_access("student_id", current_user)
        return self.__student_id
    
    def update_eligibility(self, new_status: EligibilityStatus):
        # Business logic validation
        if self._validate_eligibility_change(new_status):
            self._eligibility_status = new_status
            self._notify_compliance_office()
```

- **Private:** Student IDs, medical records (FERPA/HIPAA compliance)
- **Protected:** Eligibility status, academic records (coach/admin access only)
- **Public:** Performance statistics, game events

### Design Patterns Used

#### 1. Observer Pattern (Real-time notifications)

```python
class MatchEventPublisher:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer: EventObserver):
        self._observers.append(observer)
    
    def notify(self, event: MatchEvent):
        for observer in self._observers:
            observer.update(event)

class InjuryRiskObserver(EventObserver):
    def update(self, event: MatchEvent):
        if isinstance(event, SprintEvent):
            self._check_fatigue_threshold(event.player)
```

#### 2. Strategy Pattern (Configurable analytics algorithms)

```python
class FormationDetectionStrategy(ABC):
    @abstractmethod
    def detect_formation(self, player_positions: List[PlayerPosition]) -> Formation:
        pass

class TemplateMatchingStrategy(FormationDetectionStrategy):
    def detect_formation(self, player_positions):
        # Template-based detection logic
        pass

class ClusteringStrategy(FormationDetectionStrategy):
    def detect_formation(self, player_positions):
        # ML clustering approach
        pass
```

#### 3. Repository Pattern (Data access abstraction)

```python
class PlayerRepository:
    def find_by_eligibility(self, status: str) -> List[Player]:
        # Abstracts database queries
        pass
    
    def find_transfers_by_conference(self, conference: Conference) -> List[Player]:
        # Complex query logic hidden from business layer
        pass
```

#### 4. Factory Pattern (Event creation from multiple sources)

```python
class EventFactory:
    @staticmethod
    def create_event(source_type: str, raw_data: Dict) -> MatchEvent:
        if source_type == "statsbomb":
            return StatsBombEventAdapter(raw_data).to_match_event()
        elif source_type == "hudl":
            return HudlEventAdapter(raw_data).to_match_event()
```

#### 5. Decorator Pattern (Adding contextual information)

```python
class PressureDecorator(MatchEventDecorator):
    def __init__(self, event: MatchEvent):
        self._event = event
        self._pressure_value = self._calculate_pressure()
    
    def get_pressure_context(self) -> float:
        return self._pressure_value
```

---

## 4. Supporting Project Requirements

### Data Collection and Storage

- **Multi-Source Integration:**  
  Factory pattern enables ingestion from multiple providers (Hudl, StatsBomb, manual entry). Adapter classes normalize formats. Event sourcing stores raw data for reprocessing.

- **Temporal Data Management:**  
  All entities include created_at/updated_at timestamps. Soft deletes preserve history. Temporal tables track eligibility changes.

- **Storage Architecture:**

```python
class DataStorageManager:
    def __init__(self):
        self.event_store = EventStore()  # Immutable event log
        self.read_store = PostgreSQL()   # Optimized for queries
        self.cache = Redis()             # Real-time data
        self.file_store = S3()           # Video/documents
```

### Analysis and Reporting

- **Player Performance Analysis:**

```python
class PlayerPerformanceAnalyzer:
    def analyze_player(self, player: Player, date_range: DateRange):
        return {
            'technical': self._analyze_technical_skills(player),
            'physical': self._analyze_physical_metrics(player),
            'tactical': self._analyze_tactical_awareness(player),
            'trend': self._calculate_performance_trend(player)
        }
```

- **Team Tactical Analysis:**

```python
class TacticalAnalyzer:
    def analyze_match_tactics(self, match: Match):
        return {
            'formations': self._detect_formation_changes(match),
            'pressing_intensity': self._calculate_pressing_metrics(match),
            'passing_networks': self._build_passing_networks(match),
            'space_control': self._analyze_pitch_control(match)
        }
```

- **Recruitment Analytics:**

```python
class RecruitmentAnalyzer:
    def evaluate_prospect(self, player: Player):
        return {
            'performance_score': self._calculate_performance_rating(player),
            'fit_score': self._assess_tactical_fit(player),
            'development_potential': self._project_growth(player),
            'academic_fit': self._evaluate_academic_profile(player)
        }
```

- **NCAA Compliance Reporting:**

```python
class ComplianceReporter:
    def generate_eligibility_report(self, team: Team):
        return {
            'roster_compliance': self._check_roster_limits(team),
            'academic_progress': self._verify_apr_compliance(team),
            'recruiting_violations': self._audit_contact_logs(team),
            'financial_aid': self._validate_scholarship_limits(team)
        }
```

### Extensibility for Future Features

- **Plugin Architecture:**

```python
class AnalyticsPlugin(ABC):
    @abstractmethod
    def process_event(self, event: MatchEvent):
        pass
    
    @abstractmethod
    def get_metrics(self) -> Dict:
        pass

class ExpectedThreatPlugin(AnalyticsPlugin):
    def process_event(self, event: MatchEvent):
        if isinstance(event, PassEvent):
            self._update_field_progression(event)
```

- **API Versioning:**

```python
class APIEndpoint:
    @version(1)
    def get_player_stats_v1(self, player_id: int):
        # Original implementation
        pass
    
    @version(2)
    def get_player_stats_v2(self, player_id: int):
        # Enhanced with new metrics
        pass
```

- **Feature Flags:**

```python
class FeatureManager:
    def is_enabled(self, feature: str, team: Team) -> bool:
        # Progressive rollout of new analytics
        return self._check_feature_flag(feature, team)
```

- **Machine Learning Integration:**

```python
class MLPipeline:
    def __init__(self):
        self.feature_store = FeatureStore()
        self.model_registry = ModelRegistry()
        self.prediction_service = PredictionService()
    
    def add_model(self, model_type: str, model: MLModel):
        # Extensible ML model integration
        self.model_registry.register(model_type, model)
```

---

**Summary:**  
This object model provides a comprehensive foundation for NCAA soccer analytics while maintaining flexibility for future enhancements. The design balances soccer-specific requirements with NCAA compliance needs, enabling sophisticated analysis while protecting student-athlete privacy.

