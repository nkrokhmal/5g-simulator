# 5g-simulator


## Model description

We consider a rectangle where M base stations are based. The size of rectangle and parameters of base stations can be customized for specific model. Each base station has own area of coverage. We assume that this area is a circle.  The data rate decays exponentially in each coverage area of base station. 


For each base station there are parameters of maximum, average and minimum number of clients. We assume that the number of users in a coverage zone is a normal distribution with mean equals to average number of clients. The variance of normal distribution is also a parameter of our model.


## Model parameters

Optional arguments: 

| Parameter                 | Default       | Description   |	
| :------------------------ |:-------------:| :-------------|
| -ep --epochs 	       |	100           | the duration of simulation process, total number of TTI 
| -tti  --tti          | 0.001           | TTI duration in seconds
| -minr --minradius 	       |	0.9	            | minimum radius of coverage area
| -maxr --maxradius  		       | 1.1	           | maximum radius of coverage area
| -x --x 		           | 1             | x length of area 
| -y  --y 	        | 1           | y length of area 
| -bs --bsnumber	         | 3             | number of base stations
| -prb --prb          | 10           | number of prb for each base station
| -k --k       | 1  | k-parameter for data rate   
| -sigma --sigma    | 4         | sigma-parameter for data rate 
| -maxc --maxclients			             | 12 	           | maximum number of clients per base station
| -minc --minclients			     | 50         | minimum number of clients per base station
| -meanc --meanclients			             | 20     	     | mean number of clients per base station
| -sigmac --sigmaclients		    | 5     	     | sigma of client number
|
