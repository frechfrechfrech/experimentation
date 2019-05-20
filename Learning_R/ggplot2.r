# Run in command line using Rscript ggplot2.r

options(scipen=999)
library(ggplot2)
# download data
data("midwest", package="ggplot2")

# initialize plot
g <- ggplot(midwest, aes(x=area, y=poptotal))

# plots scatter
g <- g + geom_point(col="darkorchid4", size=3)
plot(g)

# plots best fit line
g <- g + geom_smooth(method="lm")
plot(g)

# Delete the points outside the limits
g <- g + xlim(c(0, 0.1)) + ylim(c(0, 1000000))
plot(g)

# Zoom in without deleting the points outside the limits.
# As a result, the line of best fit is the same as the original plot.
g1 <- g + coord_cartesian(xlim=c(0.02,0.04), ylim=c(0,200000))  # zooms in
plot(g1)


g1 + labs(title="Area Vs Population", subtitle="From midwest dataset",
y="Population", x="Area", caption="Midwest Demographics")
# or
g1 + ggtitle("Area Vs Population", subtitle="From midwest dataset")
+ xlab("Area") + ylab("Population")






mydata <- read.table('pim.csv', header=TRUE, sep=",")
