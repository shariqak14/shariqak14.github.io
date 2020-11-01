class AboutMe:
    def __init__(self):
        self.origin = "Vernon, CT"
        self.education = "University of Connecticut"
        self.major = "Computer Science and Engineering"
        self.expected_graduation = "May 2021"
        self.email = "shariq.a.khan@uconn.edu"
        self.interests = [
            "software engineering",
            "machine learning",
            "web development",
        ]

    def __str__(self):
        return f"""Lorem ipsum dolor sit amet {self.origin} adipisicing elit. Cum doloremque consequuntur
		Nemo, {self.education} culpa in illo nobis quasi impedit, dolore tempora obcaecati quod exercitationem. 
		Odit, nostrum doloremque asperiores ducimus ex excepturi {self.major} rerum enim fugiat tiae 
		sit rem animi deserunt inventore quaerat, unde laborum dolores, similique eat quos ratione. Aut molestiae 
		minima laborum {self.email} ullam iste aperiam, eius alias sint, {self.interests[0]}, {self.interests[1]},
		and {self.interests[2]} beatae molestiae ullam atque quisquam  praesentium nisi. Tempore officiis 😇!"""


if __name__ == "__main__":
    about_me = AboutMe()
    print(about_me)