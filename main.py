from common import Config
import git 

if __name__ == "__main__":
    repo = git.Repo(Config.repo_path)
    commits = list(repo.iter_commits('master', max_count=50))

    headcommit = repo.head.commit
    print(headcommit.hexsha)
    print(headcommit.parents)
    print(headcommit.tree.blobs)
    print(headcommit.tree.trees)