# UFRJ-Thesis

![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/825444971729256499/thesis.gif)

## Table of Contents

<!--ts-->
   * [About](#about)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
      * [CSV Structure](#csv-structure)
      * [Setting up Program](#program-setup)
   * [Technologies](#technologies)
<!--te-->

## About

A simple program constructed using Python3 and some other libraries made by Bruno Dantas and Pedro Boechat.

This program is a simple web crawler that gets every [thesis information](https://monografias.poli.ufrj.br/relatorios.html) and stores it in a database (MongoDB).

## Requirements

To run this repository by yourself you will need to install python3 in your machine and them install all the requirements inside the [requirements](requirements.txt) file

## How to use

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/DantasB/ufrj-thesis>

# Access the project page on your terminal
$ cd ufrj-thesis

# Install all the requirements
$ pip install -r requirements.txt

# Create a .env file
$ touch .env  

# Create the following parameters
 CONNECTION_URL #Your MongoDB connection url
 USERNAME #Your MongoDB connection username
 PASSWORD #Your MongoDB connection password
 DATABASE #The database that contains the collection to store the informations
 COLLECTION #The collection where you will store the informations
 PORT #Your database port

# Execute the main program
$ python main.py

# Them it's just wait for the code run
```
![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/825446078132387890/unknown.png)


## Technologies

* Python3
* beautifulsoup4
* pymongo


If you still need help, fell free to contact me on discord: BDantas#3692
