from nvd3 import cumulativeLineChart
from github import Github
import datetime
g = Github("3fabf3ef6a5ba3e8f9a7e814e8ea0a3c73d06d52")
repo_count = 0
user = g.get_user("phadej")
print("Name:",user.name)
print("location:",user.location)
user_repos = user.get_repos()
print("No of Repos:",user_repos.totalCount)
# for repo in user_repos:
print("No of Contributions:",user.contributions)
additions = []
deletions = []
total_net_code  = []
authors = []
commit_date = []
hask_api = user.get_repo("github")
#for content in hask_api.get_contents(""):
#    print(content)
com_list = hask_api.get_commits()
for com_y in com_list:
    authors.append(com_y.committer)
for com_x in com_list:
    dt = (com_x.commit.author.date)
    d = (10000*dt.year + 100*dt.month + dt.day)

    commit_date.append(d)
    print(d)
for com_stats_total in com_list:
    total_net_code.append(com_stats_total.stats.total)
    print(com_stats_total.stats.total)
for com_stats_add in com_list:
    assert isinstance(com_stats_add.stats.additions, int)
    additions.append(com_stats_add.stats.additions)
    print(com_stats_add.stats.additions)
for com_stats_del in com_list:
    deletions.append(com_stats_del.stats.deletions)
    print("bother")

#xdata = [1365026400000, 1365026500000, 1365026600000]
#ydata = [6, 5, 1]
#y2data = [36, 55, 11]

#chart = cumulativeLineChart(name='Churn Chart!', x_is_date=True)
#extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}
#chart.add_serie(name="additions", y=additions, x=commit_date, extra=extra_serie)

#extra_serie = {"tooltip": {"y_start": "", "y_end": " mins"}}
#chart.add_serie(name="deletions", y=deletions, x=commit_date, extra=extra_serie)

#extra_serie = {"tooltip": {"y_start": "", "y_end": " mins"}}
#chart.add_serie(name="net code addention", y=total_net_code, x=commit_date, extra=extra_serie)

#chart.buildhtml()
#print(chart.htmlcontent)
chart = cumulativeLineChart(name='cumulativeLineChart', x_is_date=True)

extra_serie = {"tooltip": {"y_start": "The user committed ", "y_end": " net lines of code"}}
chart.add_serie(name="Net Code Addition", y=total_net_code, x=commit_date, extra=extra_serie)
chart.buildhtml()
print(chart.htmlcontent)