playlist = []
print('Введите плей-лист папы:')
for i in range(5):
    song = input()
    playlist.append(song)
print('Плей-лист мамы:')
for k in range(5):
    print(playlist[::-1][k])
