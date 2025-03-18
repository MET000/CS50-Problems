air <- read_csv("air.csv") |>
  select(c("State", "State-County", "POLLUTANT", "Emissions (Tons)", contains("LEVEL"))) |>
  rename("state" = 1, "county" = 2, "pollutant" = 3, "emissions" = 4, "level_1" = 5, "level_2" = 6, "level_3" = 7, "level_4" = 8)

save(air, file = "air.RData")
