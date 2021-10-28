# <p align="center">Marcus</p>
<p align="center"><img alt="GitHub Madeby" src="https://img.shields.io/badge/made%20by-AlienFoun-blue"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/AlienFoun/Marcus"> <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Alienfoun/marcus?style=social"> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/AlienFoun/Marcus"> </p>

# About
**The program allows you to categorize text information based on downloaded examples**

# Project structure
The project is structured for better scaling. In general, files names reflect their essence
* helper - contains the functions necessary for the program to work
* sql and config - contains the functions necessary for the program to work with MySQL database

# Selected libraries
* Flask
* Flask-RESTful
* Flask-CORS
* PyMySQL
* Typing
* Unitest
* Json
* String

# Installation
Download Python 3.8 or higher

```
git clone https://github.com/AlienFoun/Marcus
cd Marcus
pip install -r requirements.txt
```

Fill in the data to connect to the MySQL database in the file `setup.py`

# Usage

Open the terminal and go to the folder with the project, then start the server using the command `py server.py` after that, an API will be available to you, with which you can perform basic actions with the program

* The API for training will be available at `http://host:port/study`

* The API for the response will be available at `http://host:port/reply`

By default, `host` is `localhost`, and `port` is `4000`

For the program to work, you must first add to the database a list of categories and examples of words/phrases associated with this category using the training API or manually in a file study.py

* For further training, you can use the training API again

* To get an array of suitable categories, use the reply API.

The data transmitted by the API for training should be presented in json format as:
```Python
{
	"user_text": "text",
	"user_tags": ["tag1", "tag2", ..., "tagn"]
}
```

The data transmitted by the API for the response must also be presented in json format as:

```Python
{
	"user_text": "text"
}
```
# How it works?

## Study algorithm

After entering the program, the user's text will be cleared of any punctuation marks using the sanitizer function.

```Python
def sanitizer(clear_text: str) -> str:
    return clear_text.strip(string.punctuation)
```
After that, the text will be divided into fragments, first by 1 word, by 2, 3, etc. Words of less than 3 characters will be eliminated.
```Python
"I have a problem" -> ["have", "problem", "I have", "have a", "a problem", "I have a", "have a problem", "I have a problem"]
```
Then each fragment, depending on its length, will be assigned a "weight" that will affect the execution of the response algorithm

```Python
["have", "problem", "I have", "have a", "a problem", "I have a", "have a problem", "I have a problem"] ->
{'have': 1, 'problem': 2, 'I have': 2, 'have a': 2, 'a problem': 2, 'I have a': 2, 'have a problem': 3, 'I have a problem': 4}
```

Next, a check will be made for the presence of matches with words from the database for a certain category. In case of a match, the weight of the fragments will be increased

After that, this dictionary will be loaded into the database along with the tags in json format

| Tag | Words |
|:---------:|:---------:|
| Tag | {'have': 1, 'problem': 2, 'I have': 2, 'have a': 2, 'a problem': 2, 'I have a': 2, 'have a problem': 3, 'I have a problem': 4} |


## Reply algorithm

After entering the program, the user's text will be cleared of any punctuation marks using the sanitizer function.

```Python
def sanitizer(clear_text: str) -> str:
    return clear_text.strip(string.punctuation)
```
After that, the text will be divided into fragments, first by 1 word, by 2, 3, etc. Words of less than 3 characters will be eliminated.
```Python
"I have a problem" -> ["have", "problem", "I have", "have a", "a problem", "I have a", "have a problem", "I have a problem"]
```
Next, all the data for each category will be loaded from the database, after which the words of the input text will be compared with the words from the database and a list consisting of categories and their weights for a specific input text will be created. The list will be sorted and the first three categories will be displayed.

### Example

Input text:
```Python
{
	"user_text": "I have a problem"
}
```

Output message:

```Python
[
  	"Tag1"
]
```
# Testing

For UNIT testing of functions, the unittest library is used. I have shown an example of testing the functions cutter, found_duplication, reply_output, weight_out_calibrator and word_dict_gen. In the examples, the output values of the function are based on the input data, with the specified output parameters.

# Contributions

You can contribute to project in the following ways:

* [Submit new feature ideas](https://github.com/AlienFoun/Marcus/issues)
* [Report bugs as issues](https://github.com/AlienFoun/Marcus/issues)
* Star ⭐ this repository
* Spread the word about this project

Do you have an idea for an amazing new feature? Did you find a bug you want to fix? Great! Please submit an issue for discussion before making a pull request.
