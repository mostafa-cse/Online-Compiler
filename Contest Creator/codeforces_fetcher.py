import requests
import json

# Configuration
HANDLE = "...-_-..."
RATING = 1200
PAGE = 1

def get_unsolved_problems():
    try:
        # Fetch all problems and filter locally by rating.
        print("Fetching all problems...")
        problems_url = "https://codeforces.com/api/problemset.problems"

        problems_response = requests.get(problems_url, timeout=15)
        problems_response.raise_for_status()
        problems_data = problems_response.json()

        if problems_data["status"] != "OK":
            print(f"API Error: {problems_data}")
            return

        all_problems = problems_data["result"]["problems"]

        # Filter by rating
        problems_list = [p for p in all_problems if p.get("rating") == RATING]

        print(f"Found {len(problems_list)} problems with rating {RATING}")

        # Fetch user's solved problems
        print(f"Fetching solved problems for handle: {HANDLE}...")
        status_url = "https://codeforces.com/api/user.status"
        status_params = {"handle": HANDLE}

        status_response = requests.get(status_url, params=status_params, timeout=15)
        status_response.raise_for_status()
        status_data = status_response.json()

        if status_data["status"] != "OK":
            print(f"Handle not found or API Error: {status_data}")
            return

        # Get solved problem IDs
        solved_ids = set()
        for submission in status_data["result"]:
            if submission.get("verdict") != "OK":
                continue

            problem = submission.get("problem", {})
            contest_id = problem.get("contestId")
            index = problem.get("index")
            if contest_id is None or index is None:
                continue

            solved_ids.add(f"{contest_id}{index}")

        print(f"Total solved problems: {len(solved_ids)}")
        print(f"Total {RATING}-rated problems: {len(problems_list)}\n")

        # Find problems that are not accepted yet.
        unsolved = []
        for problem in problems_list:
            contest_id = problem.get("contestId")
            index = problem.get("index")
            if contest_id is None or index is None:
                continue

            problem_id = f"{contest_id}{index}"
            if problem_id not in solved_ids:
                unsolved.append(problem)

        # Display unsolved problems.
        print(f"All {RATING}-rated NOT ACCEPTED problems:")
        print("=" * 80)

        vjudge_lines = ["CodeForces\t|\tProblemID\t|\tCount\t|"]

        for idx, problem in enumerate(unsolved, 1):
            contest_id = problem["contestId"]
            index = problem["index"]
            problem_id = f"{contest_id}{index}"
            print(f"{idx:3}. ID: {problem_id} | {problem['name']}")
            vjudge_lines.append(f"CodeForces\t|\t{problem_id}\t|\t{idx}\t|")

        print("=" * 80)
        print(f"\nTotal NOT ACCEPTED problems: {len(unsolved)}")

        with open("vjudge_contest_script.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(vjudge_lines) + "\n")
        print("Saved to vjudge_contest_script.txt")
        
        # Save to file
        with open("not_accepted_problems.json", "w") as f:
            json.dump(unsolved, f, indent=2)
        print("Saved to not_accepted_problems.json")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_unsolved_problems()
