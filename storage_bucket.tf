resource "google_storage_bucket" "raw_data" {
  name          = "raw-data-for-de-project"
  location      = "US"
  force_destroy = true
}

resource "google_storage_bucket" "transformed_data" {
  name          = "transformed-data-for-de-project"
  location      = "US"
  force_destroy = true
}