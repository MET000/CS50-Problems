library(tidyverse)
lyrics <- read_file("lyrics/summerwind.txt") |>
  str_to_title() |>
  str_remove_all('[,()\"]') |>
  str_squish() |>
  str_split(" ")

lyrics <- tibble(data.frame("words" = lyrics[[1]])) |>
  group_by(words) |>
  summarize(count = n()) |>
  arrange(desc(count)) |>
  filter(count > 1)

ggplot(lyrics, aes(x = reorder(words, -count), y = count)) +
  geom_col(
  aes(fill = count),
  show.legend = TRUE
  ) +
  scale_fill_gradient(low = "blue", high = "green", "Count") +
  scale_y_continuous(limits = c(0, 25)) +
  labs(
    x = "Words",
    y = "Count",
    title = "Word Count"
  ) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

ggsave(
  "lyrics.png",
  width = 1200,
  height = 900,
  units = "px"
)

