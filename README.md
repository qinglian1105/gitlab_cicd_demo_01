# **gitlab_cicd_demo_01**

## **A simple example: deploying a service of making predictions by Deep Learning with GitLab CI/CD**

#### **Ⅰ. 目的** 
使用GitLab CI/CD提升自動化部署深度學習(Deep Learning)模型預測服務(API)。 

#### **Ⅱ. 主要工具或套件**
GitLab CI/CD、Harbor(Docker Registry)、Flask、Tensorflow(Keras)

#### **Ⅲ. 說明**
1. 資料：<br>
來自 Kaggle 的 Pima Indians Diabetes Database，資料內容、欄位 ([詳見](<https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data>))。
2. 深度學習模型：<br>
本專案主要目的為展示CI/CD，模型訓練並不嚴謹，並忽略模型績效衡量指標，相關參數如下：<br>
```python
# define model
model=Sequential()
model.add(Dense(12, input_dim=8, activation="relu"))
model.add(Dense(8,activation="relu"))
model.add(Dense(1,activation="sigmoid"))
# compile the model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
# fit the model
model.fit(x=x_train, y=y_train, epochs=150, batch_size=10, verbose=0)
```

3. CI/CD Pipeline：<br>
詳如程式檔「.gitlab-ci.yml」，Pipeline僅有二個stage。<br>
(1) stege_01:<br>用Dockerfile、flask_ml_demo.py、requirements.txt及模型檔model_pima.h5打包成 image，即模型預測服務API，上傳到Harbor。<br>
(2) stege_02:<br>檢查舊服務是否存在，若是則清除。從Harbor拉取之前打包上傳的image，啟動container，即模型預測服務(API)。<br><br>
簡言之，當專案內的檔案變動，如：深度學習模型更新、服務的主程式flask_ml_demo.py有變動…等，git push後使觸發Pipeline開始執行，自動執行二個stage，最後完成重新部署該預測服務。<br>
若新增其他stage，如：資料ETL、模型訓練、模型測試…等功能，便可達成MLOps(Machine Learning Operations)的精神。

<br>

---

#### **References**

[1] [Get started with GitLab CI/CD](<https://docs.gitlab.com/ee/ci/>)

[2] [GitLab: 建立第一條 CI/CD Pipeline](<https://ithelp.ithome.com.tw/articles/10219427>)

[3] [Flask’s documentation](<https://flask.palletsprojects.com/en/stable/>)

[4] [Kaggle - Pima Indians Diabetes Database](<https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data>)

[5] [TensorFlow - tf.keras](<https://www.tensorflow.org/api_docs/python/tf/keras>)

[6] [Google - MLOps: Continuous delivery and automation pipelines in machine learning](<https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>)