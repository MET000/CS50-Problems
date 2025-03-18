load("air.RData")

air <- air |>
  group_by(county) |>
  arrange(desc(emissions)) |>
  slice_head()

save(air, file = "5.RData")
