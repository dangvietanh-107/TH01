#vd11
import pandas as pd
path ="data.xlsx"
data=pd.read_csv(path)
data.info

#vd13
data1 =pd.read_csv(path,index_col=0)
data1.info()
data1.head()
#vd14
data2=pd.read_csv(path,nrows=100,usecols=["height_cm","weight_kg"])
data2.info()
data2.head()
#vd15
data3=pd.read_csv(path,names=["id","sex","h(cm)","w(kg)"],skiprows=5)
data3.info()
data3.head()

#vd21
import pandas as pd
path_excel ="students_data.xlsx"
data_ex=pd.read_excel(path_excel)
data_ex.info()
data_ex.head()
#vd23
data_ex1=pd.read_excel(path_excel,sheet_name="0",usecols=[1,6,7,8,9,10],index_col=0)
data_ex1.info()
#vd24
data_ex3=pd.read_excel(path_excel,sheet_name="4080130_02",skiprows=9)
data_ex3.info()
data_ex3.head()
#vd25
data_ex4=pd.read_excel(path_excel,sheet_name="4080130_00",haeder=None)
data_ex4.info()
data_ex4.head()
#vd26
data_ex41=pd.read_excel(path_excel,sheet_name="4080130_03",haeder=None,usecols=[1,6,7,8,10],names=["ma sv","a","b1","b2","c2"],index_col=0)
data_ex41.info()
data_ex41.head()