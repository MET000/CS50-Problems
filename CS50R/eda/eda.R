library(tidyverse)

data <- read_csv("database.csv")

data <- data |> filter(Team == "Real Madrid", Player == "Kylian Mbappé" | Player == "Vinicius Júnior") |>
  group_by(Player, Date) |>
  summarise(ratio = ifelse(`Dribble Attempts` > 0 & `Successful Dribbles` > 0, round(`Successful Dribbles` / `Dribble Attempts`, digits = 2), 0))

ggplot(data, aes(x=Date, y=ratio, color=Player)) +
  geom_line() +
  xlab("") +
  scale_y_continuous(limits = c(0, 1)) +
  labs(
    x = "Months",
    y = "Successful Driblles / Dribble Attempts",
    title = "Dribbling Statistics Comparison Between Mbappé and Vinicius from
August to December 2024"
  ) +
  theme_classic()

ggsave(
  "visualization.png",
  width = 2000,
  height = 1400,
  units = "px"
)

