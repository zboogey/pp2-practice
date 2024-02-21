import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for entry in data:
    dn = entry['DN']
    description = entry.get('Description', '')
    speed = entry.get('Speed', 'inherit')
    mtu = entry.get('MTU', '')
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))
