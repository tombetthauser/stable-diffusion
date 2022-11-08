for filename in ./*
do
  base=${filename%.*}
  convert $filename "${base}.jpg"
done