def health_inference_system(symptoms):

    symptoms = symptoms.lower()
    advice = []

    if "fever" in symptoms:
        advice.append("Drink plenty of fluids and take rest.")
        advice.append("Monitor temperature regularly.")
        advice.append("Consult a doctor if fever persists more than 3 days.")

    if "cough" in symptoms:
        advice.append("Drink warm fluids like ginger tea.")
        advice.append("Avoid cold drinks and dusty environments.")
        advice.append("Consult a doctor if cough lasts for more than 2 weeks.")

    if "headache" in symptoms:
        advice.append("Take a short break and relax in a quiet place.")
        advice.append("Drink water to stay hydrated.")
        advice.append("Sleep for at least 7-8 hours a day.")

    if "fatigue" in symptoms or "tired" in symptoms:
        advice.append("Ensure balanced diet with enough proteins.")
        advice.append("Get adequate sleep.")
        advice.append("Take light exercises or short walks daily.")

    if "stomach" in symptoms or "abdominal pain" in symptoms:
        advice.append("Avoid spicy/oily foods and drink plenty of water.")
        advice.append("Eat smaller, more frequent meals.")
        advice.append("Consult a doctor if pain is severe or persistent.")

    if not advice:
        advice.append("No specific advice found. Consider consulting a doctor for proper diagnosis.")

    return advice

print("Welcome to the Preventive Health Tips System!")
user_symptoms = input("Enter your symptoms (comma separated): ")

suggestions = health_inference_system(user_symptoms)

print("\n--- Preventive Health Tips ---")
for i, tip in enumerate(suggestions, start=1):
    print(f"{i}. {tip}")
exp 4                                                                                                                                                            def chatbot():
    print("Welcome to the College Helpdesk Chatbot!")
    print("Ask me anything about admissions, courses, fees, library, or campus.\n")

    # Keyword-response mapping
    responses = {
        "admission": "Admissions are open from June to August. You can apply online through our college website.",
        "course": "We offer undergraduate and postgraduate courses in Engineering, Arts, Science, and Commerce.",
        "fee": "Tuition fees vary by course. Please specify your course for detailed fee structure.",
        "library": "The library is open from 8 AM to 8 PM on weekdays and has a vast collection of books and e-resources.",
        "campus": "Our campus has modern facilities including sports grounds, labs, and cafeterias.",
        "scholarship": "Scholarships are available for meritorious and financially needy students. You can apply during the admission process.",
        "hostel": "Hostel accommodations are available for both boys and girls with all basic amenities.",
        "exam": "Exams are conducted at the end of each semester. You will receive your schedule two weeks prior.",
        "result": "Results are published online on the college website. You can check them using your student ID.",
        "contact": "You can contact us at helpdesk@college.edu or call 123-456-7890."
    }

    while True:
        user_input = input("You: ").lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Thank you for using the College Helpdesk Chatbot. Goodbye!")
            break

        response_given = False
        for keyword in responses:
            if keyword in user_input:
                print(f"Chatbot: {responses[keyword]}")
                response_given = True
                break

        if not response_given:
            print("Chatbot: Sorry, I didn't understand that. Can you please ask something else or be more specific?")

if __name__ == "__main__":
    chatbot()
