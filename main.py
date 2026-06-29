#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Greatest Showman"

print("My favorite movie is " + favMovie)


#Part 3 Investigate the data



#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

favMovieBooleanList = movieData["movie_title"] == favMovie

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre


dramaBooleanList = movieData["genres"].str.contains("Drama")
dramaMovieData = movieData.loc[dramaBooleanList]

numOfMovies = dramaMovieData.shape[0]


print("We will be comparing " + favMovie +
      " to other movies under the genre Drama in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Drama.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
tgsAudRating = 86

#min
ratings = dramaMovieData["audience_rating"]

min = ratings.min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(tgsAudRating - min) + " points higher than the lowest rated movie.")
print()

#find max
max = ratings.max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(max - tgsAudRating) + " points lower than the highest rated movie.")
print()

#find mean
sum = 0
for rating in ratings:
    sum += rating

mean = int(sum / numOfMovies)

print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median

median = ratings.median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist(ratings, range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Rating Distribution in Drama Movies")
plt.xlabel("Audience Rating")
plt.ylabel("# of Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, the most movies have an audience rating between 75 to 79"
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")

plt.figure()

#Create scatterplot
plt.scatter(data = dramaMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Critic Ratings vs. Audience Ratings in Drama Movies")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between the audience ratings and critic ratings. However, that are many outliers."
)
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
