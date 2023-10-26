xs = ['foo', 'bar', 'baz', 'Waldo', 'foobar']

videl_sem_waldo = False

for str in xs:
    if str == "Waldo":
        videl_sem_waldo = True

print(videl_sem_waldo)
if videl_sem_waldo:
    print("Res sem videl Waldo.")