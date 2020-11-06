import numpy as np
from spacy.tokens import Doc
from sentence_transformers import SentenceTransformer

## --------------------------------------

## The following are required:
##   - This file must be named __init__.py
##   - The folder name must match self.name
##   - The class name must be 'Plugin'
##   - The Plugin class must implement the 'analyze' method
##   - The Plugin class must implement the 'debug' method

##   - Please Enjoy and happy searching!!

class Plugin():

    def analyze(self,doc:Doc)->list:
        #This example only analyzes the first sentence of the document
        #Dense Vector fields in Elastic/Solr are not multivalued
        #When you use this in real life, distill all sentences down to one vector
        sentence = [span.text for span in doc.sents][0]
        embeddings = self.model.encode([sentence])
        vector = [embedding.tolist() for embedding in embeddings][0]
        return vector

    def debug(self,vector:list)->list:
        return vector
        
    def __init__(self,metadata):
        self.name="vectorize"
        self.pipeline = metadata
        self.pipeline[self.name] = True
        self.index = None
        self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')