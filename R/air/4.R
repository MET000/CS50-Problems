load("air.RData")

air <- air |> filter(county == "OR - Washington") |>
  arrange(desc(emissions))

save(air, file = "4.RData")
