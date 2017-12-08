# Imports
import requests
import os
from py_ms_cognitive_ml import PyMsCognitiveImageSearch

# Settings
search_terms = ["cats", "dogs", "penguins"]
serach_quota_per_term = 100
output_folder = "output"
api_key = 'INSERT_YOUR_API_KEY_HERE'

results = []
total_downloads = 0

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Main
for search_term in search_terms:
    
    # Make API call
    search_service = PyMsCognitiveImageSearch(api_key, search_term)
    result_list = search_service.search_all(quota=serach_quota_per_term)

    # Scrape images
    if not os.path.exists(output_folder + "/" + str(search_term)):
        os.mkdir(output_folder + "/" + str(search_term))

    print("\nDownloading images for term: '" + str(search_term) + "'")

    i = 0
    urls = []
    for i in range(0, len(result_list)):
        print ("Downloading image from " + str(result_list[i].name))

        # Download the image
        try:
            if result_list[i].url not in urls:

                image_file = requests.get(result_list[i].url, stream=True)

                if image_file.status_code == 200:
                    if result_list[i].extension != "unknown":
                        with open(output_folder + "/" + search_term + "/" + str(i) + "." + result_list[i].extension, 'wb') as f:
                            f.write(image_file.content)

                        urls.append(result_list[i].url)
                    else:
                        print("Image extension unkonwn. Skipping image.")
                else:
                    raise requests.exceptions.RequestException

            else:
                print("Image already downloaded. Skipping image.")

        except requests.exceptions.RequestException:
            print("Something went wrong with the request. Skipping image.")

        i += 1

    results.append(str(len(urls)) + " images downloaded for term '" + str(search_term) + "'.")
    total_downloads += len(urls)

print("\n")

for result in results:
    print(result)

print(str(total_downloads) + " images based on " + str(len(search_terms)) + " search term(s) downloaded.")
