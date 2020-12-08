import requests

headers = {
	'Authorization': 'token 44eb5f706b64a659f8b23816e817eaae9e0dfd8f' #Replace with your personal token
}

response = requests.get('https://api.github.com/users/5mo6tx/received_events',headers=headers) #After users/ replace your UserName

data = response.json()

event_actions ={'IssueCommentEvent':'commentIssue','PullRequestEvent':'pull from','PushedEvent':'pushed to','WatchEvent':'starred'}

for event in data:
	if event['type'] in event_actions:
		name = event['actor']['display_login']
		action = event_actions[event['type']]
		repo = event['repo']['name']
		print('{name} {action} {repo}'.format(name=name,action=action,repo=repo)) 
	
	if event['type'] == 'ForkEvent':
		name = event['actor']['display_login']
		repo = event['repo']['name']
		forked_repo = event['payload']['forkee']['full_name']
		print('{name} forked {forked_repo} from {repo}'.format(name=name,forked_repo=forked_repo,repo=repo))		

