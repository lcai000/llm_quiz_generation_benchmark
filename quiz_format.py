import random
import os
import json
from dotenv import load_dotenv
load_dotenv(override=True)
DELIMETER=os.getenv('DELIMETER')

def remove_empty(x:list)->list:
        removed = [line.strip() for line in x if line.strip()]
        return removed
    
def format_question(questions:str)->str:
    raw_set = questions.split('\n')
    raw_set = remove_empty(raw_set)
    all_question_data = {}
    for index,question in enumerate(raw_set):
        curr_individual_q = question.split(DELIMETER)
        choices = curr_individual_q[1:]
        random.shuffle(choices)
        remove_empty(choices)
        correct_index = choices.index(curr_individual_q[1])
        curr_q_dict={
            'QUESTION':curr_individual_q[0],
            'ANSWER':correct_index,
            'CHOICES':choices
        }
        all_question_data[index]=curr_q_dict
    question_data_json = json.dumps(all_question_data,indent=2)
    return question_data_json

if __name__=="__main__":
    quiz = """
question: What is 123 × 456? | 56088 | 55088 | 57088 | 54088
question: What is 234 × 567? | 132678 | 131678 | 133678 | 130678
question: What is 345 × 678? | 233910 | 232910 | 234910 | 231910
question: What is 456 × 789? | 359784 | 358784 | 360784 | 357784
question: What is 567 × 891? | 505197 | 504197 | 506197 | 503197
question: What is 678 × 912? | 618336 | 617336 | 619336 | 616336
question: What is 789 × 123? | 97047 | 96047 | 98047 | 95047
question: What is 891 × 234? | 208494 | 207494 | 209494 | 206494
question: What is 912 × 345? | 314640 | 313640 | 315640 | 312640
question: What is 123 × 789? | 97047 | 96047 | 98047 | 95047
"""
    print(format_question(questions=quiz))