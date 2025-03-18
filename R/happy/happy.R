d1 <- read.csv("2020.csv")
d2 <- read.csv("2021.csv")
d3 <- read.csv("2022.csv")
d4 <- read.csv("2023.csv")
d5 <- read.csv("2024.csv")


d1$year <- 2020
d2$year <- 2021
d3$year <- 2022
d4$year <- 2023
d5$year <- 2024

data <- rbind(d1, d2, d3, d4, d5)

selected_country <- readline("Country: ")

target <- subset(data, country == selected_country)[2:8]
happiness <- round(apply(target, MARGIN = 1, FUN = sum), digits = 2)
i <- 1
for (year in unique(data$year)){
  if (is.na(happiness[i])){
    cat(paste0(selected_country, " (", year, "): ", "data unavailable"), sep="\n")
    i <- i + 1
  } else {
      cat(paste0(selected_country, " (", year, "): ", happiness[i]), sep="\n")
      i <- i + 1
    }
}
