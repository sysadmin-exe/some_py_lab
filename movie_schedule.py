current_movies = {}
current_movies['F9'] = '1:00PM'
current_movies['Eternals'] = '9:00PM'
current_movies['Doctor Strange'] = '3:00PM'
current_movies['Without Remorse'] = '6:00PM'

print("We are currently showing the following movies:")
for key in current_movies:
  print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
  print("Requested movie is not playing")
else:
  print(movie, "is playing at", showtime)