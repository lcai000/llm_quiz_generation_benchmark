"""
Precalculus benchmark prompt generator with challenging advanced mathematics problems.
"""
from typing import Dict, List, Tuple, Optional
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class PrecalculusBenchmark(BaseBenchmarkGenerator):
    """Precalculus benchmark generator focused on challenging advanced mathematics problems."""

    def __init__(self):
        super().__init__("Precalculus")
        self._setup_templates()

    # Topic-specific methods for direct access
    def trigonometric_functions(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for trigonometric functions topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for trigonometric functions
        """
        return self.generate_benchmark_prompt('trigonometric_functions', question_count, **kwargs)

    def exponential_and_logarithmic_functions(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for exponential and logarithmic functions topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for exponential and logarithmic functions
        """
        return self.generate_benchmark_prompt('exponential_and_logarithmic_functions', question_count, **kwargs)

    def conic_sections(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for conic sections topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for conic sections
        """
        return self.generate_benchmark_prompt('conic_sections', question_count, **kwargs)

    def sequences_and_series(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for sequences and series topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for sequences and series
        """
        return self.generate_benchmark_prompt('sequences_and_series', question_count, **kwargs)

    def vectors(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for vectors topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for vectors
        """
        return self.generate_benchmark_prompt('vectors', question_count, **kwargs)

    def parametric_equations(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for parametric equations topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for parametric equations
        """
        return self.generate_benchmark_prompt('parametric_equations', question_count, **kwargs)

    def polar_coordinates(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for polar coordinates topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for polar coordinates
        """
        return self.generate_benchmark_prompt('polar_coordinates', question_count, **kwargs)

    def matrices(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for matrices topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for matrices
        """
        return self.generate_benchmark_prompt('matrices', question_count, **kwargs)

    def limits(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for limits topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for limits
        """
        return self.generate_benchmark_prompt('limits', question_count, **kwargs)

    def _setup_templates(self) -> None:
        """Set up precalculus topic templates."""
        self.topic_templates = {
            'trigonometric_functions': {
                'user': """
Generate {quantity} challenging trigonometric function problems.
Include problems involving:
- Complex trigonometric identities and proofs
- Trigonometric equations with multiple angles and periods
- Applications to periodic phenomena and waves
- Inverse trigonometric functions and their properties
- Polar coordinates and complex number applications

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring deep understanding of trigonometric relationships.
Include both exact and approximate solutions where appropriate.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in trigonometric functions and their applications.

Create sophisticated trigonometric problems that test advanced mathematical thinking.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the periodic nature of trigonometric functions.
Use accurate mathematical models and appropriate terminology.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to physics, engineering, and natural phenomena
- Ensure mathematical accuracy and realistic solutions
- Provide distractors that test common trigonometric misconceptions
"""
            },
            'exponential_and_logarithmic_functions': {
                'user': """
Generate {quantity} advanced exponential and logarithmic function problems.
Include problems involving:
- Complex exponential growth and decay models
- Logarithmic equations with multiple steps and constraints
- Applications to finance, population dynamics, and radioactive decay
- Properties of logarithms and exponential relationships
- Real-world modeling with continuous functions

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring analytical thinking and modeling skills.
Include problems that test understanding of asymptotic behavior.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in exponential and logarithmic functions.

Create challenging problems that test deep understanding of exponential relationships.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the power of exponential modeling.
Use accurate mathematical models and reasonable parameter values.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include diverse applications across different fields
- Emphasize domain restrictions and behavior analysis
- Provide distractors that reflect common calculation errors
"""
            },
            'conic_sections': {
                'user': """
Generate {quantity} challenging conic section problems.
Include problems involving:
- Complex conic identification and analysis
- Applications to orbital mechanics and optics
- Conic sections in standard and general forms
- Eccentricity calculations and geometric properties
- Systems involving multiple conic sections

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring geometric intuition and algebraic manipulation.
Include problems that test understanding of conic properties.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in conic sections and their applications.

Create sophisticated conic section problems that test advanced geometric thinking.
Ensure all problems have realistic applications and meaningful contexts.
Include problems that demonstrate the importance of conic sections in science.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to physics, astronomy, and engineering
- Emphasize geometric properties and algebraic relationships
- Provide distractors that test conceptual understanding
"""
            },
            'sequences_and_series': {
                'user': """
Generate {quantity} advanced sequences and series problems.
Include problems involving:
- Complex arithmetic and geometric sequences
- Convergence tests and infinite series
- Applications to finance and recursive modeling
- Summation formulas and telescoping series
- Mathematical induction and proof techniques

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring analytical thinking and pattern recognition.
Include problems that test understanding of infinite processes.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in sequences and series.

Create challenging problems that test deep understanding of sequential patterns.
Ensure all problems have meaningful applications and realistic contexts.
Include problems that demonstrate the importance of infinite processes.
Use accurate mathematical models and appropriate notation.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include both theoretical and applied problems
- Emphasize convergence behavior and summation techniques
- Provide distractors that test common misconceptions
"""
            },
            'vectors': {
                'user': """
Generate {quantity} challenging vector problems.
Include problems involving:
- Complex vector operations in 2D and 3D space
- Applications to physics and engineering
- Vector equations and geometric interpretations
- Dot products, cross products, and projections
- Parametric equations and motion problems

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring spatial reasoning and algebraic manipulation.
Include problems that test understanding of vector properties.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in vectors and their applications.

Create sophisticated vector problems that test advanced mathematical thinking.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the power of vector analysis.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to physics, engineering, and computer science
- Emphasize geometric interpretations and algebraic operations
- Provide distractors that test understanding of vector concepts
"""
            },
            'parametric_equations': {
                'user': """
Generate {quantity} advanced parametric equation problems.
Include problems involving:
- Complex parametric curves and their analysis
- Applications to motion and trajectory problems
- Converting between parametric and Cartesian forms
- Projectile motion and physics applications
- Lissajous curves and complex patterns

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring analytical thinking and visualization skills.
Include problems that test understanding of parametric relationships.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in parametric equations and their applications.

Create challenging parametric problems that test advanced mathematical thinking.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the versatility of parametric modeling.
Use accurate mathematical models and appropriate parameter values.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to physics, engineering, and computer graphics
- Emphasize parametric behavior and curve analysis
- Provide distractors that test understanding of parametric concepts
"""
            },
            'polar_coordinates': {
                'user': """
Generate {quantity} challenging polar coordinate problems.
Include problems involving:
- Complex polar curve analysis and graphing
- Converting between polar and Cartesian coordinates
- Applications to circular and spiral motion
- Polar equations of conic sections
- Area and arc length calculations in polar coordinates

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring geometric intuition and algebraic manipulation.
Include problems that test understanding of polar coordinate systems.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in polar coordinates and their applications.

Create sophisticated polar coordinate problems that test advanced geometric thinking.
Ensure all problems have realistic applications and meaningful contexts.
Include problems that demonstrate the advantages of polar coordinate systems.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to physics, engineering, and navigation
- Emphasize geometric interpretations and coordinate conversions
- Provide distractors that test conceptual understanding
"""
            },
            'matrices': {
                'user': """
Generate {quantity} advanced matrix problems.
Include problems involving:
- Complex matrix operations and properties
- Applications to systems of equations and transformations
- Matrix equations and their solutions
- Determinants, inverses, and matrix algebra
- Real-world applications in computer graphics and data analysis

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring algebraic manipulation and conceptual understanding.
Include problems that test understanding of matrix properties.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in matrices and their applications.

Create challenging matrix problems that test advanced mathematical thinking.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the power of matrix algebra.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include applications to computer science, physics, and data analysis
- Emphasize matrix properties and algebraic operations
- Provide distractors that test understanding of matrix concepts
"""
            },
            'limits': {
                'user': """
Generate {quantity} challenging limit problems.
Include problems involving:
- Complex limit evaluation using multiple techniques
- Applications to calculus and continuity
- Limits at infinity and indeterminate forms
- One-sided limits and continuity analysis
- Real-world applications involving rates of change

Grade level: 11th-12th grade Honors/AP level
Focus on problems requiring analytical thinking and understanding of limiting processes.
Include problems that test understanding of continuity and behavior.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in limits and their applications.

Create sophisticated limit problems that test advanced mathematical thinking.
Ensure all problems have meaningful contexts and demonstrate limiting behavior.
Include problems that bridge algebra and calculus concepts.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include applications to physics, engineering, and calculus preparation
- Emphasize limiting behavior and continuity concepts
- Provide distractors that test common limit misconceptions
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
        """Get specific grading criteria for precalculus topics."""
        base_criteria = [
            "Mathematical accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and real-world connections",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'trigonometric_functions': ["Proper use of trigonometric identities and relationships"],
            'exponential_and_logarithmic_functions': ["Understanding of exponential growth and logarithmic properties"],
            'conic_sections': ["Geometric intuition and algebraic manipulation of conic equations"],
            'sequences_and_series': ["Pattern recognition and understanding of infinite processes"],
            'vectors': ["Spatial reasoning and vector algebra understanding"],
            'parametric_equations': ["Analytical thinking and parametric relationship understanding"],
            'polar_coordinates': ["Geometric interpretation and coordinate conversion skills"],
            'matrices': ["Matrix algebra understanding and transformation concepts"],
            'limits': ["Understanding of limiting processes and continuity concepts"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available precalculus topics."""
        return [
            "Trigonometric Functions",
            "Exponential and Logarithmic Functions",
            "Conic Sections",
            "Sequences and Series",
            "Vectors",
            "Parametric Equations",
            "Polar Coordinates",
            "Matrices",
            "Limits"
        ]