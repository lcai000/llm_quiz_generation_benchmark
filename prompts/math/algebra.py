"""
Algebra benchmark prompt generator with challenging high school level questions.
"""
from typing import Dict, List, Tuple, Optional
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class AlgebraBenchmark(BaseBenchmarkGenerator):
    """Algebra benchmark generator focused on challenging high school problems."""

    def __init__(self):
        super().__init__("Algebra")
        self._setup_templates()

    # Topic-specific methods for direct access
    def linear_equations(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for linear equations topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for linear equations
        """
        return self.generate_benchmark_prompt('linear_equations', question_count, **kwargs)

    def quadratic_equations(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for quadratic equations topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for quadratic equations
        """
        return self.generate_benchmark_prompt('quadratic_equations', question_count, **kwargs)

    def systems_of_equations(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for systems of equations topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for systems of equations
        """
        return self.generate_benchmark_prompt('systems_of_equations', question_count, **kwargs)

    def polynomials(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for polynomials topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for polynomials
        """
        return self.generate_benchmark_prompt('polynomials', question_count, **kwargs)

    def functions(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for functions topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for functions
        """
        return self.generate_benchmark_prompt('functions', question_count, **kwargs)

    def exponents_and_radicals(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for exponents and radicals topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for exponents and radicals
        """
        return self.generate_benchmark_prompt('exponents_and_radicals', question_count, **kwargs)

    def rational_expressions(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for rational expressions topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for rational expressions
        """
        return self.generate_benchmark_prompt('rational_expressions', question_count, **kwargs)

    def inequalities(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for inequalities topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for inequalities
        """
        return self.generate_benchmark_prompt('inequalities', question_count, **kwargs)

    def _setup_templates(self) -> None:
        """Set up algebra topic templates."""
        self.topic_templates = {
            'linear_equations': {
                'user': """
Generate {quantity} challenging linear equation problems that test deep understanding.
Include problems involving:
- Multi-step equations with variables on both sides
- Equations with fractions and decimals
- Literal equations and formula manipulation
- Real-world applications requiring equation setup
- Systems of linear equations with multiple variables

Grade level: 9th-10th grade Honors/AP level
Focus on problems requiring analytical thinking and multiple solution steps.
Each problem should have exactly one unambiguous correct answer.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in challenging algebra problems.

Create sophisticated linear equation problems that require critical thinking.
Ensure all problems are mathematically sound and have reasonable solutions.
Include problems that demonstrate the practical applications of linear equations.
Use appropriate mathematical terminology and maintain high academic standards.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be challenging for advanced high school students
- Include real-world contexts where appropriate
- Ensure only one correct answer per question
- Provide plausible distractors that test common misconceptions
"""
            },
            'quadratic_equations': {
                'user': """
Generate {quantity} advanced quadratic equation problems.
Include problems involving:
- Complex quadratic equations requiring multiple methods
- Applications to optimization and maximum/minimum problems
- Projectile motion and physics applications
- Geometric applications with area and perimeter
- Systems involving quadratic and linear equations

Grade level: 10th-11th grade Honors/AP level
Focus on problems requiring deep understanding of quadratic relationships.
Include both exact and approximate solutions where appropriate.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in quadratic equations and their applications.

Create challenging quadratic problems that test advanced algebraic thinking.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that require multiple steps and strategic thinking.
Use accurate mathematical models and reasonable parameter values.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors/AP high school level
- Include real-world applications that demonstrate quadratic relationships
- Ensure mathematical accuracy and realistic solutions
- Provide distractors that reflect common calculation errors
"""
            },
            'systems_of_equations': {
                'user': """
Generate {quantity} challenging systems of equations problems.
Include problems involving:
- Three-variable systems requiring strategic elimination
- Non-linear systems (quadratic-linear combinations)
- Systems with no solution or infinite solutions
- Real-world applications with multiple constraints
- Matrix applications and advanced solution methods

Grade level: 10th-11th grade Honors/AP level
Focus on problems requiring analytical thinking and systematic approaches.
Include problems that test understanding of solution methods and interpretations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in systems of equations.

Create sophisticated systems of equations problems that require advanced problem-solving skills.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the power of algebraic modeling.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include diverse solution methods and applications
- Ensure problems have clear, interpretable solutions
- Provide distractors that test understanding of solution concepts
"""
            },
            'polynomials': {
                'user': """
Generate {quantity} advanced polynomial problems.
Include problems involving:
- Polynomial division with remainders
- Factor theorem and rational root theorem applications
- Polynomial inequalities and interval analysis
- Applications to volume, surface area, and optimization
- Graphical analysis of polynomial behavior

Grade level: 10th-11th grade Honors level
Focus on problems requiring deep understanding of polynomial properties.
Include both computational and conceptual challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in polynomial functions and their applications.

Create challenging polynomial problems that test advanced algebraic concepts.
Ensure all problems have realistic applications and meaningful contexts.
Include problems that demonstrate the importance of polynomial modeling.
Use accurate mathematical relationships and reasonable coefficients.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors high school level
- Include both theoretical and applied problems
- Ensure mathematical accuracy and reasonable solutions
- Provide distractors that test conceptual understanding
"""
            },
            'functions': {
                'user': """
Generate {quantity} advanced function problems.
Include problems involving:
- Function composition and decomposition
- Inverse functions and their properties
- Transformations of functions (translations, reflections, stretches)
- Piecewise functions and continuity
- Real-world modeling with various function types

Grade level: 11th grade Honors/AP level
Focus on problems requiring deep understanding of function concepts and relationships.
Include problems that test analytical and graphical reasoning skills.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in function theory and applications.

Create sophisticated function problems that test conceptual understanding and analytical skills.
Ensure all problems have meaningful contexts and realistic applications.
Include problems that demonstrate the versatility of functions as mathematical models.
Use appropriate mathematical terminology and maintain high academic standards.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include diverse function types and applications
- Ensure problems test both computational and conceptual understanding
- Provide distractors that reflect common misconceptions
"""
            },
            'exponents_and_radicals': {
                'user': """
Generate {quantity} challenging exponent and radical problems.
Include problems involving:
- Rational exponents and complex radical expressions
- Exponential equations requiring logarithms
- Applications to exponential growth and decay
- Complex radical equations and extraneous solutions
- Scientific notation and significant figures in context

Grade level: 10th-11th grade Honors level
Focus on problems requiring mastery of exponent rules and radical operations.
Include problems that connect to real-world applications in science and finance.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in exponents, radicals, and their applications.

Create challenging problems that test deep understanding of exponential and radical concepts.
Ensure all problems have realistic applications and meaningful contexts.
Include problems that demonstrate the importance of exponential relationships.
Use accurate mathematical models and reasonable parameter values.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors high school level
- Include applications to science, finance, and other fields
- Ensure mathematical accuracy and realistic solutions
- Provide distractors that test understanding of exponent rules
"""
            },
            'rational_expressions': {
                'user': """
Generate {quantity} advanced rational expression problems.
Include problems involving:
- Complex rational expressions with multiple variables
- Advanced rational equations requiring strategic solving
- Applications to rates, work problems, and mixture problems
- Asymptote analysis and graphical behavior
- Real-world modeling with rational functions

Grade level: 11th grade Honors/AP level
Focus on problems requiring algebraic manipulation and analytical thinking.
Include problems that test understanding of domain restrictions and behavior.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in rational expressions and their applications.

Create sophisticated rational expression problems that test advanced algebraic skills.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the practical importance of rational functions.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced high school students
- Include diverse applications and solution methods
- Emphasize domain considerations and extraneous solutions
- Provide distractors that test conceptual understanding
"""
            },
            'inequalities': {
                'user': """
Generate {quantity} challenging inequality problems.
Include problems involving:
- Compound inequalities with multiple conditions
- Absolute value inequalities in various forms
- Polynomial and rational inequalities
- Systems of inequalities and feasible regions
- Real-world optimization with constraints

Grade level: 10th-11th grade Honors level
Focus on problems requiring analytical thinking and systematic approaches.
Include problems that test understanding of solution sets and their interpretations.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert mathematics educator specializing in inequalities and their applications.

Create challenging inequality problems that test logical reasoning and algebraic skills.
Ensure all problems have realistic contexts and meaningful applications.
Include problems that demonstrate the importance of constraint modeling.
Use appropriate mathematical techniques and ensure solution validity.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should be at honors high school level
- Include diverse inequality types and applications
- Ensure problems test both computational and conceptual understanding
- Provide distractors that reflect common solution errors
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
        """Get specific grading criteria for algebra topics."""
        base_criteria = [
            "Mathematical accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for honors/AP high school",
            "Educational relevance and real-world connections",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'linear_equations': ["Proper equation setup and solution methods"],
            'quadratic_equations': ["Multiple solution approaches and interpretation"],
            'systems_of_equations': ["Strategic solution selection and verification"],
            'polynomials': ["Understanding of polynomial properties and behavior"],
            'functions': ["Conceptual understanding of function relationships"],
            'exponents_and_radicals': ["Mastery of exponent rules and radical operations"],
            'rational_expressions': ["Domain considerations and algebraic manipulation"],
            'inequalities': ["Logical reasoning and solution set interpretation"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available algebra topics."""
        return [
            "Linear Equations",
            "Quadratic Equations",
            "Systems of Equations",
            "Polynomials",
            "Functions",
            "Exponents and Radicals",
            "Rational Expressions",
            "Inequalities"
        ]