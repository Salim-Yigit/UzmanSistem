import pandas as pd
import pickle 
import warnings 
import seaborn as sns
import matplotlib.pyplot as plt
warnings.simplefilter("ignore") 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score 
from pathlib import Path

def prepare():
    with open(str(Path(__file__).parent.parent) + "/amazonlogistic","rb") as file: 
        global pipeline
        pipeline = pickle.load(file)


def tahmin(text):   
    value = pipeline.predict_proba(text) 
    return value

    
def predict(text,threshold=0.68): 
    val = tahmin([text])  
    #print(val)
    if(val[0][1]>=threshold): 
        return "Positive"
    else: 
        return "Negative"  


def export_graph():
    df = pd.read_csv(str(Path(__file__).parent.parent) + "/test_100.csv")
    prepare()
    global y_test
    y_test = df["score"]
    x = df["text"]
    global y_pred
    y_pred = pipeline.predict(x)

    toReturn = {
        "accuracy": round(accuracy_score(y_pred, y_test), 2),
        "recall": round(recall_score(y_pred,y_test),2),
        "precision": round(precision_score(y_pred,y_test), 2),
        "auc": round(roc_auc_score(y_pred,y_test), 2),
        "f1": round(f1_score(y_pred,y_test), 2)
    }
    
    return toReturn

def export_heatmap():
    prepare()
    df = pd.read_csv(str(Path(__file__).parent.parent) + "/test_100.csv")
    print(df)
    global y_test
    y_test = df["score"]
    x = df["text"]
    global y_pred
    y_pred = pipeline.predict(x)
    fig = sns.heatmap(confusion_matrix(y_test, y_pred), 
                annot=True, fmt='.0f', 
                xticklabels=['Predicted negative', 'Predicted positive'], 
                yticklabels=['Negative', 'Positive']).get_figure()
    
    fig.savefig("webapp\heatmap.png")
    #plt.show()
    
    #return sns.heatmap(confusion_matrix(y_test, y_pred), 
    #            annot=True, fmt='.0f', 
    #            xticklabels=['Predicted negative', 'Predicted positive'], 
    #            yticklabels=['Negative', 'Positive'])

    