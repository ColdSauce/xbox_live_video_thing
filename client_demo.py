from xbox_api_client import *
import random

auths = None
with open('./auth.txt', 'r') as f:
	client = f.read()
	
client = XboxAPIClient(auths)

title_ids = None
with open('./title_ids.txt', 'r') as f:
	title_ids = f.readlines()
	
for i in range(0, 8):
	tid = title_ids[random.randint(0, len(title_ids) -1)]
	clips = client.get_games_clips_for_title(tid, params={'type': 'UserGenerated'})
	uri = None
	r = client.download_game_clip(str(i) + '.mp4', clips[random.randint(0, len(clips) - 1)])
	print r
