class people:
    country="Nepal"
    def showDetails(self):
        print("Here the people are Nepali")
class Nepali(people):
    language="Nepali"
    Religion="Hindu"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("their religion is Hinduism")   

p=people()
p.showDetails()
n=Nepali()
n.showDetails()
print(p.country)
    