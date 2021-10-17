guests = ['espen', 'arne', 'andrew']

print(f"{guests[1].title()} can't come to dinner?")

guests[1] = 'hans jørgen'
print(guests)

print(f"{guests[0].title()} can come to dinner!")
print(f"{guests[1].title()} can come to dinner!")
print(f"{guests[2].title()} can come to dinner!")

print(f"\nI have found a bigger table!\n")

guests.insert(0,'andré')
guests.insert(2,'kim')
guests.append('per kristian')

print(f"{guests[0].title()} can come to dinner!")
print(f"{guests[1].title()} can come to dinner!")
print(f"{guests[2].title()} can come to dinner!")
print(f"{guests[3].title()} can come to dinner!")
print(f"{guests[4].title()} can come to dinner!")
print(f"{guests[5].title()} can come to dinner!")
