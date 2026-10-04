def report_format(function):
    def wrapper(self):
        print("=" * 40)
        print("Report Start")
        print("=" * 40)
        function(self)
        print("=" * 40)
        print("Report End")
        print("=" * 40)
    return wrapper


class Report:
    def __init__(self, title, section, student, math, science, english):
        self.title = title
        self.section = section
        self.student = student
        self.math = math
        self.science = science
        self.english = english

    @classmethod
    def sample_report(cls):
        title = input("Enter Report Title: ")
        section = input("Enter Section: ")
        student = input("Enter Student Name: ")
        math = int(input("Enter Math Marks: "))
        science = int(input("Enter Science Marks: "))
        english = int(input("Enter English Marks: "))
        return cls(title, section, student, math, science, english)

    def __str__(self):
        return f"Title : {self.title}"

    def __len__(self):
        return len(self.section)

    @report_format
    def generate_report(self):
        print("Title   :", self.title)
        print("Section :", self.section)
        print("Student :", self.student)
        print("Math    :", self.math)
        print("Science :", self.science)
        print("English :", self.english)


# Create report using user input
r = Report.sample_report()

print(r)
print("Length of Section:", len(r))

r.generate_report()