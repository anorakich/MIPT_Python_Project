import time


'''класс кликера'''
class Clicker:
    score = 0
    autoScoringSpeed = 0
    oneClickCost = 1

    def increaseScore(self, increase):
        self.score += increase

    def automine(self):
        time.sleep(0.2)
        self.increaseScore(self.autoScoringSpeed)

    def click(self):
        self.increaseScore(self.oneClickCost)

    def increaseAutomineSpeed(self, increase):
        self.autoScoringSpeed += increase
    def increaseOneClickCost(self,increase):
        self.oneClickCost += increase