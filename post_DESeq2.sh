
if [ $# -lt 3 ]
then
echo ""
echo "1 - PCA csv file"
echo "2  - metadata file. For example metadataNew2_liver.txt "
echo "3 - counts_norm_rld"
exit 1
fi



PCA_file=$1
metadata_file=$2

sed 's/\"//g' $PCA_file | sed 's/,PC1/sampleName,PC1/'  | sed 's/sampleName/ID/'>test

mv test $PCA_file

python ~/code/cmd/mergeCsvByField.py $PCA_file $metadata_file test ID

mv test $PCA_file

python ~/code/adriana_jake/code/matrix_add_metadata.py $3 $PCA_file ~/code/cmd/DE/gene_id_name_table_ensembl37/gene_id_name_table.csv ${3}_metadata.csv

#python ~/code/cmd/DE/countsDE2Matrix.py control_steatosis_uncertain_vs_NASH_H_norm_rld.csv PCA_txt_control_steatosis_uncertain_vs_NASH_H.csv ~/code/cmd/DE/gene_id_name_table_ensembl37/gene_id_name_table.csv matrix