from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import functions
import csv

api_id = 8726937
api_hash = '30a987d21ae35bef18e98ddba88265f3'
phone = '+15712746465'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

print('Choose a channel to scrape from:')
i = 0
for g in chats:
    print(str(i) + '- ' + g.username)
    i += 1

g_index = input("Enter a Number: ")
target_group = int(g_index)


print('Fetching Channel Details...')
print("ID:",chats[target_group].id)

print("Title:",chats[target_group].title)
print("Username:",chats[target_group].username)
if chats[target_group].has_geo:
    print("Date:",chats[target_group].date)


full = client(functions.channels.GetFullChannelRequest(chats[target_group].username))
full_channel = full.full_chat

print("Bio:" , full_channel.about)


print("Number of Subscribers:",chats[target_group].participants_count)


print('Storing the data of selected channel in csv')
print('Saving In file...')
with open("channel.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'channel_id', 'channel_title', 'channel_date', 'channel_bio','subscribers'])

    username = chats[target_group].username

    channel_id = chats[target_group].id

    channel_title = chats[target_group].title

    if chats[target_group].has_geo:
        channel_date = chats[target_group].date
    else :
        channel_date = ""

    channel_bio = full_channel.about

    subscibers = chats[target_group].participants_count

    writer.writerow([chats[target_group].username, chats[target_group].id, chats[target_group].title, chats[target_group].date,full_channel.about, chats[target_group].participants_count])
print('Data scraped successfully.')

print('Storing all data of channels in csv')
print('Saving In file...')
with open("channels.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'channel_id', 'channel_title', 'channel_date','channel_bio' ,'subscribers'])
    for user in chats:
        if user.username:
            username = user.username

        if user.id:
            channel_id = user.id

        if user.title:
            channel_title = user.title

        if user.has_geo:
            channel_date = user.date
        else:
            channel_date = ""

        full = client(functions.channels.GetFullChannelRequest(user.username))
        full_channel = full.full_chat
        if user.date:
            channel_bio = full_channel.about

        if user.participants_count:
            subscibers = user.participants_count


        writer.writerow([user.username, user.id, user.title, user.date, full_channel.about,user.participants_count])
print('Members scraped successfully.')

