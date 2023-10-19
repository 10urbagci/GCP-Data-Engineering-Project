import requests
from google.cloud import storage

def hello_world(request):
    try:
        # Fetch data from API
        # Endpoint http://api.citybik.es/v2/networks
        response = requests.get("https://api.citybik.es/v2/networks/velib")
        data = response.json()

        # Create Google Cloud Storage connection
        storage_client = storage.Client()

        # CSV column headers
        csv_data = [['station_id', 'name', 'latitude', 'longitude', 'empty_slots', 'free_bikes', 'banking',
                     'ebikes', 'last_updated', 'payment-terminal', 'renting', 'returning', 'slots', 'uid', 'timestamp']]
        # Parse JSON file
        for station in data['network']['stations']:
            station_data = [
                station['id'],
                station['name'],
                station['latitude'],
                station['longitude'],
                station['empty_slots'],
                station['free_bikes'],
                station['extra']['banking'],
                station['extra']['ebikes'],
                station['extra']['last_updated'],
                station['extra']['payment-terminal'],
                station['extra']['renting'],
                station['extra']['returning'],
                station['extra']['slots'],
                station['extra']['uid'],
                station['timestamp']
            ]
            csv_data.append(station_data)

        # Create CSV data in memory for Cloud Functions
        csv_content = '\n'.join([','.join(map(str, row)) for row in csv_data])

        # Data Load section Upload CSV data to GCS
        bucket_name = "raw-data-for-de-project"  # Bucket name
        csv_filename = "bike_data_velib.csv"
        
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(csv_filename)
        blob.upload_from_string(csv_content)

        return "Job Done"

    except Exception as e:
        return f"Error: {str(e)}"

# Extract and Load section. This script used for Cloud Functions
# This script was triggered with Cloud Scheduler.