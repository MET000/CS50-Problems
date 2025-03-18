zelda <- read_csv("zelda.csv") |>
  pivot_wider(
    names_from = role,
    values_from = names,
  )

zelda$year <- str_split(zelda$release, " - ", simplify = TRUE)[,1] |>
  as.numeric()
zelda$system <- str_split(zelda$release, " - ", simplify = TRUE)[,2]
colnames(zelda) <- colnames(zelda) |>
  str_to_lower()
zelda <- zelda |>
  select(title, year, system, directors, producers, designers, programmers, writers, composers, artists)
save(zelda, file = "zelda.RData")
