"""
World History benchmark prompt generator with challenging critical thinking questions.
"""
from typing import Dict, List, Tuple, Optional
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class WorldHistoryBenchmark(BaseBenchmarkGenerator):
    """World History benchmark generator focused on challenging critical thinking questions."""

    def __init__(self):
        super().__init__("World History")
        self._setup_templates()

    # Topic-specific methods for direct access
    def ancient_civilizations(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for ancient civilizations topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for ancient civilizations
        """
        return self.generate_benchmark_prompt('ancient_civilizations', question_count, **kwargs)

    def classical_period(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for classical period topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for classical period
        """
        return self.generate_benchmark_prompt('classical_period', question_count, **kwargs)

    def post_classical_era(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for post-classical era topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for post-classical era
        """
        return self.generate_benchmark_prompt('post_classical_era', question_count, **kwargs)

    def renaissance_and_reformation(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for renaissance and reformation topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for renaissance and reformation
        """
        return self.generate_benchmark_prompt('renaissance_and_reformation', question_count, **kwargs)

    def age_of_exploration(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for age of exploration topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for age of exploration
        """
        return self.generate_benchmark_prompt('age_of_exploration', question_count, **kwargs)

    def absolutism_and_revolution(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for absolutism and revolution topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for absolutism and revolution
        """
        return self.generate_benchmark_prompt('absolutism_and_revolution', question_count, **kwargs)

    def industrialization_and_imperialism(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for industrialization and imperialism topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for industrialization and imperialism
        """
        return self.generate_benchmark_prompt('industrialization_and_imperialism', question_count, **kwargs)

    def world_wars(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for world wars topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for world wars
        """
        return self.generate_benchmark_prompt('world_wars', question_count, **kwargs)

    def cold_war(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for cold war topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for cold war
        """
        return self.generate_benchmark_prompt('cold_war', question_count, **kwargs)

    def globalization(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for globalization topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for globalization
        """
        return self.generate_benchmark_prompt('globalization', question_count, **kwargs)

    def _setup_templates(self) -> None:
        """Set up world history topic templates."""
        self.topic_templates = {
            'ancient_civilizations': {
                'user': """
Generate {quantity} challenging ancient civilizations problems.
Include problems involving:
- Complex analysis of river valley civilizations and their achievements
- Comparative study of political systems and social structures
- Religious developments and their cultural impacts
- Technological innovations and their historical significance
- Long-term influences of ancient civilizations on modern societies

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring critical thinking about early human societies.
Include both specific civilizations and broader patterns of development.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in ancient civilizations and classical history.

Create sophisticated ancient civilization problems that test advanced historical thinking skills.
Ensure all problems reflect current archaeological and historical scholarship.
Include problems that demonstrate the diversity and complexity of early civilizations.
Use accurate historical information and appropriate comparative analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include multiple civilizations and comparative perspectives
- Emphasize cultural achievements and historical significance
- Provide distractors that test common ancient civilization misconceptions
"""
            },
            'classical_period': {
                'user': """
Generate {quantity} advanced classical period problems.
Include problems involving:
- Complex analysis of Greek city-states and their political innovations
- Roman Republic and Empire development and administrative achievements
- Classical philosophy, art, and literature and their enduring influence
- Cultural exchanges between Mediterranean and Near Eastern civilizations
- Military conflicts and their impacts on classical civilization

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of classical foundations of Western civilization.
Include both political developments and cultural achievements.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in classical Mediterranean civilizations.

Create challenging classical period problems that test advanced understanding of classical foundations.
Ensure all problems reflect current historical scholarship and diverse perspectives.
Include problems that demonstrate the complexity of classical political and cultural systems.
Use accurate historical information and appropriate analytical frameworks.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include Greek, Roman, and other classical civilizations
- Emphasize both political and cultural classical achievements
- Provide distractors that test common classical period misconceptions
"""
            },
            'post_classical_era': {
                'user': """
Generate {quantity} challenging post-classical era problems.
Include problems involving:
- Complex analysis of religious developments and their spread
- Trade networks and cultural exchanges across Eurasia
- Political decentralization and new forms of governance
- Technological and scientific achievements in different regions
- Comparative study of civilizations in Americas, Africa, and Asia

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of global patterns after classical period.
Include both regional developments and cross-cultural interactions.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in post-classical civilizations and global exchanges.

Create sophisticated post-classical problems that test advanced understanding of medieval developments.
Ensure all problems reflect current historical scholarship and global perspectives.
Include problems that demonstrate the diversity of post-classical civilizations.
Use accurate historical information and appropriate comparative analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include developments across multiple continents and civilizations
- Emphasize both regional uniqueness and global connections
- Provide distractors that test common post-classical misconceptions
"""
            },
            'renaissance_reformation': {
                'user': """
Generate {quantity} advanced Renaissance and Reformation problems.
Include problems involving:
- Complex analysis of Renaissance humanism and its cultural impact
- Artistic and scientific achievements and their historical significance
- Religious reform movements and their political and social consequences
- Printing revolution and its role in spreading new ideas
- Long-term effects on Western intellectual and religious traditions

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of intellectual and religious transformations.
Include both cultural achievements and broader social changes.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the Renaissance and Reformation.

Create challenging Renaissance problems that test advanced understanding of early modern transformations.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of intellectual and religious change.
Use accurate historical information and appropriate cultural analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include both Italian Renaissance and Northern Renaissance developments
- Emphasize intellectual, artistic, and religious dimensions
- Provide distractors that test common Renaissance misconceptions
"""
            },
            'age_of_exploration': {
                'user': """
Generate {quantity} challenging age of exploration problems.
Include problems involving:
- Complex analysis of technological innovations enabling exploration
- Economic motivations and consequences of global exploration
- Cultural encounters and their impacts on both explorers and native peoples
- Columbian Exchange and its biological and cultural effects
- Long-term consequences for global power relationships

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of global encounters and their effects.
Include both technological achievements and broader historical impacts.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the Age of Exploration and global encounters.

Create sophisticated exploration problems that test advanced understanding of global interactions.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of cross-cultural encounters.
Use accurate historical information and appropriate global analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include European, Asian, and African perspectives on exploration
- Emphasize both technological achievements and human costs
- Provide distractors that test common exploration misconceptions
"""
            },
            'absolutism_revolution': {
                'user': """
Generate {quantity} advanced absolutism and revolution problems.
Include problems involving:
- Complex analysis of absolute monarchy development and its challenges
- Enlightenment philosophy and its influence on political thought
- Comparative study of Atlantic revolutions and their outcomes
- Revolutionary wars and their international consequences
- Long-term effects on modern political systems and ideologies

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of political transformations and revolutions.
Include both theoretical developments and practical revolutionary movements.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in absolutism, Enlightenment, and Atlantic revolutions.

Create challenging revolution problems that test advanced understanding of political transformation.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of revolutionary change and its global impact.
Use accurate historical information and appropriate political analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include multiple revolutionary movements and their comparisons
- Emphasize both ideological and practical revolutionary dimensions
- Provide distractors that test common revolution misconceptions
"""
            },
            'industrialization_imperialism': {
                'user': """
Generate {quantity} challenging industrialization and imperialism problems.
Include problems involving:
- Complex analysis of industrial revolution's global spread and effects
- Economic transformations and social changes in different regions
- Imperialism justifications and their intellectual foundations
- Resistance movements and anti-colonial struggles
- Long-term consequences for global power and development patterns

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of economic and imperial transformations.
Include both technological developments and broader social impacts.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in industrialization and imperialism.

Create sophisticated industrialization problems that test advanced understanding of global transformation.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of industrial and imperial change.
Use accurate historical information and appropriate economic and social analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include both industrializing and colonized regions' perspectives
- Emphasize economic, social, and political dimensions
- Provide distractors that test common industrialization misconceptions
"""
            },
            'world_wars_global': {
                'user': """
Generate {quantity} challenging world wars problems.
Include problems involving:
- Complex analysis of underlying causes and global conditions
- Total war mobilization and its societal impacts
- Diplomatic relations and alliance systems
- Global consequences and redrawing of world order
- Long-term effects on international relations and global institutions

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of global conflicts and their effects.
Include both military events and broader social transformations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the World Wars and global conflict.

Create challenging World War problems that test advanced understanding of global conflict.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of total war and its global impact.
Use accurate historical information and appropriate military and diplomatic analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include both European and Pacific theaters of war
- Emphasize military, political, and social dimensions
- Provide distractors that test common World War misconceptions
"""
            },
            'cold_war_global': {
                'user': """
Generate {quantity} challenging Cold War problems.
Include problems involving:
- Complex analysis of ideological conflicts and bipolar world order
- Proxy wars and their regional impacts
- Decolonization and its relationship to Cold War dynamics
- Nuclear arms race and its global implications
- Long-term consequences for international relations and development

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of Cold War dynamics and global effects.
Include both superpower relations and impacts on developing nations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in the global Cold War and decolonization.

Create sophisticated Cold War problems that test advanced understanding of bipolar conflict.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of Cold War politics and its global impact.
Use accurate historical information and appropriate international relations analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include superpower relations and developing world perspectives
- Emphasize political, military, and economic dimensions
- Provide distractors that test common Cold War misconceptions
"""
            },
            'globalization': {
                'user': """
Generate {quantity} advanced globalization problems.
Include problems involving:
- Complex analysis of economic integration and its effects
- Cultural globalization and resistance to homogenization
- Technological revolution and its role in connecting the world
- Environmental challenges and global governance
- Contemporary issues and their historical context

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring understanding of contemporary global developments.
Include both current events and their historical roots.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert history educator specializing in contemporary global history and globalization.

Create challenging globalization problems that test advanced understanding of current global trends.
Ensure all problems reflect current historical scholarship and multiple perspectives.
Include problems that demonstrate the complexity of global interconnection and its challenges.
Use accurate historical information and appropriate contemporary analysis.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include economic, cultural, and technological dimensions
- Emphasize both benefits and challenges of globalization
- Provide distractors that test common globalization misconceptions
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
        """Get specific grading criteria for world history topics."""
        base_criteria = [
            "Historical accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and historical context",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'ancient_civilizations': ["Understanding of early human societies and their achievements"],
            'classical_period': ["Analysis of classical foundations and cultural achievements"],
            'post_classical_era': ["Understanding of medieval developments and global exchanges"],
            'renaissance_reformation': ["Analysis of intellectual and religious transformations"],
            'age_of_exploration': ["Understanding of global encounters and their effects"],
            'absolutism_revolution': ["Analysis of political transformations and revolutionary movements"],
            'industrialization_imperialism': ["Understanding of economic and imperial transformations"],
            'world_wars_global': ["Analysis of global conflicts and their consequences"],
            'cold_war_global': ["Understanding of bipolar conflict and its global impact"],
            'globalization': ["Analysis of contemporary global developments and challenges"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available world history topics."""
        return [
            "Ancient Civilizations",
            "Classical Period",
            "Post-Classical Era",
            "Renaissance and Reformation",
            "Age of Exploration",
            "Absolutism and Revolution",
            "Industrialization and Imperialism",
            "World Wars",
            "Cold War",
            "Globalization"
        ]