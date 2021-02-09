# this class represents a single github repository

class GitHubRepo:

    def __init__(self,name,language,stars):
        self.name = name
        self.language = language
        self.stars = stars

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.stars}"
    
    def __repr__(self):
        return f"GitHubRepo({self.name} ,{self.language} ,{self.stars})"




