"""
Biology benchmark prompt generator with challenging advanced biology concepts.
"""
from typing import Dict, List, Tuple
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class BiologyBenchmark(BaseBenchmarkGenerator):
    """Biology benchmark generator focused on challenging advanced biology concepts."""

    def __init__(self):
        super().__init__("Biology")
        self._setup_templates()

    def _setup_templates(self) -> None:
        """Set up biology topic templates."""
        self.topic_templates = {
            'cell_biology': {
                'user': """
Generate {quantity} challenging cell biology problems.
Include problems involving:
- Complex cellular signaling pathways and cascades
- Membrane transport mechanisms and electrochemical gradients
- Organelle interactions and cellular compartmentalization
- Cell cycle regulation and cancer biology connections
- Advanced microscopy and cellular imaging techniques

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring deep understanding of cellular processes.
Include both molecular and systems-level approaches.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in cell biology and molecular biology.

Create sophisticated cell biology problems that test advanced biological thinking.
Ensure all problems reflect current scientific understanding and terminology.
Include problems that demonstrate the complexity of cellular systems.
Use accurate biological models and appropriate terminology.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to medicine, biotechnology, and research
- Ensure scientific accuracy and realistic biological scenarios
- Provide distractors that test common cellular misconceptions
"""
            },
            'genetics': {
                'user': """
Generate {quantity} advanced genetics problems.
Include problems involving:
- Complex inheritance patterns and gene interactions
- Population genetics and Hardy-Weinberg equilibrium
- Genetic linkage and crossing over calculations
- Epigenetic modifications and gene expression regulation
- Applications to genetic disorders and biotechnology

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of genetic principles and applications.
Include both classical and molecular genetics approaches.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in genetics and molecular biology.

Create challenging genetics problems that test advanced understanding of inheritance.
Ensure all problems reflect current genetic understanding and research findings.
Include problems that demonstrate the relevance of genetics in modern biology.
Use accurate genetic models and appropriate statistical approaches.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to medicine, evolution, and biotechnology
- Emphasize both classical and molecular genetic concepts
- Provide distractors that test common genetic misconceptions
"""
            },
            'evolution': {
                'user': """
Generate {quantity} challenging evolution problems.
Include problems involving:
- Phylogenetic analysis and evolutionary relationships
- Speciation mechanisms and reproductive isolation
- Molecular evolution and genetic drift calculations
- Coevolution and ecological interactions
- Evidence for evolution across multiple disciplines

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of evolutionary mechanisms and evidence.
Include both microevolutionary and macroevolutionary concepts.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in evolutionary biology.

Create sophisticated evolution problems that test advanced understanding of evolutionary processes.
Ensure all problems reflect current evolutionary theory and research findings.
Include problems that demonstrate the importance of evolution in biology.
Use accurate evolutionary models and appropriate evidence.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to conservation, medicine, and biodiversity
- Emphasize both theoretical and practical evolutionary concepts
- Provide distractors that test common evolutionary misconceptions
"""
            },
            'ecology': {
                'user': """
Generate {quantity} advanced ecology problems.
Include problems involving:
- Complex ecosystem interactions and food web dynamics
- Population growth models and carrying capacity calculations
- Biogeochemical cycles and nutrient flow analysis
- Community ecology and species interactions
- Applications to conservation and environmental management

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of ecological systems and relationships.
Include both theoretical and applied ecological concepts.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in ecology and environmental science.

Create challenging ecology problems that test advanced understanding of ecological systems.
Ensure all problems reflect current ecological understanding and research findings.
Include problems that demonstrate the importance of ecological relationships.
Use accurate ecological models and appropriate field data scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to conservation, climate change, and resource management
- Emphasize both theoretical and practical ecological concepts
- Provide distractors that test common ecological misconceptions
"""
            },
            'physiology': {
                'user': """
Generate {quantity} challenging physiology problems.
Include problems involving:
- Complex organ system interactions and homeostasis
- Neurophysiology and signal transduction pathways
- Endocrine system regulation and feedback mechanisms
- Cardiovascular and respiratory system coordination
- Applications to medicine and human health

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of physiological processes and regulation.
Include both molecular and systems-level physiological approaches.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in human physiology and anatomy.

Create sophisticated physiology problems that test advanced understanding of body systems.
Ensure all problems reflect current physiological understanding and medical research.
Include problems that demonstrate the complexity of physiological regulation.
Use accurate physiological models and appropriate clinical scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to medicine, health, and disease
- Emphasize both molecular and systems-level physiology
- Provide distractors that test common physiological misconceptions
"""
            },
            'biochemistry': {
                'user': """
Generate {quantity} advanced biochemistry problems.
Include problems involving:
- Complex enzyme kinetics and metabolic pathway regulation
- Protein structure-function relationships and folding
- Carbohydrate, lipid, and nucleic acid metabolism
- Bioenergetics and thermodynamic calculations
- Applications to medicine and biotechnology

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of biochemical principles and processes.
Include both theoretical and practical biochemical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in biochemistry and molecular biology.

Create challenging biochemistry problems that test advanced understanding of molecular processes.
Ensure all problems reflect current biochemical understanding and research findings.
Include problems that demonstrate the importance of biochemistry in living systems.
Use accurate biochemical models and appropriate experimental scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to medicine, biotechnology, and research
- Emphasize both theoretical and practical biochemical concepts
- Provide distractors that test common biochemical misconceptions
"""
            },
            'molecular_biology': {
                'user': """
Generate {quantity} challenging molecular biology problems.
Include problems involving:
- DNA replication, transcription, and translation mechanisms
- Gene expression regulation and epigenetic modifications
- Recombinant DNA technology and genetic engineering
- PCR, sequencing, and genomic analysis techniques
- Applications to medicine, forensics, and biotechnology

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of molecular biology techniques and concepts.
Include both theoretical knowledge and practical applications.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in molecular biology and biotechnology.

Create sophisticated molecular biology problems that test advanced understanding of genetic processes.
Ensure all problems reflect current molecular biology understanding and research techniques.
Include problems that demonstrate the importance of molecular approaches in biology.
Use accurate molecular biology models and appropriate laboratory scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to medicine, forensics, and biotechnology
- Emphasize both theoretical and technical molecular biology concepts
- Provide distractors that test common molecular biology misconceptions
"""
            },
            'biotechnology': {
                'user': """
Generate {quantity} advanced biotechnology problems.
Include problems involving:
- Genetic engineering techniques and applications
- Biopharmaceutical development and production
- Agricultural biotechnology and GMO analysis
- Bioinformatics and genomic data analysis
- Ethical considerations and regulatory frameworks

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of biotechnology principles and applications.
Include both technical and ethical aspects of biotechnology.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert biology educator specializing in biotechnology and bioethics.

Create challenging biotechnology problems that test advanced understanding of biological applications.
Ensure all problems reflect current biotechnology practices and research developments.
Include problems that demonstrate the impact of biotechnology on society.
Use accurate biotechnology models and appropriate real-world scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to medicine, agriculture, and industry
- Emphasize both technical and ethical biotechnology aspects
- Provide distractors that test common biotechnology misconceptions
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
        """Get specific grading criteria for biology topics."""
        base_criteria = [
            "Scientific accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and real-world connections",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'cell_biology': ["Understanding of cellular processes and molecular mechanisms"],
            'genetics': ["Mastery of genetic principles and applications"],
            'evolution': ["Understanding of evolutionary mechanisms and evidence"],
            'ecology': ["Knowledge of ecological systems and environmental interactions"],
            'physiology': ["Understanding of physiological processes and regulation"],
            'biochemistry': ["Mastery of biochemical principles and metabolic pathways"],
            'molecular_biology': ["Understanding of molecular techniques and genetic processes"],
            'biotechnology': ["Knowledge of biotechnology applications and ethical considerations"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available biology topics."""
        return [
            "Cell Biology",
            "Genetics",
            "Evolution",
            "Ecology",
            "Physiology",
            "Biochemistry",
            "Molecular Biology",
            "Biotechnology"
        ]