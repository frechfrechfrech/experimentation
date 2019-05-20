
vector_1 <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
vector_2 <- vector_1[1:2]
matrix_1 <- matrix(vector_1, byrow=TRUE, nrow=3)

mean(vector)

box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
star_wars_matrix <- matrix(box_office, nrow = 3, byrow = TRUE,
                           dimnames = list(c("A New Hope", "The Empire Strikes Back", "Return of the Jedi"),
                                           c("US", "non-US")))
movie_sums <- rowSums(star_wars_matrix)

# The worldwide box office figures
worldwide_vector <- rowSums(star_wars_matrix)

# add rows and columns to matrix
# Bind the new variable worldwide_vector as a column to star_wars_matrix
all_wars_matrix <- cbind(star_wars_matrix, worldwide_vector)
# rbind()

# Selecting parts of matrix
# select first column
all_wars_matrix[,1]


all_wars_matrix/5
# element-wise matrix multiplication
my_matrix1 * my_matrix2

# categorical vectors
# Animals - nominal
animals_vector <- c("Elephant", "Giraffe", "Donkey", "Horse")
factor_animals_vector <- factor(animals_vector)
# Temperature - ordinal
temperature_vector <- c("High", "Low", "High","Low", "Medium")
factor_temperature_vector <- factor(temperature_vector, order = TRUE, levels = c("Low", "Medium", "High"))
levels(factor_temperature_vector) <- c("L","M","H")

summary(my_variable) works like .describe()
summary(factor_vector) more useful than summary(vector)


# working with dataframes
head() and tail()
str() shows structure of df, kinda like .info()

# Make a dataframes
# Definition of vectors
name <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet",
          "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
# Create a data frame from the vectors
planets_df <- data.frame(name, type, diameter, rotation, rings)

# select parts of df
planets_df[1,'type']
planets_df[1:3,4]
planets_df$rings # selects the rings column  of planets_df
df[mask,1]

planets_df[planets_df$rings,] #selects rows where rings=TRUE
subset(planets_df, subset=rings) # also selects rows where rings=TRUE
subset(planets_df, subset= diameter <1)

#lists - can have all kinds of different elements
my_list <- list(name1 = your_comp1,
                name2 = your_comp2)
my_list <- list(your_comp1, your_comp2)
names(my_list) <- c("name1", "name2")

# getting elements out of a list
shining_list[[1]]
shining_list[["reviews"]]
shining_list$reviews

# add something to list
ext_list <- c(my_list , my_val)

# read in data into a dataframe
# using ggplot
# import functions
# download R
