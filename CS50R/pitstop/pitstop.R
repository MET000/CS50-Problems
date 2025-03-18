data <- read.csv(readline("Please provide a csv file: "))

total_pit_stops <-nrow(data)
shortest <- sort(unique(data$time))[1]
longest <- sort(unique(data$time), decreasing = TRUE)[1]
total_time <- sum(data$time)

print(paste("The total pit stops:", total_pit_stops))
print(paste("The shortest pit stop:", shortest))
print(paste("The longest pit stop:", longest))
print(paste("The total time spent on pit stops:", total_time))