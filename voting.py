def create_candidates():
    candidates = []
    num_candidates = int(input("Enter the number of candidates: "))
    for i in range(num_candidates):
        candidate = input(f"Enter the name of candidate {i+1}: ")
        candidates.append({"name": candidate, "votes": 0})
    return candidates

def display_candidates(candidates):
    print("List of Candidates:")
    for i, candidate in enumerate(candidates):
        print(f"{i+1}. {candidate['name']}")

def vote(candidates):
    print("Please vote for a candidate by entering the corresponding number:")
    for i, candidate in enumerate(candidates):
        print(f"{i+1}. {candidate['name']}")
    choice = int(input("Your choice: "))
    if 1 <= choice <= len(candidates):
        candidates[choice - 1]['votes'] += 1
        print("Thank you for voting!")
    else:
        print("Invalid choice. Please try again.")

def display_results(candidates):

    print("Voting Results:")
    for candidate in candidates:
        print(f"{candidate['name']}: {candidate['votes']} votes")

def voting():
    candidates = create_candidates()
    while True:
        print("\n1. Display Candidates\n2. Vote\n3. Display Results\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_candidates(candidates)
        elif choice == '2':
            vote(candidates)
        elif choice == '3':
            display_results(candidates)
        elif choice == '4':
            print("Thank you for participating in the voting!")
            break
        else:
            print("Invalid choice. Please try again.")


voting()
