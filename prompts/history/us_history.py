"""
US History benchmark prompt generator with challenging analytical questions.
"""
from typing import Dict, List, Tuple
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class USHistoryBenchmark(BaseBenchmarkGenerator):
    """US History benchmark generator focused on challenging analytical questions."""

    def __init__(self):
        super().__init__("US History")
        self._setup_templates()

    def _setup_templates(self) -> None:
        """Set up US history topic templates."""
        self.topic_templates = {
            'colonial_era': {
                'user': """
Generate {quantity} challenging colonial era problems.
Include problems involving:
- Complex analysis of colonial economic systems and labor patterns
- Comparative study of different colonial regions and their development
- Native American-European relations and cultural exchange impacts
- Religious movements and their influence on colonial society
- Long-term effects of colonial institutions on American development

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring analytical thinking about colonial foundations.
Include both specific historical events and broader patterns.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in colonial American history.

Create sophisticated colonial era problems that test advanced historical thinking skills.
Ensure all problems reflect current historical scholarship and diverse perspectives.
Include problems that demonstrate the complexity of colonial development and its legacy.
Use accurate historical information and appropriate analytical frameworks.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include multiple perspectives and historical interpretations
- Emphasize cause-and-effect relationships and historical significance
- Provide distractors that test common historical misconceptions
"""
            },
            'american_revolution': {
                'user': """
Generate {quantity} advanced American Revolution problems.
Include problems involving:
- Complex analysis of revolutionary ideology and Enlightenment influences
- Military strategy and turning points in the Revolutionary War
- Social and economic impacts of the Revolution on different groups
- Diplomatic relations and international context of the Revolution
- Long-term constitutional and political consequences

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of revolutionary causes and consequences.
Include both military events and broader social transformations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the American Revolution and early republic.

Create challenging revolutionary war problems that test advanced understanding of revolutionary movements.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of revolutionary change and its global context.
Use accurate historical information and appropriate analytical approaches.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include military, political, and social dimensions of the Revolution
- Emphasize both immediate and long-term historical significance
- Provide distractors that test common revolutionary misconceptions
"""
            },
            'constitutional_era': {
                'user': """
Generate {quantity} challenging constitutional era problems.
Include problems involving:
- Complex analysis of the Articles of Confederation and their weaknesses
- Constitutional Convention debates and compromise solutions
- Federalist vs. Anti-Federalist arguments and their modern relevance
- Bill of Rights development and historical context
- Early constitutional interpretations and their lasting impact

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of constitutional development and principles.
Include both specific provisions and broader constitutional philosophy.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in constitutional development and early republic politics.

Create sophisticated constitutional era problems that test advanced understanding of American governance.
Ensure all problems reflect current constitutional scholarship and historical context.
Include problems that demonstrate the complexity of constitutional design and implementation.
Use accurate historical information and appropriate constitutional analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include both theoretical and practical constitutional dimensions
- Emphasize historical context and modern constitutional relevance
- Provide distractors that test common constitutional misconceptions
"""
            },
            'civil_war_era': {
                'user': """
Generate {quantity} advanced Civil War era problems.
Include problems involving:
- Complex analysis of sectional differences and their historical roots
- Political developments and constitutional crises leading to war
- Military strategy and major turning points in the Civil War
- Social and economic impacts of the war on different populations
- Reconstruction challenges and their long-term consequences

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of the war's causes, course, and consequences.
Include both military events and broader social transformations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the Civil War and Reconstruction era.

Create challenging Civil War problems that test advanced understanding of this pivotal period.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of sectional conflict and its resolution.
Use accurate historical information and appropriate analytical frameworks.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include political, military, and social dimensions of the conflict
- Emphasize both immediate and long-term historical significance
- Provide distractors that test common Civil War misconceptions
"""
            },
            'industrialization': {
                'user': """
Generate {quantity} challenging industrialization problems.
Include problems involving:
- Complex analysis of technological innovations and their economic impact
- Social changes resulting from industrialization and urbanization
- Labor movements and responses to industrial capitalism
- Government regulation and political responses to industrial growth
- Cultural and environmental impacts of industrial development

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of industrial transformation and its effects.
Include both technological developments and broader social changes.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in American industrialization and the Gilded Age.

Create sophisticated industrialization problems that test advanced understanding of economic transformation.
Ensure all problems reflect current historical scholarship and diverse perspectives.
Include problems that demonstrate the complexity of industrial change and its social impact.
Use accurate historical information and appropriate economic analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include technological, economic, and social dimensions of industrialization
- Emphasize both positive and negative aspects of industrial growth
- Provide distractors that test common industrialization misconceptions
"""
            },
            'progressive_era': {
                'user': """
Generate {quantity} advanced Progressive Era problems.
Include problems involving:
- Complex analysis of reform movements and their motivations
- Muckraking journalism and its impact on public opinion
- Political reforms and changes in democratic participation
- Social justice movements and civil rights developments
- Limitations and contradictions within progressive reforms

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of reform efforts and their consequences.
Include both political reforms and broader social changes.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the Progressive Era and reform movements.

Create challenging Progressive Era problems that test advanced understanding of political and social reform.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of reform efforts and their limitations.
Use accurate historical information and appropriate analytical approaches.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include political, social, and economic dimensions of reform
- Emphasize both achievements and limitations of progressive reforms
- Provide distractors that test common progressive era misconceptions
"""
            },
            'world_wars': {
                'user': """
Generate {quantity} challenging World Wars problems.
Include problems involving:
- Complex analysis of American entry into both world wars
- Home front mobilization and its social impacts
- Military strategy and American contributions to Allied victory
- Diplomatic relations and the emergence of American global leadership
- Long-term domestic and international consequences of the wars

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of America's role in global conflicts.
Include both military events and broader social transformations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in American involvement in the World Wars.

Create sophisticated World War problems that test advanced understanding of America's global role.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of total war and its societal impact.
Use accurate historical information and appropriate diplomatic and military analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include military, diplomatic, and social dimensions of the wars
- Emphasize both immediate and long-term historical significance
- Provide distractors that test common World War misconceptions
"""
            },
            'civil_rights': {
                'user': """
Generate {quantity} advanced civil rights problems.
Include problems involving:
- Complex analysis of civil rights movements and strategies
- Key legislation and court decisions and their impacts
- Leadership conflicts and different approaches to civil rights
- Intersection of civil rights with other social movements
- Ongoing challenges and unfinished civil rights agendas

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of civil rights struggles and their significance.
Include both legal developments and broader social movements.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in civil rights movements and social justice.

Create challenging civil rights problems that test advanced understanding of equality struggles.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of civil rights movements and their evolution.
Use accurate historical information and appropriate social movement analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include legal, political, and social dimensions of civil rights
- Emphasize both historical achievements and ongoing challenges
- Provide distractors that test common civil rights misconceptions
"""
            },
            'cold_war': {
                'user': """
Generate {quantity} challenging Cold War problems.
Include problems involving:
- Complex analysis of ideological conflicts and their global implications
- Key events and crises in US-Soviet relations
- Domestic impacts of Cold War policies on American society
- Military interventions and proxy wars during the Cold War
- Long-term consequences of Cold War on international relations

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of Cold War dynamics and their effects.
Include both international relations and domestic impacts.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the Cold War and international relations.

Create sophisticated Cold War problems that test advanced understanding of superpower conflict.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of Cold War politics and their global impact.
Use accurate historical information and appropriate diplomatic and strategic analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include international, domestic, and military dimensions of the Cold War
- Emphasize both global and local impacts of Cold War policies
- Provide distractors that test common Cold War misconceptions
"""
            },
            'modern_america': {
                'user': """
Generate {quantity} advanced modern America problems.
Include problems involving:
- Complex analysis of political realignments and partisan polarization
- Economic globalization and its effects on American society
- Social and cultural changes in late 20th and early 21st century
- Technological revolution and its impact on American life
- Contemporary challenges and their historical roots

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of recent American developments.
Include both current events and their historical context.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in modern American history and contemporary issues.

Create challenging modern America problems that test advanced understanding of recent developments.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the connection between past and present in American history.
Use accurate historical information and appropriate contemporary analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include political, social, and economic dimensions of modern America
- Emphasize historical context and contemporary relevance
- Provide distractors that test common modern history misconceptions
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
        """Get specific grading criteria for US history topics."""
        base_criteria = [
            "Historical accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and historical context",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'colonial_era': ["Understanding of colonial development and its legacy"],
            'american_revolution': ["Analysis of revolutionary causes and consequences"],
            'constitutional_era': ["Understanding of constitutional development and principles"],
            'civil_war_era': ["Analysis of sectional conflict and its resolution"],
            'industrialization': ["Understanding of economic transformation and social change"],
            'progressive_era': ["Analysis of reform movements and their limitations"],
            'world_wars': ["Understanding of America's global role and war impact"],
            'civil_rights': ["Analysis of equality struggles and social justice movements"],
            'cold_war': ["Understanding of superpower conflict and its global impact"],
            'modern_america': ["Analysis of contemporary developments and historical context"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available US history topics."""
        return [
            "Colonial Era",
            "American Revolution",
            "Constitutional Era",
            "Civil War Era",
            "Industrialization",
            "Progressive Era",
            "World Wars",
            "Civil Rights",
            "Cold War",
            "Modern America"
        ]