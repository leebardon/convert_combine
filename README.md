This folder current contains two sets of scripts. Before running, please ensure Python3 is loaded. 

SET 1

 * Extract surface data for physical quantities (Stave, Ttave, etc) contained in bigendian binary files (>f4) saved in .data format
 * Convert from binary to 3D numpy matrix of shape (144,90,22)
 * Slice only the surface-level data, leaving a matrix of shape (144, 90,)
 * Combine surface data for each monthly dataset (n)
 * Produce a folder in current directory (depth0) with a combined numpy matrix of shape (144, 90, n)  
  
To run, please copy "convert_and_combine.sh", "binary_to_npy.py" and "combine.npy" into the folder containing the ".data" files
and run the shell script: ./convert_and_combine.sh

SET 2


