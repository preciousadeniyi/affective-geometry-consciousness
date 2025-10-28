```python
"""
Affective Core Implementation for CDG Framework
Implements basic biological drives and interoceptive processing
"""

import numpy as np
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class DriveType(Enum):
    """Core biological drives based on Panksepp's affective neuroscience"""
    SEEK = 1      # Exploration, curiosity, anticipation
    AVOID = 2     # Fear, anxiety, threat response  
    REST = 3      # Sleep, energy conservation, recovery
    CARE = 4      # Nurturing, social attachment
    PLAY = 5      # Social engagement, joy
    RAGE = 6      # Anger, frustration, boundaries
    LUST = 7      # Sexual drive, reproduction

@dataclass
class DriveState:
    """Current state of a biological drive"""
    drive_type: DriveType
    current_level: float  # 0.0 to 1.0
    optimal_level: float  # Homeostatic set point
    urgency: float        # 0.0 to 1.0
    satisfaction_history: List[float]
    
    def tension(self) -> float:
        """Calculate tension as distance from optimal level"""
        return abs(self.current_level - self.optimal_level)
    
    def update(self, stimulus: float, delta_time: float) -> None:
        """Update drive level based on stimulus and time"""
        # Homeostatic drift toward optimal level
        homeostasis = (self.optimal_level - self.current_level) * 0.1
        
        # Stimulus effect
        stimulus_effect = stimulus * delta_time
        
        # Update level
        self.current_level = np.clip(
            self.current_level + homeostasis + stimulus_effect, 0.0, 1.0
        )
        
        # Update urgency based on tension
        self.urgency = self.tension()
        
        # Keep recent history
        self.satisfaction_history.append(self.current_level)
        if len(self.satisfaction_history) > 100:
            self.satisfaction_history.pop(0)

@dataclass  
class InteroceptiveSignal:
    """Internal bodily signal"""
    signal_type: str
    current_value: float
    optimal_range: Tuple[float, float]
    affective_weight: float  # How much this signal matters
    
    def is_optimal(self) -> bool:
        low, high = self.optimal_range
        return low <= self.current_value <= high
    
    def deviation(self) -> float:
        """How far from optimal range"""
        low, high = self.optimal_range
        if self.current_value < low:
            return low - self.current_value
        elif self.current_value > high:
            return self.current_value - high
        return 0.0

class AffectiveCore:
    """
    Core affective system implementing biological drives and interoception
    Models the subcortical foundations of consciousness
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        
        # Initialize core drives
        self.drives = self._initialize_drives()
        
        # Interoceptive signals (internal bodily states)
        self.interoceptive_signals = self._initialize_interoception()
        
        # Affective state history
        self.affective_history = []
        self.decision_history = []
        
        # Current affective tension
        self.current_tension = 0.0
        
        # Developmental stage
        self.developmental_stage = 1  # 1-3 for experimental phases
        
    def _initialize_drives(self) -> Dict[DriveType, DriveState]:
        """Initialize core biological drives with optimal levels"""
        return {
            DriveType.SEEK: DriveState(
                drive_type=DriveType.SEEK,
                current_level=0.5,
                optimal_level=0.6,  # Slightly curious by default
                urgency=0.0,
                satisfaction_history=[]
            ),
            DriveType.AVOID: DriveState(
                drive_type=DriveType.AVOID, 
                current_level=0.3,
                optimal_level=0.1,  # Prefer safety
                urgency=0.0,
                satisfaction_history=[]
            ),
            DriveType.REST: DriveState(
                drive_type=DriveType.REST,
                current_level=0.5,
                optimal_level=0.7,  # Prefer rested state
                urgency=0.0, 
                satisfaction_history=[]
            ),
            DriveType.CARE: DriveState(
                drive_type=DriveType.CARE,
                current_level=0.4,
                optimal_level=0.5,  # Moderate social drive
                urgency=0.0,
                satisfaction_history=[]
            ),
            DriveType.PLAY: DriveState(
                drive_type=DriveType.PLAY,
                current_level=0.3,
                optimal_level=0.4,  # Some playfulness
                urgency=0.0,
                satisfaction_history=[]
            ),
            DriveType.RAGE: DriveState(
                drive_type=DriveType.RAGE,
                current_level=0.1,
                optimal_level=0.05,  # Low anger optimal
                urgency=0.0,
                satisfaction_history=[]
            ),
            DriveType.LUST: DriveState(
                drive_type=DriveType.LUST,
                current_level=0.2, 
                optimal_level=0.3,  # Moderate sexual drive
                urgency=0.0,
                satisfaction_history=[]
            )
        }
    
    def _initialize_interoception(self) -> Dict[str, InteroceptiveSignal]:
        """Initialize internal bodily signal monitoring"""
        return {
            'energy': InteroceptiveSignal(
                signal_type='energy',
                current_value=0.8,
                optimal_range=(0.6, 0.9),
                affective_weight=0.9
            ),
            'integrity': InteroceptiveSignal(
                signal_type='integrity', 
                current_value=1.0,
                optimal_range=(0.8, 1.0),
                affective_weight=1.0  # High weight - survival critical
            ),
            'comfort': InteroceptiveSignal(
                signal_type='comfort',
                current_value=0.7,
                optimal_range=(0.5, 0.8),
                affective_weight=0.6
            ),
            'social_connection': InteroceptiveSignal(
                signal_type='social_connection',
                current_value=0.5,
                optimal_range=(0.4, 0.7), 
                affective_weight=0.7
            )
        }
    
    def update_drives(self, external_stimuli: Dict[DriveType, float], 
                     delta_time: float = 1.0) -> float:
        """
        Update all drives based on external stimuli and time passage
        Returns total affective tension
        """
        total_tension = 0.0
        
        for drive_type, drive_state in self.drives.items():
            # Get stimulus for this drive (0 if not specified)
            stimulus = external_stimuli.get(drive_type, 0.0)
            
            # Update drive state
            drive_state.update(stimulus, delta_time)
            
            # Add to total tension (weighted by urgency)
            total_tension += drive_state.urgency * drive_state.tension()
        
        # Update interoceptive-based tension
        interoceptive_tension = self._compute_interoceptive_tension()
        total_tension += interoceptive_tension
        
        self.current_tension = total_tension
        
        # Record affective state
        self.affective_history.append({
            'timestamp': len(self.affective_history),
            'tension': total_tension,
            'drive_states': {drive.name: state.current_level 
                           for drive, state in self.drives.items()},
            'interoceptive_states': {name: signal.current_value
                                   for name, signal in self.interoceptive_signals.items()}
        })
        
        # Keep history manageable
        if len(self.affective_history) > 1000:
            self.affective_history.pop(0)
            
        return total_tension
    
    def _compute_interoceptive_tension(self) -> float:
        """Compute tension from interoceptive signals"""
        tension = 0.0
        
        for signal_name, signal in self.interoceptive_signals.items():
            if not signal.is_optimal():
                deviation = signal.deviation()
                # Normalize deviation and weight by importance
                normalized_tension = (deviation * signal.affective_weight)
                tension += normalized_tension
                
        return tension
    
    def update_interoception(self, internal_changes: Dict[str, float]) -> None:
        """Update interoceptive signals based on internal changes"""
        for signal_name, change in internal_changes.items():
            if signal_name in self.interoceptive_signals:
                current_signal = self.interoceptive_signals[signal_name]
                current_signal.current_value = np.clip(
                    current_signal.current_value + change, 0.0, 1.0
                )
    
    def get_dominant_drive(self) -> Tuple[DriveType, float]:
        """Get the currently most urgent drive and its urgency"""
        most_urgent_drive = None
        highest_urgency = -1.0
        
        for drive_type, drive_state in self.drives.items():
            if drive_state.urgency > highest_urgency:
                highest_urgency = drive_state.urgency
                most_urgent_drive = drive_type
                
        return most_urgent_drive, highest_urgency
    
    def compute_affective_conflict(self) -> float:
        """
        Compute current level of affective conflict between drives
        High conflict indicates competing biological imperatives
        """
        urgent_drives = []
        
        for drive_type, drive_state in self.drives.items():
            if drive_state.urgency > 0.3:  # Only consider moderately urgent drives
                urgent_drives.append((drive_type, drive_state))
        
        if len(urgent_drives) < 2:
            return 0.0  # No significant conflict
        
        # Compute conflict as product of urgent drives with opposing valences
        conflict = 0.0
        for i, (drive1, state1) in enumerate(urgent_drives):
            for drive2, state2 in urgent_drives[i+1:]:
                # Approximate valence opposition (simplified)
                if self._drives_opposed(drive1, drive2):
                    conflict += state1.urgency * state2.urgency
                    
        return conflict
    
    def _drives_opposed(self, drive1: DriveType, drive2: DriveType) -> bool:
        """Check if two drives typically have opposing action tendencies"""
        opposed_pairs = [
            (DriveType.SEEK, DriveType.AVOID),   # Approach vs Avoid
            (DriveType.RAGE, DriveType.CARE),    # Anger vs Nurturing
            (DriveType.PLAY, DriveType.REST),    # Activity vs Rest
        ]
        
        return (drive1, drive2) in opposed_pairs or (drive2, drive1) in opposed_pairs
    
    def get_affective_summary(self) -> Dict:
        """Get comprehensive summary of current affective state"""
        dominant_drive, urgency = self.get_dominant_drive()
        
        return {
            'current_tension': self.current_tension,
            'affective_conflict': self.compute_affective_conflict(),
            'dominant_drive': dominant_drive.name if dominant_drive else None,
            'dominant_urgency': urgency,
            'drive_states': {
                drive.name: {
                    'level': state.current_level,
                    'urgency': state.urgency,
                    'tension': state.tension()
                }
                for drive, state in self.drives.items()
            },
            'interoceptive_states': {
                name: {
                    'value': signal.current_value,
                    'optimal': signal.is_optimal(),
                    'deviation': signal.deviation()
                }
                for name, signal in self.interoceptive_signals.items()
            },
            'developmental_stage': self.developmental_stage
        }
    
    def record_decision(self, decision_context: Dict, choice: str) -> None:
        """Record a decision for later analysis"""
        self.decision_history.append({
            'timestamp': len(self.decision_history),
            'context': decision_context,
            'choice': choice,
            'affective_state': self.get_affective_summary()
        })
        
        # Keep history manageable
        if len(self.decision_history) > 500:
            self.decision_history.pop(0)
    
    def advance_developmental_stage(self) -> None:
        """Advance to next developmental stage (for Experiment 4)"""
        if self.developmental_stage < 3:
            self.developmental_stage += 1
            
            # Adjust drive optimal levels based on development
            if self.developmental_stage == 2:  # Predictive phase
                # Increase SEEK and PLAY for exploration
                self.drives[DriveType.SEEK].optimal_level = 0.7
                self.drives[DriveType.PLAY].optimal_level = 0.6
                
            elif self.developmental_stage == 3:  # Extended self phase
                # Balance all drives for integrated functioning
                for drive in self.drives.values():
                    drive.optimal_level = 0.5  # Balanced state

# Example usage and testing
if __name__ == "__main__":
    # Create affective core
    core = AffectiveCore()
    
    # Simulate some stimuli
    stimuli = {
        DriveType.SEEK: 0.3,   # Interesting discovery
        DriveType.AVOID: 0.4,  # Potential threat detected
        DriveType.REST: -0.2   # Getting tired
    }
    
    # Update drives
    tension = core.update_drives(stimuli)
    
    # Get affective summary
    summary = core.get_affective_summary()
    
    print("Affective Core Test")
    print(f"Current tension: {tension:.3f}")
    print(f"Affective conflict: {summary['affective_conflict']:.3f}")
    print(f"Dominant drive: {summary['dominant_drive']}")
    print("\nDrive states:")
    for drive_name, state in summary['drive_states'].items():
        print(f"  {drive_name}: level={state['level']:.3f}, "
              f"urgency={state['urgency']:.3f}")
```
