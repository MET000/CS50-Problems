coffee <- data.frame(
  Cold = c("iced coffee", "iced latte"),
  Hot = c("espresso", "latte")
)

rownames(coffee) <- c("No", "Yes")
type <- readline("Type: ")
milk <- readline("Milk: ")


if (type %in% colnames(coffee) && milk %in% rownames(coffee)){
  cat("You might like", coffee[milk, type], "☕")
} else {
  cat("Please enter Cold or Hot for 'Type'.", sep="\n")
  cat("Please enter Yes or No for 'Milk'.")
}

