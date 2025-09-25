"""
Chemistry benchmark prompt generator with challenging advanced chemistry problems.
"""
from typing import Dict, List, Tuple
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class ChemistryBenchmark(BaseBenchmarkGenerator):
    """Chemistry benchmark generator focused on challenging advanced chemistry problems."""

    def __init__(self):
        super().__init__("Chemistry")
        self._setup_templates()

    def _setup_templates(self) -> None:
        """Set up chemistry topic templates."""
        self.topic_templates = {
            'atomic_structure': {
                'user': """
Generate {quantity} challenging atomic structure problems.
Include problems involving:
- Complex electron configurations and orbital notation
- Quantum numbers and their relationships
- Atomic spectra and energy level calculations
- Periodic trends and their explanations
- Applications to spectroscopy and material properties

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of atomic theory and quantum mechanics.
Include both theoretical and practical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in atomic structure and quantum chemistry.

Create sophisticated atomic structure problems that test advanced understanding of atomic theory.
Ensure all problems reflect current atomic models and quantum mechanical principles.
Include problems that demonstrate the importance of atomic structure in chemistry.
Use accurate atomic models and appropriate scientific notation.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to spectroscopy, materials, and chemical behavior
- Ensure scientific accuracy and realistic atomic scenarios
- Provide distractors that test common atomic misconceptions
"""
            },
            'chemical_bonding': {
                'user': """
Generate {quantity} advanced chemical bonding problems.
Include problems involving:
- Complex molecular geometry and VSEPR theory
- Hybridization and molecular orbital theory
- Bond polarity and intermolecular forces
- Resonance structures and formal charge calculations
- Applications to material properties and biological molecules

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of bonding theories and molecular behavior.
Include both theoretical and practical bonding applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in chemical bonding and molecular geometry.

Create challenging chemical bonding problems that test advanced understanding of molecular interactions.
Ensure all problems reflect current bonding theories and molecular models.
Include problems that demonstrate the importance of bonding in chemical behavior.
Use accurate bonding models and appropriate molecular representations.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to materials, biology, and environmental science
- Emphasize both theoretical and practical bonding concepts
- Provide distractors that test common bonding misconceptions
"""
            },
            'chemical_reactions': {
                'user': """
Generate {quantity} challenging chemical reaction problems.
Include problems involving:
- Complex reaction mechanisms and pathways
- Reaction rates and factors affecting kinetics
- Le Chatelier's principle and equilibrium shifts
- Thermodynamic calculations and spontaneity
- Applications to industrial and biological processes

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of reaction dynamics and equilibrium.
Include both theoretical and practical reaction applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in chemical kinetics and thermodynamics.

Create sophisticated reaction problems that test advanced understanding of chemical processes.
Ensure all problems reflect current reaction theories and thermodynamic principles.
Include problems that demonstrate the importance of reaction control in chemistry.
Use accurate reaction models and appropriate thermodynamic data.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to industry, biology, and environmental science
- Emphasize both kinetic and thermodynamic aspects of reactions
- Provide distractors that test common reaction misconceptions
"""
            },
            'stoichiometry': {
                'user': """
Generate {quantity} advanced stoichiometry problems.
Include problems involving:
- Complex limiting reactant scenarios
- Percent yield and theoretical yield calculations
- Solution stoichiometry and concentration units
- Gas stoichiometry and ideal gas law applications
- Applications to analytical chemistry and quality control

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring mastery of quantitative relationships in chemistry.
Include both theoretical and practical stoichiometric applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in quantitative analysis and stoichiometry.

Create challenging stoichiometry problems that test advanced quantitative reasoning skills.
Ensure all problems reflect accurate chemical relationships and realistic scenarios.
Include problems that demonstrate the importance of precise measurements in chemistry.
Use accurate stoichiometric calculations and appropriate significant figures.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to industry, research, and environmental monitoring
- Emphasize both theoretical and practical stoichiometric concepts
- Provide distractors that test common calculation errors
"""
            },
            'acids_and_bases': {
                'user': """
Generate {quantity} challenging acid and base problems.
Include problems involving:
- Complex pH calculations and buffer systems
- Titration curves and equivalence point analysis
- Acid-base equilibrium and Ka/Kb relationships
- Polyprotic acids and successive ionization
- Applications to biological systems and environmental chemistry

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of acid-base chemistry and equilibrium.
Include both theoretical and practical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in acid-base chemistry and equilibrium.

Create sophisticated acid-base problems that test advanced understanding of chemical equilibrium.
Ensure all problems reflect current acid-base theories and equilibrium principles.
Include problems that demonstrate the importance of pH in biological and environmental systems.
Use accurate equilibrium calculations and appropriate buffer scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to biology, medicine, and environmental science
- Emphasize both theoretical and practical acid-base concepts
- Provide distractors that test common equilibrium misconceptions
"""
            },
            'thermodynamics': {
                'user': """
Generate {quantity} advanced thermodynamics problems.
Include problems involving:
- Complex enthalpy, entropy, and Gibbs free energy calculations
- Heat transfer and calorimetry applications
- Phase changes and heating/cooling curves
- Spontaneity and equilibrium relationships
- Applications to energy systems and industrial processes

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of energy relationships in chemical systems.
Include both theoretical and practical thermodynamic applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in thermodynamics and energy chemistry.

Create challenging thermodynamics problems that test advanced understanding of energy relationships.
Ensure all problems reflect current thermodynamic principles and accurate energy data.
Include problems that demonstrate the importance of energy in chemical processes.
Use accurate thermodynamic calculations and appropriate energy scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to energy systems, industry, and environmental science
- Emphasize both theoretical and practical thermodynamic concepts
- Provide distractors that test common thermodynamic misconceptions
"""
            },
            'kinetics_and_equilibrium': {
                'user': """
Generate {quantity} challenging kinetics and equilibrium problems.
Include problems involving:
- Complex reaction rate calculations and mechanisms
- Factors affecting reaction rates and activation energy
- Collision theory and transition state theory
- Equilibrium constant calculations and applications
- Le Chatelier's principle and equilibrium shifts

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of reaction dynamics and equilibrium principles.
Include both theoretical and practical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in chemical kinetics and equilibrium.

Create sophisticated kinetics problems that test advanced understanding of reaction rates and equilibrium.
Ensure all problems reflect current kinetic theories and equilibrium principles.
Include problems that demonstrate the importance of reaction control in chemistry.
Use accurate kinetic calculations and appropriate experimental scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to industry, biology, and environmental science
- Emphasize both theoretical and practical kinetic concepts
- Provide distractors that test common kinetic misconceptions
"""
            },
            'electrochemistry': {
                'user': """
Generate {quantity} advanced electrochemistry problems.
Include problems involving:
- Complex galvanic cell calculations and applications
- Electrolysis and Faraday's law applications
- Corrosion processes and prevention methods
- Battery technology and fuel cell principles
- Applications to energy storage and environmental remediation

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of electrochemical principles and applications.
Include both theoretical and practical electrochemical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in electrochemistry and energy conversion.

Create challenging electrochemistry problems that test advanced understanding of redox processes.
Ensure all problems reflect current electrochemical principles and accurate cell potentials.
Include problems that demonstrate the importance of electrochemistry in modern technology.
Use accurate electrochemical calculations and appropriate cell configurations.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to energy storage, corrosion, and industrial processes
- Emphasize both theoretical and practical electrochemical concepts
- Provide distractors that test common electrochemical misconceptions
"""
            },
            'organic_chemistry': {
                'user': """
Generate {quantity} challenging organic chemistry problems.
Include problems involving:
- Complex organic reaction mechanisms and pathways
- Stereochemistry and conformational analysis
- Functional group transformations and synthesis
- Spectroscopic analysis and structure determination
- Applications to biochemistry and pharmaceutical chemistry

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of organic structure and reactivity.
Include both theoretical and practical organic chemistry applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in organic chemistry and biochemistry.

Create sophisticated organic chemistry problems that test advanced understanding of carbon compounds.
Ensure all problems reflect current organic reaction mechanisms and spectroscopic principles.
Include problems that demonstrate the importance of organic chemistry in life sciences.
Use accurate organic mechanisms and appropriate synthetic strategies.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to medicine, biochemistry, and materials science
- Emphasize both theoretical and practical organic chemistry concepts
- Provide distractors that test common organic misconceptions
"""
            },
            'nuclear_chemistry': {
                'user': """
Generate {quantity} advanced nuclear chemistry problems.
Include problems involving:
- Complex radioactive decay calculations and half-life analysis
- Nuclear reactions and binding energy calculations
- Nuclear stability and the band of stability
- Applications to medicine, energy, and dating techniques
- Environmental and safety considerations of nuclear technology

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of nuclear processes and applications.
Include both theoretical and practical nuclear chemistry applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert chemistry educator specializing in nuclear chemistry and radiochemistry.

Create challenging nuclear chemistry problems that test advanced understanding of nuclear processes.
Ensure all problems reflect current nuclear theories and accurate radioactive data.
Include problems that demonstrate the importance of nuclear chemistry in modern society.
Use accurate nuclear calculations and appropriate safety considerations.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to medicine, energy, and environmental monitoring
- Emphasize both theoretical and practical nuclear chemistry concepts
- Provide distractors that test common nuclear misconceptions
"""
            }
        }

    def _get_topic_templates(self, topic: str) -> Tuple[str, str]:
        """Get templates for a specific topic."""
        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in self.topic_templates:
            templates = self.topic_templates[topic_lower]
            return templates['user'], templates['system']
        else:
            available_topics = list(self.topic_templates.keys())
            raise ValueError(f"Topic '{topic}' not found. Available topics: {available_topics}")

    def _get_grading_criteria(self, topic: str) -> List[str]:
        """Get specific grading criteria for chemistry topics."""
        base_criteria = [
            "Scientific accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and real-world connections",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'atomic_structure': ["Understanding of atomic models and quantum principles"],
            'chemical_bonding': ["Mastery of bonding theories and molecular geometry"],
            'chemical_reactions': ["Understanding of reaction mechanisms and equilibrium"],
            'stoichiometry': ["Quantitative reasoning and calculation accuracy"],
            'acids_and_bases': ["Understanding of acid-base equilibrium and pH calculations"],
            'thermodynamics': ["Mastery of energy relationships and thermodynamic principles"],
            'kinetics_and_equilibrium': ["Understanding of reaction rates and equilibrium dynamics"],
            'electrochemistry': ["Knowledge of electrochemical principles and cell calculations"],
            'organic_chemistry': ["Understanding of organic mechanisms and synthesis strategies"],
            'nuclear_chemistry': ["Mastery of nuclear processes and radioactive decay calculations"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available chemistry topics."""
        return [
            "Atomic Structure",
            "Chemical Bonding",
            "Chemical Reactions",
            "Stoichiometry",
            "Acids and Bases",
            "Thermodynamics",
            "Kinetics and Equilibrium",
            "Electrochemistry",
            "Organic Chemistry",
            "Nuclear Chemistry"
        ]