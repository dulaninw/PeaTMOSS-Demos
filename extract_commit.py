import subprocess
import json
import os

def extract_commit_history(repo_path):
    # repository directory
    os.chdir(repo_path)
    
    # Get the commit history using git log
    commits = subprocess.check_output(
        ["git", "log", "--pretty=format:%H %an %ad %s"], 
        universal_newlines=True
    ).split('\n')
    
    # Process commit history
    commit_objects = []
    for commit in commits:
        parts = commit.split(' ', 3)
        if len(parts) != 4:
            continue
        commit_objects.append({
            "author": parts[1],
            "date": parts[2],
            "message": parts[3]
        })
    
    return commit_objects

def main():
    # Path to the local clone of the GitHub repository
    repo_path = "/Users/dulaninw/globusdata/Zipped_GitHub_Repos/AnacletoLAB_ensmallen/ensmallen"
    repo_name = os.path.basename(repo_path)
    
    commit_history = extract_commit_history(repo_path)
    
    # Create the JSON object
    data = {
        "repo_name": repo_name,
        "commit_history": commit_history
    }
    
    with open("commit_history.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

    print("Commit history saved to commit_history.json")

if __name__ == "__main__":
    main()

