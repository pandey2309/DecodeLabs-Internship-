print("=" * 60)
print("      SMART LEARNING RECOMMENDATION SYSTEM")
print("=" * 60)

recommendations = {

    "ai/ml": {
        "skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "NLP"
        ],

        "projects": [
            "Loan Prediction System",
            "Credit Card Fraud Detection",
            "Movie Recommendation System"
        ],

        "books": [
            "Hands-On Machine Learning",
            "Deep Learning with Python"
        ]
    },

    "web development": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React"
        ],

        "projects": [
            "Portfolio Website",
            "E-Commerce Website",
            "Blog Website"
        ],

        "books": [
            "Eloquent JavaScript",
            "JavaScript: The Good Parts"
        ]
    },

    "cybersecurity": {
        "skills": [
            "Networking",
            "Linux",
            "Ethical Hacking",
            "Web Security"
        ],

        "projects": [
            "Port Scanner",
            "Password Strength Checker",
            "Network Monitor"
        ],

        "books": [
            "The Web Application Hacker's Handbook",
            "Linux Basics for Hackers"
        ]
    },

    "data science": {
        "skills": [
            "Python",
            "Pandas",
            "NumPy",
            "Data Visualization"
        ],

        "projects": [
            "Sales Analysis",
            "Customer Segmentation",
            "Data Dashboard"
        ],

        "books": [
            "Python for Data Analysis",
            "Data Science from Scratch"
        ]
    },

    "competitive programming": {
        "skills": [
            "DSA",
            "STL",
            "Greedy",
            "Dynamic Programming"
        ],

        "projects": [
            "CP Tracker",
            "Contest Analyzer",
            "Problem Recommendation Tool"
        ],

        "books": [
            "CP Handbook",
            "Guide to Competitive Programming"
        ]
    }
}

print("\nAvailable Interests:")

for key in recommendations:
    print("-", key.title())

user_interest = input(
    "\nEnter your interest: "
).lower().strip()

if user_interest in recommendations:

    data = recommendations[user_interest]

    print("\nRecommended Skills:")
    for skill in data["skills"]:
        print("•", skill)

    print("\nRecommended Projects:")
    for project in data["projects"]:
        print("•", project)

    print("\nRecommended Books:")
    for book in data["books"]:
        print("•", book)

else:
    print("\nSorry! No recommendations available.")