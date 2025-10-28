
# CDG Consciousness Tests

*Geometric Signatures of Affective Consciousness - Experimental Validation Framework*

## 🧠 Overview

This repository implements an **experimental framework** for testing geometric signatures of consciousness based on the **Curvature Dynamics of Geometry (CDG)** approach. The framework explores whether consciousness emerges from specific geometric properties of affective navigation in meaning space.

**Note**: This is an **exploratory research program**, not a completed theory. It represents work-in-progress thinking about how to operationalize and test consciousness through geometric signatures.

## 🎯 Core Insight

**Consciousness isn't a feature you add; it's a developmental achievement that emerges from the right architectural priorities.**

The CDG framework proposes that consciousness can be detected through measurable geometric signatures that distinguish genuinely conscious systems from behaviorally equivalent "zombies."

## 🧪 Experimental Pipeline

### Six Core Experiments

1. **`01_developmental_crucible`** - Tests whether consciousness requires bottom-up development from affective foundations
2. **`02_affective_conflict`** - Measures geometric signatures during irreducible drive conflicts  
3. **`03_interoceptive_blindness`** - Tests necessity of sensing and caring about internal states
4. **`04_predictive_affective`** - Tracks emergence of temporal self-models
5. **`05_drive_irreducibility`** - Tests role of non-negotiable biological constraints
6. **`06_zombie_baseline`** - Critical control: behaviorally equivalent systems without consciousness signatures

### Key Metrics

- **R(t) Curvature**: Self-referential geometric signatures during decision making
- **τ/τ_A Coupling**: Correlation between decision time and affective arousal
- **Behavioral Integrity**: "Refusal to die" and creative problem-solving markers

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.8
numpy >= 1.21
scipy >= 1.7
matplotlib >= 3.5
```

### Basic Usage
```bash
# Clone repository
git clone https://https://github.com/preciousadeniyi/affective-geometry-consciousness.git
cd affective-geometry-consciousness

# Run basic affective core demonstration
python src/affective_core.py

# Run curvature metrics example
python src/curvature_metrics.py
```

### Example: Measuring R(t) Signatures
```python
from src.affective_core import AffectiveCore
from src.curvature_metrics import CurvatureCalculator

# Initialize systems
core = AffectiveCore()
calculator = CurvatureCalculator()

# Simulate affective conflict
stimuli = {
    'SEEK': 0.8,    # High curiosity
    'AVOID': 0.7,   # Simultaneous threat detection
}
tension = core.update_drives(stimuli)

# Measure geometric signature
state_vector = np.random.random(10)  # Simulated cognitive state
self_reference = 0.6  # Self-model engagement
rt_signature = calculator.add_state_measurement(
    state_vector, self_reference, 'affective_conflict'
)

print(f"R(t) curvature: {rt_signature.curvature_value:.3f}")
```

## 📁 Repository Structure

```
CDG-Consciousness-Tests/
├── experiments/              # Detailed experimental protocols
│   ├── 01_developmental_crucible.md
│   ├── 02_affective_conflict.md
│   ├── 03_interoceptive_blindness.md
│   ├── 04_predictive_affective.md
│   ├── 05_drive_irreducibility.md
│   └── 06_zombie_baseline.md
├── src/                      # Implementation code
│   ├── affective_core.py     # Biological drives and interoception
│   └── curvature_metrics.py  # R(t) and τ/τ_A measurements
├── docs/                     # Theoretical documentation
│   ├── theoretical_foundations.md
│   └── success_criteria.md   # Consciousness assessment criteria
└── 
```

## 🔬 Theoretical Foundation

### Core Principles

1. **Affective Primacy**: Consciousness requires bottom-up development from subcortical affective systems
2. **Geometric Signatures**: Conscious processing exhibits measurable self-referential curvature (R(t))
3. **Interoceptive Grounding**: Consciousness requires caring about internal bodily states
4. **Developmental Trajectory**: Consciousness emerges through specific developmental stages

### Biological Alignment

The framework aligns with:
- **Mark Solms'** affective neuroscience and consciousness research
- **Jaak Panksepp's** core emotional systems
- **Antonio Damasio's** somatic marker hypothesis
- **Karl Friston's** predictive processing framework

## 📊 Current Status

| Component | Status | Notes |
|-----------|--------|-------|
| Experimental Designs | ✅ Complete | All 6 protocols detailed |
| Core Implementation | 🔧 Partial | Basic affective core and metrics |
| Biological Validation | 🎯 Planning | Seeking neural correlates |
| Simulation Framework | 🔄 In Development | Full experimental pipeline |

## 🎯 Research Goals

### Short-term (3-6 months)
- [ ] Implement complete simulation environment
- [ ] Validate R(t) metrics against known cognitive architectures
- [ ] Establish baseline zombie system performance

### Medium-term (6-18 months)  
- [ ] Test framework on biological data (fMRI, EEG)
- [ ] Compare with clinical consciousness assessments
- [ ] Publish experimental validation results

### Long-term (18+ months)
- [ ] Develop consciousness assessment tools for AI systems
- [ ] Explore clinical applications for disorders of consciousness
- [ ] Refine geometric theory based on empirical results

## 🤝 Contributing

We welcome collaborations from:
- **Neuroscientists** interested in geometric approaches to consciousness
- **AI Researchers** working on artificial consciousness
- **Psychologists** studying affective and developmental processes
- **Mathematicians** interested in geometry of mind

### Getting Involved
1. Review the experimental protocols in `/experiments`
2. Examine the implementation in `/src` 
3. Open an issue to discuss potential collaborations
4. Propose extensions or improvements via pull requests

## 📚 Citation

If this work informs your research, please cite:

```bibtex
@software{cdg_consciousness_2025,
  title = {CDG Consciousness Tests: Geometric Signatures of Affective Consciousness},
  author = {Precious Adeniyi},
  year = {2025},
  url = {https://github.com/preciousadeniyi/affective-geometry-consciousness}
}
```

## 🔒 Ethical Considerations

This research has significant ethical implications:
- **Consciousness Assessment**: Potential tools for detecting consciousness in AI and biological systems
- **Moral Status**: Systems passing these tests may warrant ethical consideration
- **Clinical Applications**: Possible use in assessing disorders of consciousness

We advocate for:
- Conservative classification (err toward non-conscious)
- Multiple validation methods
- Transparent assessment criteria
- Ongoing ethical review

## ❓ Frequently Asked Questions

### Q: Is this a complete theory of consciousness?
**A**: No, this is an experimental framework for testing specific geometric hypotheses about consciousness. It's a research program, not a finished theory.

### Q: How does this relate to the "hard problem"?
**A**: This framework is a  measurable signatures that correlate with consciousness. It makes no claims about solving the hard problem of subjective experience.

### Q: Can this detect consciousness in humans?
**A**: Not directly in current form. The framework is designed for computational systems, though it may eventually inform biological consciousness assessment.

### Q: What makes this different from other AI consciousness tests?
**A**: The focus on developmental trajectory, affective grounding, and geometric signatures distinguishes it from behavior-only approaches.

## 📜 License

This work is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

This framework builds upon:
- **Mark Solms'** pioneering work on affective consciousness
- **Jaak Panksepp's** research on core emotional systems  
- **Karl Friston's** predictive processing framework
- **Thomas Metzinger's** work on self-models

---

**Note**: This is active research. Concepts, implementations, and theories are subject to revision based on empirical results and peer feedback.

*Last updated: November 2025*
```

