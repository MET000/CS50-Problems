tea_house <- data.frame(
 Light = c("green", "chamomile"),
 Bold = c("black", "rooibos")
)

rownames(tea_house) <- c("Yes", "No")
flavor <- readline("Flavor: ")
caffeine <- readline("Caffeine: ")


if (flavor %in% colnames(tea_house) && caffeine %in% rownames(tea_house)){
  cat("You might like", tea_house[caffeine, flavor], "tea 🫖")
} else {
  cat("Please enter Light or Bold for 'Flavor'.", sep="\n")
  cat("Please enter Yes or No for 'Caffeine'.")
}

