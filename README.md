# Daylight saving time impact on web usage around the world

# Abstract

The daylight saving time (DST) has been debated more and more recently, bringing into discussion whether it should be abolished or not. While most of the countries do not observe daylight saving time, most of Europe and North America does, making it an important problem, especially for us Europeans.
We will analyze the impact that the DST has on several timezones related to the web usage. In this regard, we will use different datasets to monitor the posting behavior of users around the time of hour changes in different parts of the world. To frame the change of general behavior, the use of several platforms is necessary.
We will study the data distributions of StackOverflow, Wikipedia and a gym to derive hypotheses and verify them.
We would like to study the impact of this time change on the distribution of positions on different scales, and the time taken to find a "normal" activity. We focused our study on the US geographical area, having encountered difficulty to obtain localized data for users, probably outside the legal framework.

# Research questions

We would like to answer the following questions:

1. Does the hour change have an immediate effect on the users' behavior?
2. Does one of the hour changes (spring time or winter time) have a more drastic impact than the other?
3. Does the hour change affect only digital behavior or also habits in terms of health?
4. How long do users take to find a more conventional pace?

# Dataset

Given that the Twitter dataset provided consists only of posts from the 16th June, we will need to collect another dataset using the Twitter API.
The posts come in the format of a list of dictionary objects, each describing a published post or a deleted one. We will only monitor the published posts, which also provide the date the post was created (through the _created_at_ tag) and the timezone of the user (in the _user/time_zone_ field). The date and the timezone will constitute the main data that we are going to use in our analysis. The data will consist of posts in the range of about a week before and after the hour changes.
As an extension, we also consider making use of the Wikipedia dataset to enrich our observations.

1. StackOverFlow dataset : The dataset was provided during the HW3. StackOverflow is the most popular programming-related Q&A website. It serves as a platform for users to ask and answer questions and to vote questions and answers up or down. Users of StackOverflow can earn reputation points and "badges"; for example, a person is awarded 10 reputation points for receiving an "up" vote on an answer given to a question, and 5 points for the "up" vote on a question asked. Also, users receive badges for their valued contributions, which represents a kind of gamification of the traditional Q&A site.
2. Wikipedia dataset : The data available in time by Wikipedia are limited so as not to saturate their servers. That's why we had to write a script using the wikipedia API to extract the changes that occurred one week before and one week after the time change. Indeed, with 1.7 changes per second, we were unable to download more data from Wikipedia, especially for legal problems.
   So we extracted 100 changes in every 15 minutes and format it into a JSON file.
   This dataset has a size of 595 MB. Details about the API and our request is available into our notebook.
3. Gym dataset : The dataset consists of 26,000 people counts (about every 10 minutes) over the last year. In addition, we gathered extra info including weather and semester-specific information that might affect how crowded it is. The label is the number of people, which I'd like to predict given some subset of the features.
   The dataset is coming from Kaggle at the [link](https://www.kaggle.com/nsrose7224/crowdedness-at-the-campus-gym/version/2).

# Project Steps

The project respected the different milestones as described below:

1. Milestone 1

- data scraping
- Hypotheses and first exploration of the data

2. Milestone 2

- Data Wrangling
- Statistical and mathematical analysis of data
- Choice of final datasets

3. Milestone 3 (Final)

- Advanced data analysis
- Verification of hypotheses
- Report and presentation preparation

#Contributions

- Alexandre: Wikipedia data scraping script, wikipedia data analysis, general report formatting, "Immediate Effect" part (wikipedia part) & "Find these habits", README update
- Alex: data analysis of StackOverflow, "Immediate Effect" section (StackOverflow part) & "Spring or Winter?" section, last proofreading and analyzes improvement
- Rusu: Gym data scraping, Gym dataset analysis, "Health habits", ideas provider

# Some useful links

1. [Wikipedia Python Client](https://mwclient.readthedocs.io/en/master/reference/site.html?highlight=changes#mwclient.client.Site.recentchanges)
