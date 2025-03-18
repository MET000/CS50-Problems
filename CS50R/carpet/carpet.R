calculate_growth_rate <- function(years, visitors) {
  # TODO: Calculate yearly growth of visitors
  growth_rate <- (visitors[length(visitors)] - visitors[1]) / (years[length(years)] - years[1])
}

predict_visitors <- function(years, visitors, year) {
  # TODO: Predict visitors in given year
  visitors[length(visitors)] + (calculate_growth_rate(years, visitors) * (year - years[length(years)]))
}

visitors <- read.csv("visitors.csv")
year <- as.integer(readline("Year: "))
predicted_visitors <- predict_visitors(visitors$year, visitors$visitors, year)
cat(paste0(predicted_visitors, " million visitors\n"))



