bus <- read.csv("bus.csv")
rail <- read.csv("rail.csv")

# Bind bus and rail data to reate a single dataset.
data <- rbind(bus, rail)

# Select a route.
selected_route <- readline("Route: ")

# Check if the selected route is valid.
if (selected_route %in% data$route){

  # Calculate off peak reliability for each row in the subset related to the selected route (get a vector of calculated reliability).
  off_peak_reliability <- subset(data, route == selected_route & peak == "OFF_PEAK")$numerator / subset(data, route == selected_route & peak == "OFF_PEAK")$denominator

  # Calculate peak reliability for each row in the subset related to the selected route (get a vector of calculated reliability).
  peak_reliability <- subset(data, route == selected_route & peak == "PEAK")$numerator / subset(data, route == selected_route & peak == "PEAK")$denominator

  # Calculate the rounded average percentage related to peak and off-peak reliability and use of paste to create a single sentence.
  p <- paste0("On time ", round(mean(peak_reliability) * 100), "% of the time during peak hours.")
  op <- paste0("On time ", round(mean(off_peak_reliability) * 100), "% of the time during off-peak hours.")

  # Print the desired data.
  cat(p, sep="\n")
  cat(op)

  # Handle invalid input.
} else {
  cat("Invalid route.")
}


