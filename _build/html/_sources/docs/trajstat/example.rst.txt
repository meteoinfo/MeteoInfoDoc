.. docs-trajstat-example:


**************************
Example
**************************

For new users to better understand the software, an example was described in this help document. Sand and dust storm 
(SDS) pathways and sources could be identified using trajectory statistics methods. In this example, we want to do 
such analysis to Jiuquan which is located in northwest of China. We have the data of daily averaged PM10 concentration 
at Jiuquan in springtime from 2004 to 2006. Following is the steps to implement the job:

    1. Add Jiuquan station into the project..
    2. Calculate 3-day back trajectories during PM10 data measurement period.
    3. Convert end point files to .tgs files. Then join .tgs files to one file.
    4. Convert .tgs file to trajectory line shape file and add the shape file into the project.
    5. Show press profile of the trajectories.
    6. Add measurement data into the trajectories.
    7. Select polluted trajectories.
    8. Cluster calculation to the trajectories.
    9. Calculate mean trajectory of cluster and add the cluster line shape file into the project.
    10. Decide cluster number.
    11. Add cluster to each trajectory.
    12. Do cluster statistics and find the pathways of SDS.
    13. Create grid polygon shape layers of PSCF and CWT.
    14. PSCF and CWT analysis.
    
Three sample files ‘JiuquanSpr.tgs’, ‘Stations.txt’ and ‘Jiuquan_PM10_Spr_DA.csv’ could be found in ‘Sample’ folder 
under software installation directory. The example could be done with them except trajectory calculation step which 
need large meteorological data. Please read HYSPLIT help documents for details of trajectory calculation.