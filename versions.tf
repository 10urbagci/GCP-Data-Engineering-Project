terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.2.0"
    }
  }
}

provider "google" {
    credentials = file("credential-file.json")
    project = var.google_project_id
    region = "us-central1"
  
}