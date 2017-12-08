# Python Machine Learning Tools
This repository contains a set of helper tools to assit with gathering and sorting data for machine learning. Please feel free to request any additional tools.

Installation
====
To use these tools, you'll need to install a few dependancies. I recommend setting up a virtual environment.

#### Quick instructions for Python 3.*
```sh
git clone https://github.com/beardo01/pymltools && cd pymltools
virtualenv -p python3 pymytools-env && source pymltools-env/bin/activate
pip install -r requirements.txt
```

#### Full instructions for Python 3.*
1. Install Python 3: `sudo apt-get install python3-pip`
2. Install Virtual Environments: `pip install virtualenv`
3. Clone the repository to somewhere useful: `cd ~/Desktop/ && git clone https://github.com/beardo01/pymltools`
4. Create a Virtual Environment for your project: `virtualenv -p python3 pymytools-env`
5. Activate the Virtual Environment: `source pymytools-env/bin/activate`
6. Install the requirements: `pip install -r requirements.txt`
7. You can now run the tools.

Usage
====
I've included two scripts for gathering and sorting data for machine learning. At this stage, the primary focus is on finding images, however I can add more tools if people need other sorts of data. 

The first script `gather.py` uses the Bing Image API to gather images for training, testing and validating machine learning models. Please note that you'll need to get a Microsoft Cognitive Services API for this script to work. You can find instructions on how to get one __[here](https://raw.githubusercontent.com/beardo01/py-ms-cognitive-ml)__, under the "Introduction" section of the README. In `gather.py` you can configure the following settings:

```python
search_terms = ["cats", "dogs", "penguins"] # This is a list of terms used in the Bing Image Search API to find images.
serach_quota_per_term = 100 # This is how many images you want of each term.
output_folder = "output" # This is what folder you want to output the images to, relative from where you run the script.
api_key = 'INSERT_YOUR_API_KEY_HERE' # This is where you need to define the API key.
```

The second script `split.py` splits data gathered by `gather.py` into folders based on the scripts settings. For example, `split.py` can split data into training, testing and validating folders to help train and validate neural networks. In `split.py` you can configure the following settings:

```python
input_directory = "output" # This is where you want to read the images in from (or rather, the folders containing the images).
output_directory = "data" # This is where you want to write the images to.
split_into = {"train": 70, "valid": 15, "test": 15} # This is the folders within the output directory that you want to write the images into followed by the percent of total images for that category that you want in each folder. 
```

Conclusion
====
If you have any questions or recommendations, feel free to get in touch.
