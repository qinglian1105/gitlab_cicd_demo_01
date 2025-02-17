# **gitlab_cicd_demo_01**

## **An example: deploying a service of making predictions by Deep Learning with GitLab CI/CD**

#### **Ⅰ. 目的** 
使用 GitLab CI/CD 提升自動化部署 深度學習(Deep Learning) 模型預測服務(API)。 

#### **Ⅱ. 主要工具或套件**
GitLab CI/CD、Harbor(Docker Registry)、Flask、Tensorflow(Keras)

#### **Ⅲ. 說明**
1. 資料：<br>
來自 Kaggle 的 Pima Indians Diabetes Database，資料內容、欄位 ([詳見](<https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data>))。

2. 深度學習模型：<br>
主要目的為展示CI/CD，模型訓練並不嚴謹，並忽略模型績效衡量指標，相關參數如下：<br>

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
如下圖所示，Pipeline僅有二個stage，詳如程式檔「.gitlab-ci.yml」。其內容簡述如下：<br>

    (1) stege_01<br>
名稱為 package_pycode。使用Dockerfile、flask_ml_demo.py、requirements.txt及模型檔model_pima.h5打包成 image，即模型預測服務(API)，上傳到Harbor。<br>

    (2) stege_02<br>
名稱為 deploy_service。首先，檢查舊服務是否存在，若是則清除。接著，從Harbor拉取之前打包上傳的image，啟動container，即模型預測服務(API)。<br><br>

    ![avatar](./README_pics/pic_gitlab_pipeline.png)<br><br>

    簡言之，當專案內的檔案變動，如：深度學習模型更新、服務的主程式 flask_ml_demo.py有變動…等，當從本機儲存庫推送(git push)到遠端儲存庫後，將觸發Pipeline執行，自動依序執行二個stage的任務，最後完成重新部署該預測服務。<br>

    更進一步地說，若新增其他stage，如：資料ETL、模型訓練、模型測試…等功能，則從資料清洗→匯入資料庫→擷取最新資料加入訓練集→訓練模型、測試模型→通過衡量指標→部署新模型及服務…，如此便可達成 MLOps(Machine Learning Operations)的精神。

<br>

---

#### **Ⅳ. References**

[1] [Get started with GitLab CI/CD](<https://docs.gitlab.com/ee/ci/>)

[2] [GitLab: 建立第一條 CI/CD Pipeline](<https://ithelp.ithome.com.tw/articles/10219427>)

[3] [Flask’s documentation](<https://flask.palletsprojects.com/en/stable/>)

[4] [Kaggle - Pima Indians Diabetes Database](<https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database/data>)

[5] [TensorFlow - tf.keras](<https://www.tensorflow.org/api_docs/python/tf/keras>)

[6] [Google - MLOps: Continuous delivery and automation pipelines in machine learning](<https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning>)