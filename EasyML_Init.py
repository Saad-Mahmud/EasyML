from flask import Flask, render_template
import dash
import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from time import time
#hello
#lasd
EM_Server = Flask(__name__)
EM_App = dash.Dash(__name__, server=EM_Server, url_base_pathname='/test/')
EM_App.scripts.config.serve_locally = True
EM_App.config['suppress_callback_exceptions'] = True
EM_App.css.append_css(
    {'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'}
)

#test
@EM_Server.route('/demo')
def bstest():
    return render_template('index4.html')

@EM_Server.route('/page1')
def bstest1():
    return render_template('Page1_HTML.html')

@EM_Server.route('/page2')
def bstest2():
    return render_template('Page2_HTML.html')

@EM_Server.route('/page3')
def bstest3():
    return render_template('Page3_HTML.html')

@EM_Server.route('/page4')
def bstest4():
    return render_template('Page4_HTML.html')

@EM_Server.route('/page5')
def bstest5():
    return render_template('Page5_HTML.html')

@EM_Server.route('/page6')
def bstest6():
    return render_template('Page6_HTML.html')

@EM_Server.route('/page7')
def bstest7():
    return render_template('Page7_HTML.html')

@EM_Server.route('/page8')
def bstest8():
    return render_template('Page8_HTML.html')
@EM_Server.route('/page9')
def bstest9():
    return render_template('Page9_HTML.html')

@EM_Server.route('/page10')
def bstest10():
    return render_template('Page10_HTML.html')


@EM_Server.route('/page11')
def bstest11():
    return render_template('Page11_HTML.html')


@EM_Server.route('/page12')
def bstest12():
    return render_template('Page12_HTML.html')


@EM_Server.route('/page13')
def bstest13():
    return render_template('Page13_HTML.html')


@EM_Server.route('/page14')
def bstest14():
    return render_template('Page14_HTML.html')




@EM_Server.route('/')
def hello_world():
    return render_template('homepage.html')

@EM_Server.route('/aboutUs')
def pageAboutUs():
    return render_template('aboutUsPage.html')

@EM_Server.route('/blog')
def pageBlog():
    return render_template('blog.html')

@EM_Server.route('/request')
def pageRequest():
    return render_template('requestPage.html')

@EM_Server.route('/signup')
def signup():
    return render_template('signUpPage.html')



@EM_Server.route('/discussions/3layeredperceptronclassifieranalysis')
def disc3layerperceptron():
    return render_template('Discussions/discussion3LayeredPerceptronClassifierAnalysis.html')

@EM_Server.route('/discussions/decisiontreeclassifieranalysis')
def discDecisionTree():
    return render_template('Discussions/discussionDecisionTreeClassifierAnalysis.html')

@EM_Server.route('/discussions/dimensionalityreduction2d')
def discDimension2D():
    return render_template('Discussions/discussionDimensionalityReduction2D.html')

@EM_Server.route('/discussions/dimensionalityreduction3d')
def discDimension3D():
    return render_template('Discussions/discussionDimensionalityReduction3D.html')

@EM_Server.route('/discussions/kneighborsclassifier')
def discKNeighbors():
    return render_template('Discussions/discussionKNeighborsClassifierAnalysis.html')

@EM_Server.route('/discussions/logisticregression')
def discLogisticRegression():
    return render_template('Discussions/discussionLogisticRegressionClassifierAnalysis.html')

@EM_Server.route('/discussions/pca')
def discPCA():
    return render_template('Discussions/discussionPCA.html')

@EM_Server.route('/discussions/svm')
def discSVM():
    return render_template('Discussions/discussionSVMClassifierAnalysis.html')

@EM_Server.route('/discussions/quickview')
def discQuickView():
    return render_template('Discussions/discussionQuickView.html')

@EM_Server.route('/discussions/randomforest')
def discRandomForest():
    return render_template('Discussions/discussionRandomForestClassifierAnalysis.html')

@EM_Server.route('/discussions/recursivefeature')
def discRecursiveFeature():
    return render_template('Discussions/discussionRecursiveFeatureElimination.html')

@EM_Server.route('/discussions/dimensionalitymodel')
def discDimModel():
    return render_template('Discussions/discussionDimensionalityModel.html')

@EM_Server.route('/discussions/featureselect')
def discFeatureSelect():
    return render_template('Discussions/discussionFeatureSelection.html')

@EM_Server.route('/discussions/univariatefeature')
def discUnivariateFeature():
    return render_template('Discussions/discussionUnivariantFeature.html')

@EM_Server.route('/discussions/dataframeedit')
def discDataframeEdit():
    return render_template('Discussions/discussionDataframe.html')

@EM_Server.route('/discussions/votingclassifier')
def discVoting():
    return render_template('Discussions/discussionVotingClassifier.html')

@EM_Server.route('/discussions/adaboost')
def discAdaBoost():
    return render_template('Discussions/discussionAdaBoost.html')

@EM_Server.route('/discussions/variancethreshold')
def discVariance():
    return render_template('Discussions/discussionVarianceThreshold.html')
