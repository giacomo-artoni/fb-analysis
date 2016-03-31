for file in `ls original_pages/*` 
do
  echo "Working on: "$file 
  python get_info.py --input $file
done
