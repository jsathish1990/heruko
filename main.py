# -*- coding: utf-8 -*-
"""main.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pt_ts9LklVSDqB-8lswsF40bPTFt9Oa4
"""

#!pip install sentence_transformers

#conda install sentence_transformer
from flask import Flask, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('bert-base-nli-mean-tokens')
app = Flask(__name__)
@app.route("/index")
def index():
  
  sentences = [
      "Outdated computer systems are hampering the work of police inspectors to find gangsters",
      "The suspect in yesterday's string of robberies is identified as 18-year-old Crish",
      "Sometimes crimes and attacks are carried out by youths for gaining street cred among gangs",
      "this is a culture-rich city with carnatic music, delicious food, mountains and popular temples"
      ]


  sentence_embeddings = model.encode(sentences)
  similarities = cosine_similarity(
    [sentence_embeddings[0]],
    sentence_embeddings[1:]
  )
  return jsonify(similarities.tolist())

if __name__ == "__main__":
  app.run(debug = True)

