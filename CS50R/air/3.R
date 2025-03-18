load("air.RData")

air <- air |> filter(county == "OR - Washington")

save(air, file = "3.RData")

