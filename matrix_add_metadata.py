
import argparse
import csv
import sys
import glob
import os

def file2list(file,cList):
    file=open(file)
    reader=csv.reader(file,delimiter="\t")
    for row in reader:
        if "__" not in row[0]:
            cList.append(int(row[1]))

    file.close()


ap=argparse.ArgumentParser()
ap.add_argument('matrix',help='file with metadata')
ap.add_argument('metadata',help='file with metadata')
ap.add_argument('table',help='file with metadata, ~/code/cmd/DE/gene_id_name_table_ensembl37/gene_id_name_table.csv')
ap.add_argument('out',help='file to save matrix')
args=ap.parse_args()






#metadata
#ID,PC1,PC2,group,condition,name,nReads,n_exon_reads,Steatosis,Ballooning,Inflammation,NAS,HGNA,Status,Age,Sex,BMI,Glucose,Totalcholesterol,Triglycerides,HDL,AST(liverenzime),ALT(liverenzime),batch
#RL287,12.3955218735,6.12860423694,control+steatosis+uncertain,control+steatosis+uncertain,RL287,29556451,22925053,0,0,0,0,0,Control,28.0,Female,40.61,,,,,,,1

samplesSetMetadata=set()

dict_PC1={}
dict_PC2={}
dict_Steatosis={}
dict_Ballooning={}
dict_Inflammation={}
dict_NAS={}
dict_HGNA={}
dict_Status={}
dict_Age={}
dict_Sex={}
dict_BMI={}
dict_Glucose={}
dict_Totalcholesterol={}
dict_Triglycerides={}
dict_HDL={}
dict_AST={}
dict_ALT={}
dict_batch={}

file=open(args.metadata)
reader=csv.reader(file)
for row in reader:
    sample=row[0]
    samplesSetMetadata.add(sample)
    Steatosis=row[8]
    Ballooning=row[9]
    Inflammation=row[10]
    NAS=row[11]
    HGNA=row[12]
    Status=row[13]
    Age=row[14]
    Sex=row[15]
    BMI=row[16]
    Glucose=row[17]
    Totalcholesterol=row[18]
    Triglycerides=row[19]
    HDL=row[20]
    AST=row[21]
    ALT=row[22]
    batch=row[23]
    
    
    
    
    dict_Steatosis[sample]=Steatosis
    dict_Ballooning[sample]=Ballooning
    dict_Inflammation[sample]=Inflammation
    dict_NAS[sample]=NAS
    dict_HGNA[sample]=HGNA
    dict_Status[sample]=Status
    dict_Age[sample]=Age
    dict_Sex[sample]=Sex
    dict_BMI[sample]=BMI
    dict_Glucose[sample]=Glucose
    dict_Totalcholesterol[sample]=Totalcholesterol
    dict_Triglycerides[sample]=Triglycerides
    dict_HDL[sample]=HDL
    dict_AST[sample]=AST
    dict_ALT[sample]=ALT
    dict_batch[sample]=batch

dict_genes={}

#get gene id list
geneIDs=[]
geneNames=[]





#get gene names
#ENSG00000110514,MADD

k=0
file=open(args.table)
reader=csv.reader(file)
for row in reader:
    id=row[0]
    name=row[1]
    dict_genes[id]=name
    geneIDs.append(id)
    k+=1
file.close()


geneNames=[]








# After file is saved open again



geneNames.append("GeneID")



list_batch=[]
list_Steatosis=[]
list_Ballooning=[]
list_Inflammation=[]
list_NAS=[]
list_HGNA=[]
list_Status=[]
list_Age=[]
list_Sex=[]
list_BMI=[]
list_Glucose=[]
list_Totalcholesterol=[]
list_Triglycerides=[]
list_HDL=[]
list_AST=[]
list_ALT=[]

file=open(args.matrix)
reader=csv.reader(file)
next(reader,None)
for row in reader:
    geneID=row[0]
    geneNames.append(dict_genes[geneID])
file.close()




#"","GEA21","GEA33","RL167","RL281","RL287","RL294","RL295","RL298","RL319","RL347","RL353","RL361","RL369","RL371","RL382","RL406","RL410","RL415","RL420","RL431","RL454","RL456","GEA017","GEA019","GEA022","GEA027","GEA035","GEA066","RL013","RL029","RL095","RL099","RL111","RL136","RL159","RL182","RL346","RL349","RL356","RL358","RL366","RL374","RL385","RL389","RL391","RL394","RL395","RL409","RL414","RL416","RL417","RL418","RL424","RL426","RL427","RL432","RL441","RL444","RL445","RL446","RL448","RL457","RL458","RL459"



file=open(args.matrix)
reader=csv.reader(file)



for row in reader:
    for i in row:
        sample=i
        if sample in samplesSetMetadata:
                list_Steatosis.append(dict_Steatosis[sample])
                list_Ballooning.append(dict_Ballooning[sample])
                list_Inflammation.append(dict_Inflammation[sample])
                list_NAS.append(dict_NAS[sample])
                list_HGNA.append(dict_HGNA[sample])
                list_Status.append(dict_Status[sample])
                list_Age.append(dict_Age[sample])
                list_Sex.append(dict_Sex[sample])
                list_BMI.append(dict_BMI[sample])
                list_Glucose.append(dict_Glucose[sample])
                list_Totalcholesterol.append(dict_Totalcholesterol[sample])
                list_Triglycerides.append(dict_Triglycerides[sample])
                list_HDL.append(dict_HDL[sample])
                list_AST.append(dict_AST[sample])
                list_ALT.append(dict_ALT[sample])
                list_batch.append(dict_batch[sample])
        else:
                print "WARNING ", sample


    break


fileOut=open(args.out,"w")

batch="GeneName,GeneID," + ','.join(list_batch)
Steatosis="GeneName,GeneID," + ','.join(list_Steatosis)
Ballooning="GeneName,GeneID," + ','.join(list_Ballooning)
Inflammation="GeneName,GeneID," + ','.join(list_Inflammation)
NAS="GeneName,GeneID," + ','.join(list_NAS)
HGNA="GeneName,GeneID," + ','.join(list_HGNA)
Status="GeneName,GeneID," + ','.join(list_Status)
Age="GeneName,GeneID," + ','.join(list_Age)
Sex="GeneName,GeneID," + ','.join(list_Sex)
BMI="GeneName,GeneID," + ','.join(list_BMI)
Glucose="GeneName,GeneID," + ','.join(list_Glucose)
Totalcholesterol="GeneName,GeneID," + ','.join(list_Totalcholesterol)
Triglycerides="GeneName,GeneID," + ','.join(list_Triglycerides)
HDL="GeneName,GeneID," + ','.join(list_HDL)
AST="GeneName,GeneID," + ','.join(list_AST)
ALT="GeneName,GeneID," + ','.join(list_AST)




fileOut.write(batch)
fileOut.write("\n")
fileOut.write(Steatosis)
fileOut.write("\n")
fileOut.write(Status)
fileOut.write("\n")
fileOut.write(Ballooning)
fileOut.write("\n")
fileOut.write(Inflammation)
fileOut.write("\n")
fileOut.write(NAS)
fileOut.write("\n")
fileOut.write(HGNA)
fileOut.write("\n")
fileOut.write(Age)
fileOut.write("\n")
fileOut.write(Sex)
fileOut.write("\n")
fileOut.write(BMI)
fileOut.write("\n")
fileOut.write(Glucose)
fileOut.write("\n")
fileOut.write(Totalcholesterol)
fileOut.write("\n")
fileOut.write(Triglycerides)
fileOut.write("\n")
fileOut.write(HDL)
fileOut.write("\n")
fileOut.write(AST)
fileOut.write("\n")
fileOut.write(ALT)
fileOut.write("\n")

file=open(args.matrix)
reader=csv.reader(file)
             



for row in reader:
    tString=""
    if row[0]=="":
        row[0]="GeneName,GeneID"
        tString=','.join(row)
    else:
        
        tString=dict_genes[row[0]] +","+','.join(row)
        
    fileOut.write(tString)
    fileOut.write("\n")

file.close()
fileOut.close()
