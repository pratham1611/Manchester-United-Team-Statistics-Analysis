import pandas as pd
import glob
import calendar
import numpy as np
import matplotlib.pyplot as plt
path=r'C:\Users\Prathamesh Marathe\Desktop\Assignments\Machine Learning\Analyzing Manchester United\Ferguson Era'
path_post=r'C:\Users\Prathamesh Marathe\Desktop\Assignments\Machine Learning\Analyzing Manchester United\Post Ferguson Era'
filenames = glob.glob(path + "/*.csv")
filenames_post = glob.glob(path_post + "/*.csv")

def read_file(path,filenames):
	dfs = []
	for filename in filenames:
		dfs.append(pd.read_csv(filename))
	df= pd.concat(dfs, ignore_index=True)
	return df

def visualize(df,text):
	df.xticks=[np.arange(1,13)]
	#plt.xlim('2','12')
	#plt.figure();
	ax=df.plot(x='Month',y='FTHG',label='Goals (FT)')
	#plt.type="scatter"
	plt.title(text)
	df.plot(x='Month',y='HS',label='Shots',ax=ax)
	df.plot(x='Month',y='HST',label='SOT',ax=ax)
	df.plot(x='Month',y='HC',label='Corners',ax=ax)
	df.plot(x='Month',y='HF',label='Yellow Cards',ax=ax)
	df.plot(x='Month',y='HR',label='Red Cards',ax=ax)
	plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.3))
	plt.show()

def process_df(df):
	df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d').dt.strftime('%m-%d-%Y')
	df['Month']=df['Date'].astype(str).str[0:2]
	df_home=df[df['HomeTeam']=='Man United'] 
	df_away=df[df['AwayTeam']=='Man United']
	df_home=df_home.groupby(['Month'],as_index=False).mean()
	df_away=df_away.groupby(['Month'],as_index=False).mean()
	print(df_home)
	df_home['Month']=df_home['Month'].apply(pd.to_numeric).astype(np.int64)
	return(df_home,df_away)

df_ferguson_era=read_file(path,filenames)
df_h,df_a=process_df(df_ferguson_era)
visualize(df_h,"Home Fergie Era")
visualize(df_a,"Away Fergie Era")


df_post_ferguson_era=read_file(path_post,filenames_post)
df_h,df_a=process_df(df_post_ferguson_era)
visualize(df_h,"Home Post Fergie Era")
visualize(df_a,"Away Post Fergie Era")
