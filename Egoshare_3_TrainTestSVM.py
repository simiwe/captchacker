#!coding: utf-8

from svm import *
import os
import time

CRANGE = [1000]
KERNEL_TYPE = [RBF, POLY]


for C in CRANGE:
    for KERNEL in KERNEL_TYPE:
        #TRAINING_FOLDER = 'Egoshare/DBTraining'
        TRAINING_FOLDER = 'Egoshare/DBTraining-Simulation_based'
        TEST_FOLDER = 'Egoshare/DBTest'
        VERBOSE = 0
        MODEL_FOLDER = 'Egoshare/Models'
        MODEL_FILE = "captcha_based_TR=576_TEST=143_C="+str(C)+"_KERNEL="+str(KERNEL)+".svm"
        GENERATE_ANYWAY = 1

        #G�n�ration du mod�le
        execfile("Train & Test SVM.py")
        
        #Test du mod�le
        execfile("Break_Egoshare_Captcha.py")


raw_input()