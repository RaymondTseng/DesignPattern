from abc import abstractmethod, ABC


# Decorator Pattern
class SchoolReport(ABC):
    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def sign(self, name):
        pass


class FourthGradeSchoolReport(SchoolReport):
    def report(self):
        print("------------------------------------")
        print("Dear XXX,")
        print("Your grades are listed as follow")
        print("Chinese: 60, Math: 61, English: 63")
        print("------------------------------------")

    def sign(self, name):
        print("The name is %s" % name)


class Decorator(ABC):
    def __init__(self, school_report):
        self.school_report = school_report

    def report(self):
        self.school_report.report()

    def sign(self, name):
        self.school_report.sign(name)


class HighScoreDecorator(Decorator):
    def __init__(self, school_report):
        super().__init__(school_report)

    def report_high_score(self):
        print("The highest scores are")
        print("Chinese: 75, Math: 77, English: 78")

    def report(self):
        self.report_high_score()
        super().report()


class RankingDecorator(Decorator):
    def __init__(self, school_report):
        super().__init__(school_report)

    def report_ranking(self):
        print("Your ranking is: 38th")

    def report(self):
        super().report()
        self.report_ranking()


if __name__ == "__main__":
    sr = FourthGradeSchoolReport()
    sr = HighScoreDecorator(sr)
    sr = RankingDecorator(sr)
    sr.report()
