load("zelda.RData")

zelda <- zelda |>
  filter(str_detect(zelda$producers, "Shigeru Miyamoto")) |>
  group_by(title) |>
  slice_min(order_by = year) |>
  arrange(year, title, system)

save(zelda, file = "4.RData")
