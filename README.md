###Please see untitled word document for full Readme with pictures 




Grazioso Salvare
Erwin Gove

About the Project/Grazioso Salvare
Grazioso Salvare is an interactive Dash html application designed to help find dogs that can be trained as specialized rescue dogs. This application gathers, displays and sorts data pulled from a mongodb database containing a number of animals as well as important data to that animal.  It displays a datatable of all the animals in the database, a pie chart showing the ratios of breeds in said group of animals as well as a map that allows you to see the assigned location of any given animal. This application also has filtering and sorting options designed to help you find potential candidates to be trained to be a specialized rescue dog.


Motivation
Every year search and rescue dogs save countless people but specialized animals such as these require quite a bit of training and not every dog is suitable for that kind of training. The idea behind Grazioso Salvare is to be able to search for potential candidates for these kinds of training programs. We are currently taking data from the Austin Animal Center but hope to bring in data from other sources to make looking for these animals quick and easy. 


Getting Started
To use this service you are going to need a few things first:
Grazioso Salvare runs on Python so if you don’t have an up to date copy already you can download the most up to date version of Python on their website. https://www.python.org/downloads/ 
Grazioso Salvare uses Data From MongoDb which you will also need to download if you have not done so already. https://www.mongodb.com/try/download/community 
As mentioned above Grazioso Salvare gathers its information from the Austin Animal Center. A copy of that database can be found on my github page.
Once you have everything downloaded you will need to start mongoDB. If you are running on linux simply open a terminal and type <<Path_to_mongodb>/Mongod_ctl start.
You should make an admin account to use this with your own name and password and ensure that you give it permissions to use the database you will be using. This link should describe how to make an account in mongodb https://www.mongodb.com/docs/manual/tutorial/create-users/ To ensure you have made the account properly refer to this picture:
\
If you are starting this up and need to use the database that you have already worked on here is how to get it into a usable state by uploading it to mongodb.

Once Mongodb is up and running you simply need to run the python script. If you do not have the software to run python script you can use a browser based service such as jupiter notebook. 

Installation
You will need to install python if you have not already. The link to do that is here https://www.python.org/downloads/ 
To download this interface simply click on this link www.fakelinkhere.pretend. Once there click on the download now button. If you have pip3 activated simply type into the command prompt pip3 Animal_shelter_database_iterface (does not actually work). You can also simply download it from github. 
Once downloaded you need to ensure that you have mongodb on your computer. The link to download mongodb is here https://www.mongodb.com/try/download/community


Usage
Once you get the application up and running it should look something like this:



If you do not see the pie chart or map just give it some time it can take a while to load sometimes. 
To the left on the datatable you will notice some clickable bubbles. These allow you to pick a particular animal. Doing so will update the map showing that animal's sighted location. It will look something like this.
  
As you can see the arrow is in a completely different place. If you hover over the arrow it will show the name of the animal in question.
If you find any of the data in these columns unhelpful you can delete them to reduce clutter. To the top of each column you will see a trash can that will allow you to do that.

You may also notice some arrows that allow you to sort all the animals in ascending or descending order in whatever category you choose.

Above the data table there are four options labeled water rescue, mountain rescue, disaster rescue and reset. These allow you to filter the data to see all animals that fit the criteria of the selected category







Contact
Erwin Gove

