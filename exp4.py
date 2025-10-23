import re

class CollegeHelpdeskChatbot:
    def __init__(self):
        # Mapping keywords/synonyms to main categories
        self.keywords = {
            "admission": ["admission", "apply", "enroll", "registration"],
            "course": ["course", "program", "branch", "degree"],
            "fees": ["fees", "fee", "tuition", "payment", "cost"],
            "library": ["library", "books", "reading room"],
            "hostel": ["hostel", "accommodation", "room", "stay"],
            "placement": ["placement", "job", "career", "campus"],
            "sports": ["sports", "games", "gym", "playground"],
            "transport": ["bus", "transport", "shuttle"],
            "exam": ["exam", "test", "assessment", "timetable"],
            "contact": ["contact", "email", "phone", "helpdesk"]
        }

        # Responses for categories
        self.responses = {
            "admission": "📌 Admission details are available on our website. Applications usually open in June.",
            "course": "📚 We offer B.Tech, M.Tech, MBA, and PhD. Which program are you interested in?",
            "fees": "💰 The fee structure depends on the course. Visit the accounts section on the website.",
            "library": "📖 The library is open 8 AM–8 PM. Students can borrow 3 books at a time for 15 days.",
            "hostel": "🏠 Hostels are available with Wi-Fi, mess, and 24/7 security. Separate hostels for boys & girls.",
            "placement": "💼 Our Placement Cell invites top recruiters like TCS, Infosys, Wipro, and Amazon.",
            "sports": "⚽ We have cricket, football, badminton courts, and a gym inside the campus.",
            "transport": "🚌 Buses cover major routes across the city. Timings are updated on the notice board.",
            "exam": "📝 Exams are semester-wise. The timetable is available in the exam section of the portal.",
            "contact": "☎ You can contact the helpdesk at helpdesk@college.edu or call +91-9876543210."
        }

        # To maintain context
        self.last_topic = None

    def get_category(self, user_input):
        for category, keywords in self.keywords.items():
            for word in keywords:
                if re.search(rf"\b{word}\b", user_input.lower()):
                    return category
        return None

    def chat(self):
        print("🤖 College Helpdesk Chatbot (Advanced)")
        print("Type 'exit' to end the chat.\n")

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print("Chatbot: Thank you! Wishing you success in your studies. 👋")
                break

            category = self.get_category(user_input)

            if category:
                self.last_topic = category
                print(f"Chatbot: {self.responses[category]}")
            elif "more" in user_input.lower() and self.last_topic:
                print(f"Chatbot: Here's more info about {self.last_topic}: {self.responses[self.last_topic]}")
            else:
                print("Chatbot: Sorry, I don't have info on that. Please try rephrasing or contact helpdesk.")
