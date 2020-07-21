# SCCA Autocross Class Calculator

This project is for the creation of a set of tools to make calculating autocross car classes based on make, model, year, and common upgrades. 
This project began in 2020, so the 2020 rule book is what is being used for data. 
First tool that is being built is an API that will be written using python and flask.

I started this project because I have not seen an easy to use tool to calculate autocross classes. 
What I have seen is a bunch of questions on forums asking about car classes. 
If you are not familiar with autocross, but like race cars, keep reading.
Figuring out your car's class can be complex, intimidating, and act as a barrier to some. 
Some people may not know that they can have fun in their car and test their abilities legally for under $50.00. 
I think that autocross can reach a greater audience and has great potential to become bigger than it is but needs some help in doing so. 
I am not going to go into all the benefits that autocross as an activity can provide to an individual and society here, but if you'd like to discuss please submit a commit message.

From personal experience, I started racing in autocross with a 2008 Scion Xb. 
That model year was eligible to race in autocross, but previous years of that model were ineligible. 
They were disqualified due to the height of the car being larger than the width. 
I found out about this after I registered for an event one day. 
Later that evening, I got a call from the race organizer. He said that I could not run my car, even though I did at other events. 
So, I dug into the rule book, broke out a tape measure, and showed up the next morning to race. 
Not everyone would do this, and things like this could make autocross less approachable to someone who just wants to try it.
 ---

### Install/Build/Test/Run
- First, you will need: `python 3`, `pipenv`, and `npm` on your system
- Then you can use the bash scripts.
- To install dependencies and build, while in ```AutoXCalc/API/``` run ```./install.sh```
- To build and run the application, while in ```AutoXCalc/API/``` run ```./run.sh```
- To run tests, while in ```AutoXCalc/API/``` run ```pipenv run pytest```
 
 ---
##### Resources
- Data sources can be found at: https://www.scca.com/pages/solo-cars-and-rules

 ---
### TODO
- Docker container
- CI pipeline
- Deploy to a cloud platform
- simple react interface for data entry
- simple react interface for lookup
