from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages_list = [python, ruby, visual_basic]
for i in range(0, len(languages_list)):
    if languages_list[i].is_dynamic():
        print(languages_list[i].name)