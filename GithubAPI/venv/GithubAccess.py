from github import Github
g = Github("token")
repo_count = 0
user = g.get_user("phadej")
print("Name:",user.name)
print("location:",user.location)
user_repos = user.get_repos()
print("No of Repos:",user_repos.totalCount)
# for repo in user_repos:
print("No of Contributions:",user.contributions)
hask_api = user.get_repo("github")
for content in hask_api.get_contents(""):
    print(content)
branch = hask_api.get_branch("master")
head = branch.commit.sha
gtree = hask_api.get_git_tree(head)
print(gtree.tree)






