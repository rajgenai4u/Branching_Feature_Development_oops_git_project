def display_dashboard(role):
    if role == "Student":
        return "Welcome to Student Dashboard: View enrolled courses."
    elif role == "Mentor":
        return "Welcome to Mentor Dashboard: View assigned mentees."
    return "Welcome to General Dashboard."

if __name__ == "__main__":
    print(display_dashboard("Student"))