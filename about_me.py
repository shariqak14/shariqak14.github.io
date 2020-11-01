class AboutMe:
    def __init__(self):
        self.origin = "Vernon, CT"
        self.education = "University of Connecticut"
        self.major = "Computer Science and Engineering"
        self.expected_graduation = "May 2021"
        self.email = "shariq.a.khan@uconn.edu"
        self.interests = [
            "software engineering",
            "data science",
            "data engineering",
            "web development",
        ]

    def __str__(self):
        return f"""I love {self.interests[0]}. I am into sdfkhsdif {self.interests[1]} sdfsfh"""


if __name__ == "__main__":
    about_me = AboutMe()
    print(about_me)