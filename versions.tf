terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "5.2.0"
    }
  }
}

provider "google" {
    credentials = file("peerless-tiger-400109-d76af527198c.json")
    project = var.google_project_id
    region = "us-central1"
  
}