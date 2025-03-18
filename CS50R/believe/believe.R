gc_content <- function(dna) {
  # Single-element case
  if (length(dna) == 1) {
    if (!is.character(dna) || is.na(dna)) {
      stop("Invalid input: must be a non-NA character string")
    }
    if (dna == "") return(NA)
    x <- tolower(dna)
    if (grepl("[^atcg]", x)) {
      stop("Invalid input: contains characters other than a, t, c, g")
    }
    gc_count <- stringr::str_count(x, "[gc]")
    total <- nchar(x)
    return(round((gc_count / total) * 100))
  }

  # Vectorized case
  dna <- as.character(dna)
  out <- vector("numeric", length(dna))
  warn_flag <- FALSE

  for (i in seq_along(dna)) {
    x <- dna[i]
    if (is.na(x)) {
      out[i] <- NA
      warn_flag <- TRUE
    } else if (x == "") {
      out[i] <- NA
    } else {
      x <- tolower(x)
      if (grepl("[^atcg]", x)) {
        out[i] <- NA
        warn_flag <- TRUE
      } else {
        gc_count <- stringr::str_count(x, "[gc]")
        total <- nchar(x)
        out[i] <- round((gc_count / total) * 100)
      }
    }
  }
  if (warn_flag) {
    warning("Some inputs are invalid and have been returned as NA")
  }
  return(out)
}
