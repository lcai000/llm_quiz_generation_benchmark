import json
from llm_framework import LLM, Gemini
import prompts
from quiz_format import format_question

class Generate:
    def __init__(self):
        self.LLM = LLM()
        self.key,self.name,self.url=self.LLM.initialize_llm(KEY='LLM_KEY',
                                                            NAME='LLM_NAME',
                                                            URL='LLM_URL')
        
    def __call__(self,
                 prompt:str,
                 system_prompt:str|None=None,
                 max_tokens:int|None=None,
                 mode:str="default")->str:
        if mode == "gemini":
            self.LLM = Gemini()
        contents = self.LLM.llm_contents(key=self.key,
                                         name=self.name,
                                         prompt=prompt,
                                         system_prompt=system_prompt,
                                         max_tokens=max_tokens)
        return self.LLM.get_output(url=self.url, llm_contents=contents)

class CreateQuiz:
    def __init__(self):
        self.GEN = Generate()
        self.llm_info = LLM().initialize_llm(KEY='LLM_KEY',NAME='LLM_NAME',URL='LLM_URL')
        self.name = self.llm_info[1]

    def __call__(self,batch_size:int,
                 batches:int,
                 prompt:str,
                 system_prompt:str,
                 mode:str="default")->str:
        llm_mode = mode
        print(f"mode:{mode}")
        generated = {}
        quiz = ""
        benchmark_quantity = batches*batch_size
        for batch in range(batches):
            curr_set = self.GEN(prompt=prompt,
                        system_prompt=system_prompt,
                        mode=llm_mode
                        )
            if curr_set:
                print(f"question batch number {batch} generated\n")
                #print(curr_set)
            quiz=quiz+'\n'+curr_set+'\n'
        quiz = format_question(questions=quiz)
        print(quiz)
        return {
            "MODEL":self.name,
            "QUANTITY":benchmark_quantity,
            "BATCH_SIZE":batch_size,
            "QUIZ":quiz
        }
        

if __name__=="__main__":
    # from prompts import Math
    # math_prompt = Math()
    # quiz = CreateQuiz()
    # multiplication_prompt = math_prompt.multiplication(quantity=10)
    # user_prompt, system_prompt = multiplication_prompt["user_prompt"],multiplication_prompt["system_prompt"]
    # multiplication_quiz = quiz(batch_size=10,
    #                            batches=3,
    #                            prompt=user_prompt,
    #                            system_prompt=system_prompt)
    # print(multiplication_quiz)
    # with open("example_result.json","w") as f:
    #     m = json.dumps(multiplication_quiz,indent=2)
    #     f.write(str(multiplication_quiz))

    from prompts import Math
    math_prompt = Math()
    quiz = CreateQuiz()
    multiplication_prompt = math_prompt.multiplication(quantity=10)
    user_prompt, system_prompt = multiplication_prompt["user_prompt"],multiplication_prompt["system_prompt"]
    multiplication_quiz = quiz(batch_size=10,
                                batches=3,
                                prompt=user_prompt,
                                system_prompt=system_prompt,
                                mode="gemini")
    print(multiplication_quiz)
    with open("example_result.json","w") as f:
        m = json.dumps(multiplication_quiz,indent=2)
        f.write(str(multiplication_quiz))