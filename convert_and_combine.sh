 #/bin/bash
 echo ""
 echo "**************************************************************************"
 echo ""
 echo "This program converts from bigendian binary files (>f4) to 3D numpy matrix, extracts surface layer data at Z=0 for each month, and combines them into one array ----> 'combined.npy'."
 echo ""
 echo ""
 echo "NOTE --> Please ensure that 'convert_and_combine.sh', binary_to_npy.py' and 'combine_arrays.py' are in the same same folder as you binary '.data' files."
 echo ""
 echo "**************************************************************************"
 echo ""

 depth=0
 export depth=$depth
 export root="depth"$depth
 mkdir "depth"$depth

 cwd=$(pwd)
 file_path=$cwd
 month=1
 
 progressbar () {
 
    trap 'break' USR1
    while printf '#' >&2; do
        sleep 0.25
    done
    
 }

 progressfoo () {
 
    progressbar & pid="$!"
    echo 'Program Running.....'
     
        for f in $file_path/*.data
        do
            export binary=$f
            python binary_to_npy.py $month
            ((month=month+1))
        done

        cp $(pwd)/depth0/month1.npy $(pwd)/depth0/combined.npy
        python combine_arrays.py
        rm $(pwd)/depth0/month*.npy
        
    kill -s USR1 "$pid"
 }

 progressfoo

 echo ""
 echo "<<<<<<<<<<<<<<<   CONVERSION AND EXTRACTION SUCCESSFUL  >>>>>>>>>>>>>>>>>>"
 echo ""
