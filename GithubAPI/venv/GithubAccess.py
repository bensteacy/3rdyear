from github import Github
g = Github("token")

user = g.get_user("phadej")
print(user)
print("list of repos:")
for repo in user.get_repos():
    print(repo.name)







