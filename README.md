# 5G-simulator


## Model description

We consider a rectangle where M base stations are based. The size of rectangle and parameters of base stations can be customized for specific model. Each base station has own area of coverage. We assume that this area is a circle.  The data rate decays exponentially in each coverage area of base station. 


For each base station there are parameters of maximum, average and minimum number of clients. We assume that the number of users in a coverage zone is a normal distribution with mean equals to average number of clients. The variance of normal distribution is also a parameter of our model.


## Model parameters

Optional arguments: 

| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| --epochs 	       |	100           | the duration of simulation process, total number of TTI 
| --tti          | 0.001           | TTI duration in seconds
| --minradius 	       |	0.9	            | minimum radius of coverage area
| --maxradius  		       | 1.1	           | maximum radius of coverage area
| --x 		           | 1             | x length of area 
| --y 	        | 1           | y length of area 
| --bsnumber	         | 3             | number of base stations
| --prb          | 10           | number of prb for each base station
| --k       | 1  | k-parameter for data rate   
| --sigma    | 4         | sigma-parameter for data rate 
| --maxclients			             | 12 	           | maximum number of clients per base station
| --minclients			     | 50         | minimum number of clients per base station
| --meanclients			             | 20     	     | mean number of clients per base station
| --sigmaclients		    | 5     	     | sigma of client number


## Run simulation


Install requirements
```
pip install -r requirements.txt
```
Run models (you can choose between pff, srpt and random)
```
python pff_simulate.py
python srpt_simulate.py
python random_simulate.py
```
