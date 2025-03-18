# Read books data
books <- read.csv("books.csv")

# Read authors data
authors <- read.csv("authors.csv")

# Get the title of the book whose author's name is Mia Morgan.
subset(books, author == "Mia Morgan")$title

# Get the title of the book whose year is 1613 and topic is music.
subset(books, year == 1613 & topic == "Music")$title

# Get the title of the book whose author's name is Elena Petrova or Lysandra Silverleaf and year is 1775.
subset(books, (author == "Lysandra Silverleaf" | author == "Elena Petrova") & year == 1775)$title

# Get the title of the book between 200 and 300 pages long, published in 1990 or 1992.
subset(books, (pages > 200 & pages < 300) & (year == 1990 | year == 1992))$title

# Get the book whose title includes the sentence “Quantum Mechanics”
subset(books, grepl("Quantum Mechanics", books$title))$title

# Get the subset of the authors from Zenthia
authors_from_zenthia <- subset(authors, hometown == "Zenthia")

# Get the title of the book whose author is from Zenthia and whose topic is education and which was published in the 1700s
subset(books, (author %in% authors_from_zenthia) & year > 1699 & year < 1800 & topic == "Education")$title







