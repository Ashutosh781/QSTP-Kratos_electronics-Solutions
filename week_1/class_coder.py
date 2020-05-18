#! /usr/bin/env python

## DEFINING CLASS ##
class Coder:
    score = 0    # Initialising score to be 0
    def __init__(self,name,age,languages = None ,projects = None): # Class constructor
        self.name = name
        self.age = age
        self.languages = languages
        self.projects = projects
        
        if self.languages is not None:
            l = len(self.languages)
        else:
            l = 0
            self.languages = []
        
        if self.projects is not None:
            p = len(self.projects)
        else:
            p = 0
            self.projects = []

        Coder.score = (10*l)*(1.5**p)
        print("Coder initialised\n")

     ## DEFINING METHODS ##    
    def addLanguage(self,x): # Adds 1 or more language to the object
        for y in x:
            self.languages.append(y)

        l = len(self.languages)

        if self.projects is not None:
            p = len(self.projects)
        else:
            p = 0
            self.projects = []
        
        Coder.score = (10*l)*(1.5**p)
        print("Languages added\n")
    
    def addProject(self,x): # Adds 1 or more project to the object
        for y in x:
            self.projects.append(y)
        
        p = len(self.projects)

        if self.languages is not None:
            l = len(self.languages)
        else:
            l = 0
            self.languages = []

        Coder.score = (10*l)*(1.5**p)
        print("Projects added\n")
           

    def info(self): # Prints a breif about the object
        print("Coder {} is of age {}." .format(self.name,self.age))
        
        lang = " language" if len(self.languages) == 1 else "NO languages" if len(self.languages) == 0 else " languages"
        proj = " project" if len(self.projects) == 1 else "NO projects" if len(self.projects) == 0 else " projects"
        
        print("{} knows" .format(self.name) ,end=' ')
        print(', '.join(self.languages) ,end='')
        print(f'{lang}.')

        print("{} is part of" .format(self.name) ,end=' ')
        print(', '.join(self.projects) ,end='')
        print(f'{proj}.')
        
        print("{}'s score is {}.\n" .format(self.name,Coder.score))

## DRIVER CODE ##
if __name__ == '__main__':
    num = int(input("Enter the number of coders to be initialised : "))
    for i in range(1,(num+1)):
        name = input("Enter name of the coder {} : " .format(i))
        age = int(input("Enter age of the coder {} : " .format(i)))
        language = input("Enter a list of languages : ")
        if language != '':
            language = language.split(',')
        else:
            language = []
        project = input("Enter a list of projects : ")
        if project != '':
            project = project.split(',')
        else:
            project = []

        a = Coder(name,age,language,project)
        a.info()

        while True:
            c = input("Do you want to append languages (Y/n) : ")
            if c == 'Y':
                x = input("Enter the languages to be appended : ")
                if x != '':
                    x = x.split(',')
                    a.addLanguage(x)
                else:
                    c = 'n'
                break
            elif c == 'n':
                break
        while True:
            d = input("Do you want to append projects (Y/n) : ")
            if d == 'Y':
                z = input("Enter the projects to be appended : ")
                if z != '':
                    z = z.split(',')
                    a.addProject(z)
                else:
                    d = 'n'
                break
            elif d == 'n':
                break

        if (c=='Y') or (d=='Y'): # Prints info again only when user appends inputs
            print("\n")
            a.info()
        
        print(f'End for Coder {i}')

    print("\nEnd")

#Sample object/instance
# a = Coder("Jack",20,["C","Java"],["Line follower","Cansat"])
# a.addLanguage(["C++","Python"])
# a.addProject(["Trotbot","Kratos","RT"])
# a.info()