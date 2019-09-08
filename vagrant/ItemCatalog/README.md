Udacity Item Catalog
====================

## Description

An item catalog web app created using Flask for the Udacity Full Stack Nanodegree. The application provides a list of items within a variety of categories and integrates third party user registration and authentication. Authenticated users have the ability to post, edit, and delete their own items and categories.


## Setup

You will need Vagrant and Virtualbox installed in order to run the app.

Download or clone the repository.

Clone the [Udacity virtual machine repository](https://github.com/udacity/fullstack-nanodegree-vm/tree/master/vagrant), which contains the vagrant file needed to run the application.

Copy or move the files from the Item Catalog repository, which was downloaded first, into the catalog folder of the vagrant repository. Navigate to this folder in the terminal before launching the app.

## Usage

Launch the Vagrant virtual machine by running `vagrant up` in the command line. Then log in using `vagrant ssh`. Change into the Vagrant shared directory using `cd /vagrant/catalog`.

Install the dependency libraries (Flask, sqlalchemy, requests and oauth2client) by running `pip install -r requirements.txt`.


Add sample database categories and items using `python catalog_items.py`.

To run the app, enter `python application.py`, then navigate to `localhost:8000` in the browser.

## JSON Endpoints

`/catalog/JSON` - Returns data for all categories.

`/catalog/<int:category_id>/items/JSON` - Returns data for all items of a specific category.

`/catalog/<int:category_id>/items/<int:category_item_id>/JSON` - Returns data regarding a specific category item.