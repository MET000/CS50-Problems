load("air.RData")

air <- air |> select(level_1, pollutant, emissions) |>
  group_by(level_1, pollutant) |>
  summarize(emissions = sum(emissions)) |>
  arrange(level_1, pollutant) |>
  rename("source" = "level_1")

save(air, file = "7.RData")
