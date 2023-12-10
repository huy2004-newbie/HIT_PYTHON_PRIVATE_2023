class Job: 
    def __init__(self, ma_Job , ten, nganh, luong):
        self.ma_Job = ma_Job
        self.ten = ten
        self.nganh = nganh
        self.luong = luong
        
    def evaluate(self, skills):
        average = sum(skills.values()) / len(skills)
        if average > 9.0:
            return "Rất phù hợp"
        elif average > 7.0:
            return "Phù hợp"
        elif average > 5.0:
            return "Tạm được"
        elif average > 3.0:
            list_skill = []
            for key, value in skills.items():
                if(value < 4.0):
                    list_skill.append(key)
            return f"Cần bổ sung kiến thức: {', '.join(list_skill)}"
        else:
            return "Cần học lại kiến thức base"    
        
    def __str__(self):
        return f'Mã Job: {self.ma_Job}  \nTên Job: {self.ten}  \nNgành: {self.nganh}  \nLương: {self.luong}'
    
    
class AI(Job):
    def __init__(self, ma_Job, ten, nganh, luong, python_Skill, ml_Skill, deep_Skill, math_Skill):
        super().__init__(ma_Job, ten, nganh, luong)
        self.python_Skill = python_Skill
        self.ml_Skill = ml_Skill
        self.deep_Skill = deep_Skill
        self.math_Skill = math_Skill
        
    def evaluate(self):
        skill = {"Python": self.python_Skill, "ML": self.ml_Skill, "Deep": self.deep_Skill, "Math": self.math_Skill}
        result = super().evaluate(skill)
        print(result)
    
    def __str__(self):
        return f'{super().__str__()} \nPython_skill: {self.python_Skill} \nML_skill: {self.ml_Skill} \nDeep_skill: {self.deep_Skill} \nMath_skill: {self.math_Skill}'
        
class Backend(Job):
    def __init__(self, ma_Job, ten, nganh, luong, sql_Skill, oop_Skill, api_Skill, java_Skill):
        super().__init__(ma_Job, ten, nganh, luong)
        self.sql_Skill = sql_Skill
        self.oop_Skill = oop_Skill
        self.api_Skill = api_Skill
        self.java_Skill = java_Skill
        
    def evaluate(self):
        skill = {"SQL": self.sql_Skill, "OOP": self.oop_Skill, "API": self.api_Skill, "Java": self.java_Skill}
        result = super().evaluate(skill)
        print(result)

    def __str__(self):
        return f'{super().__str__()} \nSQL_skill: {self.sql_Skill} \nOOP_skill: {self.oop_Skill} \nAPI_skill: {self.api_Skill} \nJava: {self.java_Skill}'
    

class Frontend(Job):
    def __init__(self, ma_Job, ten, nganh, luong, html_Skill, css_Skill, nodejs_Skill, ux, ui):
        super().__init__(ma_Job, ten, nganh, luong)
        self.html_Skill = html_Skill
        self.css_Skill = css_Skill
        self.nodejs_Skill = nodejs_Skill
        self.ux = ux
        self.ui = ui
        
    def evaluate(self):
        skill = {"HTML": self.html_Skill, "CSS": self.css_Skill, "NodeJS": self.nodejs_Skill, "UX": self.ux, "UI": self.ui}
        result = super().evaluate(skill)
        print(result)
    
    def __str__(self):
        return f'{super().__str__()} \nHTML_skill: {self.html_Skill} \nCss_skill: {self.css_Skill} \nNodejs_skill: {self.nodejs_Skill} \nUX: {self.ux} \nUI: {self.ui}'
    
        
class Fullstack(Backend, Frontend):
    def __init__(self, ma_Job, ten, nganh, luong, sql_Skill, oop_Skill, api_Skill, java_Skill, html_Skill, css_Skill, nodejs_Skill, ux, ui):
        Backend.__init__(self, ma_Job, ten, nganh, luong, sql_Skill, oop_Skill, api_Skill, java_Skill)
        Frontend.__init__(self,ma_Job, ten, nganh, luong, html_Skill, css_Skill, nodejs_Skill, ux, ui)
        
    # def __str__(self):
    #     return super().__str__()

    def evaluate(self):
        skill = {
            "SQL": self.sql_Skill, "OOP": self.oop_Skill, "API": self.api_Skill, "Java": self.java_Skill,
            "HTML": self.html_Skill, "CSS": self.css_Skill, "NodeJS": self.nodejs_Skill, "UX": self.ux, "UI": self.ui
        }
        result = super().evaluate(skill)
        print(result)    
        

ai_job = AI(1, "AI001", "Data Scientist", 10000, 9.5, 9.0, 8.5, 9.0)
backend_job = Backend(2, "BE001", "Backend Developer", 8000, 8.0, 8.5, 8.0, 7.5)
frontend_job = Frontend(3, "FE001", "Frontend Developer", 7500, 8.0, 9.0, 8.5, 8.0, 8.5)
# fullstack_job = Fullstack(5, "FS001", "Fullstack Developer", 9000, 8.0, 8.5, 8.0, 7.5, 8.0, 9.0, 8.5, 8.0, 8.5)
jobs = [ai_job, backend_job, frontend_job]
for x in jobs:
    print(x)