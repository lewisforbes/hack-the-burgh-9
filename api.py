import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials("4ab845d9fdb149a38e93ea7defa85e78","53441921f29e48078e4308cc5e90bea9")
sp = spotipy.Spotify(auth_manager=auth_manager)


def read_csv(col):
    output = {}
    f = open('countries.csv', 'r')
    first = True
    for line in f:
        if first:
            first = False
            continue
        current = line.strip().split(",")
        output[current[0]] = current[1]
    f.close()
    return output

filename = "viral 50.csv"
f = open(filename, "w")
output = "country"
features = ["acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","valence"]
for feat in features: 
    output += ", {}".format(feat)

f.write(output + "\n")
f.close()

data = read_csv(2)
for country in list(data.keys()):
    f = open(filename, 'a')
    print(country)
    if data[country]=="":
        continue

    pl = sp.playlist_items(data[country][len("/playlist/"):])
    tracks = []
    for t in range(len(pl["items"])):
        tracks.append(pl["items"][t]["track"]["id"])
    
    f_totals = [0 for _ in features]
    for t in sp.audio_features(tracks):
        for i in range(len(features)):
            f_totals[i] += t[features[i]]
    
    current_line = country
    for ft in f_totals:
        current_line += "," + str(ft/len(tracks))
    
    f.write(current_line + "\n")
    f.close()

# tracks = []
# pl = sp.playlist_items("37i9dQZEVXbMDoHDwVN2tF")

# for t in range(len(pl["items"])):
#     tracks.append(pl["items"][t]["track"]["id"])

# energies = [t["energy"] for t in sp.audio_features(tracks)]