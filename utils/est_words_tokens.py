import math
from scipy import stats
#import seaborn as sns
#import matplotlib.pyplot as plt

def est_words_tokens(df):
    df["num_sentences"] = df["text"].apply(lambda x: len(x.split()))
    df["num_tokens"] = ((4/3)*df["num_sentences"]).apply(lambda x: math.ceil(x))
    print("Ran est_words_tokens")
    print(f"Estimated 10% trimmed mean number of tokens: {round(stats.trim_mean(df['num_tokens'], 0.10))}")
    print(f"Estimated 10% Winsorized mean number of tokens: {round(stats.mstats.winsorize(df['num_tokens'], limits=0.10).mean())}")
    print(f"Estimated median number of tokens: {round(df['num_tokens'].median())}")
    print(f"Estimated Max. number of tokens: {df['num_tokens'].max()}")
    print(f"Estimated ratio of rows exceeding the 256 token limit:", round(100*len(df.query("num_tokens > 256"))/len(df)), "%")
    print(f"Estimated ratio of rows exceeding the 512 token limit:", round(100*len(df.query("num_tokens > 512"))/len(df)), "%")

    #sns.set(style="dark")
    #plt.style.use("dark_background")
    #plt.figure(figsize=(5, 5*9/16))
    #sns.kdeplot(data=df, x="num_tokens", fill=True, color="salmon", alpha=0.75, linewidth=0).set(title = "Distribution of the Number of Tokens")
    #plt.xlim(0, 1.05*df["num_tokens"].max())
    #plt.show()
    #df["num_tokens"].plot.hist(bins=round(math.sqrt(len(df))), alpha=0.75, figsize = (5, 2.5))
    return df