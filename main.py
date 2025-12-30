# ==========================================
# Project: Hackathon 2 - Phase 1
# Topic: In-Memory To-Do Console App
# ==========================================

# Hum 'tasks' ki aik khali list banate hain jo data ko temporary save rakhegi
# Jab program band hoga, ye list khali ho jayegi (Isi ko In-Memory kehte hain)
tasks = []

def show_menu():
    """Ye function user ko options dikhayega"""
    print("\n--- WELCOME TO MY TO-DO APP ---")
    print("1. Naya Task Likhein")
    print("2. Puri List Dekhein")
    print("3. Koi Task Delete Karein")
    print("4. App Band Karein")
    return input("\nAap kya karna chahte hain? (1-4): ")

def add_task():
    """Naya kaam list mein shamil karne ke liye"""
    new_task = input("\nTask ka naam batayein: ")
    if new_task.strip() != "":
        tasks.append(new_task)
        print("Done! Task add ho gaya.")
    else:
        print("Galti: Khali task add nahi ho sakta!")

def view_tasks():
    """List ko screen par dikhane ke liye"""
    print("\n--- AAPKI CURRENT LIST ---")
    if not tasks:
        print("List abhi khali hai.")
    else:
        # Enumerate se hum 1, 2, 3 numbering dikhate hain
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def delete_task():
    """Number ke zariye list se task hatane ke liye"""
    view_tasks()
    if tasks:
        try:
            choice = int(input("\nKaunsa number delete karna hai? "))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice - 1)
                print(f"Removed: {removed}")
            else:
                print("Galti: Ye number list mein nahi hai.")
        except ValueError:
            print("Galti: Sirf number enter karein!")

# --- MAIN PROGRAM LOOP ---
# Ye hissa program ko tab tak chalata rahega jab tak user Exit na karde
def start():
    while True:
        user_input = show_menu()

        if user_input == "1":
            add_task()
        elif user_input == "2":
            view_tasks()
        elif user_input == "3":
            delete_task()
        elif user_input == "4":
            print("\nProject Phase 1 Complete. Allah Hafiz!")
            break
        else:
            print("\nSahi option choose karein (1 se 4 tak).")

# Program yahan se shuru hota hai
if __name__ == "__main__":
    start()