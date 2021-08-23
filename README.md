I Chose to use pandas, SQLAlchemy, sqlite and dynaconf for this project.
pandas provides extensive tools to manipulate and transform data. 
it also integrates with SQLAlchemy, sqlite and csvs.
for the current task given pandas is a bit of a waste since its underutilized but since
this can grow into a bigger project i thought we wouldnt need to change our main technology.
SQLAlchemy gives us the flexibility we need to integrate into most databases.
If and when we switch to a more robust DB SQLAlchemy will make the switch easier.
Sqlite provides a fast to setup and easy to use DB for this project. It does not scale at all but is a good standin for 
a future db. 
Dynaconf is a very accessible configuration library which I use often. It is fast to setup and has many features in 
order to support the complicated configuration needs of a bigger project.

The code itself is sparse with abstractions for reading, transforming and writing data. I wrote it this way to save time.
For a bigger project or with more time I would wrap most functionalities in interchangeable abstractions to support the changing needs of data pipeline projects such as this.  
