import os
import random
import datetime
from git import Repo

def check_git_config():
    try:
        username = os.popen('git config --global user.name').read().strip()
        email = os.popen('git config --global user.email').read().strip()
        
        if not username or not email:
            print("Git credentials not fully configured!")
            print("Please run:")
            print('git config --global user.name "bastosuman"')
            print('git config --global user.email "bastolasuman@gmail.com"')
            return False
        print(f"Git configured with: {username} <{email}>")
        return True
    except Exception as e:
        print(f"Error checking git config: {e}")
        return False

def create_commits(start_date, end_date, repo_path, min_commits=1, max_commits=5):
    repo = Repo(repo_path)
    os.chdir(repo_path)
    
    current_date = start_date
    while current_date <= end_date:
        num_commits = random.randint(min_commits, max_commits)
        
        for _ in range(num_commits):
            # Create a unique filename with timestamp
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"auto_commit_{timestamp}.txt"
            
            # Write to file
            with open(filename, 'w') as f:
                f.write(f"Automated commit on {current_date}")
            
            # Explicitly stage the file
            repo.index.add([filename])
            
            # Commit with the specified date
            repo.index.commit(
                message=f"Auto commit on {current_date}",
                commit_date=current_date.isoformat()
            )
        
        current_date += datetime.timedelta(days=1)

def main():
    repo_path = r"C:\Users\basto\Documents\Projects\new"
    
    if not check_git_config():
        return
    
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    
    create_commits(
        start_date=start_date,
        end_date=end_date,
        repo_path=repo_path,
        min_commits=1,
        max_commits=3
    )
    
    repo = Repo(repo_path)
    repo.git.push()

if __name__ == "__main__":
    repo_path = r"C:\Users\basto\Documents\Projects\new"
    
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print("Error: This is not a Git repository. Please initialize it with 'git init' first.")
        print("Then set up a remote with: git remote add origin <your-repo-url>")
        exit(1)
    
    try:
        import git
    except ImportError:
        print("Error: Please install GitPython: pip install gitpython")
        exit(1)
    
    main()