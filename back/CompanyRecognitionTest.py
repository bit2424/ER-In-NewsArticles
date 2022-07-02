import re
import News
import Identificator
import Companies
import Clasificator

dataset = {}
metrics = {}

def main():
    dataSetLoad()
    dataSetTest()
    accuaracy()
    precision()
    recall()
    F1()
    print(metrics)

def accuaracy():
    metrics['acc'] = (metrics['TP']+metrics['TN']) / (metrics['TP']+metrics['TN']+metrics['FN']+metrics['FP'])
    print("Accuaracy: ",metrics['acc'])

def precision():
    metrics['prs'] = (metrics['TP']) / (metrics['TP']+metrics['FP'])
    print("Precision: ",metrics['prs'])

def recall():
    metrics['rcl'] = (metrics['TP']) / (metrics['TP']+metrics['FN'])
    print("Recall: ",metrics['rcl'])

def F1():
    metrics["f1"] = 2*(metrics['prs']*metrics['rcl'])/(metrics['prs']+metrics['rcl'])
    print("F1: ",metrics['f1'])

def dataSetTest():
    TP,TN,FP,FN = 0,0,0,0
    for id in dataset:
        x = dataset[id].pop(0)
        found_companies = Identificator.identify_companies_in_text(x)
        real_y = dataset[id]
        pred_y = list(found_companies)
        #print(real_y)
        #print(pred_y)
        for word in pred_y:
            if (word in real_y):
                TP = TP+1
                real_y.remove(word)
            else:
                FP = FP+1
                #print(word)
            x.replace(word,"")
        TN = TN + len(x.split())
        FN = FN + len(real_y)
        #print("...")

    metrics["TP"] = TP
    metrics["TN"] = TN
    metrics["FP"] = FP
    metrics["FN"] = FN

def dataSetLoad():
    f = open("dataset.txt", "r", encoding='utf-8')
    id = 0
    for x in f:
        dataset[id] = x.split(';')
        pos = 0
        for elem in dataset[id]:
            dataset[id][pos] = elem.strip()
            pos = pos+1
        id = id+1
    
    #print(dataset)


def dataSetCreation():
    news = News.getArticles('Investment Banking & Brokerage', '','en','2022-07-01','2022-06-05',20,[])

    with open('dataset.txt', 'a',encoding='utf-8') as f:
        for article_content in news:
            f.write(article_content['title'].replace(';',' ')+"\n")

if __name__ == "__main__":
    main()