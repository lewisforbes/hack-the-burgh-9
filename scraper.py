def complete(dict, n):
    for k in dict:
        while len(dict[k])<n:
            dict[k].append("")
    return dict

i = 1
countries = {}
charts = ["Top 50","Viral 50","Top Songs"]
for chart in charts:
    f = open('{}.txt'.format(chart), 'r')

    raw = f.read()
    raw = raw.split("{} - ".format(chart))[1:]
    raw = raw[1::3]

    for c in raw:
        name = c[0:c.find("\"")]
        c = c[c.find("/playlist"):]
        uri = c[0:c.find("\"")]
        
        if name in countries:
            countries[name].append(uri)
        else:
            current = ["" for _ in range(i-1)]
            countries[name] = current + [uri]
    f.close()
    countries = complete(countries, i)
    i+=1

to_write = "country, daily, viral, weekly\n"
for k in countries:
    uris = countries[k] 
    to_write += "{},{},{},{}\n".format(k, uris[0], uris[1], uris[2])

f = open('countries.csv', 'w')
f.write(to_write)
f.close()