<h1> Oceanic Data from MITgcm Binary Outputs </h1>

<b>This program extracts monthly oceanic data from MITgcm output files at Z=0 (ocean surface).</b>


It applies to N-monthly files stored in the '.data' format, and returns a numpy matrix of shape (144, 90, N).

 * Extract surface data for physical quantities (Stave, Ttave, etc) contained in big-endian binary files (>f4) saved in .data format
 * Convert from binary to 3D numpy matrix of shape (144,90,22)
 * Slice only the surface-level data, leaving a matrix of shape (144, 90,)
 * Combine surface data for each monthly dataset (N)
 * Produce a folder in current directory (depth0) with a combined numpy matrix of shape (144, 90, N)  
  

<h3> To Run </h3> 

1) Please ensure you have python3 installed.
2) Copy "convert_and_combine.sh", "binary_to_npy.py" and "combine.npy" into the folder containing the ".data" files
3) Execute shell script: ./convert_and_combine.sh


NOTE: Biteswaping is performed relative to the machine running the scripts, so it should be portable. But this can't be guaranteed.




