library(testthat)
library(stringr)
source("believe.R")

test_that("gc_content correctly computes the rounded GC percentage for valid DNA sequences", {
  expect_equal(gc_content("atcggtc"), 57)
  expect_equal(gc_content("ttctata"), 14)
  expect_equal(gc_content("atgcaacataagatc"), 33)
  expect_equal(gc_content("tcg"), 67)
  expect_equal(gc_content("ATCG"), 50)
})

test_that("gc_content throws an error when the input is not a valid DNA sequence (non-character, NA, or contains invalid characters)", {
  expect_error(gc_content("adf"))
  expect_error(gc_content(34))
  expect_error(gc_content("._+"))
  expect_error(gc_content(NA))
})

test_that("gc_content returns NA (without throwing an error) when given an empty string", {
  expect_no_error(gc_content(""))
})

test_that("gc_content computes the GC percentage for each element in a vector of DNA sequences", {
  expect_equal(gc_content(c("tcg", "atcg", "aat")), c(67, 50, 0))
})

test_that("gc_content returns NA for invalid entries in a vector and issues a warning", {
  expect_warning(gc_content(c("attcg", "ss", "aat")))
  expect_warning(gc_content(c(33, "z", 0)))
})
