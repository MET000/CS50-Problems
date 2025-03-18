library(stringr)
library(testthat)


test_that("`str_length` calculates string length", {
  expect_equal(str_length("khrizou"), 7)
  expect_equal(str_length("1"), 1)

})


test_that("`str_length` calculates vector elements length", {
  expect_equal(str_length(c("a", "bt", 3)), c(1, 2, 1))

})


test_that("`str_length` calculates length with numeric in input", {
  expect_equal(str_length(12), 2)

})

test_that("`str_length` does not return error with NA in input", {
  expect_no_error(str_length(NA))

})

