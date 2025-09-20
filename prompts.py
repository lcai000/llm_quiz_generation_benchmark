import os
from dotenv import load_dotenv
from llm_framework import LLM
load_dotenv(override=True)
DELIMETER=os.getenv('DELIMETER')

class GeneratePrompts:
    def __init__(self):
        self.LLM = LLM()
    def _user_prompt(self,details:str)->str:
        prompt = f"""
Generate a multiple-choice quiz based on a list of details.
Only ouput the specified number of questions. Each question has 4 answer choices.
No blank lines.
No labels, only content.
Question can only have question in it, no answer.
this is the correct output format for a single question:

<format>
    question {DELIMETER} correct {DELIMETER} incorrect1 {DELIMETER} incorrect2 {DELIMETER} incorrect3
<format>

These are the quiz details:
<details>
    {details}
<details>
    """
        return prompt
    def _system_prompt(self,)->str:
        agent = self.LLM.agent(
            identity="Quiz creating agent",
            purpose="Create accurate and quality quizzes for any given topic",
            output_style="follow the format strictly",
            agent_context="Educational AI assistant"
        )
        return agent
    def __call__(self,details)->dict[str,str]:
       prompt = {"user_prompt":self._user_prompt(details=details),
                 "system_prompt":self._system_prompt()}
       return prompt
    
class Math:
    def __init__(self):
        self.QUIZ = GeneratePrompts()
        self.quantity:int=0
    def multiplication(self):
        topic = f"Create a {self.quantity} question 3 digit by 3 digit multiplication quiz for 3rd-4th graders"
        return self.QUIZ(details=topic)
    def algebraic_equations(self):
        topic = f"Create a {self.quantity} question algebraic equations with multiple operations, for 5th-6th graders"
        return self.QUIZ(details=topic)
    
if __name__=="__main__":
    m = Math()
    prompt = m.multiplication()
    print(prompt["user_prompt"]+"\n")
    print(prompt["system_prompt"])